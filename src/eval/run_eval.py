import json
import time
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from .providers import stub

DATA_PATH = Path("data/test_cases.json")
REPORT_PATH = Path("reports/latest.json")

@dataclass
class CaseResult:
    id: str
    passed: bool
    latency_ms: float
    expected_contains: list[str]
    output_preview: str

def _contains_all(text: str, needles: list[str]) -> bool:
    t = text.lower()
    return all(n.lower() in t for n in needles)

def run(data_path: Path = DATA_PATH) -> dict[str, Any]:
    payload = json.loads(data_path.read_text(encoding="utf-8"))
    results: list[CaseResult] = []

    for c in payload.get("cases", []):
        t0 = time.perf_counter()
        out = stub.generate(str(c["prompt"]))
        latency = (time.perf_counter() - t0) * 1000.0
        expected = list(c.get("expected_contains", []))
        passed = _contains_all(out, expected)
        results.append(
            CaseResult(
                id=str(c["id"]),
                passed=bool(passed),
                latency_ms=round(latency, 2),
                expected_contains=expected,
                output_preview=out[:160],
            )
        )

    summary = {
        "total": len(results),
        "passed": sum(1 for r in results if r.passed),
        "failed": sum(1 for r in results if not r.passed),
        "avg_latency_ms": round(sum(r.latency_ms for r in results) / len(results), 2) if results else 0.0,
    }
    return {"summary": summary, "results": [asdict(r) for r in results]}

def main() -> int:
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    report = run()
    REPORT_PATH.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"Wrote report: {REPORT_PATH}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
