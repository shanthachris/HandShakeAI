import json
import re
from collections import Counter
from pathlib import Path

LOG_PATH = Path("/app/access.log")
REPORT_PATH = Path("/app/report.json")


def parse_access_log(path: Path) -> dict:
    paths = Counter()
    ips = set()
    total = 0

    with path.open("r", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            total += 1
            parts = line.split()
            ips.add(parts[0])
            match = re.search(r'"(?:GET|POST|PUT|DELETE|HEAD|PATCH) (\S+) ', line)
            if match:
                paths[match.group(1)] += 1

    return {
        "total_requests": total,
        "unique_ips": len(ips),
        "top_path": paths.most_common(1)[0][0],
    }


def test_report_exists():
    assert REPORT_PATH.exists(), "no report.json found"


def test_report_valid_json():
    report = json.loads(REPORT_PATH.read_text(encoding="utf-8"))
    assert isinstance(report, dict), "report.json must contain a JSON object"
    assert set(report.keys()) == {"total_requests", "unique_ips", "top_path"}


def test_report_matches_log():
    expected = parse_access_log(LOG_PATH)
    actual = json.loads(REPORT_PATH.read_text(encoding="utf-8"))
    assert actual == expected, "report.json does not match /app/access.log"
