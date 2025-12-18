# llm-eval-harness

A lightweight evaluation runner for prompt/LLM regression testing. Secret-free by default (uses a stub provider).

## Quickstart
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

python -m src.eval.run_eval
cat reports/latest.json
```

## Tests
```bash
pytest -q
```
