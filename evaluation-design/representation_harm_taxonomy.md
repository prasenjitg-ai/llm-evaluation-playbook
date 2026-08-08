# A Layered Approach to Representation Harm Taxonomy

Representation harms (stereotyping, demeaning, erasure) are some of the
hardest fairness-related harms to measure — unlike allocation or
quality-of-service harms, no single metric objectively captures whether
a piece of text is representationally harmful. Fairness here is closer
to a theoretical construct than a measurable quantity, which means the
measurement approach has to be built deliberately, not assumed.

This is a framework I designed (previously presented externally) for
building granular, sociotechnical test sets for representation harms,
grounded in social organization theory and linguistics rather than
ad-hoc example lists.

## Design principles
A good measurement framework for this class of harm should be:
- **Scalable** — generates test coverage systematically, not one example at a time
- **Automated** — where possible, reduces reliance on slow manual annotation
- **Valid** — grounded in theory, not just intuition about what "feels" harmful
- **Interpretable** — a practitioner can trace *why* something is scored as harmful
- **Inclusive** — covers a broad range of demographic factors and harm types, not just the obvious ones

## The harm taxonomy: traversable in both directions
Representation harms are broken into discrete layers, from abstract to
concrete:

1. **Harm Layer** — top-level harm category (e.g. demeaning, stereotyping, erasure)
2. **Sub-Harm Layer** — a more specific harm within that category (e.g. within "demeaning": equating a group to something devoid of value)
3. **Sub-Harm Pattern Layer** — the concrete linguistic pattern that realizes the sub-harm (e.g. "equate to a disease," "equate to an inanimate object")
4. **Harm Potential Layer** — how strongly the harm is present in a given utterance: **asserted** (explicit), **activated** (implicit but present), **accessible** (invited via term choice, not activated), or **absent**
5. **Social and Linguistic Features** — the grammatical/linguistic mechanics that carry the harm
6. **Concrete Text** — the actual example

The key design idea: this tree can be traversed **top-down** (start from
a harm category, generate diverse concrete examples of it — useful for
building test sets) or **bottom-up** (start from a real piece of text,
walk up the tree to understand *if* and *why* it's harmful — useful for
adjudicating ambiguous cases consistently).

## Why this matters for evaluation design generally
The taxonomy's real value isn't the specific harm categories — it's the
underlying idea that **decomposing a fuzzy, contested harm concept into
discrete, traversable layers makes both generation and adjudication more
consistent and explainable**. The same layered approach generalizes well
beyond representation harms: any harm category that's more of a spectrum
than a binary benefits from being broken into a Harm → Sub-Harm →
Pattern → Potential structure rather than evaluated as one flat label.

## Measurement process
For a given scenario, the process is: choose a harm and demographic
factor of interest → translate it into concrete templates using the
harm tree and relevant lexicons → implement scoring mechanisms that
assess system responses against those templates → document assumptions,
constraints, and known pitfalls in a measurement-model worksheet before
trusting the results → report metrics tied to that specific harm and
factor.

Documenting reliability, validity, and known pitfalls *before* running
a measurement — rather than after seeing a result you like — is what
keeps a fairness metric honest.
