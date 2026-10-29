# 2026-10-29: project setup

## Goal
Turn the roadmap into a repository we can work in.

## What I did
- Agreed the roadmap: seven phases, each starting from a question and ending at a gate.
- Settled the setup: Mac M2 (8 GB) for development, capture and live play; free cloud
  GPUs for training; recording from an Android phone with scrcpy; a throwaway account.
- Created this repo and the Phase 0 skeleton: README, design note, ADRs 0001 and 0002,
  this notebook, a self-check, Python tooling and CI.

## What happened
Nothing runs against the game yet. CI checks only a smoke test.

## What I learned
Most of the hard work in this project is engineering around the learning algorithm
(seeing the screen, building a state), not the algorithm itself.

## Next
Do the self-check in `docs/learning/self-check.md`, then read the KataCR paper.
