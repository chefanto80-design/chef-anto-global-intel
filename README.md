# Chef Anto Global Intelligence Agent 🌍

**A daily world brief on food, food waste, agriculture, water, energy, money, hospitality and AI, turned into actions, content hooks and new agent ideas for Chef Anto.**
Part of the [Chef Anto AI Agency](https://github.com/chefanto80-design/chef-anto-agent). Built by Chef Anto (Antoanela Alexander), Miami.

## What it does
1. **Searches the web** for the last 24–48 hours across 8 areas (it never answers from memory)
2. Keeps only real, dated stories from credible sources, **each with a link**
3. Writes: Top 3 · By area · Opportunities · Content hook of the day · Agent lab · Watch list
4. Skips an area if nothing verifiable happened, and says so instead of padding
5. Under 700 words. No investment advice. Drafts only.

## Files
| Path | What it is |
|---|---|
| [`skill/SKILL.md`](skill/SKILL.md) | The agent's full instructions (Claude skill) |
| [`demo/output.md`](demo/output.md) | Real brief for Sep 30, 2026, verbatim |
| [`tests/check_brief.py`](tests/check_brief.py) | Structure, sourcing and length checker (+ optional link check) |

## How to use
**Claude app:** zip the `skill` folder renamed to `chef-anto-global-intel`, upload it in Claude's Settings → Skills, make sure web search is on, then ask:
> Use chef-anto-global-intel. Today's Chef Anto Daily Brief.

**Claude Code:** `mkdir -p ~/.claude/skills/chef-anto-global-intel && cp skill/SKILL.md ~/.claude/skills/chef-anto-global-intel/`

Tip: run it as a scheduled task every weekday morning.

## Real demo
Run on **2026-10-01 (UTC)** in Claude (Cowork), model `claude-opus-5-5`, by invoking the `chef-anto-global-intel` skill. The agent ran 6 web searches and tried to open 9 pages (6 opened, 3 blocked).

**Input (exact):**
```
Demo order: Today's Chef Anto Daily Brief.
```

**Output** ([full, verbatim](demo/output.md)), with sources:
- UN News (Sep 29): over a billion meals uneaten daily; food loss and waste ≈ $1 trillion a year
- BLS CPI (Sep 11): food away from home +3.4% vs food at home +2.2% over 12 months; energy +16.3%
- Washington State Food Waste Prevention Week (Sep 28–Oct 4)
- Tandem AI-agent platform for restaurant operators (Sep 30)
- Agent lab idea: an **Energy-Smart Kitchen Agent**

## Test results (only tests actually run)
| # | Test | Result |
|---|---|---|
| 1 | Live run with real web search | ✅ Brief produced; 4 of 8 areas covered, 4 declared "skipped" (no verified story found) |
| 2 | `python3 tests/check_brief.py demo/output.md` | ✅ **13/13 passed**: all sections present, 560 words, every fact bullet has a dated source link, skipped areas declared |
| 3 | Source pages opened during research | ✅ All 5 cited URLs were opened and read by the agent's web-fetch tool on 2026-10-01 |
| 4 | `--links` reachability check from the build sandbox | ❌ Could not run: the sandbox's network blocked those domains. **Not reported as a pass.** Run it on your own computer. |
| 5 | Checker on a deliberately bad sample | ✅ Caught it: **4/13 passed** |

Honest notes from the run: one FAO result was from 2025, so it was dropped; two Miami pages and one CNN page could not be opened, so they were left out.

**Not tested yet:** facts were not re-checked by a human; the brief has not been run on a schedule.

## Run the tests
```bash
python3 tests/check_brief.py demo/output.md          # structure + sourcing
python3 tests/check_brief.py demo/output.md --links  # also checks every link (needs internet)
```

---
Chef Anto 🌿🤓❤️
