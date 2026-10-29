# 0002. Python tooling: uv, ruff, pytest, GitHub Actions

- **Status:** Proposed
- **Date:** 2026-10-29
- **Phase:** 0

## Context

The agent will be Python: the ML libraries we need (PyTorch, detection models,
Gymnasium) are Python-first. Development happens on a Mac M2 with 8 GB of memory;
heavy training happens later in cloud GPU notebooks. Both places need the same
dependency versions, or results won't reproduce.

## Options considered

1. **pip + requirements.txt.** Familiar. No lock file by default, so two machines can
   end up with different versions.
2. **Conda.** Good for compiled scientific packages. Slow, heavy, and awkward in cloud
   notebooks that already ship their own Python.
3. **Poetry.** Lock file and project metadata. Slower, and its own config format.
4. **uv.** Standard `pyproject.toml`, a lock file, fast installs, manages the Python
   version too. Newer tool.

For code quality: **ruff** (lint and format in one fast tool) instead of
flake8 + black + isort. For tests: **pytest**, the standard. For CI: **GitHub Actions**,
built into the repo host.

## Decision

Use uv with `pyproject.toml` and a committed `uv.lock`, ruff for lint and format,
pytest for tests, and a GitHub Actions workflow that runs ruff and pytest on every
pull request. Target Python 3.11 or newer.

## Consequences

- `uv sync` gives an identical environment on the Mac and in CI.
- Cloud notebooks can install the same pinned versions from the lock file.
- If a key library (for example a detector) is hard to install with uv on macOS,
  we revisit this in a new ADR rather than mixing tools silently.
