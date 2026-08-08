# Research Ideas

Open questions I keep thinking about — not complete ideas, just
directions I want to explore as I build deeper AI security skills.

## Evaluating agentic memory safety
As agents retain state across sessions, what does it mean for
memory itself to be poisoned rather than a single turn or tool
result? How would you evaluate for that differently than prompt
injection?

## Robustness under context poisoning
If an agent's context window includes retrieved content from
multiple untrusted sources, how do you measure whether the model
is appropriately skeptical of any single source, versus taking
majority-vote content at face value?

## Conversation-level deception metrics
Most evaluation treats deception as a single-response property. Is
there a meaningful way to measure whether a model's behavior across
a conversation is internally consistent with what it claims, versus
drifting?

## Adaptive red-teaming using LLM-generated adversarial prompts
Static adversarial test sets decay. What would a red-teaming loop
look like where the adversarial generator itself adapts based on
which categories are currently passing too easily?

These are genuinely open to me — I don't have answers yet, which is
part of why FAST-style hands-on exposure to the offensive side is
useful before I'd trust my own instincts here.
