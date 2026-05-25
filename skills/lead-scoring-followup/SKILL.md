---
name: lead-scoring-followup
version: 0.1.0
description: Score and prioritize B2B leads, identify risks and missing information, and draft compliant follow-up guidance.
inputs:
  - lead_context
tools:
  - query_product
outputs:
  - structured_analysis
---

# Skill: lead-scoring-followup

## Objective
Given a lead context, produce a structured assessment for marketing/sales operations while avoiding unsupported claims.

## Required behavior
1. Create a short **Reasoning Summary** (auditable, not full chain-of-thought).
2. Decide whether to call `query_product`.
3. If needed, call `query_product` with `product_of_interest` and related keywords.
4. Observe tool output and produce a structured final answer with:
   - lead score (0-100)
   - intent level
   - pain points
   - missing information
   - risk points
   - next actions
   - follow-up script
   - human review needed (yes/no + reason)
5. Respect forbidden claims policy.

## Guardrails
- Do not invent pricing, timeline, customer cases, or undocumented capabilities.
- If evidence is unavailable, explicitly mark as unknown and request human follow-up.
