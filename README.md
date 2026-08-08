# LLM Evaluation Playbook

Notes and small tools on evaluating and hardening large language model
systems against adversarial behavior — jailbreaks, prompt injection,
grounding failures, and behavioral harms.

I write these from the perspective of someone who designs the
evaluation systems that gate whether a frontier AI feature is ready to
ship — not from academic security research. The goal here is to
organize how I think about evaluation design, and to keep a running
record of what I'm reading as I build toward deeper technical AI
security skills.

## Structure

- `taxonomy/` — how I categorize classes of adversarial behavior, by mechanism
- `evaluation-design/` — how I think about designing evaluation strategies, not just cataloguing attacks
- `case-studies/` — worked examples: problem, why it's hard, evaluation approach, mitigations
- `examples/` — illustrative (non-operational) attack patterns
- `tools/` — small scripts for working with evaluation datasets
- `lessons_from_deployment.md` — general principles from designing evaluation for real deployment decisions
- `research_ideas.md` — open questions I'm exploring as I build deeper technical security skills
- `references.md` — papers, researchers, orgs I follow

## A note on scope

Nothing here reflects proprietary methods, metrics, or systems from any
employer. This is general, publicly-informed thinking about AI
evaluation and security, written for my own learning.
