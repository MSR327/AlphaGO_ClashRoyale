# Phase 0 design note: Foundations

- **Status:** In progress
- **Question:** What does a good research codebase look like?
- **Gate:** CI runs on every pull request; this design note and the first ADRs are merged.

## Why this phase exists

Everything later (capture, perception, training) will produce code, data and
results over months. If we can't reproduce an old result, find why we made a choice,
or pick up after a two-week break, the project stalls. Phase 0 sets up the habits
and tools that prevent that, while the codebase is still tiny and changes are cheap.

## Requirements

1. Anyone (including future us) can clone the repo and run tests with one command.
2. Every lasting decision is written down with its reasons and the rejected options.
3. Every working session leaves a short dated note.
4. Every change goes through a pull request with an automatic check.
5. We know where the owner is starting from, so later explanations pitch at the right level.

## Plan

| Requirement | What we set up | Where |
| --- | --- | --- |
| 1. One-command setup | `pyproject.toml` managed by uv; ruff for lint and format; pytest | repo root |
| 2. Decisions recorded | ADRs, numbered, with a template | `docs/adr/` |
| 3. Session notes | Lab notebook, one file per session | `docs/lab-notebook/` |
| 4. Checked changes | GitHub Actions CI running ruff and pytest; PR template | `.github/` |
| 5. Starting point | Self-check on Python, NumPy, PyTorch and probability | `docs/learning/self-check.md` |

## Study for this phase

Read only what the requirements need:

- **Git and pull requests:** branches, commits, reviewing a diff.
  Why: every change goes through a PR from now on.
- **Testing with pytest:** what a unit test is and why we test the boring parts
  (state model, action mapping) hardest. Why: perception and RL bugs are silent;
  tests are how we notice.
- **ADRs:** Michael Nygard's original post, "Documenting Architecture Decisions".
  Why: we will make about a dozen big choices, and the reasons fade fast.
- **RL vocabulary (preview only):** agent, environment, state, action, reward, policy.
  Why: the roadmap uses these words from Phase 3 on. Sutton and Barto, *Reinforcement
  Learning: An Introduction*, chapter 1.
- **Prior work:** read the KataCR paper (arXiv 2504.04783) and skim its code
  (github.com/wty-yy/katacr). Write a lab-notebook entry on how it splits the problem.

## Open items

- Choose the free cloud GPU option for training (Colab or Kaggle) after checking their
  current limits. Not needed until Phase 2; recorded here so it isn't forgotten.
- Choose a licence for the repo (owner's call).
