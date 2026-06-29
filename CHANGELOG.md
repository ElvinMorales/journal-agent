Changelog

All notable changes to this artifact system will be documented here.

Unreleased

* No unreleased changes yet.

[v0.3.0] - 2026-06-29

Added

* Guided-intake prompts, response schema, synthetic example, proposal walkthrough, and boundary evals.
* A private-vault runtime package and safe Python standard-library initializer for creating a blank private vault outside the public repository.
* A narrow local stdio MCP server for selected-session reads, allowlisted Memory and State reads, separate pending proposals, guarded exact apply, and metadata-only audit.
* A Memory/State proposal approval and character-exact apply workflow with destination-specific confirmation, State lifecycle triggers, fixed target allowlists, append-only writes, and repeat-apply refusal.
* ChatGPT MCP connector setup documentation, conservative tool-permission guidance, a synthetic first-run walkthrough, a tool review guide, and manual connector safety cases without committed live connectivity configuration.
* A local static runtime viewer with bounded reads, separate Memory/State display, State trigger visibility, proposal status/applied metadata, metadata-only defaults, HTML escaping, restrictive CSP, and repository output-path refusal.
* Automated initializer, MCP boundary, proposal/apply, local viewer, and integrated runtime safety tests.
* Manual synthetic eval matrices for intake boundaries, MCP runtime boundaries, prompt injection, clinical/safety boundaries, ChatGPT connector first run, and local viewer boundaries.
* A runtime validation checklist with schema/test/help commands, stable test counts, leakage scans, generated-output review, and taxonomy audit guidance.
* v0.3.0 release notes, release checklist, usable-product handoff, and release-focused navigation.

Changed

* Updated README navigation to point to the v0.3 runtime docs, private-vault setup, MCP server guide, ChatGPT connector setup, proposal workflow, local viewer, runtime validation checklist, release notes, and usable-product handoff.
* Updated architecture, ADR, roadmap, controller-contract, eval, privacy/security, artifact map, taxonomy mapping, changelog, and backlog documentation for the v0.3 local/private runtime path.
* Clarified v0.2.0 as the manual/control-plane release and v0.3.0 as the optional local/private MCP runtime prototype.
* Separated shipped v0.3.0 scope from future v0.4 candidates such as packaging/CLI polish, stronger CI, formal threat modeling, private deployment design, richer viewer UX, eval automation, framework mappings, adapter docs, and release automation.

Safety / Privacy

* Retained the public repository as the reusable control plane and the private vault as the user-controlled data plane.
* Kept Memory and State separate across intake, proposal creation, review, apply, display, and validation.
* Required reviewed exact wording, destination-specific confirmation, and an allowlisted target before apply.
* Preserved metadata-only audit behavior without logging raw journal content, full proposal bodies, or full approved wording.
* Used synthetic fixtures and public-safe eval scenarios only.
* Added no private data or paths, connector configuration, live endpoint, tunnel setup, generated viewer HTML, screenshot, log, export, token, secret, credential, or other private runtime artifact.
* Made no production-hardening, confidentiality, security, clinical-safety, medical, therapeutic, or crisis-support guarantee.

Intentionally Unsupported

* No hosted service.
* No production authentication, authorization, monitoring, or hardening claim.
* No public dashboard.
* No automatic synchronization.
* No automatic Memory updates.
* No automatic State-to-Memory promotion.
* No whole-vault scan.
* No arbitrary file browser.
* No committed connector configuration, live endpoint, tunnel configuration, or hosted deployment.
* No clinical diagnosis, treatment planning, medication guidance, therapy replacement, crisis counseling, or emergency-support replacement.

[v0.2.0] - 2026-06-28

Added

* Started the Journal Mirror runtime pattern: natural private writing first, reflection after selection, and user-reviewed Memory or State proposals.
* Added a private Obsidian/private-notes runtime starter guide for manual setup, selected-context sessions, and reviewed Memory/State updates without a plugin or server.
* Added Journal Mirror prompts for selected-context sessions, freeform entries, recent pattern review, gentle next actions, and separate Memory/State proposal review.
* Added session and update-review capability modules, extended existing reflection capabilities, and added privacy-first trust metadata to journal skills.
* Added separate Memory and State update proposal schemas.
* Added four synthetic Memory/State lifecycle examples.
* Added a manual proposal review guide for approve, edit, discard, and expiration decisions.
* Added three public-safe synthetic Journal Mirror walkthroughs covering a freeform entry, a recent pattern review, and separate Memory/State proposal decisions.
* Added manual eval cases for template avoidance, evidence-bound reflection, Memory overreach, State staleness, required proposal fields, clinical scope, crisis routing, and selected-context privacy.
* Added a design-only future MCP/VPS controller contract defining the private runtime edge, data classes, narrow allowed operations, denied operations, approval gates, audit expectations, failure mitigations, threat model, and pre-implementation checklist.
* Added synthetic manual future-controller boundary cases.
* Added v0.2.0 release notes, a usable-product handoff, and a pre-release checklist.
* Added conservative cross-platform line-ending normalization through .gitattributes.
* Ignored the local .agents/ scratch workspace without adding its contents.

Changed

* Reframed the repo from a template-heavy journaling scaffold into a public, file-first Journal Mirror Agent pattern.
* Updated navigation, workflow, runtime, taxonomy, output, roadmap, backlog, privacy, security, and lifecycle documentation for the manual prompt/runtime surfaces.
* Linked the future-controller contract through architecture, workflow, lifecycle, proposal-review, privacy, security, taxonomy, roadmap, and navigation docs.
* Tightened README and cross-repo navigation around manual private-first use, public/private boundaries, separate Memory and State review, and release readiness.

Safety / Privacy

* Clarified that proposal artifacts remain private and review-only.
* Clarified that approved wording is copied manually in v0.2.0.
* Preserved separate Memory and State review.
* Preserved selected-context privacy.
* Kept public examples synthetic.
* Added no real journal data, private vault content, logs, screenshots, exports, secrets, credentials, private paths, or private runtime artifacts.
* Added no automatic persistence and no State-to-Memory promotion.

Intentionally Unsupported

* No MCP runtime implementation.
* No connector configuration.
* No hosted endpoint.
* No private-vault initializer.
* No local viewer.
* No Obsidian plugin.
* No server.
* No live runtime.
* No future controller implementation beyond design documentation.

[v0.1.0] - 2026-05-31

Added

* Reposition README as a public reference implementation of the Agentic AI Artifact Taxonomy.
* Add taxonomy mapping documentation across the 14 artifact buckets.
* Add public/private architecture documentation for journal content boundaries.
* Add decision record for keeping public artifacts separate from private journal content.
* Add v0.1.0 release checklist.
* Add GitHub Actions schema validation workflow.
* Add synthetic example audit documentation.

Changed

* Clarify eval cases as synthetic/fictional examples.
* Rename memory example section to Synthetic Shape Example.

Safety / Privacy

* Document public control-plane artifacts vs private user-owned journal content.
* Confirm public examples are synthetic-only or blank templates.
* Keep real journal entries, summaries, memory, state, exports, logs, therapy notes, crisis notes, screenshots, databases, secrets, and identifying details outside the repo.