from typing import Dict, Any, List
from tools.query_product import query_product
from llm import generate_analysis

SKILL_NAME = "lead-scoring-followup"
SKILL_VERSION = "0.1.0"


def run_lead_scoring(lead_context: Dict[str, Any]) -> Dict[str, Any]:
    trace: List[Dict[str, Any]] = []

    reasoning_summary = (
        "Lead contains business pain and pilot intent. Need product constraints + SOP + forbidden claims "
        "to avoid unsupported commitments. Route: call query_product then produce structured recommendation."
    )
    trace.append({"step": "Reasoning Summary", "content": reasoning_summary})

    act_input = {
        "product_of_interest": lead_context.get("product_of_interest", ""),
        "query": f"{lead_context.get('industry','')} {lead_context.get('customer_message','')}"
    }
    trace.append({"step": "Act", "tool": "query_product", "input": act_input})
    tool_result = query_product(**act_input)
    trace.append({"step": "Observe", "tool_result": tool_result})

    prompt = f"""
You are a B2B marketing lead operations copilot.

Skill: {SKILL_NAME} v{SKILL_VERSION}

Lead Context:
{lead_context}

Business Assets from tool:
{tool_result}

Output requirements:
- Use clear Markdown sections.
- Include: lead score (0-100), intent level, customer pain points, missing information,
  risk points, next actions, follow-up script, human review needed.
- Ground statements in provided assets.
- If unknown, say unknown.
- Do NOT fabricate pricing, timeline commitments, customer cases, or capabilities.
""".strip()

    trace.append({"step": "Answer", "prompt_context": {"skill": SKILL_NAME, "skill_version": SKILL_VERSION}})
    analysis = generate_analysis(prompt)

    return {
        "skill": SKILL_NAME,
        "skill_version": SKILL_VERSION,
        "trace": trace,
        "result": analysis
    }
