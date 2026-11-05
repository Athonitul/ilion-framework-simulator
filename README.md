ILION Framework Simulator
Public research demonstrator · Semantic execution-gate concepts · Agentic AI authorization
> ## THE AGENT HAS ACCESS. DOES THE ACTION HAVE AUTHORITY?
AI agents can have valid credentials, legitimate access to tools, and still propose an operation that falls outside their actual authority.
ILION is an independent research initiative developing a deterministic, model-agnostic, defense-in-depth pre-execution authorization architecture for agentic AI systems. Its objective is to separate an agent's proposed action from the independent decision to permit that action to execute.
The model proposes. ILION authorizes.
ILION v5 — Research Collaboration & Technology Transfer Brief · ILION v5 × OWASP Architectural Crosswalk · Project website / demonstrations
---
1. What this repository is
This repository contains a public, research-grade simulator of selected ILION semantic-verification and veto concepts. It is a historical and reproducible demonstration artifact, not the complete ILION v5 authorization stack and not a deployable enterprise security gateway.
The repository currently includes:
Path	Contents	Intended use
`index.html`	Browser-based interactive semantic runtime simulator with selected role/identity, alignment, veto, and multi-agent research concepts	Explore the behavior of a public research demonstrator
`benchmark/`	ILION-Bench v2 scenario dataset and accompanying methodology	Review and reproduce research evaluations, subject to their documented limitations
`liora/liora_observer.py`	LIORA identity-coherence observer using geometric deviation and diagnostic logging	Study a separate experimental drift-observation component
`LICENSE` and `COMMERCIAL_LICENSE.md`	Existing public licensing notices	Review applicable permissions and commercial enquiries
The simulator explores concepts identified in its code and documentation as TII, SCB/SVRF, IDC, CVL, MACS, and IIRL. Its browser implementation may use external JavaScript libraries and an optional Gemini API integration for illustrative interactions.
Important distinction: the simulator does not implement or validate the complete five-stage ILION v5 pipeline described below. It also does not provide enforcement over a real enterprise tool/API execution boundary on its own.
2. The execution authorization problem
For agentic systems, the critical question is not only whether the agent can access a tool, but whether this particular action, on this target, in this context, with this evidence and scope, should execute.
ILION's architectural direction is to add a separate authorization boundary around proposed operations while complementing existing IAM, policy decision/enforcement points, workflow controls, and audit infrastructure.
The research questions include:
Can independently checked context and policy constraints be coordinated into a consistent execution decision?
Can valid individual authorizations still fail to justify their combination for a specific operation?
Can a model-independent enforcement point reject an operation before side effects occur?
What incremental security and operational value, if any, does this architecture add over properly configured existing authorization systems?
These are subjects for engineering evaluation, not claims that existing enterprise authorization is absent or ineffective.
3. Current public ILION v5 architecture
The present architectural framing is a layered execution-authorization pipeline:
```text
AI agent proposes an operation
             |
             v
CAP — Context Attestation Pipeline
             |
             v
CGC — Claim Graph Coherence
             |
             v
PCL — Policy Constraint Layer
             |
             v
ILION Gate — Role/action compatibility and independent vetoes
             |
             v
SRM — Session Risk Memory [EXPERIMENTAL]
             |
             v
        ALLOW / BLOCK
             |
             v
Execution only if authorized by the applicable enforcement boundary
```
Dimension	Architectural purpose	Status relative to this repository
CAP	Attest the provenance, freshness, scope, and request binding of authorization context	Not implemented here
CGC	Assess whether separately valid claims coherently authorize the exact action, target, and scope	Not implemented here
PCL	Apply explicit deterministic contextual policy constraints	Not implemented here
ILION Gate	Evaluate compatibility of the proposed operation with role/action constraints through veto-based checks	This repo contains earlier simulator concepts, not the complete current gate implementation
SRM	Examine session-level and cumulative temporal risk	Experimental; not integrated here
At the architectural level, mandatory checks are intended to fail closed and stop at the first veto (fail fast). The effectiveness of that design depends on correct integration at the actual execution boundary; a verdict displayed in a browser simulator is not equivalent to preventing a production side effect.
4. What the public simulator demonstrates
The browser demonstration includes selected research mechanisms and terminology:
TII (Transient Identity Imprint) — experimental identity/context representation.
SCB / SVRF — semantic context and resonance/alignment concepts used in the simulator lineage.
IDC (Identity Deviation Control) — deviation-oriented checks against a reference representation.
CVL (Consensus Veto Layer) — veto logic illustrated in simulation.
MACS (Moral Axiological Compatibility Score) — experimental value/compatibility scoring.
IIRL — research-oriented multi-agent alignment/consensus demonstrations.
These mechanisms are not all equivalent to enterprise authorization policies. The simulator illustrates selected decision logic; it should not be treated as evidence that semantic similarity alone establishes permission or that a model-generated response has been independently authorized.
Running the simulator
Open `index.html` in a modern browser, or serve the repository locally for a consistent development environment:
```bash
python -m http.server 8000
```
Then visit `http://localhost:8000`.
An internet connection may be needed for external JavaScript/model assets, and certain optional demonstrations require a user-provided Gemini API key. Do not enter production credentials or sensitive banking/customer information into the research demonstrator.
5. Research evidence and limitations
ILION-Bench v2
The repository includes `benchmark/benchmark_v2.csv`, with 400 documented synthetic scenarios (380 test / 20 development), and a benchmark methodology README.
These materials help examine proposed-action classification in controlled research settings. They do not establish production robustness, and comparisons against content-moderation systems should not be presented as comparisons against well-configured enterprise authorization engines.
Any reported gate latency concerns the measured component and test environment, not end-to-end CAP → CGC → PCL → Gate → SRM throughput.
Separate banking integration research
A separate, non-public, executable ILION banking proof of concept has passed 51 automated integration tests in a synthetic environment. In the tested workflows, denied export requests produced no export execution effects.
That implementation and its tests are not contained in this GitHub repository. The result is lab evidence, not a claim of independent enterprise validation, production certification, or demonstrated superiority over IAM / OPA / Cedar implementations.
A proposed next step is a reproducible comparative benchmark against properly configured enterprise authorization baselines, measuring additional detections, false blocks, latency, integration complexity, and containment at the true execution point.
6. Published intellectual property and research
Three ILION-related Romanian patent applications were published by OSIM in BOPI 8/2026 on 28 August 2026:
OSIM publication	Application number	Published subject / lineage
RO 139757 A0	a 2026 00170	Deterministic contextual authorization of executable AI-agent actions — PCL lineage
RO 139758 A0	a 2026 00171	Deterministic temporal authorization using cumulative session risk — SRM lineage
RO 139759 A0	a 2026 00052	Deterministic geometric/vector-space verification of executable AI-agent decisions — ILION Gate lineage
These are published patent applications, not granted patents. Their scope and enforceability depend on the actual claims, procedural status, applicable jurisdictions, and law.
Further public references:
ILION Gate preprint — arXiv:2603.13247
Current ILION v5 research / technology-transfer brief — Zenodo v48
ILION v5 × OWASP architectural security crosswalk — Zenodo v47
ILION research series — Zenodo concept DOI
Early semantic anchoring and SCB/TII research archive
ILION Gate and Session Risk Memory were mentioned by an independent contributor as related work in a CoSAI/OASIS WS4 discussion. This does not constitute official CoSAI endorsement, standards adoption, or independent validation.
7. Research collaboration and technology transfer
ILION welcomes discussions with AI security developers, agent-platform providers, banks, regulated enterprises, cybersecurity integrators, automation vendors, and applied research teams.
Areas of interest include:
Independent technical evaluation and comparative benchmarking.
Controlled enterprise pilots that measure incremental value over existing authorization controls.
Joint research and engineering to mature execution-boundary integration.
Technology licensing and strategic IP partnerships, subject to legal and technical review.
Technology transfer and partnership contact: contact@ilion-project.org  
Project website: https://ilion-project.org  
Non-confidential collaboration brief: https://zenodo.org/records/23960729
Non-public architecture extensions, proprietary implementations, and detailed commercial terms are not disclosed in this repository.
8. Licensing and scope of use
The repository currently carries a CC BY-NC-ND 4.0 notice and a separate commercial licensing notice. Readers should consult the applicable terms for individual materials, including the benchmark dataset. Public access does not by itself confer patent or enterprise deployment rights.
Because software, datasets, and research text can have different licensing requirements, any commercial reuse or integration should be clarified in writing before implementation.
Research lead: Adrian Chitan  
Contact: contact@ilion-project.org
---
ILION Framework Simulator is a public research artifact, not the complete ILION v5 stack and not a production authorization service.
