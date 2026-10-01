"""Checks a Chef Anto Daily Brief (skill: chef-anto-global-intel).

Usage: python3 tests/check_brief.py demo/output.md [--links]
--links also requests every source URL and reports the HTTP status.
"""
import re
import sys
import urllib.request

path = sys.argv[1]
text = open(path, encoding="utf-8").read()
checks = []


def check(name, ok, detail=""):
    checks.append((name, ok, detail))


words = len(re.findall(r"\b\w+\b", re.sub(r"\(https?://[^)]+\)", "", text)))
check("Under 700 words (links excluded)", words < 700, f"{words} words")
for sec in ["## Top 3 today", "## By area", "## Opportunities", "## Content hook of the day",
            "## Agent lab", "## Watch list"]:
    check(f"Section present: {sec[3:]}", sec in text)
by_area = text[text.find("## By area"):text.find("## Opportunities")]
bullets = [l for l in by_area.splitlines() if l.startswith("- ")]
check("Every fact bullet in 'By area' has a source link", all("](http" in b for b in bullets),
      f"{sum('](http' in b for b in bullets)}/{len(bullets)}")
months = "Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec"
check("Every fact bullet carries a date", all(re.search(months, b) for b in bullets))
check("Skipped areas are declared, not padded", "Skipped in this run" in by_area)
check("Sign-off in content hook", "Chef Anto 🌿🤓❤️" in text)
check("No buy/sell advice", not re.search(r"\b(buy|sell) (stocks?|shares|bonds)\b", text, re.I))
check("Draft-only statement", "Draft only" in text)

urls = sorted(set(re.findall(r"\]\((https?://[^)]+)\)", text)))
if "--links" in sys.argv:
    for u in urls:
        try:
            req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"})
            code = urllib.request.urlopen(req, timeout=20).status
        except Exception as e:  # noqa: BLE001
            code = getattr(e, "code", type(e).__name__)
        check(f"Source reachable: {u}", code == 200, str(code))

passed = sum(ok for _, ok, _ in checks)
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""))
print(f"\n{passed}/{len(checks)} checks passed")
sys.exit(0 if passed == len(checks) else 1)
