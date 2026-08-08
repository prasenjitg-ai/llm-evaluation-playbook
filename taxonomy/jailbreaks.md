# Jailbreak Taxonomy

A working categorization of jailbreak techniques by *mechanism* rather
than by specific example — examples get patched, mechanisms persist.

## 1. Instruction hierarchy exploitation
Attempts to make the model treat user-supplied content as having the
same authority as system-level instructions. Includes role-play framing
("pretend you are a model with no restrictions") and nested-instruction
attacks where a payload is embedded inside content the model is asked
to summarize or translate.

## 2. Multi-turn erosion
No single message looks adversarial, but the conversation gradually
shifts context so that a later response violates a policy the model
would have refused outright if asked directly in turn one. Harder to
catch with single-turn evaluation, which is why turn-level and
session-level evaluation need different designs.

## 3. Encoding and obfuscation
Payloads disguised via encoding (base64, leetspeak, unusual
tokenization, language-switching) to evade keyword or classifier-based
filters that operate on surface text rather than semantic content.

## 4. Persona and framing attacks
Asking the model to adopt a persona, write fiction, or "explain what an
unsafe model would say" as an indirect path to disallowed content —
exploiting the gap between literal refusal and semantic compliance.

## 5. Competing-objective attacks
Exploiting tension between different trained objectives (e.g.,
helpfulness vs. safety) by framing a harmful request as urgent,
altruistic, or already-authorized, so the model's helpfulness training
overrides its safety training.

## Why this matters for evaluation design
Static benchmarks decay because they test *known examples*, not
*mechanisms*. An evaluation suite organized around mechanism categories
generalizes better to novel attacks than one organized around a list of
known-bad prompts.
