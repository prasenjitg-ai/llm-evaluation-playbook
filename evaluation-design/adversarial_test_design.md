# Designing Adversarial Test Sets

## Start from the mechanism, not the example
Pick a mechanism from `taxonomy/` (e.g., multi-turn erosion), then
generate multiple surface variations of it, rather than starting from
one clever prompt and treating it as representative.

## Vary the surface, hold the mechanism constant
For a given mechanism, vary tone, topic, language, and framing while
keeping the underlying exploit the same. If the model resists 9 of 10
surface variants but fails the 10th, that's more useful signal than a
single pass/fail on one prompt — it tells you the defense is
inconsistent, not absent.

## Include near-miss negatives
A test set that only contains clearly-adversarial prompts can't tell
you if a mitigation is over-triggering on legitimate requests that
merely resemble an attack. Pairing each adversarial case with a
benign near-miss is what catches over-blocking.

## Red-team the evaluation, not just the model
An adversarial test set itself can be gamed if its structure becomes
predictable (e.g., always the same sentence template for a given
category). Periodically trying to defeat your own test set's
structure — not just the model — keeps the evaluation honest.
