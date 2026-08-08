# tools/

Small utilities for working with adversarial evaluation datasets.

## evaluate_dataset.py

Loads a JSON dataset of labeled prompts and prints a summary: counts
by category, counts by expected behavior, and the adversarial-to-benign
ratio of the dataset. This is a dataset-inspection tool, not a model
evaluator — it doesn't call any model or API.

### Run it

```bash
python evaluate_dataset.py sample_prompts.json
```

### Example output

Loaded 8 prompts

By category:
benign 4
instruction_hierarchy 1
indirect_injection 1
persona_framing 1
competing_objective 1

By expected behavior:
comply 4
refuse 4

Adversarial share: 4/8 (50.0%)


### Why this exists

Before evaluating a model against a dataset, it's worth checking the
dataset's own composition — an evaluation set that's accidentally 90%
benign, for example, will make a system look far safer than it is.
This is a first, small step toward the kind of dataset sanity-checking
I'd want before trusting any evaluation result.
