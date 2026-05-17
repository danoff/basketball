#!/usr/bin/env python3
"""
NBA Combine Rookie Defensive Model — Python visualization.
Generates a 3-panel dashboard PNG: top-15 projections bar chart,
actual-vs-predicted scatter, and coefficient chart.

Run from the repo root:
    python3 visualize.py
Output: model_dashboard.png
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.gridspec import GridSpec
import pandas as pd
import numpy as np
from pathlib import Path

# ── Model ────────────────────────────────────────────────────────────────────
INTERCEPT = -8.895696
COEFS = {
    "Wingspan_in":       0.065647,
    "Lane_Agility_Time": 0.638983,
    "Shuttle_Run":      -3.392342,
    "Hand_Width":        0.628937,
}
PVALS = {
    "Wingspan_in": 0.404,
    "Lane_Agility_Time": 0.389,
    "Shuttle_Run": 0.062,
    "Hand_Width": 0.156,
}

# ── Dark theme ───────────────────────────────────────────────────────────────
BG    = "#07111f"
PANEL = "#0d1b2d"
LINE  = "#1e3350"
TEXT  = "#edf5ff"
MUTED = "#8ba5c2"
BLUE  = "#5cc8ff"
GREEN = "#6ef0a3"
RED   = "#ff7a90"
GOLD  = "#ffd166"

plt.rcParams.update({
    "figure.facecolor":  BG,
    "axes.facecolor":    PANEL,
    "axes.edgecolor":    LINE,
    "axes.labelcolor":   MUTED,
    "xtick.color":       MUTED,
    "ytick.color":       MUTED,
    "text.color":        TEXT,
    "grid.color":        LINE,
    "grid.linestyle":    "--",
    "grid.alpha":        0.6,
    "font.family":       "DejaVu Sans",
    "font.size":         11,
    "axes.spines.top":   False,
    "axes.spines.right": False,
})

# ── Load CSVs ────────────────────────────────────────────────────────────────
base = Path(__file__).parent

df25 = pd.read_csv(
    base / "combine_rookie_defensive_model_data_v2_20260516_031444_CT.csv"
)
df26 = pd.read_csv(
    base / "combine_rookie_defensive_prediction_data_2026_v2_full_model_inputs_20260516_034524_CT.csv"
)

# Compute predicted DBPM for 2025 training rows
df25["Predicted_DBPM"] = (
    INTERCEPT
    + sum(COEFS[c] * df25[c] for c in COEFS)
)

# Filter 2025 to model-ready rows
model_df = df25.dropna(
    subset=["Wingspan_in", "Lane_Agility_Time", "Shuttle_Run", "Hand_Width", "DBPM", "MP"]
).query("MP > 0").copy()

# Filter 2026 to complete inputs, sort by prediction
proj26 = (
    df26[df26["Has_Full_Prediction_Inputs"] == True]
    .sort_values("Predicted_DBPM", ascending=False)
    .reset_index(drop=True)
)

# ── Figure layout ─────────────────────────────────────────────────────────────
fig = plt.figure(figsize=(17, 12), facecolor=BG)
gs = GridSpec(2, 2, figure=fig, hspace=0.45, wspace=0.32,
              top=0.92, bottom=0.07, left=0.06, right=0.97)

ax_bar  = fig.add_subplot(gs[0, :])   # full width top
ax_scat = fig.add_subplot(gs[1, 0])   # bottom left
ax_coef = fig.add_subplot(gs[1, 1])   # bottom right

fig.suptitle(
    "NBA Combine Rookie Defensive Model  ·  2026 Predictions",
    fontsize=16, fontweight="bold", color=TEXT, y=0.97,
)

# ── Panel 1: Top-15 2026 projections ─────────────────────────────────────────
top15 = proj26.head(15)
bar_colors = [GREEN if v >= 0 else RED for v in top15["Predicted_DBPM"]]

bars = ax_bar.barh(
    top15["Player"][::-1],
    top15["Predicted_DBPM"][::-1],
    color=bar_colors[::-1],
    edgecolor="none",
    height=0.62,
)

ax_bar.axvline(0, color=LINE, lw=1.5, zorder=2)
ax_bar.set_xlabel("Predicted DBPM", color=MUTED, labelpad=6)
ax_bar.set_title("Top 15 · 2026 Rookie DBPM Projections", fontweight="bold",
                 color=TEXT, pad=10, loc="left")
ax_bar.grid(axis="x", zorder=0)

# Value labels on bars
for bar, val in zip(bars, top15["Predicted_DBPM"][::-1]):
    ax_bar.text(
        val + 0.015, bar.get_y() + bar.get_height() / 2,
        f"{val:+.3f}", va="center", ha="left",
        color=TEXT, fontsize=9,
    )

ax_bar.tick_params(axis="y", labelsize=10)

# ── Panel 2: Actual vs Predicted scatter (2025 training) ─────────────────────
x = model_df["Predicted_DBPM"]
y = model_df["DBPM"]
pt_colors = [GREEN if yi >= xi else RED for xi, yi in zip(x, y)]

ax_scat.scatter(x, y, c=pt_colors, s=58, alpha=0.85, edgecolors="none", zorder=3)

lo = min(x.min(), y.min()) - 0.6
hi = max(x.max(), y.max()) + 0.6
ax_scat.plot([lo, hi], [lo, hi], color=BLUE, lw=1.5, ls="--", alpha=0.45,
             label="Perfect prediction", zorder=2)

# Label biggest outliers
for _, row in model_df.iterrows():
    resid = abs(row["DBPM"] - row["Predicted_DBPM"])
    if resid > 2.8:
        ax_scat.annotate(
            row["Player"].split()[0],
            (row["Predicted_DBPM"], row["DBPM"]),
            xytext=(5, 3), textcoords="offset points",
            fontsize=8.5, color=MUTED,
        )

ax_scat.set_xlabel("Predicted DBPM", labelpad=6)
ax_scat.set_ylabel("Actual DBPM", labelpad=6)
ax_scat.set_title("2025 Training · Actual vs Predicted", fontweight="bold",
                  color=TEXT, pad=10, loc="left")
ax_scat.grid(True, zorder=0)

r2 = float(np.corrcoef(x, y)[0, 1] ** 2)
ax_scat.text(0.04, 0.97, f"R² = {r2:.3f}  ·  n = {len(model_df)}",
             transform=ax_scat.transAxes, va="top", fontsize=9.5, color=MUTED)

above = mpatches.Patch(color=GREEN, label="Above model (underrated)")
below = mpatches.Patch(color=RED,   label="Below model (overrated)")
ax_scat.legend(handles=[above, below], fontsize=8.5,
               framealpha=0.15, facecolor=PANEL, edgecolor=LINE)

# ── Panel 3: Coefficient chart ────────────────────────────────────────────────
labels = ["Wingspan", "Lane Agility", "Shuttle Run", "Hand Width"]
vals   = [COEFS["Wingspan_in"], COEFS["Lane_Agility_Time"],
          COEFS["Shuttle_Run"], COEFS["Hand_Width"]]
pvals  = [PVALS["Wingspan_in"], PVALS["Lane_Agility_Time"],
          PVALS["Shuttle_Run"], PVALS["Hand_Width"]]

c_colors = [GREEN if v >= 0 else RED for v in vals]
c_alphas = [1.0 if p < 0.1 else 0.5 for p in pvals]

bars2 = ax_coef.barh(labels, vals, color=c_colors, edgecolor="none", height=0.45)
for bar, alpha in zip(bars2, c_alphas):
    bar.set_alpha(alpha)

ax_coef.axvline(0, color=LINE, lw=1.5, zorder=2)
ax_coef.set_xlabel("Coefficient value", labelpad=6)
ax_coef.set_title("Model Coefficients (OLS)", fontweight="bold",
                  color=TEXT, pad=10, loc="left")
ax_coef.grid(axis="x", zorder=0)

for bar, val, pv in zip(bars2, vals, pvals):
    sig = " †" if pv < 0.1 else ""
    label = f"{val:+.3f}{sig}   p={pv:.3f}"
    xoff = 0.04 if val >= 0 else -0.04
    ha   = "left" if val >= 0 else "right"
    ax_coef.text(
        val + xoff, bar.get_y() + bar.get_height() / 2,
        label, va="center", ha=ha, fontsize=9, color=TEXT,
    )

ax_coef.text(0.04, 0.04, "† p < 0.10  (full model R² = 0.258, Adj R² = 0.176)",
             transform=ax_coef.transAxes, fontsize=8, color=MUTED, va="bottom")

# ── Uniform spine styling ─────────────────────────────────────────────────────
for ax in (ax_bar, ax_scat, ax_coef):
    ax.set_facecolor(PANEL)
    for spine in ax.spines.values():
        spine.set_edgecolor(LINE)

# ── Save ──────────────────────────────────────────────────────────────────────
out = base / "model_dashboard.png"
fig.savefig(out, dpi=150, bbox_inches="tight", facecolor=BG)
print(f"Saved → {out}")
plt.close(fig)
