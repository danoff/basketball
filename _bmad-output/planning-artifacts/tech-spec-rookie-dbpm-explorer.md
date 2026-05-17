# Tech Spec — Rookie DBPM Model Explorer

## Status

Drafted as a manual BMad-style tech spec after technical research because the full BMad Method installer is unavailable in this environment.

## Scope

Finish and stabilize the browser-only single-page app for exploratory rookie DBPM projections.

### In Scope

- Static app shell in `rookie_dbpm_model_explorer.html`.
- Embedded DBPM model coefficients and seed player rows.
- Search, filter, sort, CSV export, top projection bars, and actual-vs-predicted scatterplot.
- Custom prospect calculator with save/delete persisted rows.
- BMad project context, technical research, tech spec, and sprint tracking artifacts.
- Lightweight command-line validation.

### Out of Scope

- Backend service or database.
- Frontend framework, bundler, npm runtime dependencies, or CDN dependencies.
- Re-training the model or changing coefficients.
- Using rookie DBPM/DWS as prediction inputs.
- Canonical data editing for the checked-in CSV files.

## Architecture

```text
repository root
├── rookie_dbpm_model_explorer.html       # self-contained SPA
├── README.md                             # usage + BMad notes
├── combine_*.csv                         # source data artifacts
└── _bmad-output/
    ├── project-context.md
    ├── research-artifacts/
    │   └── technical-research-rookie-dbpm-explorer.md
    ├── planning-artifacts/
    │   ├── quick-spec-rookie-dbpm-explorer.md
    │   └── tech-spec-rookie-dbpm-explorer.md
    └── implementation-artifacts/
        └── sprint-status.yaml
```

## Data Contract

### Model

```js
MODEL = {
  intercept: -8.895696,
  wingspan: 0.065647,
  lane: 0.638983,
  shuttle: -3.392342,
  hand: 0.628937,
  n: 41,
  r2: 0.258,
  adjR2: 0.176,
  rmse: 1.487
}
```

### Prediction Formula

```text
Predicted DBPM = intercept
               + wingspan_coefficient × Wingspan_in
               + lane_coefficient × Lane_Agility_Time
               + shuttle_coefficient × Shuttle_Run
               + hand_coefficient × Hand_Width
```

Prediction returns `null` when any required numeric input is missing.

### Player Row Shape

```js
{
  id?: string,
  player: string,
  class: '2025 Training' | '2026 Projection' | 'Custom Projection',
  wingspan: number | null,
  lane: number | null,
  shuttle: number | null,
  hand: number | null,
  actualDbpm: number | null,
  minutes: number | null,
  status: string,
  source: string
}
```

## UI Requirements

1. Display model formula and fit metrics.
2. Provide filters for all rows, 2025 training, 2026 projection, custom projection, positive predictions, and top-10 projections.
3. Provide a calculator with player name, wingspan, lane agility, shuttle run, and hand width.
4. Add valid custom calculator rows to the board and persist them in `localStorage`.
5. Show delete controls only for `Custom Projection` rows.
6. Reset local data to embedded seed rows.
7. Export the current filtered table to CSV.
8. Keep missing-input rows visible with blank predictions.

## Persistence

- Key: `rookie-dbpm-single-page-app-v1`.
- Value: JSON array of player rows.
- On load: normalize persisted rows to the current row shape and coerce invalid numerics to `null`.
- On reset: remove the key and restore `SEED_PLAYERS`.

## Validation Plan

Run these checks before committing changes:

1. Extract the inline browser script and run `node --check`.
2. Validate embedded constants and row counts:
   - `MODEL.n === 41`
   - 41 `2025 Training` rows
   - 75 `2026 Projection` rows
3. Exercise custom-row persistence with a DOM/localStorage stub.
4. Serve the page with `python3 -m http.server` and fetch it over HTTP.
5. Run `git diff --check`.

## Acceptance Criteria

- Technical research and tech spec exist under `_bmad-output/`.
- README points readers to the BMad artifacts.
- The SPA still passes syntax, data-count, custom workflow, HTTP smoke, and whitespace checks.
- No new runtime dependencies are introduced.
