# Technical Research — Rookie DBPM Model Explorer

## BMad Workflow Framing

- Intended workflow: `bmad-technical-research` in BMad's Analysis phase.
- Source guidance: BMad's workflow map describes `bmad-technical-research` as a research workflow for validating technical assumptions and producing research findings; BMad Quick Flow is appropriate for small, clear-scope work that produces a tech spec plus code.
- Local constraint: the BMad npm installer is currently blocked in this environment by npm registry HTTP 403, so this document is a manual BMad-style technical research artifact under `_bmad-output/`.

## Research Question

What is the smallest reliable technical shape for a browser-only basketball model explorer that can:

1. Expose the preferred rookie DBPM model and its caveats.
2. Load the checked-in 2025 training rows and 2026 projection rows without a backend.
3. Let a user calculate, persist, compare, delete, and export custom prospect projections.
4. Remain easy to review in a small analytics repository with no build pipeline.

## Repository Evidence Reviewed

| Evidence | Finding |
|---|---|
| `README.md` | Preferred model is DBPM, not DWS, because DBPM behaves more like a rate-style defensive impact measure. The app should not use rookie outcomes as predictors. |
| `combine_rookie_defensive_model_data_v2_20260516_031444_CT.csv` | 78 total 2025 rows; 43 rows marked `Modeling_Ready`; 41 rows have complete preferred-model inputs plus DBPM outcome. |
| `combine_rookie_defensive_prediction_data_2026_v2_full_model_inputs_20260516_034524_CT.csv` | 75 total 2026 projection rows; 71 have full prediction inputs; 4 rows are missing agility/shuttle inputs and should remain visible but unpredicted. |
| `rookie_dbpm_model_explorer.html` | Current implementation is a self-contained HTML/CSS/JS SPA with embedded model coefficients and seed data. |
| `_bmad-output/project-context.md` | Existing project rules require no runtime third-party dependencies, no build step, row provenance preservation, seed reset, and embedded data-count validation. |

## Technical Assumptions and Validation

| Assumption | Validation | Decision |
|---|---|---|
| A single static HTML file is enough for this feature. | The app only needs deterministic client-side math, table rendering, SVG rendering, local persistence, and CSV export. | Keep the SPA self-contained in `rookie_dbpm_model_explorer.html`. |
| A build step would add more maintenance cost than value right now. | There is no package manifest, test runner, bundler, or app framework in the repo. | Do not introduce npm dependencies or a frontend framework for this slice. |
| Embedded seed data is acceptable for the current data size. | 116 embedded rows are small enough for direct browser parsing/rendering. | Embed the seed rows directly, but keep validation scripts/checks for row counts. |
| `localStorage` is sufficient for ad hoc custom rows. | Custom rows are personal scratchpad data, not canonical model inputs. | Persist custom rows locally and provide a seed-data reset. |
| Missing 2026 inputs should not be silently dropped. | Four 2026 rows lack full prediction inputs; hiding them would obscure data quality/provenance. | Keep missing-input rows visible with `Pred DBPM` as blank/`—`. |
| Browser-only CSV export is adequate. | Exporting filtered board rows requires only Blob/ObjectURL support. | Keep CSV export client-side. |
| The app should avoid external CDNs. | Project context requires offline clone usability and no third-party runtime dependency. | Use plain CSS/JS only. |

## Recommended Technical Approach

1. **Static app shell**: maintain one HTML file with inline CSS and JavaScript.
2. **Model constants**: store coefficients in a `MODEL` object and calculate predictions with a single `predict(row)` function.
3. **Seed rows**: embed 41 complete 2025 training rows and all 75 2026 projection rows, retaining rows with missing inputs for provenance.
4. **Row classes**: use `2025 Training`, `2026 Projection`, and `Custom Projection` as first-class filters.
5. **Custom workflow**: let users name a prospect, enter four numeric measurements, add the custom row to the table, delete it later, and reset all local edits.
6. **Validation strategy**: use lightweight command-line checks rather than a full test framework until the repo adopts a build/test stack.

## Risks and Mitigations

| Risk | Impact | Mitigation |
|---|---|---|
| Embedded data drifts from CSV files. | App predictions or row counts become stale. | Validate embedded counts after each update; if updates become frequent, add a generator script in a later PR. |
| `localStorage` schema changes strand old rows. | Users may see malformed custom rows. | Normalize persisted rows on load and keep reset available. |
| Users overinterpret model output. | Scouting misuse. | Keep model-fit/caveat language visible in README/app copy; preserve DBPM-only framing. |
| Single-file app grows hard to maintain. | Harder reviews. | Extract generation/test scripts only when the next feature requires them. |
| Missing inputs are sorted awkwardly. | UX confusion. | Keep blanks visible and sorted after numeric values by comparator behavior. |

## Follow-up Recommendations

- Add a small generator script only if model coefficients or seed CSVs change often.
- Add a static fixture-based test harness if interactive features continue to grow.
- Add a visible model caveat panel in the app if users begin sharing screenshots externally.
- Consider splitting the BMad artifacts into a `/docs` or `_bmad-output` index if more workflows are added.
