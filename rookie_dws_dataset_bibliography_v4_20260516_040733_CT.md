# Bibliography — 2025 NBA Draft Combine / Rookie DWS Dataset

Version: 4  
Timestamp: 20260516_040733_CT

## Primary data outputs from this chat

1. ChatGPT. (2026). *Clean 2025 NBA Draft Combine rookie DWS master dataset* [CSV dataset].  
   File: `clean_2025_combine_rookie_dws_master.csv`  
   Notes: Uses Copilot’s 75-player invitee list as the roster backbone, merges richer measurement/stat fields from the working combined dataset, preserves the corrected Adou Thiero wingspan, and flags original invitees versus additional/StatLab-only rows.

2. ChatGPT. (2026). *2025 combine heights* [CSV dataset].  
   File: `2025_combine_heights.csv`  
   Notes: Fresh CSV with player names and height values extracted from the previously consolidated 2025 combine table.

3. ChatGPT. (2026). *Current combined rookie DWS dataset* [Excel workbook].  
   File: `current_combined_rookie_dws_dataset.xlsx`  
   Notes: Earlier working workbook with combined measurements, Basketball Reference rookie stats, modeling subset, missingness summary, and source notes.

4. ChatGPT. (2026). *Comparison workbook: Current combined dataset vs. Claude v2* [Excel workbook].  
   File: `comparison_current_vs_claude_v2.xlsx`  
   Notes: Audit workbook comparing the current combined file with Claude’s v2 spreadsheet.

## Public web/data sources

5. Basketball Reference. (2026). *2025-26 NBA rookies*. Basketball-Reference.com.  
   https://www.basketball-reference.com/leagues/NBA_2026_rookies.html

6. Basketball Reference. (2026). *2025-26 NBA advanced stats*. Basketball-Reference.com.  
   https://www.basketball-reference.com/leagues/NBA_2026_advanced.html

7. Basketball Reference. (n.d.). *NBA win shares*. Basketball-Reference.com.  
   https://www.basketball-reference.com/about/ws.html  
   Notes: Added for the definition and methodology background for Win Shares / Defensive Win Shares.

8. NBA.com. (2025). *NBA Draft Combine anthropometric stats / Combine Anthro*. NBA.com.  
   https://www.nba.com/stats/draft/combine-anthro

9. NBA.com / AWS. (2026). *NBA Draft Combine Stat Lab*.  
   https://combine.nba.com/stat-lab?year=2026

10. NBA.com / AWS. (2025). *NBA Draft Combine Stat Lab*.  
    https://combine.nba.com/stat-lab?year=2025  
    Notes: Attempted direct browser access during agent-mode work. The interactive site rendered inconsistently and sometimes returned “Site Unavailable” inside the environment.

11. Hoops Rumors. (2025, May). *NBA announces 75 invitees for 2025 draft combine*.  
    https://www.hoopsrumors.com/2025/05/nba-announces-75-invitees-for-2025-draft-combine.html  
    Notes: Used to validate the 75-player invitee backbone.

12. Sporting News / Yahoo Sports. (2025). *NBA Draft Combine live results: Height, wingspan and more measurements for 2025 NBA Draft prospects*.  
    https://sports.yahoo.com/articles/nba-draft-combine-live-results-081002798.html  
    Notes: Primary source reported by Claude’s measurement spreadsheet; later treated as useful but not fully canonical because of the Adou Thiero wingspan issue.

13. Sporting News. (2024). *NBA Draft Combine live results: Height, wingspan and more measurements for 2024 NBA Draft prospects*.  
    https://www.sportingnews.com/uk/nba/news/nba-draft-combine-results-height-wingspan-measurements-2024/eaf7a513cdeb6e5a44c31fc4  
    Notes: Used during agent-mode exploration for 2024 height/measurement values when the NBA API could not be accessed.

14. NBADraft.net. (2025). *2025 NBA Draft Combine: Measurement & athleticism winners and losers*.  
    https://www.nbadraft.net/2025-nba-draft-combine-measurement-athletic-testing-winners-and-losers/

15. ESPN. (2025). *2025 NBA draft combine: Top prospects, highlights, more*.  
    https://www.espn.com/nba/story/_/id/45104149/2025-nba-draft-combine-chicago-prospects-workout-highlights-measurements-stats-cooper-flagg-dallas-mavericks

16. CBS Sports. (2025). *2025 NBA Draft Combine measurements: Cooper Flagg reaches new height; Ace Bailey comes up short*.  
    https://secure-www.cbssports.com/nba/news/2025-nba-draft-combine-measurements-cooper-flagg-reaches-new-height-ace-bailey-comes-up-short

17. Floor & Ceiling. (2025). *2025 NBA Draft combine wrap-up, measurement takeaways, and intel*. Substack.  
    https://floorandceiling.substack.com/p/nba-draft-combine-sleepers

## NBA Stats API / scraper research sources

18. NBA Stats API endpoint attempted: `draftcombineplayeranthro`.  
    Example URLs attempted:  
    - `https://stats.nba.com/stats/draftcombineplayeranthro?LeagueID=00&SeasonYear=2025-26`  
    - `https://stats.nba.com/stats/draftcombineplayeranthro?SeasonYear=2024&LeagueID=00`  
    Result: Requests from this environment were blocked with HTTP 403 or timed out through browser-based access. No complete API scrape was produced.

19. nba_api_ex documentation. (n.d.). *NBA.Stats.DraftCombine*. HexDocs.  
    https://hexdocs.pm/nba_api_ex/NBA.Stats.DraftCombine.html  
    Notes: Used to verify that the draft combine API supports data types such as `anthro`, `drills`, `spot`, `stats`, and `nonstationary`; also confirms that `SeasonYear` is a required parameter.

20. Search result / public reference consulted: Stack Overflow discussion on scraping NBA combine data.  
    Query context: `draftcombineplayeranthro` endpoint with `LeagueID` and `SeasonYear` parameters.  
    Notes: Used only as a directional clue; no Stack Overflow content was incorporated into the dataset.

## API attempt summary

During agent-mode work, I attempted to access the NBA Stats API endpoint for draft combine anthropometric data:

```text
Endpoint: https://stats.nba.com/stats/draftcombineplayeranthro
Parameters tried:
  LeagueID=00
  SeasonYear=2025-26
  SeasonYear=2024
```

The endpoint appears to be the correct one for anthropometric combine data, based on public API documentation, but it was not usable from this execution environment. Requests returned HTTP 403 “Forbidden,” and browser-based attempts to reach the endpoint or the AWS Stat Lab page either timed out, showed a redirect placeholder, or rendered “Site Unavailable.” Because of that, the 2025 height CSV was generated from the already consolidated combine workbook rather than a fresh official API scrape. For 2024, the Sporting News table was identified as a useful fallback source, but a full official 2024 NBA API export was not obtained.

## Audit notes

- The cleaned CSV treats Copilot’s 75-player file as the official invitee-list backbone.
- Three rows are retained as additional/StatLab-only entries: Lachlan Olbrich, Mackenzie Mgbako, and Yanic Konan Niederhauser.
- Adou Thiero’s wingspan is corrected to `7' 0.00"` and flagged as a likely typo correction from the Yahoo/Sporting News table.
- Basketball Reference is the source for rookie minutes played and Defensive Win Shares.
- Basketball Reference’s Win Shares explainer was added in v3 to document the target metric’s methodological background.
- No complete NBA Stats API scraper was successfully run in this environment.

## Additional player-level validation source

21. Sports Reference. (n.d.). *Flory Bidunga College Stats*. Sports-Reference.com College Basketball.  
    https://www.sports-reference.com/cbb/players/flory-bidunga-1.html  
    Notes: Added as a player-level validation/sanity-check source for comparing the 2026 predicted rookie DBPM leader against college defensive production, including college DBPM, DWS, BLK%, DRB%, and career defensive indicators.