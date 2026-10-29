# 0001. Record decisions as ADRs

- **Status:** Proposed
- **Date:** 2026-10-29
- **Phase:** 0

## Context

This project runs for months with long gaps between sessions. We will make roughly a
dozen choices that shape everything after them: how we connect to the game, how we
represent state, which learning method we use. The reasons behind a choice are easy
to forget, and a forgotten reason gets re-argued or quietly broken.

## Options considered

1. **Nothing written down.** No overhead. Reasons are lost, and old choices get
   revisited without knowing why they were made.
2. **One long design document.** Everything in one place. It drifts out of date, and
   it is hard to see when and why something changed.
3. **Architecture decision records (ADRs).** One short numbered file per decision,
   never rewritten; a later ADR supersedes an earlier one. Small overhead per
   decision; history stays readable.

## Decision

Use ADRs in `docs/adr/`, from `0000-template.md`. Each starts as `Proposed` and
becomes `Accepted` when the owner merges it. Phase design notes in `docs/design/`
explain the plan for a phase; ADRs hold the individual choices inside it.

## Consequences

- Each big choice costs ten minutes of writing.
- Anyone can see why the project looks the way it does by reading `docs/adr/` in order.
- Writing down the rejected options is part of the learning: it forces us to
  understand the alternatives, not just the winner.
