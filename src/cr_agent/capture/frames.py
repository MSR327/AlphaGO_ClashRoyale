"""Frames: the one record the rest of the code receives from capture.

A frame source is anything that yields `Frame` objects one at a time, in order.
`iter_frames` turns any iterable of images (decoded video frames, test arrays) into
such a source.
"""

from collections.abc import Iterable, Iterator
from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class Frame:
    """One screen image plus the facts later code needs to line it up with taps."""

    image: np.ndarray  # height x width x 3, uint8, RGB
    index: int  # position in the stream, starting at 0
    timestamp_s: float  # seconds since the start of the recording
    source: str  # where it came from, e.g. a file name or "live"


def iter_frames(images: Iterable[np.ndarray], fps: float, source: str) -> Iterator[Frame]:
    """Yield one `Frame` per image, in order, pulling images only as they are needed.

    Raises ValueError for an image that is not a uint8 array of shape (height, width, 3).
    """
    for index, image in enumerate(images):
        if image.dtype != np.uint8 or image.ndim != 3 or image.shape[2] != 3:
            raise ValueError(
                f"frame {index} must be a uint8 array of shape (H, W, 3), "
                f"got dtype={image.dtype} shape={image.shape}"
            )
        yield Frame(image=image, index=index, timestamp_s=index / fps, source=source)
