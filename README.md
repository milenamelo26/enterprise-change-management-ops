# Enterprise Change Management & PMO Ops 🚀

## Title & Value Proposition
An enterprise-grade, full-stack architectural blueprint designed to orchestrate complex corporate transitions (such as workspace relocations, system migrations, or post-merger integrations). This framework demonstrates a secure, Zero-Trust backend integration with an advanced Generative AI layer engineered to transform unstructured task metadata into deterministic operational insights for strategic People Operations management.

## The Business Problem
During high-impact corporate changes, PMO teams and People Operations encounter severe alignment and stress bottlenecks. Qualitative logs and kanban boards generate significant text overhead that fails to surface systematic resource imbalances, risk exposure, or team burnout metrics. This architecture automates the transformation of unstructured operational data into clear, risk-mitigated metrics ready for downstream People Analytics dashboards.

## Core AI Architecture
The analysis framework operates via a specialized agentic workflow:
1. **Sanitization Interface:** Ingests raw, anonymized operational records to enforce absolute corporate data privacy.
2. **Chain-of-Thought Extraction:** Processes backlog items through an elite PMO persona using Gemini 1.5 Flash.
3. **Structured Pydantic Enforcement:** Guarantees strict JSON compliance to eliminate data drift and allow automated ingestion into business intelligence pipelines.

## System Prompts & Guardrails

### PMO Burnout & Bottleneck Analyzer Prompt
```text
You are an Elite Enterprise PMO Intelligence Architect and Organizational Psychologist.
Your task is to analyze the provided JSON array containing anonymized project task records.

Evaluate the text dataset for:
1. Critical operational bottlenecks or single points of failure in role assignments.
2. Indicators of systemic team burnout or unrealistic velocity expectations based on task urgency.
3. Actionable adjustments to rebalance workloads and preserve psychological safety.

You must output your complete analysis conforming strictly to the requested JSON schema. Do not include conversational prose.
