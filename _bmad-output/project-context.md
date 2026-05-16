# Project Context — Basketball Rookie DBPM Model Explorer

## BMad Activation Note

BMad Method installation was attempted with the documented headless installer command:

```bash
npx --yes bmad-method install --yes --modules bmm --tools claude-code --set core.user_name=Codex --set core.output_folder=_bmad-output --set bmm.project_knowledge=research --set bmm.user_skill_level=expert
```

The environment blocked access to the npm registry with HTTP 403, so the full `_bmad/` agent/workflow bundle could not be installed in this run. Following BMad's documented manual project-context path, this file captures the project implementation rules so future BMad workflows can load consistent context from `_bmad-output/project-context.md`.

## Technology Stack & Versions

- Runtime: browser-only HTML, CSS, and JavaScript; no build step.
- Local verification: Node.js 24.x for browser-script syntax checks.
- Local serving: `python3 -m http.server` from the repository root.
- Data inputs: checked-in CSV files for 2025 model-building data and 2026 prediction data.
- App entry point: `rookie_dbpm_model_explorer.html`.

## Critical Implementation Rules

- Keep the web app self-contained unless a future PR explicitly introduces a build pipeline.
- Do not load third-party runtime dependencies from a CDN; the page should work offline after cloning the repo.
- Treat DBPM and DWS as outcomes, not predictive inputs.
- Use the preferred DBPM model coefficients exactly unless the README model section and source data are updated together.
- Preserve row provenance: distinguish `2025 Training`, `2026 Projection`, and user-created `Custom Projection` rows.
- When adding local persistence, provide a seed-data reset path so users can recover the checked-in baseline.
- Validate embedded data counts after changes: 41 complete 2025 training rows and 75 2026 projection rows.

## Current Product Slice

The active scope is a Quick Flow-sized UI feature: finish the single-page model explorer with practical scouting workflows. The expected user can:

1. Review model coefficients and fit metrics.
2. Search, filter, sort, and export the model board.
3. Enter a custom prospect's combine measurements and see a live DBPM prediction.
4. Save custom calculator rows to the board and delete them later.
5. Restore the embedded seed dataset.
