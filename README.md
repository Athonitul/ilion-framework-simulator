# ILION — Deterministic Execution Safety for AI Agents

ILION is a deterministic pre-execution safety layer for agentic AI systems.

It evaluates whether an agent is allowed to execute a proposed action **before** the action happens.

Unlike approaches centered on text moderation, memory, or post-hoc monitoring, ILION focuses on the core execution problem:

> not just what an agent says or remembers,  
> but what it is allowed to do.

This repository contains the reference proof-of-concept simulator of the ILION framework.

---

## Why ILION matters

As AI systems evolve into autonomous agents that can call APIs, access files, trigger workflows, and perform real-world operations, the safety problem changes.

The critical question is no longer only:

- Is the output harmful?
- Is the reasoning coherent?

It becomes:

- Is this action authorized?
- Should this tool call be allowed?
- Does this operation stay within the agent's permitted scope?

ILION is designed to answer that question deterministically.

---

## Core idea

ILION introduces a semantic verification layer that sits between an agent and execution.

Instead of relying on training, probabilistic classifiers, or persistent memory, ILION uses deterministic semantic geometry and veto logic to classify proposed actions as:

- **ALLOW**
- **BLOCK**

before execution occurs.

---

## What this repository contains

This repository provides a research-grade, stateless simulator demonstrating the main components of the ILION framework:

- **Transient Identity Imprint (TII)**
- **Semantic Vertical Resonance Field (SVRF / SCB)**
- **Identity Deviation Control (IDC)**
- **Consensus Veto Layer (CVL)** — dual-stage veto logic
- **MACS** — Moral Axiological Compatibility Score
- **IIRL** — multi-agent consensus alignment

It is intended as a technical and academic artifact for understanding the framework, testing scenarios, and evaluating deterministic execution safety.

---

## Extended modules (in development)

Beyond the core ILION architecture, additional modules extend the framework toward real-world deployment scenarios:

- **SRM (Session Risk Memory)**  
  A temporal risk accumulation layer that models session-level drift using semantic centroids and exponential decay. Extends stateless per-action authorization to trajectory-aware session-level authorization.

- **PCL (Policy Constraint Layer)**  
  A deterministic layer that encodes explicit execution constraints, defining what actions are permitted, restricted, or conditionally allowed within an agent's operational scope.

These modules are part of ongoing research and are not fully integrated into the current PoC simulator.

---

## What ILION is not

ILION is **not**:

- a foundation model
- a chatbot
- a memory system
- a post-hoc monitoring tool
- a production-ready agent platform

It is a **semantic governance and execution verification layer**.

Its role is to determine whether an action should be permitted before the action reaches the real world.

---

## Repository purpose

This PoC exists to:

- demonstrate deterministic runtime semantic control of agent decisions
- expose axiomatic and consensus-based veto mechanisms
- illustrate identity-conditioned semantic alignment
- support academic review, technical evaluation, and benchmarking
- provide a reference implementation of the ILION architecture

---

## Live demo

**Live demo:**  
https://ilion-project.org

---

## Benchmark and reproducibility

**ILION-Bench v2:**  
This repository includes the benchmark used to evaluate execution safety in agentic systems.

See the `benchmark/` folder for the benchmark files and README.

---

## Research documentation

**Paper (arXiv):**  
https://arxiv.org/abs/2603.13247

**Zenodo (paper + datasets):**  
https://zenodo.org/records/18733566

---

## Positioning

A useful way to think about ILION is:

- memory systems help agents retain information
- reasoning systems help agents plan
- world models help agents predict
- **ILION helps determine whether an action should be allowed at all**

In that sense, ILION is a missing control layer for agentic AI.

---

## Scope

This repository represents a reference proof-of-concept implementation of ILION framework concepts.

It is designed for:

- researchers studying AI safety and agent governance
- engineers exploring deterministic execution control
- organizations evaluating semantic authorization layers for agents
- technical reviewers interested in stateless safety architectures

---

## License

This repository and its associated concepts are released under:

**Creative Commons Attribution–NonCommercial–NoDerivatives 4.0 International (CC BY-NC-ND 4.0)**

Commercial use, derivative works, product integration, or deployment in proprietary systems requires an explicit licensing agreement.

---

## Contact

**Website:** https://ilion-project.org  
**Email:** contact@ilion-project.org
