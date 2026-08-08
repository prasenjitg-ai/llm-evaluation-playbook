# Choosing Metrics for Adversarial Evaluation

## Coverage vs. depth
A wide, shallow benchmark (many categories, few examples each) tells
you where the weak spots roughly are. A narrow, deep benchmark (few
categories, many adversarial variants) tells you how bad the weak spot
actually is. Most real evaluation programs need both, run at different
cadences — wide coverage continuously, deep dives when a category
shows early signal.

## Leading vs. lagging indicators
Failure rate on a static benchmark is a lagging indicator — it tells
you about attacks you already know. A leading indicator (e.g., rate of
successful *novel* adversarial rewrites during red-teaming) tells you
whether your defenses are keeping pace with attacker creativity, which
matters more for systems facing an adaptive adversary.

## Why static benchmarks decay
Once a benchmark is used to train against or gate releases, its
prompts stop measuring the underlying vulnerability and start
measuring memorization of that specific benchmark. Rotating and
regenerating adversarial examples — ideally via mechanism-based
generation rather than hand-curation — keeps a metric meaningful over
time.

## A metric is only as good as its labeling protocol
Two evaluators can disagree sharply on borderline cases (is this
response harmful, or edgy-but-fine?). Investing in a clear, examples-
based labeling rubric before scaling an evaluation matters more than
almost any modeling choice downstream.
