ILION Framework Simulator
Public research demonstrator · Semantic execution-gate concepts · Agentic AI authorization
> ## THE AGENT HAS ACCESS. DOES THE ACTION HAVE AUTHORITY?
AI agents can have valid credentials and legitimate tool access yet still propose an operation outside the authority granted for that specific action, target, and context.
ILION is an independent research initiative developing a deterministic, model-agnostic, defense-in-depth pre-execution authorization architecture for agentic AI. Its objective is to separate an agent's proposal from the independent decision to permit execution.
The model proposes. ILION authorizes.
Start here
ILION v5 — Research Collaboration & Technology Transfer Brief (Zenodo v48) — current overview and partnership invitation.
ILION v5 × OWASP Architectural Security Crosswalk (Zenodo v47) — public architecture and OWASP mapping.
ILION Gate paper (arXiv) · Session Risk Memory paper (arXiv) — research preprints.
Early SCB/TII CoEmergence research · ILION project website.
Partnership enquiries — contact@ilion-project.org.
---
1. What this repository contains
This repository preserves a public, research-grade simulator of selected ILION semantic-verification and veto concepts. It is a historical and reproducible demonstration artifact — not the complete ILION v5 authorization stack and not a deployable enterprise security gateway.
Path	Contents	Intended use
`index.html`	Browser-based interactive simulator covering selected semantic alignment, identity/deviation, veto, and multi-agent concepts	Explore public demonstrator behavior
`benchmark/`	ILION-Bench v2 synthetic scenario dataset and methodology	Examine research evaluations and limitations
`liora/liora_observer.py`	Separate geometric identity-drift observer with diagnostic logging	Study a research observation component
`LICENSE` and `COMMERCIAL_LICENSE.md`	Existing public license and commercial-contact notices	Review usage terms; see the licensing caveat below
The browser simulator includes research concepts named TII, SCB/SVRF, IDC, CVL, MACS, and IIRL. It uses external JavaScript libraries and offers an optional Gemini API integration for illustrative interactions.
Scope boundary: this repository does not implement the complete v5 pipeline and, by itself, does not enforce authorization against real enterprise tool/API side effects.
2. The execution-authorization problem
For an agentic system, the critical question is not only whether an agent can access a tool, but whether this exact action on this target, with this context, evidence, and scope, is authorized to execute.
ILION's architecture is intended to complement, not replace, existing identity and access management (IAM), enterprise policy decision/enforcement points, workflow controls, and audit infrastructure.
Research questions include:
Can context evidence and policy constraints be coordinated into a consistent authorization decision?
Can individually valid claims fail to justify a particular combination of authority, scope, and action?
Can an independent execution boundary reject an operation before side effects occur?
Does the integrated architecture add measurable security or operational value over properly configured existing authorization systems?
These questions require comparative evaluation; they are not assertions that existing enterprise authorization is absent or ineffective.
3. Current public ILION v5 architecture
The architectural model is a layered pre-execution authorization pipeline:
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
ILION Gate — Role/action compatibility; independent vetoes
             |
             v
SRM — Session Risk Memory [EXPERIMENTAL]
             |
             v
       ALLOW / BLOCK
             |
             v
Execution only through an enforced authorization boundary
```
Dimension	Architectural purpose	Status in this repository
CAP	Check provenance, freshness, scope, and request binding of authorization context	Not implemented here
CGC	Evaluate whether individually valid claims jointly authorize the precise action, target, and scope	Not implemented here
PCL	Enforce deterministic contextual policy constraints	Not implemented here
ILION Gate	Apply role/action compatibility and veto-based pre-execution checks	Earlier simulator concepts only; not the complete current Gate engine
SRM	Investigate temporal, session-level and cumulative risk	Experimental; not integrated here
The architecture is designed for fail-closed, fail-fast decisions at mandatory verification layers. Correct enforcement at the actual execution boundary is essential: an ALLOW/BLOCK label in a browser demonstration is not itself protection against real-world side effects.
4. What the public simulator demonstrates
The interactive demonstration illustrates selected earlier mechanisms:
TII — Transient Identity Imprint: experimental contextual/identity representation.
SCB / SVRF: semantic context and resonance/alignment concepts within the simulator lineage.
IDC — Identity Deviation Control: deviation-oriented comparisons against reference representations.
CVL — Consensus Veto Layer: veto logic illustrated in simulated decision paths.
MACS — Moral Axiological Compatibility Score: experimental value/compatibility scoring.
IIRL: research-oriented multi-agent alignment and consensus demonstrations.
LIORA: a separate Python observer of identity-vector drift, not a production enforcement component.
These mechanisms should not be equated with enterprise policy authorization. In particular, semantic similarity by itself is not proof of permission.
Run the simulator locally
Open `index.html` in a modern browser, or serve the repository from its root:
```bash
python -m http.server 8000
```
Then visit http://localhost:8000.
External JavaScript/model assets may require internet access. Some optional interactions use a user-supplied Gemini API key.
Security note: the current browser code stores that optional key in browser `localStorage` and passes it in a request to the Google API. Use only a restricted, non-production test key; do not enter sensitive enterprise/customer data or production credentials into this research demonstration.
5. Research evidence and limitations
ILION-Bench v2
The repository contains `benchmark/benchmark_v2.csv` with 400 documented synthetic scenarios (380 test / 20 development) and a benchmark methodology README.
This material supports controlled research on proposed-action decisions. It does not establish production robustness. Comparisons with content-moderation tools should not be interpreted as equivalent comparisons with correctly configured enterprise policy engines.
Where Gate-only latency measurements are reported, they do not represent end-to-end CAP → CGC → PCL → Gate → SRM latency.
Separate synthetic banking proof of concept
A separate, non-public executable ILION banking PoC passed 51 automated integration tests in a synthetic environment. In the tested scenarios, denied export requests resulted in no export execution effects.
The banking engines and those tests are not in this GitHub repository. This result is laboratory evidence, not independent enterprise validation, production certification, or demonstrated superiority over IAM, OPA, or Cedar implementations.
A useful next experiment is a reproducible comparison against properly configured authorization baselines that measures incremental detections, legitimate-action false blocks, execution containment, latency, and integration overhead.
6. Published Romanian patent applications and research
Three ILION-related patent applications were published by OSIM in BOPI 8/2026, 28 August 2026:
OSIM publication	Application	Technical focus
RO 139757 A0	a 2026 00170	Deterministic contextual authorization of executable AI-agent actions (PCL lineage)
RO 139758 A0	a 2026 00171	Deterministic temporal authorization and cumulative session risk (SRM lineage)
RO 139759 A0	a 2026 00052	Deterministic geometric/vector-space verification of executable AI-agent decisions (ILION Gate lineage)
These are published patent applications, not granted patents. The scope of any rights depends on the claims, legal status, territory, and applicable law.
Further public references:
ILION Gate preprint — arXiv:2603.13247
Session Risk Memory preprint — arXiv:2603.22350
ILION v5: Research Collaboration & Technology Transfer Brief — Zenodo v48
ILION v5 × OWASP architectural security crosswalk — Zenodo v47
ILION research series — Zenodo concept DOI
Early CoEmergence / SCB / TII research archive
ILION Gate and Session Risk Memory were mentioned as related work by an independent contributor in a CoSAI/OASIS WS4 discussion. This is not official CoSAI endorsement, standards adoption, or independent validation.
7. Research collaboration and technology transfer
ILION welcomes technical discussions with AI security vendors, agent-platform developers, banks, regulated enterprises, cybersecurity integrators, automation providers, and applied research organizations.
Potential collaboration areas:
Independent comparative evaluation and reproducible benchmarking.
Controlled enterprise pilots measuring additional value over existing authorization controls.
Joint research and engineering to mature integration at the true execution boundary.
Technology licensing and strategic IP partnerships, subject to appropriate technical and legal review.
Partnerships and technology-transfer enquiries: contact@ilion-project.org  
Project: ilion-project.org  
Non-confidential collaboration brief: Zenodo v48
Non-public implementation details and confidential architecture extensions are not disclosed in this repository.
8. License and permitted uses
This repository currently contains a CC BY-NC-ND 4.0 notice and a commercial licensing notice. These are separate from patent rights.
Licensing clarification needed: the benchmark documentation currently includes inconsistent CC BY / CC BY-NC-ND statements. Before reusing or redistributing individual code/data assets, verify the applicable license with the rights holder; the README here does not resolve that inconsistency. Public availability alone is not authorization for commercial deployment or patent use.
Research lead: Adrian Chitan  
Contact: contact@ilion-project.org
---
ILION Framework Simulator is a public research artifact, not the full ILION v5 stack or a production execution-authorization service.
