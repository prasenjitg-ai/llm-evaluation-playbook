# Lessons from Deployment

Reflections from designing evaluation systems that gate whether
frontier AI features are ready to ship. General principles, not
specific to any employer or system.

## Benchmark scores alone don't determine launch readiness
A model can score well on a static benchmark and still fail in ways
that matter once real users interact with it in unpredictable ways.
Launch readiness is a judgment call informed by evaluation, not a
threshold crossed on one number.

## Over-blocking is as real a failure as under-blocking
It's easy to optimize purely for "never say the bad thing" and end up
with a system that refuses reasonable requests constantly. Both
failure directions cost trust, just differently — one visibly, one
quietly, through users who stop trying.

## Evaluation should precede mitigation, not follow intuition
The temptation is to fix a failure mode as soon as it's noticed
anecdotally. Without a measurement in place first, you can't tell
whether a fix actually worked, made things worse elsewhere, or just
moved the failure somewhere your evaluation doesn't look.

## Conversation-level harms need different methodology than single-turn harms
Some of the hardest failure modes to catch never show up in any single
response — they're a property of how a conversation drifts over
several turns. Evaluating only sampled single turns systematically
misses this category, no matter how good the single-turn evaluation
is.

## The hardest part isn't detecting known failure modes
It's building evaluation that generalizes to failure modes you haven't
seen yet — which is why I keep coming back to mechanism-based design
(see `evaluation-design/`) over prompt-based lists.
