# Quick Spec — Finish Rookie DBPM Single-page Explorer

## Goal

Make the browser-only DBPM model explorer usable as a small scouting worksheet rather than a static embedded table.

## User Stories

- As a basketball analytics user, I can calculate a DBPM projection for a custom prospect from four combine measurements.
- As a user, I can save that custom projection to the board for comparison with 2025 and 2026 rows.
- As a user, I can remove saved custom rows without disturbing the seed dataset.
- As a reviewer, I can confirm which BMad context and implementation rules guided the work.

## Acceptance Criteria

- The calculator includes a player-name field and add-to-board action.
- Saved custom rows use `Custom Projection`, persist in `localStorage`, appear in the table filter, and can be deleted.
- Reset restores the original embedded seed data.
- Existing search, sort, CSV export, top-bars, and scatterplot behavior continue to work.
- Script syntax and embedded data counts are validated from the command line.
