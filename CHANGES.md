# Changes: Unified Web App + Python Visualization

**Branch:** `claude/explore-repo-files-pwlNl`
**Date:** 2026-05-16

---

## What changed

### `index.html` — rewritten as a single cohesive web app

The repo previously had three separate HTML files, each a different draft of a rookie DBPM explorer:

- `index.html` — a light-themed static summary page (model formula, coefficient table, CSV-loaded leaderboard)
- `rookie_dbpm_model_explorer.html` — a dark interactive app with embedded data, live calculator, SVG scatter plot, and bar chart
- `20260516 meta ai and deepseek HTML draft.html` — a Tailwind-based dark app with gem detection, player editor, CSV import/export, and mobile card layout

All three shared the same model and data but had overlapping and sometimes duplicated features. `index.html` was replaced with a single self-contained page that consolidates the best elements of all three:

**Visual and layout**
- Dark navy color scheme (no external CSS framework)
- Sticky navigation with smooth anchor links
- Hero section: model formula displayed in a monospace box, four metric cards (n, R², Adj R², RMSE)
- Two-column insights section: top-10 2026 projections bar chart (SVG) and 2025 actual-vs-predicted scatter plot (SVG, color-coded green/red by model direction)

**Leaderboard**
- Filterable by player name (live search), class (2026 Projection / 2025 Training / Custom), and DBPM threshold (any / ≥ 0 / top 10)
- Gem toggle: flags 2026 players with predicted DBPM above the median as 💎
- Stats bar: total rows, visible rows, gem count, median predicted DBPM
- Sortable by any column (click headers, toggling asc/desc)
- Desktop table and mobile card layout (responsive breakpoints)
- CSV export of the current filtered view

**Live calculator**
- Enter wingspan, lane agility, shuttle run, and hand width to get an instant predicted DBPM
- Shows approximate rank among loaded 2026 projections
- "Add to board" saves a custom row; custom rows have a delete button
- Reset button restores default values

**Data persistence**
- All player data (including custom rows) stored in `localStorage`
- "Restore data" button resets to embedded seed data

**Model section**
- Full coefficient table (predictor, coefficient, p-value, interpretation)
- Model fit summary grid (n, R², Adj R², AIC, RMSE)
- Caveats section explaining limitations

**Data embedded**
- 41 complete 2025 training rows
- 71 complete 2026 projection rows
- 4 incomplete 2026 rows (missing lane agility / shuttle) included but excluded from predictions

No external dependencies — the page is fully self-contained and works opened directly as a local file or served from GitHub Pages.

---

### `visualize.py` — new Python visualization script

A standalone script that loads the two CSV files from the repository and generates a three-panel dashboard saved as `model_dashboard.png`.

**Panel 1 (top, full width): Top-15 2026 Projected DBPM**
Horizontal bar chart of the 15 highest predicted rookie DBPM values from the 2026 combine class, with value labels on each bar.

**Panel 2 (bottom left): 2025 Actual vs Predicted**
Scatter plot of actual rookie DBPM (Basketball Reference) against model-predicted DBPM for the 41 training-set players. Points above the diagonal (green) outperformed the model; points below (red) underperformed. Largest outliers are labeled by last name. R² and n shown in the plot.

**Panel 3 (bottom right): Model Coefficients**
Horizontal bar chart of the four OLS coefficients. Bars are full opacity when p < 0.10 (marginally significant) and dimmed otherwise. Each bar is labeled with coefficient value and p-value.

All panels use the same dark color palette as `index.html`.

**Dependencies:** `matplotlib`, `pandas`, `numpy`

**Usage:**
```bash
pip install matplotlib pandas numpy
python3 visualize.py
# → model_dashboard.png
```

---

### `model_dashboard.png` — generated output

The PNG produced by `visualize.py`, committed alongside the script so it can be viewed directly on GitHub without running the script locally.

---

## Files changed

| File | Action |
|---|---|
| `index.html` | Rewritten — unified single-page app |
| `visualize.py` | Added — Python visualization script |
| `model_dashboard.png` | Added — generated dashboard image |

---

*Written and signed by Claude (claude-sonnet-4-6), Anthropic, May 2026.*
