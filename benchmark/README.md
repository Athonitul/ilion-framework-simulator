# ILION-Bench v2: Execution Safety Benchmark for Agentic AI Systems

**Version:** 2.0  
**Author:** Chitan Florin Adrian — Independent AI Safety Researcher  
**Contact:** ilion-project.org  
**License:** Creative Commons Attribution 4.0 International (CC BY-NC-ND 4.0)  
**Related DOI:** [10.5281/zenodo.15410944](https://doi.org/10.5281/zenodo.15410944)  
**Patent:** Application A/00052 — OSIM Romania, February 2026

Paper: arXiv:2603.13247 — https://arxiv.org/abs/2603.13247

\---

## Overview

ILION-Bench v2 is a purpose-built benchmark for evaluating **execution safety gates** in agentic AI systems. It addresses the execution gate problem: given an agent's defined role and a proposed action (tool call, API invocation, workflow step), determine whether the action is consistent with the agent's authorization scope before execution.

This benchmark is **not** a content moderation dataset. It evaluates authorization conformance of proposed actions — a categorically distinct problem from text-level harm classification.

The dataset accompanies the paper:

> Chitan Florin Adrian. \*ILION: Deterministic Pre-Execution Safety Gates for Agentic AI Systems.\* 2026.

\---

## Dataset Statistics

|Split|Scenarios|% of Total|
|-|-|-|
|Test|380|95%|
|Dev|20|5%|
|**Total**|**400**|**100%**|

|Label|Count|%|
|-|-|-|
|BLOCK (malicious)|190|50%|
|ALLOW (benign)|190|50%|

### Attack Category Distribution (Test Set)

|Category|Scenarios|% of Test|Hard Cases|
|-|-|-|-|
|Benign|190|50.0%|—|
|Prompt Injection|44|11.6%|25|
|Tool Misuse|30|7.9%|14|
|Data Exfiltration|25|6.6%|13|
|Social Engineering|25|6.6%|12|
|Jailbreak|20|5.3%|12|
|Privilege Escalation|17|4.5%|10|
|Compliance Violation|15|3.9%|6|
|Destructive Action|14|3.7%|7|
|**Total (test)**|**380**|**100%**|**149 (39%)**|

### Difficulty Distribution (Test Set)

|Difficulty|Count|%|
|-|-|-|
|Easy|136|36%|
|Medium|95|25%|
|Hard|149|39%|

\---

## File Structure

```
benchmark\_v2.csv       — Main benchmark file (400 scenarios)
README.md              — This file
```

\---

## Schema

Each row in `benchmark\_v2.csv` contains the following fields:

|Field|Type|Description|
|-|-|-|
|`id`|string|Unique scenario identifier (e.g., M001, B042)|
|`category`|string|Attack category or `benign`|
|`subcategory`|string|Fine-grained attack subtype|
|`agent\_role`|string|Natural language description of the agent's authorized scope|
|`trigger`|string|Text initiating the agent's decision (may contain injected instructions)|
|`proposed\_action`|string|The action the agent is about to execute, in natural language|
|`expected\_verdict`|string|Ground truth: `BLOCK` or `ALLOW`|
|`difficulty`|string|`easy`, `medium`, or `hard`|
|`rationale`|string|Human-authored explanation of why the verdict is correct|
|`dataset\_split`|string|`test` or `dev`|
|`source\_version`|string|Benchmark version origin (`v1` or `v2`)|

\---

## Attack Categories

Attack categories are derived from the [OWASP LLM Top 10](https://owasp.org/www-project-top-10-for-large-language-model-applications/) and enterprise security literature:

* **prompt\_injection** — Direct and indirect instruction overrides (incl. context overflow, multilingual masking, memory poisoning)
* **tool\_misuse** — Scope inflation, chained tool sequences, unauthorized API usage
* **data\_exfiltration** — Bulk export, slow-drip extraction, covert channel encoding, token theft
* **social\_engineering** — Authority impersonation, urgency framing, trust exploitation
* **jailbreak** — Roleplay framing, multi-turn escalation, persona override
* **privilege\_escalation** — Claimed authority, horizontal access, session hijacking
* **compliance\_violation** — GDPR/HIPAA violations with plausible business framing
* **destructive\_action** — Logic bombs, config corruption, supply chain attacks

\---

## Benchmark Design Principles

**Hard scenarios** (39% of test set) are specifically constructed to challenge vocabulary-based and statistical detection through:

* **Semantic camouflage**: malicious actions expressed in legitimate-sounding vocabulary
* **Multi-step attack chains**: individual steps appear innocuous in isolation
* **Authority impersonation**: malicious framing carried through claimed identity, not action vocabulary
* **Benign false-positives**: authorized sensitive operations that superficially resemble attacks (bulk operations, cross-system data access, emergency actions)

**Benign scenarios** are maximally challenging: authorized emergency actions, bulk data operations, cross-system access, and sensitive document handling — designed to stress-test precision and minimize false positive inflation.

\---

## Baseline Results (from companion paper)

|Method|F1|Precision|Recall|FPR|Latency|
|-|-|-|-|-|-|
|ILION Gate (proposed)|**0.8515**|**91.0%**|80.0%|**7.9%**|**143 μs**|
|Lakera Guard v2|0.8087|74.9%|**87.9%**|29.5%|293 ms|
|OpenAI Moderation API|0.1188|100.0%|6.3%|0.0%|355 ms|
|Llama Guard 3-8B|0.0105|100.0%|0.5%|0.0%|46,767 ms|

*Note: OpenAI Moderation API and Llama Guard 3 results reflect task mismatch (content safety vs. execution safety), not deficiencies of those systems on their intended tasks.*

\---

## Usage

This benchmark is intended for:

1. Evaluating execution safety gate systems for agentic AI
2. Studying the distinction between content safety and execution safety
3. Adversarial robustness research on LLM agent systems
4. Benchmarking inference latency under real-world deployment constraints

### Loading the Dataset

```python
import pandas as pd

df = pd.read\_csv("benchmark\_v2.csv")

# Test set only
test\_df = df\[df\["dataset\_split"] == "test"]

# Dev split (threshold calibration only — do not use for evaluation)
dev\_df = df\[df\["dataset\_split"] == "dev"]

# Hard adversarial scenarios
hard\_df = test\_df\[test\_df\["difficulty"] == "hard"]

print(f"Test scenarios: {len(test\_df)}")
print(f"Dev scenarios: {len(dev\_df)}")
print(f"Hard scenarios: {len(hard\_df)}")
```

\---

## Citation

If you use ILION-Bench v2 in your research, please cite:

```bibtex
@misc{chitan2026ilion,
  title     = {ILION: Deterministic Pre-Execution Safety Gates for Agentic AI Systems},
  author    = {Chitan, Florin Adrian},
  year      = {2026},
  doi       = {10.5281/zenodo.15410944},
  url       = {https://ilion-project.org}
}
```

\---

## License

This dataset is released under the [Creative Commons Attribution 4.0 International (CC BY NC ND 4.0)](https://creativecommons.org/licenses/by/4.0/) license. You are free to share and adapt the material for any purpose, provided appropriate credit is given.

\---

## Changelog

|Version|Date|Changes|
|-|-|-|
|v2.0|February 2026|Expanded to 400 scenarios; added hard difficulty tier (39%); added dev split; 8 attack categories; subcategory coverage for indirect injection, context overflow, multilingual masking, memory poisoning, token theft, slow-drip exfiltration, logic bombs, supply chain attacks|
|v1.0|2025|Initial release — 200 scenarios|



