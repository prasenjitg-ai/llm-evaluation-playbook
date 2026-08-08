# Case Study: Agent Tool Misuse

**Problem.** Once a model can call tools (browse, execute code, use
external APIs), a successful attack doesn't just produce bad text — it
can trigger real-world actions: unwanted purchases, data exfiltration,
destructive operations.

**Why it's hard.** The attack surface now includes every piece of
content the agent might read or receive as a tool result, not just
what the user types (see `taxonomy/prompt_injection.md` on indirect
injection). The agent also has more autonomy to chain actions, so a
single successful injection can cascade into multiple downstream
effects before a human reviews anything.

**Evaluation considerations.**
- Needs threat modeling of the tool surface itself: what can each tool
  actually do, and what's the worst plausible action an attacker could
  trigger through it?
- Evaluation should include adversarial *content* the agent might
  encounter via tools (a poisoned webpage, a malicious file), not only
  adversarial prompts from the user.
- Outcome-based evaluation (did an unwanted action occur) matters as
  much as text-based evaluation (did the model say something harmful).

**Possible mitigations.**
- Least-privilege tool access: agents should default to the minimum
  capability needed for a task, not broad standing access.
- Human-in-the-loop confirmation for consequential actions, calibrated
  to the risk of the specific tool.
- Treating all tool-sourced content as untrusted input by default, with
  explicit boundaries between instructions and retrieved content.
