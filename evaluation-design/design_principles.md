# Evaluation Design Principles

Ideas I keep coming back to when designing evaluation for deployed
conversational AI systems.

## Evaluate before you mitigate
It's tempting to build a mitigation for a failure mode you've noticed
anecdotally. The evaluation should come first — you need a way to
measure the failure rate before a fix, or you can't tell whether the
fix worked, made it worse, or just moved the failure somewhere your
evaluation doesn't look.

## Mechanism-based evaluation scales better than prompt-based evaluation
A fixed list of known-bad prompts decays the moment attackers shift
technique slightly. Evaluation designed around *mechanisms* (see
`taxonomy/`) generalizes to prompts you haven't seen yet, because it's
testing the underlying vulnerability class, not a specific string.

## Measure robustness, not pass/fail
A single pass/fail number hides whether a system fails rarely-but-
catastrophically or often-but-mildly. Distributional metrics — failure
rate under paraphrase, failure rate under adversarial rewriting of the
same intent — tell you much more about deployment risk than a single
aggregate score.

## Conversation-level harms need conversation-level evaluation
Some failure modes (see `taxonomy/behavioral_harms.md`) only show up
across a trajectory of turns, not in any single response. Evaluating
only single-turn outputs systematically misses this entire class of
risk.

## Over-blocking is also a failure
An evaluation regime that only measures "did the model say something
harmful" will drift toward maximal suppression, which degrades the
product without necessarily improving safety. Good evaluation design
tracks both harm rate and unnecessary refusal rate as a pair, not
separately.
