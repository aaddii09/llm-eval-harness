from pathlib import Path
import json
from src.eval.run_eval import run

def test_run_generates_summary(tmp_path: Path) -> None:
    data_path = tmp_path / "cases.json"
    data_path.write_text(json.dumps({"cases": [{"id": "x", "prompt": "Rayleigh scattering", "expected_contains": ["Rayleigh"]}]}))
    report = run(data_path)
    assert report["summary"]["total"] == 1
