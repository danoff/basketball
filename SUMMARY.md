# Rookie Defensive Forecast — Build Summary

**Live file:** `index.html` &nbsp; **Data file:** `data.js`
**Built:** May 17, 2026 &nbsp; **Author:** Charlie Danoff &nbsp; **Designer/Engineer:** Claude (CMO)

---

## What you're shipping

A single-page, no-backend, mobile-responsive web app that lets a reader:

1. Read the headline finding in plain English (hero + dek).
2. See the model's coefficient weights and a 2023–25 backtest (Actual vs Predicted, 89 dots) side-by-side.
3. Read two "Readings" (Mass over length · Hand width is real).
4. Sort, filter, search, and ⭐ favorite ("gem") the 2026 leaderboard of 75 prospects.
5. Type any five combine numbers into the live calculator and get an instant projection + plain-English interpretation.
6. Read the four-cell caveats grid.
7. Click out to sources / your other writing.

---

## File map

| File | Purpose |
|---|---|
| `index.html` | The entire app — HTML + CSS + vanilla JS, single file. No build step. |
| `data.js` | The model coefficients, 89-row training set with actuals, 75-row 2026 projections with precomputed predictions. Rebuilt straight from your CSVs. |

That's it. Drop both into a GitHub repo, enable Pages on `main` (or the `gh-pages` branch), and you're live.

---

## Page sections

| # | Section | Notes |
|---|---|---|
| Hero | Brand · headline · dek · byline · 4 fit stats (n=89, R²=0.233, Adj R²=0.187, RMSE=0.91) · formula | |
| 1 | **What the model is saying** — coefficient bars + Actual vs Predicted scatter, two-up on desktop, stacked on mobile | The visual that lands above the fold |
| 2 | **Reading the coefficients** — two "Readings" pulled from the writeup | |
| 3 | **The 2026 leaderboard** — sortable, searchable, gem-favoritable, filterable by class | 75 projections + 89 training rows accessible via "All" |
| 4 | **Try a prospect** — 5-input live calculator with interpretation copy | |
| 5 | **What this isn't** — lede caveat block + four caveat cells | |
| 6 | **Sources & bibliography** — NBA Combine · Basketball Reference · BPM methodology · Method (notebook) | |
| 7 | **More basketball analysis by Charlie Danoff** — featured Substack card + two posts | |

---

## Model loaded

```
DBPM = −6.521 + 0.390·Hand_Width + 0.046·Standing_Vert
     + 0.291·Lane_Agility − 0.084·Wingspan + 0.022·Weight
```

- n = 89 (MP ≥ 100 across 2023–25 rookie classes)
- R² = 0.233, Adj R² = 0.187, RMSE = 0.91
- Significant: Weight (p=0.003), Hand Width (p=0.037), Wingspan (p=0.032, negative — flagged as multicollinearity in caveats)

---

## Before you go fully public

There are **four placeholder URLs** to edit. Each is `href="#"` — search `index.html` for `href="#"`:

1. **Section 6 · Method** — "Notebook (TBD)" → swap in your Colab / GitHub notebook URL when you publish it.
2. **Section 7 · Subscribe on Substack** — your newsletter URL.
3. **Section 7 · How I built the DBPM model** — your write-up post URL (or just delete the card).
4. **Section 7 · All basketball posts** — your archive/tag page.

Everything else is shippable as-is.

---

## Updating the data later

When new combine results or rookie DBPM updates come in:

1. Replace the CSVs in `/uploads/`.
2. Ask me to "rebuild `data.js` from the new CSVs."
3. I'll re-emit `data.js`; nothing in `index.html` needs to change unless coefficients shift more than rounding.

---

## What was rejected

Two other design directions sit in the `archive/` snapshot of your project (Almanac — print serif/burgundy; Terminal — dark Bloomberg-style). Briefing won on the print-statistical brief and Charlie's preferred copy voice.
