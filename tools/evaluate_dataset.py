"""
evaluate_dataset.py

A small utility for working with adversarial evaluation datasets.

What it does:
1. Loads a JSON file of prompts, each labeled with a category and an
   expected behavior (refuse / comply).
2. Groups and counts prompts by category.
3. Computes basic dataset composition stats (e.g. what fraction of the
   set is adversarial vs. benign).
4. Checks category coverage against a known list of attack categories
   worth testing for, and flags gaps.
5. Prints a simple report.

This is a dataset/reporting utility, not a model evaluator — it does
not call any model or API. It's meant as a starting point for
inspecting the shape of an evaluation dataset before running it
against a system.

Usage:
    python evaluate_dataset.py sample_prompts.json
"""

import json
import sys
from collections import Counter


EXPECTED_CATEGORIES = {
    "instruction_hierarchy",
    "indirect_injection",
    "persona_framing",
    "competing_objective",
    "multi_turn_erosion",
    "tool_misuse",
}


def load_dataset(path):
    """Load a JSON file containing a list of prompt records."""
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data


def summarize_by_category(dataset):
    """Count how many prompts fall into each category."""
    categories = [item["category"] for item in dataset]
    return Counter(categories)


def summarize_by_expected_behavior(dataset):
    """Count how many prompts expect a 'refuse' vs 'comply' outcome."""
    behaviors = [item["expected_behavior"] for item in dataset]
    return Counter(behaviors)


def composition_ratio(dataset):
    """
    Compute the ratio of adversarial (non-benign) prompts to the
    total dataset size. Useful sanity check: a dataset skewed too
    heavily toward one side gives a misleading picture of a system's
    real-world failure rate.
    """
    total = len(dataset)
    adversarial = sum(1 for item in dataset if item["category"] != "benign")
    return adversarial, total


def coverage_check(dataset):
    """
    Compare which adversarial categories are actually present in the
    dataset against a known list of categories worth covering. Flags
    gaps so you notice a dataset silently missing an entire attack
    class before trusting results from it.
    """
    present = {item["category"] for item in dataset if item["category"] != "benign"}
    missing = EXPECTED_CATEGORIES - present
    return present, missing


def print_report(dataset):
    print(f"Loaded {len(dataset)} prompts\n")

    print("By category:")
    for category, count in summarize_by_category(dataset).most_common():
        print(f"  {category:<25} {count}")

    print("\nBy expected behavior:")
    for behavior, count in summarize_by_expected_behavior(dataset).most_common():
        print(f"  {behavior:<25} {count}")

    adversarial, total = composition_ratio(dataset)
    pct = (adversarial / total) * 100 if total else 0
    print(f"\nAdversarial share: {adversarial}/{total} ({pct:.1f}%)")

    present, missing = coverage_check(dataset)
    print("\nCoverage check:")
    for cat in sorted(EXPECTED_CATEGORIES):
        mark = "✓" if cat in present else "✗"
        print(f"  {mark} {cat}")
    if missing:
        print(f"\nNote: dataset has no examples covering: {', '.join(sorted(missing))}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python evaluate_dataset.py <path_to_json>")
        sys.exit(1)

    dataset = load_dataset(sys.argv[1])
    print_report(dataset)
