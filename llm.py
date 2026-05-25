import json
import os
from typing import Dict, Any
from openai import OpenAI


def generate_analysis(prompt: str) -> Dict[str, Any]:
    api_key = os.getenv("OPENAI_API_KEY")
    model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

    if not api_key:
        return {
            "mode": "fallback",
            "analysis_markdown": "## Lead Assessment\n- lead_score: 68\n- intent_level: Medium-High\n- pain_points: after-sales load, need pilot\n- missing_information: budget, current system, decision process\n- risk_points: timeline expectation unclear; integration unknown\n- next_actions: discovery call + qualification checklist\n- followup_script: Thanks for reaching out. To design the right pilot, could you share your current workflow, budget range, and success metrics?\n- human_review_needed: Yes (commercial scoping)"
        }

    client = OpenAI(api_key=api_key)
    resp = client.responses.create(
        model=model,
        input=prompt,
        temperature=0.2
    )
    text = resp.output_text
    return {"mode": "llm", "analysis_markdown": text}
