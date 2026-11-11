"""Tests for cr_agent.capture.frames. They describe the behaviour; you write the code."""

import dataclasses
import inspect

import numpy as np
import pytest

from cr_agent.capture.frames import Frame, iter_frames


def blank(h: int = 4, w: int = 3) -> np.ndarray:
    return np.zeros((h, w, 3), dtype=np.uint8)


def test_frame_holds_its_fields():
    image = blank()
    frame = Frame(image=image, index=2, timestamp_s=0.5, source="match1.mp4")
    assert frame.image is image
    assert frame.index == 2
    assert frame.timestamp_s == 0.5
    assert frame.source == "match1.mp4"


def test_frame_is_frozen():
    frame = Frame(image=blank(), index=0, timestamp_s=0.0, source="live")
    with pytest.raises(dataclasses.FrozenInstanceError):
        frame.index = 1  # type: ignore[misc]


def test_iter_frames_is_a_generator():
    assert inspect.isgenerator(iter_frames([blank()], fps=30.0, source="x"))


def test_iter_frames_numbers_and_times_frames():
    frames = list(iter_frames([blank(), blank(), blank()], fps=4.0, source="match1.mp4"))
    assert [f.index for f in frames] == [0, 1, 2]
    assert [f.timestamp_s for f in frames] == [0.0, 0.25, 0.5]
    assert {f.source for f in frames} == {"match1.mp4"}


def test_iter_frames_keeps_the_images_in_order():
    a, b = blank(), blank()
    frames = list(iter_frames([a, b], fps=30.0, source="x"))
    assert frames[0].image is a
    assert frames[1].image is b


def test_iter_frames_is_lazy():
    pulled = 0

    def images():
        nonlocal pulled
        while True:  # an endless source: only a lazy reader can handle it
            pulled += 1
            yield blank()

    stream = iter_frames(images(), fps=30.0, source="x")
    first = next(stream)
    assert first.index == 0
    assert pulled == 1


def test_iter_frames_on_no_images_yields_nothing():
    assert list(iter_frames([], fps=30.0, source="x")) == []


@pytest.mark.parametrize(
    "bad",
    [
        np.zeros((4, 3), dtype=np.uint8),  # no colour channel
        np.zeros((4, 3, 4), dtype=np.uint8),  # four channels
        np.zeros((4, 3, 3), dtype=np.float32),  # wrong dtype
    ],
)
def test_iter_frames_rejects_bad_images(bad):
    with pytest.raises(ValueError):
        list(iter_frames([bad], fps=30.0, source="x"))
