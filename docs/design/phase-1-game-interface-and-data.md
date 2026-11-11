# Phase 1 design note: Game interface and data

- **Status:** Draft (the capture interface in section 3 is a proposal for the owner to accept or change)
- **Question:** How does a program see and touch the game?
- **Gate:** One full match recorded with synced frames and inputs.

## Why this phase exists

Every later phase starts from recorded matches: perception is trained on frames,
imitation learning on frames paired with the taps a human made, and the live bot
needs the same frames in real time. If recordings are sloppy (frames without
timestamps, taps that can't be lined up with frames) every later result is suspect.
This phase builds the recording pipeline and makes the data trustworthy while it is
still small.

## What we measured

First hands-on test on the owner's Android phone, over USB:

| Fact | Value |
| --- | --- |
| Screen size | 1080 x 2400 pixels |
| One raw frame (1080 x 2400 x 3 bytes) | about 7.8 MB |
| Raw data at 30 frames per second | about 233 MB per second |
| `adb exec-out screencap -p` | 0.673 s per frame, about 1.5 frames per second |
| `scrcpy` mirror | smooth in play; recording to `.mp4` works |

At 30 fps each frame has about 33 ms. Repeated `screencap` is about 20 times too
slow, so screenshots are only for one-off frames. scrcpy asks the phone's hardware
encoder for H.264 video and streams it over one open connection, which is why it
keeps up.

## Requirements

1. Record a full match as a video with a known frame rate and resolution.
2. Record every touch the human makes, with timestamps.
3. Line up frames and touches on one clock, so "what did the screen look like when
   this tap happened" has a reliable answer.
4. Read frames back one at a time without loading the whole video into 8 GB of
   memory.
5. Give the rest of the code one way to receive frames, whether they come from a
   recorded file or, later, the live phone.
6. Recordings and datasets stay out of git and are tracked by a manifest.

## Proposal: the frame interface (requirement 5)

The owner has not yet settled this one, so this is a recommendation to react to.

Each frame travels with the facts later code will need, in one small record:

```python
@dataclass(frozen=True)
class Frame:
    image: np.ndarray  # height x width x 3, uint8, RGB
    index: int  # position in the stream, starting at 0
    timestamp_s: float  # seconds since the start of the recording
    source: str  # where it came from, e.g. a file name or "live"
```

A frame source is anything that yields `Frame` objects one at a time, in order. In
Python that is a generator, which also meets requirement 4. A video-file reader and,
later, a live reader both follow it, so perception code never needs to know which one
it is reading.

Alternatives:

- **Pass bare arrays.** Simplest, but then timestamp and index travel separately and
  drift out of step. Syncing with taps (requirement 3) needs the timestamp on the frame.
- **Callbacks** (the capture code calls a function for each frame). Fits live streaming
  but is harder to test and awkward for replaying a file at full speed.

## Plan

| Requirement | Work | Notes |
| --- | --- | --- |
| 1 | Record with scrcpy to a file in `data/` (git-ignored) | ADR 0003 |
| 2 | Capture touches, probably with `adb shell getevent -lt` | Open question below |
| 3 | Choose one clock and record both streams against it | Needs a short experiment |
| 4 and 5 | `Frame`, a frame-source generator, a video-file reader | Owner writes the core (spec and test first) |
| 6 | A small manifest file listing each recording and its settings | Format to be an ADR |

Order of work: a short test recording, then the frame interface and file reader,
then touch capture, then sync, then the full match recording that closes the gate.

## Study for this phase

From the learning plan, each with a small exercise in this codebase:

- **Generators:** the frame reader yields one frame at a time.
- **Type hints:** `Frame` and the reader signature are checked by tools.
- **Dataclasses (refresher):** `Frame` is the first one.
- **Slicing and `uint8` vs `float32` (refresher):** crops of the screen, and why
  `200 + 100` in `uint8` is `44`.

## Open questions

- How do we record touches in a way that lines up with the video? `getevent`
  timestamps come from the phone's clock, scrcpy's from the encoder, and the two have
  to be related.
- Does the recording keep the full 1080 x 2400 frame, or do we ask scrcpy to downscale
  (it has `--max-size`)? That trades disk space and decode speed against how small the
  troops and the elixir bar get. Compare on a real recording before deciding.
- Does the live bot read scrcpy's stream directly, or do we only ever process recorded
  matches at first? Leaning towards the second, matching the roadmap's offline-first
  plan. Decide in Phase 3.
- Frame rate: the phone may deliver a variable rate. Check what the recording actually
  contains before assuming 30 fps.

## Terms of service

Same ground rules as the README: throwaway account, built-in training AI or consenting
friends only, recording from the real phone. Nothing in this phase automates play.
