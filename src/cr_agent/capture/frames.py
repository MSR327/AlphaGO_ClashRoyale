"""Frames: the one record the rest of the code receives from capture.

Your job (Phase 1, exercise 1). Write two things in this file so that
`uv run pytest tests/test_frames.py` passes:

1. `Frame`: a frozen dataclass with these fields, in this order:
       image: np.ndarray    height x width x 3, uint8, RGB
       index: int           position in the stream, starting at 0
       timestamp_s: float   seconds since the start of the recording
       source: str          where it came from, e.g. a file name or "live"

2. `iter_frames(images, fps, source)`: a generator that takes any iterable of
   images and yields one `Frame` per image, in order.
       - index counts up from 0.
       - timestamp_s is index / fps.
       - It must be lazy: pull one image from `images` only when the caller asks
         for the next frame (so a long recording never sits in memory).
       - Raise ValueError for an image that is not a uint8 array of shape (H, W, 3).
       - Add type hints to everything.

Stuck on dataclasses or generators? Ask before reading ahead; the tests describe the
behaviour, not the code.
"""
