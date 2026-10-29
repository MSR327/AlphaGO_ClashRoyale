# AlphaGO_ClashRoyale

A long-term research and learning project: build an agent that plays Clash Royale
from the screen, the way a person does, and learn the ideas behind it along the way.

**Status:** Phase 0 (Foundations). Nothing plays the game yet.

## How this project works

The work follows a [research roadmap](https://claude.ai/artifact/EkgKtR32MYrnXedKYm78MK)
of seven phases. Each phase:

1. starts from one question the project must answer,
2. learns only the concepts that question needs,
3. writes a short design note before code,
4. builds in small, tested pull requests,
5. ends at a **gate**: exit criteria that must pass before the next phase opens.

| Phase | Question | Gate |
| --- | --- | --- |
| 0 Foundations | What does a good research codebase look like? | CI runs; first design note and ADR merged |
| 1 Game interface and data | How does a program see and touch the game? | One full match recorded with synced frames and inputs |
| 2 Perception | How do we turn pixels into a game state? | State matches hand labels on held-out frames, at an agreed target |
| 3 Environment and baseline | What exactly is an action, and can a simple bot play? | Bot finishes matches unattended; baseline win rate measured |
| 4 Imitation learning | Can the agent copy how a human plays? | Beats the rule-based baseline over a fixed set of matches |
| 5 Reinforcement learning | Can it improve beyond the games it has seen? | Beats the imitation policy, with a confidence interval |
| 6 Evaluation and write-up | What worked, what didn't, and why? | A reproducible agent and a write-up |

## Repository layout

```
docs/
  design/        one design note per phase
  adr/           numbered architecture decision records
  lab-notebook/  dated entries: what we tried, what happened, what we learned
  learning/      self-checks and concept notes
src/cr_agent/    the agent package (subpackages are added as phases need them)
tests/           unit tests
```

Planned subpackages, added only when a phase needs them: `capture`, `perception`,
`state`, `policy`, `actuation`, `env`.

## Development

Requires Python 3.11+ and [uv](https://docs.astral.sh/uv/).

```bash
uv sync            # create .venv and install dev tools
uv run pytest      # run tests
uv run ruff check  # lint
uv run ruff format # format
```

## Ground rules

- **Terms of service.** Supercell's terms prohibit bots, automation software and
  emulators. This project uses a separate throwaway account, plays only against the
  built-in training AI or consenting friends, never ranked or tournament play, and
  does most of its work offline on recorded matches. It is not distributed as a
  usable bot.
- **Data stays out of git.** Recordings and datasets live under `data/` (ignored)
  and are tracked by manifest.
- **Every experiment is reproducible** from a commit hash plus a config file.
