"""Refresh citations.js from Google Scholar via SerpApi (google_scholar_author engine).

Run by .github/workflows/citations.yml. Needs the SERPAPI_KEY secret.
Without a key it exits quietly and leaves citations.js unchanged.
"""
import datetime, json, os, sys, urllib.parse, urllib.request

AUTHOR_ID = "p2R-FRoAAAAJ"
OUT = os.path.join(os.path.dirname(__file__), "..", "citations.js")

key = os.environ.get("SERPAPI_KEY")
if not key:
    print("SERPAPI_KEY not set; leaving citations.js unchanged.")
    sys.exit(0)

url = "https://serpapi.com/search.json?" + urllib.parse.urlencode(
    {"engine": "google_scholar_author", "author_id": AUTHOR_ID, "hl": "en", "api_key": key})
with urllib.request.urlopen(url, timeout=60) as r:
    data = json.load(r)

cb = data.get("cited_by") or {}
table = {k: v for row in cb.get("table", []) for k, v in row.items()}
years = [[int(g["year"]), int(g["citations"])] for g in cb.get("graph", []) if "year" in g]
if not years or "citations" not in table:
    print("Unexpected response; leaving citations.js unchanged:", json.dumps(data)[:500])
    sys.exit(0)

out = {
    "updated": datetime.date.today().isoformat(),
    "source": "Google Scholar via SerpApi",
    "total": int(table["citations"]["all"]),
    "h_index": int(table.get("h_index", {}).get("all", 0)),
    "i10_index": int(table.get("i10_index", {}).get("all", 0)),
    "years": sorted(years),
}
with open(OUT, "w") as f:
    f.write("// Auto-updated weekly by .github/workflows/citations.yml. Safe to edit by hand.\n")
    f.write("window.CITATIONS = " + json.dumps(out, indent=1) + ";\n")
print("Updated:", out["total"], "citations,", len(years), "years")
