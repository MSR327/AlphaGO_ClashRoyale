# Learning plan

Built from the Phase 0 self-check (2026-10-29). Marks: **Y** know it, **~** seen it,
**N** new.

## Starting point

| Area | Y | ~ | N | Reading |
| --- | --- | --- | --- | --- |
| A. Python | virtual envs | CSV to dicts, classes and dataclasses | type hints, generators | Comfortable with basics; the gaps are the tools long-running code leans on |
| B. NumPy and images | image shape `(H, W, 3)` | slicing a crop, `uint8` vs `float32` | broadcasting, vectorised averages | Knows what an image array is, not yet how to compute on it fast |
| C. PyTorch and deep learning | overfitting, convolutions | the training loop | tensors, detector outputs | Concepts are there; hands-on PyTorch is new |
| D. Probability and RL | expected value, sample size, RL vocabulary, supervised vs RL | | explore vs exploit | Strong; ready for Phase 3 ideas |

In short: the ideas side is strong, and the gaps are practical Python and NumPy
fluency. That's good news, because Phase 1 is exactly where those get practised on
real data.

## What each phase now includes

Topics marked **from scratch** get a short explanation and a small exercise before we
use them. **Refresher** topics get a quick reminder at the point of use. Anything
marked Y is skipped.

### Phase 1: Game interface and data

- **From scratch: generators.** A recording is a stream of frames; a generator yields
  one frame at a time instead of holding minutes of video in 8 GB of memory.
- **From scratch: type hints.** The recorder passes frames, timestamps and taps
  between modules; hints make those hand-offs checkable by tools before they break.
- **From scratch: broadcasting and vectorised NumPy.** Reading the elixir bar or
  comparing a crop to a reference must run many times a second; a Python loop over
  pixels is far too slow.
- **Refresher: slicing crops, `uint8` vs `float32`.** Every screen region we read is a
  crop, and mixing dtypes silently overflows (`200 + 100` in `uint8` is `44`).
- **Refresher: dataclasses.** A frame record (image, timestamp, source) is a natural
  first dataclass.

### Phase 2: Perception

- **From scratch: tensors.** What PyTorch adds on top of NumPy: devices (CPU, the
  Mac's MPS, a cloud GPU) and automatic gradients.
- **From scratch: what a detector outputs.** Boxes, class labels, confidence scores,
  and why we filter by confidence and remove overlapping boxes.
- **Refresher: the training loop.** We'll write one by hand once before using a
  library's trainer, so the library isn't a black box.

### Phase 3 onward

- **From scratch: explore vs exploit**, introduced in Phase 3 when the agent first
  chooses between a move it knows and one it hasn't tried.

## How we'll check progress

Each from-scratch topic ends with a tiny exercise in the real codebase (a function
plus a test), not a separate tutorial. We redo the relevant self-check questions at
each phase gate.
