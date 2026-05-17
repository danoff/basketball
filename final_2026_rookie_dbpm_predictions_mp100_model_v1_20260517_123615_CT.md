# Final 2026 Rookie DBPM Predictions

**Version:** MP ≥ 100 final model predictions  
**Timestamp:** 20260517_123615_CT  
**Prediction file:** `combine_rookie_defensive_prediction_data_2026_v8_mp100_final_20260517_123413_CT.csv`  
**Outcome predicted:** Rookie-season Defensive Box Plus/Minus (`DBPM`)  

---

## 1. Final Prediction Model

The final model was trained on the 2023–2025 rookie-linked NBA Draft Combine dataset, restricted to players who logged at least **100 NBA minutes** as rookies.

Model formula:

```text
DBPM ~ Hand_Width + Standing_Vertical_Leap + Lane_Agility_Time + Wingspan_in + Weight_lbs
```

Estimated equation:

```text
Predicted DBPM =
-6.521
+ 0.390(Hand_Width)
+ 0.046(Standing_Vertical_Leap)
+ 0.291(Lane_Agility_Time)
- 0.084(Wingspan_in)
+ 0.022(Weight_lbs)
```

---

## 2. Training Model Summary

| Metric | Value |
|---|---:|
| Training rows | 89 |
| R² | 0.233 |
| Adjusted R² | 0.187 |
| AIC | 246.773 |
| RMSE | 0.905 |

Final model coefficients:

| Predictor | Coefficient | p-value |
|---|---:|---:|
| Intercept | -6.521 | 0.118 |
| Hand_Width | 0.390 | 0.037 |
| Standing_Vertical_Leap | 0.046 | 0.256 |
| Lane_Agility_Time | 0.291 | 0.328 |
| Wingspan_in | -0.084 | 0.032 |
| Weight_lbs | 0.022 | 0.003 |

---

## 3. 2026 Prediction Coverage

| Item | Count |
|---|---:|
| Total 2026 players | 75 |
| Players with full final-model inputs | 71 |
| Players missing final-model inputs | 4 |

Players missing full final-model inputs:

- Jayden Quaintance
- Luigi Suigo
- Richie Saunders
- Tyler Bilodeau

These players were missing `Standing_Vertical_Leap` and/or `Lane_Agility_Time` in the available 2026 combine data.

---

## 4. Top 20 Final 2026 Predicted Rookie DBPM

|   Rank | Player            |   Predicted_DBPM |   Weight |   Hand_Width |   Standing_Vertical |   Wingspan |   Lane_Agility |
|-------:|:------------------|-----------------:|---------:|-------------:|--------------------:|-----------:|---------------:|
|      1 | Koa Peat          |            0.475 |    245   |        10    |                34.5 |      83.25 |          11    |
|      2 | Tobe Awaka        |            0.468 |    261.4 |        10    |                32.5 |      86.25 |          10.94 |
|      3 | Joshua Jefferson  |            0.462 |    246.2 |        10    |                27   |      82.75 |          11.91 |
|      4 | Karim Lopez       |            0.267 |    221.8 |        11    |                32   |      83.5  |          11.14 |
|      5 | Tarris Reed Jr.   |            0.236 |    263.6 |        10    |                29.5 |      88.25 |          11.03 |
|      6 | Zuby Ejiofor      |            0.142 |    245.2 |         9.75 |                34   |      86    |          11.05 |
|      7 | Trey Kaufman-Renn |            0.122 |    241.2 |         9.75 |                29   |      82.5  |          11.06 |
|      8 | Cameron Boozer    |            0.099 |    252.8 |         9.75 |                28.5 |      85.5  |          11.06 |
|      9 | Morez Johnson     |            0.073 |    250.6 |        10    |                33.5 |      87.5  |          10.59 |
|     10 | Reuben Chinyelu   |            0.068 |    259.4 |        10.25 |                30.5 |      91.5  |          11.21 |
|     11 | Bruce Thornton    |            0.063 |    223   |         9    |                29.5 |      77    |          11.55 |
|     12 | Hannes Steinbach  |            0.051 |    248   |        10    |                30   |      86.25 |          10.9  |
|     13 | Flory Bidunga     |            0.025 |    228.6 |        10.5  |                34   |      87.25 |          11.24 |
|     14 | Keyshawn Hall     |           -0.084 |    227.4 |         9.75 |                30   |      82.25 |          11.15 |
|     15 | Brayden Burries   |           -0.115 |    215.4 |         9.25 |                35   |      78    |          10.59 |
|     16 | John Blackwell    |           -0.18  |    199.6 |         9.5  |                28   |      74.25 |          11.23 |
|     17 | Otega Oweh        |           -0.2   |    216   |         9.5  |                31   |      80.25 |          11.2  |
|     18 | Trevon Brazile    |           -0.204 |    225.6 |        10.25 |                36   |      87.75 |          10.84 |
|     19 | Jacob Cofie       |           -0.208 |    232   |         9.5  |                29.5 |      84    |          11.3  |
|     20 | Tobi Lawal        |           -0.22  |    214.4 |         9    |                40   |      82.5  |          11.15 |

---

## 5. Interpretation

The final model produces a compressed leaderboard. The top predicted players are positive, but the highest projected rookie DBPM is below +0.50. This is consistent with the model being trained on a more stable sample of rookies who played at least 100 minutes, rather than including tiny-minute outliers.

The top three predictions are:

1. **Koa Peat** — 0.475
2. **Tobe Awaka** — 0.468
3. **Joshua Jefferson** — 0.462

The final model primarily rewards:

- **Weight**, which was the strongest positive predictor in the training model.
- **Hand width**, which was also a statistically significant positive predictor.
- **Standing vertical leap**, which remained directionally positive but was not statistically significant.
- **Lane agility time**, retained as a standard movement measure but not statistically significant.
- **Wingspan**, which had a negative coefficient in this multivariable specification and should be interpreted cautiously.

The practical takeaway is:

> The final exploratory model suggests that early NBA defensive translation may depend more on functional physicality and ball-disruption traits than raw length alone.

---

## 6. Important Caveats

This model should be treated as an exploratory screening tool, not a scouting grade.

Key caveats:

| Caveat | Why it matters |
|---|---|
| Rookie DBPM is noisy | It depends on team context, role, scheme, teammates, and minutes. |
| MP ≥ 100 helps but does not solve context | Players still have very different roles and opportunities. |
| Combine data is incomplete | Some prospects skip events or do not record values. |
| Sample size is modest | The final model uses 89 training rows. |
| Multicollinearity is likely | Body-size variables overlap with each other. |
| Wingspan coefficient is counterintuitive | It should not be interpreted as evidence that wingspan is bad. |
| No college production included | The current model is intentionally combine-only. |
| Position not included | The model avoids position labels, but role differences still matter. |

---

## 7. Full 2026 Prediction Table

|   Rank | Player                |   Predicted_DBPM |   Weight |   Hand_Width |   Standing_Vertical |   Wingspan |   Lane_Agility |
|-------:|:----------------------|-----------------:|---------:|-------------:|--------------------:|-----------:|---------------:|
|      1 | Koa Peat              |            0.475 |    245   |        10    |                34.5 |      83.25 |          11    |
|      2 | Tobe Awaka            |            0.468 |    261.4 |        10    |                32.5 |      86.25 |          10.94 |
|      3 | Joshua Jefferson      |            0.462 |    246.2 |        10    |                27   |      82.75 |          11.91 |
|      4 | Karim Lopez           |            0.267 |    221.8 |        11    |                32   |      83.5  |          11.14 |
|      5 | Tarris Reed Jr.       |            0.236 |    263.6 |        10    |                29.5 |      88.25 |          11.03 |
|      6 | Zuby Ejiofor          |            0.142 |    245.2 |         9.75 |                34   |      86    |          11.05 |
|      7 | Trey Kaufman-Renn     |            0.122 |    241.2 |         9.75 |                29   |      82.5  |          11.06 |
|      8 | Cameron Boozer        |            0.099 |    252.8 |         9.75 |                28.5 |      85.5  |          11.06 |
|      9 | Morez Johnson         |            0.073 |    250.6 |        10    |                33.5 |      87.5  |          10.59 |
|     10 | Reuben Chinyelu       |            0.068 |    259.4 |        10.25 |                30.5 |      91.5  |          11.21 |
|     11 | Bruce Thornton        |            0.063 |    223   |         9    |                29.5 |      77    |          11.55 |
|     12 | Hannes Steinbach      |            0.051 |    248   |        10    |                30   |      86.25 |          10.9  |
|     13 | Flory Bidunga         |            0.025 |    228.6 |        10.5  |                34   |      87.25 |          11.24 |
|     14 | Keyshawn Hall         |           -0.084 |    227.4 |         9.75 |                30   |      82.25 |          11.15 |
|     15 | Brayden Burries       |           -0.115 |    215.4 |         9.25 |                35   |      78    |          10.59 |
|     16 | John Blackwell        |           -0.18  |    199.6 |         9.5  |                28   |      74.25 |          11.23 |
|     17 | Otega Oweh            |           -0.2   |    216   |         9.5  |                31   |      80.25 |          11.2  |
|     18 | Trevon Brazile        |           -0.204 |    225.6 |        10.25 |                36   |      87.75 |          10.84 |
|     19 | Jacob Cofie           |           -0.208 |    232   |         9.5  |                29.5 |      84    |          11.3  |
|     20 | Tobi Lawal            |           -0.22  |    214.4 |         9    |                40   |      82.5  |          11.15 |
|     21 | Andrej Stojakovic     |           -0.242 |    206   |        10    |                32   |      80.25 |          10.97 |
|     22 | Kylan Boswell         |           -0.287 |    226   |         8.5  |                33   |      79    |          10.82 |
|     23 | Malachi Moreno        |           -0.288 |    242.8 |         9.25 |                25.5 |      85.5  |          11.62 |
|     24 | Allen Graves          |           -0.305 |    225.6 |         9.5  |                27.5 |      84    |          11.76 |
|     25 | Aday Mara             |           -0.313 |    259.8 |         9.5  |                24   |      90    |          11.47 |
|     26 | Tyler Nickel          |           -0.318 |    217.4 |        10    |                26   |      80.5  |          10.88 |
|     27 | Bryce Hopkins         |           -0.321 |    218.8 |        10    |                30   |      82.5  |          10.71 |
|     28 | Nick Martinelli       |           -0.347 |    223.6 |         9.75 |                26.5 |      82    |          11.01 |
|     29 | Ugonna Onyenso        |           -0.348 |    236.8 |        10    |                27   |      88.75 |          11.56 |
|     30 | Tounde Yessoufou      |           -0.354 |    219.8 |         9    |                34   |      82    |          11.09 |
|     31 | Alex Karaban          |           -0.372 |    225.2 |         9.5  |                28   |      83    |          11.19 |
|     32 | Milan Momcilovic      |           -0.391 |    218.2 |         9.5  |                27.5 |      81.25 |          11.22 |
|     33 | Ryan Conwell          |           -0.395 |    214.8 |         9    |                32.5 |      79    |          10.69 |
|     34 | Caleb Wilson          |           -0.399 |    210.8 |         9.75 |                34.5 |      84.25 |          11.17 |
|     35 | Yaxel Lendeborg       |           -0.406 |    241.4 |        10    |                25.5 |      87.25 |          10.82 |
|     36 | Matthew Able          |           -0.443 |    195.8 |        10.5  |                27.5 |      80.25 |          11.08 |
|     37 | Christopher Cenac Jr. |           -0.46  |    239.6 |         9.5  |                33   |      89    |          10.76 |
|     38 | Amari Allen           |           -0.502 |    204.6 |         9.25 |                34.5 |      80    |          10.72 |
|     39 | Jaden Bradley         |           -0.513 |    205.4 |         9.25 |                30.5 |      78.25 |          10.75 |
|     40 | Peter Suder           |           -0.536 |    213.4 |         9    |                28.5 |      80    |          11.23 |
|     41 | Felix Okpara          |           -0.539 |    237.4 |         9    |                29.5 |      86    |          11.01 |
|     42 | Kingston Flemings     |           -0.564 |    183.4 |         9.5  |                33.5 |      75.5  |          10.61 |
|     43 | Nathaniel Ament       |           -0.565 |    210.8 |         9.5  |                31   |      83.5  |          11.27 |
|     44 | Bennett Stirtz        |           -0.567 |    186.2 |         9.75 |                30.5 |      78    |          11.25 |
|     45 | Rafael Castro         |           -0.569 |    224.4 |         9    |                31   |      85.25 |          11.42 |
|     46 | Izaiyah Nelson        |           -0.577 |    219.4 |         9.5  |                32.5 |      86.5  |          11.22 |
|     47 | Henri Veesaar         |           -0.578 |    227.2 |         9.5  |                28   |      86    |          11.2  |
|     48 | Jeremy Fears Jr.      |           -0.589 |    196.2 |         9    |                32   |      76    |          10.62 |
|     49 | Dillon Mitchell       |           -0.597 |    202.2 |         9.75 |                32.5 |      82.5  |          10.94 |
|     50 | Ja'Kobi Gillespie     |           -0.636 |    181.8 |         9.5  |                31.5 |      76    |          10.94 |
|     51 | Anicet Dybantsa       |           -0.656 |    217   |         9    |                33.5 |      84.5  |          11.06 |
|     52 | Dailyn Swain          |           -0.672 |    211.2 |         9.25 |                28   |      82    |          11.25 |
|     53 | Keaton Wagler         |           -0.688 |    188   |         9.25 |                33   |      78.25 |          11.05 |
|     54 | Emanuel Sharp         |           -0.697 |    208.4 |         8.25 |                27.5 |      75    |          10.77 |
|     55 | Baba Miller           |           -0.756 |    208.2 |        10    |                31.5 |      85.75 |          10.71 |
|     56 | Christopher Brown Jr  |           -0.764 |    190.2 |         9.5  |                33.5 |      79.5  |          10.57 |
|     57 | Tyler Tanner          |           -0.782 |    166.8 |        10    |                32   |      76.25 |          10.88 |
|     58 | Darryn Peterson       |           -0.782 |    198.8 |         9.25 |                31.5 |      81.75 |          11.17 |
|     59 | Maliq Brown           |           -0.823 |    216.6 |         9    |                29.5 |      84.75 |          11.22 |
|     60 | Darius Acuff Jr.      |           -0.843 |    185.8 |         9.25 |                31.5 |      78.5  |          10.99 |
|     61 | Billy Richmond III    |           -0.936 |    195.4 |         9.25 |                32.5 |      80    |          10.23 |
|     62 | Labaron Philon        |           -1.011 |    176.2 |         9    |                30.5 |      78.25 |          11.55 |
|     63 | Ebuka Okorie          |           -1.025 |    186   |         9.25 |                31.5 |      79.75 |          10.71 |
|     64 | Isaiah Evans          |           -1.076 |    186   |         9    |                27   |      80.75 |          11.87 |
|     65 | Milos Uzan            |           -1.077 |    185   |         9    |                28   |      77    |          10.7  |
|     66 | Nicholas Boyd         |           -1.212 |    176.2 |         8.25 |                30.5 |      74.5  |          10.78 |
|     67 | Cameron Carr          |           -1.254 |    184.4 |         9.25 |                38   |      84.75 |          10.46 |
|     68 | Meleek Thomas         |           -1.296 |    189.6 |         7.5  |                31.5 |      78.75 |          11.57 |
|     69 | Christian Anderson    |           -1.393 |    180.4 |         8.25 |                31   |      78.25 |          10.85 |
|     70 | Braden Smith          |           -1.466 |    166.6 |         8.25 |                31   |      75.25 |          10.76 |
|     71 | Aaron Nkrumah         |           -1.468 |    188.8 |         8.5  |                28.5 |      82.25 |          11.18 |

---

## 8. Files Referenced

- `combine_rookie_defensive_training_data_2023_2025_final_20260517_112826_CT.csv`
- `combine_rookie_defensive_training_data_2023_2025_mp100_v1_20260517_122604_CT.csv`
- `model_fit_2023_2025_no_shuttle_dbpm_mp100_v1_20260517_122604_CT.csv`
- `model_coefficients_2023_2025_no_shuttle_dbpm_mp100_v1_20260517_122604_CT.csv`
- `combine_rookie_defensive_prediction_data_2026_v8_mp100_final_20260517_123413_CT.csv`
