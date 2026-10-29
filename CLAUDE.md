# Working on this repo

This is a research and learning project. The owner wants to understand every piece,
not just have code appear.

- Follow the phase process in `README.md`. Check which phase is current before
  starting work, and don't build ahead of the current phase.
- Before code for a new phase, write or update its design note in `docs/design/`.
- Record any lasting choice (tooling, interface, state format, algorithm) as an ADR in
  `docs/adr/`, starting from `0000-template.md`. ADRs start as `Proposed` and the
  owner accepts them.
- When introducing a concept, explain what problem it solves, why it fits here, and
  the main alternative. Ask the owner for their own approach first when it is a
  design question.
- Keep PRs small. Each PR says what it changes and how it was checked.
- Tests live in `tests/`; run `uv run pytest` and `uv run ruff check` before pushing.
- Never commit recordings, datasets, model weights or account details.
