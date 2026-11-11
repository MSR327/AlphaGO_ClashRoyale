# 0003. Record matches with scrcpy, not repeated screenshots

- **Status:** Proposed
- **Date:** 2026-11-11
- **Phase:** 1

## Context

We need recordings of real matches: frames to train perception on, and later frames
paired with taps. Hardware and terms of service shape the choice. Development is on a
Mac M2 with 8 GB of memory; play is on a real Android phone with a throwaway account;
emulators are off the table because Supercell's terms prohibit them.

Measured on the owner's phone (1080 x 2400): `adb exec-out screencap -p` takes about
0.67 s per frame (about 1.5 fps). Raw frames are about 7.8 MB each, about 233 MB per
second at 30 fps, so they cannot be streamed or stored uncompressed.

## Options considered

1. **Repeated `adb screencap`.** Needs nothing but adb. About 1.5 fps, far too slow
   for a game with 33 ms frames. Fine for single frames.
2. **`adb shell screenrecord`.** Built into Android. Limited recording length and
   less control over frame rate and size.
3. **scrcpy.** Streams hardware-encoded H.264 over one connection and can record it
   to a file, with options for size and frame rate. Extra tool to install. Works
   on the owner's phone and was smooth in a test.
4. **Capture the phone screen with an HDMI or screen-capture device.** Independent of
   Android, but needs extra hardware.

## Decision

Record matches with scrcpy to video files under `data/` (git-ignored). Keep
`adb screencap` for single frames only. Recordings are read back in Python as a stream
of frames, as set out in the Phase 1 design note.

This ADR covers recording. How touches are captured, how the live bot gets frames, and
the recording resolution are open questions in the design note, to be decided with
their own ADRs.

## Consequences

- We get full matches at a steady rate with a small disk footprint.
- scrcpy's video is lossy (H.264), so very small details may blur. Check on a real
  recording that the elixir bar and troop sprites stay readable before relying on it.
- scrcpy is an extra dependency to install (`brew install scrcpy`) and is not
  managed by uv, so the README must say so.
- We revisit this if the recordings turn out too lossy for perception, or if the
  frame rate is unstable.
