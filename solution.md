# solution.md

## 1) Design Thinking
I focused on the minimum closed loop and auditability instead of adding heavy infrastructure.
This business problem is mostly about consistency and risk control in pre-sales communication, so I prioritized:
- predictable Skill/Tool boundaries,
- explicit execution trace,
- anti-fabrication constraints,
- locally runnable demo with fallback when API key is missing.

## 2) Why this Skill definition
`lead-scoring-followup` is scoped to one operational job: convert a raw lead into an actionable next-step package.
Its output fields are directly useful to marketing and SDR workflows: score, intent, gaps, risks, next actions, script, and human-review flag.
This keeps the Skill reusable and easy to evaluate.

## 3) Why query_product Tool is needed
Without a Tool boundary, the model can over-rely on prior knowledge and hallucinate product details.
`query_product` centralizes retrieval of approved internal assets:
- product catalog,
- sales SOP,
- forbidden claims policy.
The runner then injects these results as grounding context for final generation.

## 4) ReAct representation
The runner explicitly executes:
1. **Reasoning Summary**: route decision (short, auditable summary only)
2. **Act**: call `query_product`
3. **Observe**: collect tool output
4. **Answer**: produce structured analysis with LLM
The frontend displays this trace so reviewers can see how the answer was produced.

## 5) Context passed to model
The model receives:
- lead context (source/company/industry/message/note),
- retrieved approved assets (product + SOP + forbidden claims),
- output format requirements,
- explicit policy: unknown > fabrication.

## 6) How fabrication is controlled
Controls used:
- policy-as-data (`forbidden_claims.md`),
- prompt constraints in runner,
- tool-grounded context rather than free generation,
- explicit "unknown" instruction,
- human-review flag in output.
This reduces risk of invented pricing, timelines, capabilities, or customer references.

## 7) Business metrics for real deployment
If deployed in a real team, I would track:
- lead prioritization precision (sales-accepted lead rate by score bucket),
- follow-up completeness (required fields captured within 2 touches),
- time-to-first-qualified-response,
- hallucination/compliance incident rate,
- conversion uplift for high-score leads.

## 8) Future Iteration Plan
- Add output schema validator and policy checker before sending result to users.
- Add optional web search mode for public product pages with citation capture and fallback.
- Add feedback loop: sales can mark “useful / not useful” for supervised prompt tuning.
- Add run history and comparison dashboard for operational monitoring.
