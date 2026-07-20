#!/bin/bash
set -uo pipefail

mkdir -p /logs/verifier

pytest /tests/test_outputs.py -q
status=$?

if [ "$status" -eq 0 ]; then
  reward=1
else
  reward=0
fi

echo "$reward" > /logs/verifier/reward.txt

python3 - <<'PY'
import json
from pathlib import Path
reward = int(Path('/logs/verifier/reward.txt').read_text().strip())
ctrf = {
    'reward': reward,
    'score': reward,
    'verifier': {'success': reward == 1},
}
Path('/logs/verifier/ctrf.json').write_text(json.dumps(ctrf))
PY

exit "$status"
