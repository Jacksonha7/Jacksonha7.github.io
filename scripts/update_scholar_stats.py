"""Fetch Google Scholar citation stats and save to assets/data/scholar_stats.json."""
import json
import time
from pathlib import Path

from scholarly import scholarly

SCHOLAR_ID = "6ZJXY_EAAAAJ"

author = scholarly.search_author_id(SCHOLAR_ID)
author = scholarly.fill(author, sections=["basics"])

stats = {
    "citations": author.get("citedby", 0),
    "h_index": author.get("hindex", 0),
    "i10_index": author.get("i10index", 0),
    "updated_at": time.strftime("%Y-%m-%d"),
}

out_path = Path("assets/data/scholar_stats.json")
out_path.parent.mkdir(parents=True, exist_ok=True)
out_path.write_text(json.dumps(stats, indent=2) + "\n")
print(f"Updated scholar stats: {stats}")
