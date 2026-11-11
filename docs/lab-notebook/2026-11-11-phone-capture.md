# 2026-11-11: phone capture

## Goal
Get a first frame from the Android phone onto the Mac, and learn whether screenshots
or a video stream is the right way to see the game.

## What I did
- Installed adb and scrcpy with Homebrew.
- Turned on Developer options (tap Build number 7 times) and USB debugging.
- Ran `adb devices`, then `adb exec-out screencap -p > frame.png` with `time`.
- Ran `scrcpy --no-audio --record=test.mp4` and played for a few seconds.

## What happened
- First tried to enable developer features in TalkBack's "Developer settings" (the
  screen-reader menu). That is a different thing from Android's Developer options.
- `adb devices` first returned nothing useful: USB was set to "No data transfer".
  Switching it to "File Transfer" fixed it.
- Then the device showed as `unauthorized` until the "Allow USB debugging?" prompt on
  the phone was accepted.
- Screen size is 1080 x 2400. One `screencap` took 0.673 s (about 1.5 fps).
- scrcpy mirrored smoothly and recorded a file.

## What I learned
- Raw frames are about 7.8 MB, so 30 fps would be about 233 MB per second. Video
  compression is what makes recording feasible, not an optional extra.
- "adb can't see my phone" has several separate causes: USB mode, cable, and the
  authorisation prompt. Check them one at a time.

## Next
Read the Phase 1 design note, decide on the frame interface, then write a short
`Frame` dataclass and a function that yields frames from a recorded video.
