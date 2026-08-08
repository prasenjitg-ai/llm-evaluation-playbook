# Grounding Failure Taxonomy

Grounding failures are cases where a model's output isn't adequately
supported by the sources it's meant to be drawing from — distinct from
jailbreaks/injection, but often evaluated alongside them since both
concern trustworthiness of output.

## Fabrication
The model states something with no basis in the retrieved source
material — outright invention rather than misreading.

## Misattribution
The model correctly states a fact but attributes it to the wrong
source, or blends claims from multiple sources into one attributed
statement.

## Overgeneralization
The source supports a narrow or conditional claim; the model's output
strips the condition and presents it as general.

## Stale or conflicting sources
The model is grounded in something, but the sources disagree or are
outdated, and the output doesn't surface the uncertainty.

## Why this is harder to evaluate than it looks
Fluent, confident text and well-grounded text look identical on the
surface. Evaluating grounding usually requires either source-level
comparison (checking claims against retrieved text) or human
adjudication — surface-level fluency signals are actively misleading
here.
