# Bibliography — 2025 NBA Draft Combine / Rookie DWS Dataset

Version: 6  
Timestamp: 20260516_171112_CT

This file is a v6 bibliography update/addendum to `rookie_dws_dataset_bibliography_v5_20260516_054047_CT.md`. It adds a Trevon Brazile player-validation source and the NBA.com Draft Combine strength/agility source used for combine event context.

## Sources carried forward from v5

22. Eisenmann, J. (2018, May 14). *The NBA Combine, correlation, and tryouts: Individuality matters!* Volt Performance Blog.  
    https://blog.voltathletics.com/home/2018/5/14/the-nba-combine-correlation-and-tryouts  
    Notes: Added after Grok surfaced the article. Eisenmann summarizes the Teramoto et al. NBA Draft Combine predictive-validity study and emphasizes that most combine-performance relationships were low, while some body-size/length measures showed moderate relationships with year-3 DBPM. Useful secondary-source context for framing the project as exploratory rather than definitive.

23. Teramoto, M., Cross, C. L., Rieger, R. H., Maak, T. G., & Willick, S. E. (2018). *Predictive validity of National Basketball Association Draft Combine on future performance*. *Journal of Strength and Conditioning Research, 32*(2), 396–408. https://doi.org/10.1519/JSC.0000000000001798  
    Notes: Primary peer-reviewed source on NBA Draft Combine predictive validity. PubMed abstract reports that PCA identified length-size, power-quickness, and upper-body strength components; anthropometric measures and the length-size component showed positive medium-to-large correlations with DBPM, while length-size was significantly associated with future on-court performance in robust PCR models.

## Sources added in v6

24. Sports Reference. (n.d.). *Trevon Brazile College Stats*. Sports-Reference.com College Basketball.  
    https://www.sports-reference.com/cbb/players/trevon-brazile-1.html  
    Notes: Added as a player-level validation/sanity-check source after the standing-reach model ranked Trevon Brazile first in 2026 predicted rookie DBPM. The page provides college DWS, DBPM, BPM, and season/career context, including positive Arkansas and career DBPM values.

25. NBA.com. (n.d.). *NBA Draft Combine: Strength & Agility*. NBA Stats.  
    https://www.nba.com/stats/draft/combine-strength-agility  
    Notes: Added as an official NBA source for Draft Combine strength/agility context, including event fields such as lane agility, shuttle run, and vertical leap. Relevant to the project because the current preferred model uses lane agility and shuttle run, while standing vertical leap is retained as an exploratory variable with non-random missingness/DNP caveats.

## Takeaway updated in v6

Prior research supports a cautious interpretation of this project. Eisenmann’s summary of the Teramoto et al. study states that “most correlations were low,” but that year-3 anthropometric measures had moderate relationships with DBPM. Teramoto et al. report “positive, medium-to-large-sized correlations” between anthropometric measures / length-size and DBPM. In that context, the current model should be framed as consistent with prior evidence that length-size has some defensive signal, while our small-sample 2025 model additionally suggests shuttle performance may be a useful change-of-direction signal.

The Trevon Brazile Sports Reference page provides an additional player-level sanity check for the updated standing-reach model. Brazile ranked first in the 2026 standing-reach model and had a positive college defensive profile, including strong Arkansas and career DBPM values. This does not validate the model by itself, but it supports the public-facing interpretation that the model can surface plausible defensive translation candidates when combine movement, functional reach, and hand-width signals align with prior production.
