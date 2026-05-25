# AI Growth Copilot (Lead Scoring + Follow-up)

A locally runnable web demo for marketing lead operations.

## Features
- Input or select lead context
- Skill: `lead-scoring-followup` (Agent Skills-style package)
- Tool: `query_product` (queries local business assets)
- ReAct-style runner with auditable trace:
  - Reasoning Summary
  - Act (`query_product`)
  - Observe
  - Answer
- LLM-structured output with anti-fabrication constraints

## Quick Start

1. Create virtual environment and install deps:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Configure API key:

```bash
cp .env.example .env
# set OPENAI_API_KEY in .env
```

3. Run:

```bash
python app.py
```

4. Open `http://127.0.0.1:5000`

## Project Structure

- `app.py` - Flask server and API endpoints
- `runner.py` - ReAct runner orchestration
- `llm.py` - LLM wrapper
- `tools/query_product.py` - product query tool
- `skills/lead-scoring-followup/SKILL.md` - skill definition
- `data/` - mock business assets and sample leads
- `templates/index.html` - simple web UI
- `solution.md` - design rationale and trade-offs

## Notes

- This demo intentionally avoids claiming prices/timelines/cases/capabilities not found in sources.
- If no API key is configured, the app returns a deterministic fallback analysis so the closed loop still runs locally.
