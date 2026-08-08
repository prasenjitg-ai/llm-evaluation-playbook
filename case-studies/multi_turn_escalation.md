# Case Study: Multi-Turn Escalation

**Problem.** A model refuses a harmful request outright in a single
turn, but a multi-turn conversation that arrives at the same outcome
gradually — through incremental reframing — can succeed where the
direct version fails.

**Why it's hard.** Each individual turn, viewed in isolation, looks
like a reasonable continuation of the conversation. Single-turn
classifiers see nothing wrong with any one message. The harm is a
property of the trajectory, not any single point on it.

**Evaluation considerations.**
- Requires evaluating full conversation transcripts, not sampled
  single turns.
- Needs adversarial generation that plans a *multi-step* path toward a
  harmful outcome, not just single harmful prompts.
- Detection often benefits from tracking a running signal (e.g., how
  far the conversation has drifted from its opening framing) rather
  than a binary check per turn.

**Possible mitigations.**
- Periodic re-grounding: re-evaluate the conversation against the
  original safety-relevant context at intervals, not just at the
  final turn.
- Trajectory-aware refusal: allow a model to "notice" that a
  conversation has drifted and re-apply judgment, rather than treating
  each turn as independent.
