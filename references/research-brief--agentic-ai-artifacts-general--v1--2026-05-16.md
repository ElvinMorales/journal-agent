---
topic: Agentic AI Artifacts — A General-Purpose Taxonomy
version: 1.0
supersedes: none
date_researched: 2026-05-16
last_updated_signal: 2026-04-14
refresh_after: 2026-11-16
researcher: Claude
intended_use: Loaded by a coding agent that builds agentic AI artifacts (skills, identity files, prompts, schemas, eval suites, etc.) in a project repo. The brief gives the agent the conceptual map and convention knowledge it needs to choose, name, structure, and compose those artifacts correctly.
consuming_agent_profile:
  audience: technical
  verbosity: balanced
  tool_access: [filesystem, web_search]
  domain_familiarity_assumed: medium
scope_in:
  - The 15 categories of agentic AI artifacts (Identity, Operating Style, Capabilities, Tools, Knowledge/Resources, Prompts/Interfaces, Memory, State, Planning, Orchestration/Handoffs, Guardrails/Governance, Outputs/Schemas, Evaluation/Observability, Runtime/Deployment, Learning/Iteration)
  - Definitions, purposes, conventions, common file names within each category
  - Cross-category relationships, dependencies, and composition patterns
  - Framework-spanning patterns (Anthropic Skills, MCP, OpenAI Agents SDK, LangChain/LangGraph, Pydantic AI) treated as illustrations of patterns rather than as the patterns themselves
scope_out:
  - Framework-specific SDK tutorials and syntax-level walkthroughs
  - Domain-tilted examples (clinical, regulated work) — reserved for v2 brief
  - Deployment infrastructure (Kubernetes, serverless, hosting)
  - Comparative evaluation of frameworks ("which is best")
  - Multi-agent system academic theory beyond what is in working frameworks
  - Prompt engineering fundamentals
domain_tags: [agentic-ai, ai-engineering, agent-architecture, context-engineering, llm-systems]
depth: deep-dive
evidence_density: dense
overall_confidence: mixed
sources_count: 30
primary_sources_count: 15
methodology_note: Web search across primary framework documentation (Anthropic, OpenAI, Model Context Protocol, LangChain, Pydantic AI) and engineering blogs from those organizations; user provided a synthesized taxonomy document used as a starting input and re-verified against primaries. All time-sensitive claims dated inline.
---

# Agentic AI Artifacts — A General-Purpose Taxonomy

## TL;DR

An "agentic AI artifact" is a reusable, file-based piece of structure that gives an AI agent some specific capacity — an identity, a skill, a tool, a memory, a guardrail, an output schema. Modern agent design has shifted from "one big system prompt" to a **modular operating system** of cooperating artifacts, because single prompts neither scale to specialized work nor compose across teams. The current ecosystem organizes these artifacts into roughly **15 categories** (Identity, Operating Style, Capabilities, Tools, Knowledge/Resources, Prompts/Interfaces, Memory, State, Planning, Orchestration/Handoffs, Guardrails/Governance, Outputs/Schemas, Evaluation/Observability, Runtime/Deployment, Learning/Iteration). Two organizing principles dominate the design: **progressive disclosure** (load only what's needed when it's needed, codified by Anthropic's Skills standard) and **control-source separation** (the Model Context Protocol's distinction between application-driven Resources, model-controlled Tools, and user-controlled Prompts). The category an artifact belongs to is determined by what *role* it plays for the agent, not by its filename — and the conventions for filenames are still consolidating, with some standards already settled (SKILL.md, AGENTS.md) and others actively emerging (SOUL.md, MEMORY.md).

## Mental Model

Agentic AI artifact design is fundamentally about **decomposing an agent's behavior into separately-versioned, separately-loaded pieces of structure**, so that complexity grows additively rather than as a tangled monolithic prompt.

**Central tensions** — the tradeoffs the domain is constantly negotiating.
- **Always-on context vs. progressively-disclosed context**: anything in the system prompt is paid for on every call; anything loaded on demand is cheaper but must be discoverable. CLAUDE.md/AGENTS.md sit on the always-on side; SKILL.md and Resources sit on the on-demand side. Wrong placement either bleeds context budget or makes the agent miss what it needs.
- **Generality vs. specialization**: a generic agent that can do many things poorly, or a specialist that handles one workflow well and hands off everything else. The trend is toward composable specialists.
- **Composition vs. abstraction**: more artifacts give more control but more surface area; frameworks abstract that surface and risk hiding behavior. Anthropic explicitly recommends starting from raw API calls before reaching for frameworks.
- **Determinism vs. agency**: workflows (predefined code paths orchestrating LLM calls) trade flexibility for predictability; agents (LLMs directing their own tools in a loop) trade predictability for adaptability.
- **Single-prompt simplicity vs. multi-artifact reliability**: a single rich prompt is faster to ship; a 15-artifact agent is more maintainable. The right answer scales with how often the agent runs and how much variance you can tolerate.

**Decision axes** — dimensions along which choices vary.
- **Autonomy**: predefined workflow ↔ ReAct loop ↔ fully autonomous long-horizon agent. More autonomy ⇒ more cost, more variance, more required guardrails.
- **Control source**: application-controlled (Resources) ↔ model-controlled (Tools) ↔ user-controlled (Prompts). Borrowed from MCP's vocabulary, useful far beyond MCP.
- **Loading mode**: always-on (identity, operating-style files) ↔ triggered (skills, playbooks) ↔ on-demand reference (resources, knowledge files).
- **Scope**: single-agent ↔ subagents (isolated context, same session) ↔ multi-agent teams (parallel sessions, explicit handoffs).
- **Statefulness**: stateless (recomputed each turn) ↔ thread-state (one conversation) ↔ cross-thread memory (durable user/org facts).

**Causal / dependency structure** — what depends on what.
- **Capabilities depend on Tools**: a skill that says "edit the spreadsheet" is useless without a tool that can write files. Skills describe how to use tools; tools do.
- **Memory depends on State**: an agent can only remember what was first tracked in state — long-term memory is curated extraction from short-term state.
- **Orchestration depends on Identity**: routing to a "security reviewer" specialist requires that the specialist be defined as an addressable artifact.
- **Evaluation depends on Outputs**: you can only score reliably what was produced in a structured format. Free-text answers force LLM-as-judge metrics; structured answers permit exact-match.
- **Guardrails wrap everything**: they apply at four points — input (before the agent runs), output (before delivery to user), tool (around each tool call), and handoff (around delegation). They are not their own pipeline; they are a layer on every other one.
- **Progressive disclosure is enabled by the filesystem**: agents that can read files on demand do not need full context preloaded. Skills, references, and Resources only scale because the agent has a `Read` or `view` tool.

**Common pitfalls** — how a naïve reader gets it wrong.
- **Confusing Skills with Tools**: A skill is *instructions* ("here is how to write a good commit message"); a tool is *an action* (`git_commit(message)`). Skills can invoke tools, but they are not interchangeable.
- **Confusing Memory with State**: State is the current conversation thread, automatic and structural. Memory is what's worth keeping across conversations, an explicit application decision. LangGraph codifies this as Checkpointer vs. Store; conflating them produces agents that either forget everything or remember everything indiscriminately.
- **Treating CLAUDE.md as a skill**: It is identity-layer, always loaded, ~150–200 instructions max before reliability drops. Putting how-to-do-a-specific-task content there bloats context for every call. That content belongs in a skill.
- **Skipping evaluation until production**: Tracing and eval suites are usually the last category teams build, and the first one they regret skipping. A correct-looking final answer can hide a wildly inefficient or unsafe trajectory.
- **Building multi-agent before single-agent works**: Multi-agent systems multiply token cost dramatically (one analysis cited 4–7× for ordinary subagents and ~15× for full multi-session teams) and introduce coordination failures. A single well-designed agent with subagents for read-heavy tasks is almost always the right starting point.
- **Putting everything in a giant prompt**: The recurring lesson across Anthropic's, OpenAI's, and LangChain's published guidance is that monolithic prompts hit a complexity ceiling — beyond which adding instructions actively degrades performance.

## Glossary

- **[E1] Anthropic** *(org)* — Maker of Claude. Originated Agent Skills, MCP, the Claude Agent SDK, and the "Building Effective Agents" pattern vocabulary widely adopted across the industry.
- **[E2] Model Context Protocol (MCP)** *(standard)* — Open protocol (specification version 2025-06-18) for connecting AI agents to external context and capabilities. Defines three server-side primitives: Resources, Tools, and Prompts. Originated by Anthropic; broadly adopted.
- **[E3] Agent Skills** *(standard)* — Open standard (agentskills.io, released 2025-12-18) for packaging agent capabilities as folders containing a `SKILL.md` and optional scripts/, references/, assets/. Adopted by 26+ platforms.
- **[E4] SKILL.md** *(artifact)* — The required file in an Agent Skill folder. Markdown with YAML frontmatter (`name`, `description`); recommended ≤5,000 tokens or ≤500 lines.
- **[E5] AGENTS.md** *(standard)* — Cross-tool open Markdown convention for repo-root agent instructions. Originated 2025 from Sourcegraph, OpenAI, Google, Cursor, Factory; governed by the Agentic AI Foundation under the Linux Foundation.
- **[E6] CLAUDE.md** *(artifact)* — Anthropic-specific repo-root instruction file read by Claude Code. Hierarchical (user-global, project, subdirectory). Functionally analogous to AGENTS.md.
- **[E7] Progressive disclosure** *(concept)* — Loading information into the context window in stages — discovery (metadata only), activation (full instructions), execution (referenced files) — rather than preloading everything. Central design principle of Agent Skills.
- **[E8] Resource** *(MCP term)* — MCP server feature exposing data (files, schemas, app-specific information) to the model. **Application-driven** in the MCP control model: the host application chooses what to include.
- **[E9] Tool** *(generic + MCP term)* — A function the agent can invoke to take an action. **Model-controlled** in the MCP control model: the agent decides when to call it.
- **[E10] Prompt** *(MCP term, not the generic word)* — In MCP, a server-exposed template (often surfaced as a slash command). **User-controlled** in the MCP control model: the user explicitly selects it.
- **[E11] Workflow vs. Agent** *(distinction)* — Anthropic's architectural distinction: workflows orchestrate LLM calls through predefined code paths; agents let the LLM direct its own tool use in a loop. Both are "agentic systems."
- **[E12] Subagent** *(concept)* — A child agent invoked with its own isolated context window, returning only summarized results. Used for context isolation and parallelization.
- **[E13] Handoff** *(concept)* — Transferring control of a conversation from one agent to a specialist. Distinct from a tool call: the receiving agent owns the next response. Codified by OpenAI Agents SDK.
- **[E14] Guardrail** *(concept)* — A safety/validation check that runs before, after, or around an agent action. Four scopes: input, output, tool, handoff.
- **[E15] Checkpointer** *(LangGraph term, generalizable)* — Mechanism for persisting graph/agent state per conversation thread. Short-term, automatic.
- **[E16] Store** *(LangGraph term, generalizable)* — Mechanism for cross-thread/long-term memory, scoped by namespace (e.g., per user). Explicit, application-curated.
- **[E17] Claude Agent SDK** *(product/library)* — Anthropic's runtime library (renamed from Claude Code SDK in September 2025) exposing the Claude Code agent loop, built-in tools, subagents, hooks, and MCP integration.
- **[E18] OpenAI Agents SDK** *(product/library)* — OpenAI's agent framework. Primitives: Agents, Tools, Handoffs, Guardrails, Sessions.
- **[E19] LangGraph** *(product/library)* — LangChain's graph-based agent framework, defining agents as stateful graphs with checkpointed nodes.
- **[E20] Agent-Computer Interface (ACI)** *(concept)* — Anthropic's term for the quality of the surface an agent uses to interact with tools (parameter names, descriptions, error messages, format). Argued to deserve as much engineering effort as the system prompt itself.
- **[E21] SOUL.md** *(emerging convention)* — Markdown file defining an agent's persona, tone, values, and behavioral boundaries. Used by OpenClaw, Hermes Agent, ClawSouls. Not yet a settled standard.
- **[E22] Sandbox agent** *(concept)* — Agent that executes inside an isolated workspace (manifest-defined files, restricted tools, resumable sessions). Both Anthropic and OpenAI ship sandbox primitives.

## Canonical Facts

1. **[F1]** Agent Skills were released as an **open standard** at agentskills.io on **2025-12-18** and have been adopted by 26+ platforms including Claude, OpenAI Codex, Gemini CLI, GitHub Copilot, Cursor, and VS Code. [S3, S18]
2. **[F2]** A SKILL.md file MUST start with **YAML frontmatter containing `name` and `description`**; only this metadata is preloaded into the system prompt at startup. [S1, S2]
3. **[F3]** Agent Skills use **three-tier progressive disclosure**: (1) Discovery — name + description only (~30–80 tokens per skill); (2) Activation — full SKILL.md body loaded when the agent decides the skill applies; (3) Execution — additional bundled files (scripts/, references/, assets/) read on demand. [S1, S2, S3]
4. **[F4]** The Agent Skills specification **recommends SKILL.md bodies under 5,000 tokens or 500 lines**, with longer detail pushed into separate reference files. [S2, S18]
5. **[F5]** The Model Context Protocol specification (version **2025-06-18**) defines three distinct server-feature primitives with explicit control models: **Resources** are application-driven; **Tools** are model-controlled; **Prompts** are user-controlled. [S6, S7, S8]
6. **[F6]** MCP Tools include `name`, `description`, `inputSchema` (JSON Schema), and an optional `outputSchema`; tool results can be unstructured content (text/image/audio/resource) or structured JSON conforming to the output schema. [S8]
7. **[F7]** Anthropic's "Building Effective Agents" defines **five canonical workflow patterns**: prompt chaining, routing, parallelization (sectioning and voting), orchestrator-workers, and evaluator-optimizer. It distinguishes these from **agents** (LLMs directing tool use in a loop). [S4]
8. **[F8]** The OpenAI Agents SDK is built around **four primitives**: Agents, Tools (function tools and hosted tools), Handoffs, and Guardrails — with Sessions providing persistent memory. [S9, S10, S11, S12]
9. **[F9]** OpenAI guardrails apply at four scopes: **input** (before agent runs), **output** (after final response), **tool** (around each function-tool invocation), and the handoff pipeline. Tool guardrails do not apply to handoffs themselves. [S11]
10. **[F10]** LangGraph distinguishes two memory mechanisms: a **Checkpointer** that persists graph state per `thread_id` (short-term, automatic, structural) and a **Store** that holds cross-thread information by namespace (long-term, explicit, application-curated). [S13, S20]
11. **[F11]** AGENTS.md emerged as a cross-tool standard in 2025 from collaboration between Sourcegraph, OpenAI, Google, Cursor, and Factory, and is governed by the **Agentic AI Foundation under the Linux Foundation**. As of April 2026, Claude Code does not natively support AGENTS.md; it reads CLAUDE.md. [S17]
12. **[F12]** Anthropic's Claude Agent SDK was renamed from the Claude Code SDK in **September 2025** to reflect that the harness is general-purpose, not coding-specific. [S5]
13. **[F13]** Subagents in the Claude Agent SDK use **isolated context windows** and return only summarized results to the orchestrator, serving as a context-management primitive as well as a delegation primitive. [S5, S22]
14. **[F14]** Anthropic positions a three-layer stack: **MCP as the protocol** for agent–tool communication, **Agent Skills as portable capability packages**, **Claude Agent SDK as the runtime**. [S5]
15. **[F15]** LangChain's `create_agent` supports two structured-output strategies: **ProviderStrategy** (native JSON-schema response format, available on OpenAI, Anthropic, Google, xAI Grok) and **ToolStrategy** (tool-calling fallback for models without native support). [S14]

## Core Findings

1. **[CF1] [LOAD-BEARING]** An agent's behavior is best modeled as the composition of a fixed number of artifact categories — Identity, Operating Style, Capabilities, Tools, Knowledge/Resources, Prompts/Interfaces, Memory, State, Planning, Orchestration, Guardrails, Outputs, Evaluation, Runtime, Learning/Iteration. Not every agent populates every category, but every category exists implicitly: when an agent has no `MEMORY.md` it still has a memory policy (no memory), and the absence is itself a design choice. [INFERENCE from S1, S4, S5, S9, S12, S13, S23]
2. **[CF2] [LOAD-BEARING]** Progressive disclosure is the dominant solution to the context-window problem and is rapidly becoming an industry-wide architectural pattern, not a Skills-specific quirk. The same logic appears in MCP Resources (loaded on demand by the host), LangGraph state (compacted automatically), Claude Code (compaction on approach to context limit), and subagent design (isolated context returning summaries). [S1, S2, S5, S22]
3. **[CF3] [LOAD-BEARING]** The clearest formal vocabulary for distinguishing artifact types is the MCP **control-source trichotomy**: Resources (the application decides), Tools (the model decides), Prompts (the user decides). This generalizes beyond MCP and gives a precise way to ask "who initiates this?" of any artifact. Always-on identity files (CLAUDE.md / AGENTS.md) are application-controlled in this frame; Skills are model-controlled (the agent decides if a task matches); slash commands are user-controlled. [S6, S7, S8]
4. **[CF4] [LOAD-BEARING]** The distinction between Workflows and Agents is foundational: workflows give predictability via predefined code paths; agents give flexibility via model-directed tool loops. Most production "agentic systems" are workflows or workflow–agent hybrids, not autonomous agents. Anthropic's explicit guidance is to start with the simplest pattern (often a single LLM call with retrieval) and only escalate when measurably needed. [S4, S12]
5. **[CF5] [LOAD-BEARING]** Memory and State are distinct concerns with different ownership, lifetimes, and engineering treatments. Conflating them is a frequent design error. State is per-conversation, automatically managed, and serves continuity within a session. Memory is per-user (or per-org), explicitly curated, and serves continuity across sessions. Both LangGraph and OpenAI Agents SDK encode this split structurally. [S13, S20]
6. **[CF6] [LOAD-BEARING]** Tool documentation quality (the "Agent-Computer Interface" or ACI) matters as much as system prompts. Anthropic reports spending more time optimizing tools than prompts for SWE-bench. Good tool descriptions read like good docstrings for a junior engineer: example usage, edge cases, input-format requirements, clear boundaries from sibling tools, and parameter names that prevent error (e.g., absolute paths instead of relative). [S4]
7. **[CF7] [SUPPORTING]** Guardrails are not one artifact category but a layer applied at four enforcement points: input, output, around each tool call, and around handoffs. This four-point enforcement model is codified in the OpenAI Agents SDK and is good general design practice. [S11]
8. **[CF8] [SUPPORTING]** Structured outputs (JSON-schema-constrained generation, often via Pydantic models) have moved schema compliance from a prompt-engineering problem to an infrastructure guarantee. Native provider support (OpenAI, Anthropic, Google, xAI Grok) reliably produces conforming JSON; tool-calling fallbacks cover models without native support. Structured outputs are a precondition for cheap, deterministic evaluation. [S14, S15]
9. **[CF9] [SUPPORTING]** Multi-agent systems are expensive. Plain subagent use multiplies token cost roughly 4–7×; full multi-session "Agent Teams" can run 15× standard usage. The architecturally sound use case for subagents is **read-heavy bounded research** (large-file exploration, codebase scanning) where context isolation is the prize, not parallel writing. [S22, S5]
10. **[CF10] [SUPPORTING]** Identity-layer files (CLAUDE.md, AGENTS.md) are most effective when **short** — frontier LLMs reliably follow roughly 150–200 instructions before degradation begins, and these files compete with everything else in context on every call. Practitioner guidance converges on: never use them for content a linter could enforce, never use them for task-specific instructions (those belong in skills), focus on what the agent genuinely cannot know. [S16, S17]
11. **[CF11] [SUPPORTING]** The Operating Style category (SOUL.md and similar persona files) is real but not yet standardized. Multiple competing conventions exist (OpenClaw, Hermes Agent, ClawSouls/Soul Spec) and they disagree on file names and slot order. For now, treat persona content as a coherent artifact concern but expect the filename to vary by ecosystem. [S21, S24, S28]
12. **[CF12] [SUPPORTING]** Agent evaluation has converged on a multi-layer model: **session-level** (did the user's goal get met), **trajectory-level** (was the path efficient — tool-call accuracy, step efficiency, plan adherence), and **leaf-level** (single-turn LLM metrics like groundedness, factuality, safety, format compliance). Each layer requires different instrumentation; tracing is the foundation that makes all three observable. [S19, S27]
13. **[CF13] [SUPPORTING]** Across major frameworks, agentic-AI artifacts are converging on **plain Markdown plus YAML frontmatter** as the canonical format. The reasons are concrete: Markdown is selectively-attendable (the model can pull section X to the front of context), it diffs cleanly, it is parser-free, and both humans and models read it natively. [S26]

## Detailed Analysis

### What is an "agentic AI artifact" and why has this concept emerged?

An agentic AI artifact is a discrete, file-based piece of structure that defines or constrains some aspect of an AI agent's behavior. The category exists because single-prompt design hit a complexity ceiling. As Anthropic's "Building Effective Agents" puts it, the most successful production agents are not built with complex frameworks but with "simple, composable patterns" — meaning artifacts that combine rather than a single mega-prompt that scales by accretion.

The shift is from **prompt engineering** (single-turn, one-shot) to **context engineering** (multi-turn, multi-artifact, loop-based). Anthropic's Applied AI team has framed this as the successor discipline: prompt engineering optimizes a single API call; context engineering optimizes what enters and leaves the model's context window across many calls in a loop. Artifacts are the mechanism by which context engineering becomes tractable — each one packages a concern that can be authored, versioned, and reused independently.

Two forces drove the consolidation in 2024–2025. First, **context window economics**: even with 200k-token windows, practitioner reports place the effective working context closer to 60–80k tokens during agent execution, with quality degrading beyond that. Anything always-on competes with current work. Second, **organizational composition**: capability built into a single agent stays trapped there. Capability packaged as a portable artifact (a skill, a tool, a guardrail) can be shared across agents, teams, and even tool vendors — which is exactly the bet Anthropic made by releasing Agent Skills as an open standard on 2025-12-18 and getting OpenAI, Google, GitHub, and Cursor to adopt it within weeks.

The 15-category taxonomy in this brief is not a single source's invention; it is a synthesis of what major frameworks have separately codified. Anthropic ships Skills, MCP, CLAUDE.md, and subagents. OpenAI Agents SDK ships Agents, Tools, Handoffs, Guardrails, Sessions. LangGraph ships State, Checkpointers, Store, and graph orchestration. MCP ships Resources, Tools, Prompts. The categories named in this brief are the union — every one is codified somewhere, and most are codified in multiple frameworks under different names.

_Confidence: high — Anthropic and OpenAI primary sources align ([S1], [S4], [S5], [S9], [S12]), and the framing matches independent practitioner consensus._

### Identity and Operating Style artifacts

**Identity artifacts** answer "who is this agent?" — its role, scope, hard rules, and what it should never do. **Operating Style artifacts** answer "how does this agent communicate and reason?" — its tone, values, response patterns. The split is conceptual; the file conventions overlap significantly and are still consolidating.

The two settled conventions are **CLAUDE.md** (Anthropic-specific, read by Claude Code) and **AGENTS.md** (cross-tool standard governed by the Agentic AI Foundation under the Linux Foundation). Both are repo-root Markdown files loaded **always-on** at session start. Both should contain a brief project description, build/test/lint commands, non-obvious conventions, architectural decisions with rationale, security gotchas, and PR/commit conventions. Both should **exclude** anything a linter enforces deterministically, generic language style guidelines, and task-specific instructions (which belong in Skills, not Identity files).

The strongest practitioner consensus on these files is **keep them short**. Frontier LLMs reliably follow roughly 150–200 instructions before degradation begins, and these files compete with everything else in context on every call. One published analysis of Claude Code's harness estimates ~50 of those slots are already consumed by the system prompt — leaving room for roughly 100–150 user instructions across rules, plugins, skills, and the conversation itself. ETH Zurich research cited in practitioner guides found that LLM-generated context files actually *reduced* task success rates by ~3% on average while increasing inference cost over 20% — human-curated files gave a marginal 4% gain. The lesson: every line must earn its context cost.

Many teams symlink `CLAUDE.md` → `AGENTS.md` to keep a single source of truth across Claude Code, Codex, Cursor, and other tools.

**Operating Style files** — typically called `SOUL.md` (Soul Spec, OpenClaw, Hermes Agent), sometimes `PERSONA.md` or `STYLE.md` — are an emerging convention without a settled standard. They separate persona from operating instructions: SOUL.md defines tone, voice, what to push back on, what to avoid (sycophancy, hype language, overexplaining); AGENTS.md / CLAUDE.md defines the project-specific facts. The Hermes Agent convention loads SOUL.md first in the system prompt as "slot #1," then IDENTITY.md, USER.md, AGENTS.md, MEMORY.md. Treat this as a reasonable design pattern, not a binding standard.

Hierarchy and scoping matter. CLAUDE.md supports `~/.claude/CLAUDE.md` (user-global, follows the user across projects), workspace root `CLAUDE.md` (project), and subdirectory `CLAUDE.md` (path-scoped to e.g. `/src/components/` or `/db/migrations/`). Cursor and Copilot have analogous layering (`.cursor/rules/*.mdc` with glob-pattern frontmatter; `.github/copilot-instructions.md` + path-specific `.instructions.md`). The cross-cutting pattern: identity content cascades from global → project → directory, with the most specific scope winning.

_Confidence: mixed — CLAUDE.md and AGENTS.md are well-documented and stable; SOUL.md and operating-style conventions are emerging and may shift. Sources are heavily practitioner-blog rather than primary spec._

### Capability artifacts (Skills, Playbooks, SOPs)

The Capability layer is where the most-codified and most-mature conventions live. **Agent Skills** ([E3]) is now an open standard, defined at agentskills.io as: a folder containing a required `SKILL.md` (metadata + instructions in YAML-frontmatter Markdown) and optional `scripts/` (executable code), `references/` (additional docs loaded on demand), and `assets/` (templates, schemas, data). The same folder structure works across Claude, OpenAI Codex CLI, Gemini CLI, GitHub Copilot, Cursor, VS Code, and 20+ other platforms unmodified.

The defining design principle is **progressive disclosure**, a three-stage load:
1. **Discovery** — at startup, only `name` and `description` from each skill's YAML frontmatter enter the system prompt (~30–80 tokens each). One analysis of Anthropic's 17 official skills found a median discovery cost of ~80 tokens per skill; all 17 together cost ~1,700 tokens, less than a single fully-activated skill.
2. **Activation** — when the agent decides a task matches a skill's description, it reads the full `SKILL.md` body into context (typical range: 275 tokens for `internal-comms` to ~8,000 for `skill-creator`, median ~2,000).
3. **Execution** — bundled files (scripts, references, assets) are read or executed only as the active task demands. Scripts run via Bash and only their output enters context.

The spec recommends SKILL.md bodies under 5,000 tokens or 500 lines. Once a skill exceeds that, the established pattern is to split: keep `SKILL.md` as an "index" with high-level workflow, point to `references/`, `forms.md`, `OOXML.md`, etc. for detail.

Conventions for the YAML frontmatter:
- `name` — lowercase, hyphens, ≤64 chars. The verb-ing + noun pattern is common (`generating-practice-questions`, `analyzing-marketing-campaign`).
- `description` — ≤1,024 chars. Both **what** the skill does and **when to use it**, with trigger keywords. This is the *only* basis on which the agent decides to load the skill, so specificity drives reliability.

The naming distinction between **Skills, Playbooks, SOPs, Workflows, Checklists, Templates, and Recipes** in the source taxonomy is mostly stylistic — none of these are formally separate artifacts. They are all Capability-layer markdown files. In practice, the field has converged on `SKILL.md` as the primary convention because the Agent Skills standard explicitly defines it and major coding agents auto-load it.

A capability module typically holds, beyond `SKILL.md`:
- Step-by-step procedural instructions (numbered, specific, with edge cases)
- Code templates rather than descriptions (agents pattern-match more reliably against exact examples than against prose)
- Lazy-loaded reference files for branches the agent rarely needs

Important interaction with Identity files: capability content **does not** belong in CLAUDE.md or AGENTS.md, because those are always-on and capability content is task-conditional. The right home for "how to write a good commit message" is `skills/commit-message-formatter/SKILL.md`, not the always-on identity layer.

_Confidence: high — Agent Skills is an open standard with multi-vendor adoption ([S1], [S2], [S3]), and conventions are documented at the spec level._

### Tools, Knowledge/Resources, and Prompts/Interfaces

These three categories together answer "what can the agent reach for?" and are best understood through MCP's **control-source trichotomy**:

- **Tools** ([E9]) — model-controlled. The agent decides when to invoke. Examples: `read_file`, `search_web`, `send_email`. MCP tools have a `name`, `description`, `inputSchema` (JSON Schema), and optional `outputSchema`. Tools can return unstructured content (text, image, audio, resource link, embedded resource) or structured JSON conforming to the output schema. For trust and safety, MCP requires that a human be able to deny tool invocations.
- **Resources** ([E8]) — application-driven. The host application chooses what to expose, often via UI pickers, file trees, or automatic-inclusion heuristics. Examples: files, database schemas, app-specific information. Each resource has a URI (RFC 3986), MIME type, and optional annotations (`audience`, `priority`, `lastModified`).
- **Prompts** ([E10]) — user-controlled. Exposed for explicit user selection, typically as slash commands. Examples: `/code-review`, `/explain-this-error`. Each MCP Prompt has a name, description, and arguments (with autocompletion support via the completion API).

This trichotomy generalizes far beyond MCP servers. Any artifact you design can be classified by who pulls it into context. Knowledge files manually attached by a developer are Resource-like. A "deep research" command the user invokes from a menu is Prompt-like. An on-demand skill triggered by task content is Tool-like in spirit (model-controlled).

**Tool design — the ACI principle.** Anthropic argues that the agent-computer interface deserves as much engineering as a human-computer interface. Their published guidance:
- Give the model enough tokens to "think" before writing — never ask it to commit to a format prematurely
- Keep formats close to what occurs naturally in text on the internet (Markdown over JSON-escaped strings; full file rewrites over diff hunk-headers requiring exact line counts)
- Poka-yoke the inputs: prefer absolute paths to relative paths, prefer enums to free text, prefer explicit confirmations to silent assumptions
- Test how the model uses each tool with many example inputs and iterate — debugging tool quality is debugging agent quality

Three tool categories that appear in OpenAI Agents SDK: **function tools** (Python functions auto-wrapped with Pydantic schema generation), **hosted tools** (provider-side: WebSearchTool, FileSearchTool, HostedMCPTool, etc.), and **agents-as-tools** (`Agent.as_tool(...)` exposes another agent as a callable tool — distinct from handoffs because the calling agent owns the next response).

**Knowledge/Resources content.** What lives in a `references/` or `knowledge/` directory: glossaries, policies, schemas, data dictionaries, FAQs, project context, regulatory constraints, domain standards. These differ from Memory because they are *generally true* facts about the domain, not user- or session-specific facts.

**Prompts as artifacts.** The Prompts category covers user-initiated entry points: slash commands, prompt templates with variables, intake forms, routing prompts, clarification prompts, conversation starters. MCP Prompts are the formal vehicle, but the same content shows up as `.claude/commands/*.md` in Claude Code, `.cursor/rules/*.mdc` in Cursor, and free-form templates in other ecosystems.

_Confidence: high — MCP is a formal specification ([S6], [S7], [S8]); the ACI guidance comes directly from Anthropic's primary engineering blog ([S4])._

### Memory and State

The most common conceptual mistake in agent design is treating Memory and State as the same thing. They are not, and major frameworks now structurally separate them.

**State** is the working data of a single conversation thread: messages exchanged so far, intermediate tool outputs, variables passed between graph nodes. It is **automatic, structural, short-lived**. In LangGraph, state is managed by a **Checkpointer** (e.g., `MemorySaver` for development, `PostgresSaver` / `RedisSaver` / `SqliteSaver` for production). Each "super-step" of the graph produces a checkpoint. Threads are identified by `thread_id`; different `thread_id`s have fully isolated state. The Checkpointer enables three production features: resuming conversations days or weeks later, fault tolerance (restart from last successful checkpoint), and time-travel debugging (replay or fork from any prior checkpoint).

**Memory** is durable information worth keeping *across* threads — user preferences, learned facts, accumulated context. It is **explicit, curated, long-lived**. In LangGraph, memory is managed by a **Store** (`InMemoryStore`, `PostgresStore`, `RedisStore`, `MongoDBStore`) namespaced by tuple (commonly `(user_id, "memories")`). Crucially, the Store is *not* automatic: developers must write logic that decides what to extract from state and persist to the Store, typically via an LLM-call extraction step after each turn. As one practitioner formulated it: "The checkpointer is infrastructure. The Store is an application design problem."

In practice:
- `MEMORY.md` artifacts hold what should *persist across* conversations: user preferences, durable facts, lessons learned, established conventions.
- `STATE.json` or thread-state holds what is *current to* a conversation: open tasks, scratch results, the in-flight reasoning trace.
- `DECISIONS.md`, `HISTORY.md`, `RETROSPECTIVE.md` fall on the Memory side — they record what the agent learned that should apply to future work.
- `PROJECT_STATE.md` is a Memory artifact about the project, distinct from per-session state.

Compaction is the State-side counterpart to extraction. When the context window approaches its limit, frameworks (Claude Code, Claude Agent SDK, LangGraph) automatically summarize older tool outputs and conversation history. Anthropic's documentation states explicitly that older tool outputs are cleared first, then conversation is summarized if needed. The official recommendation for content that must survive long sessions: put it in CLAUDE.md (Identity layer, always reloaded), not in earlier messages.

A subtler memory pattern is **subagent context isolation**. A subagent does a verbose read-heavy task (e.g., scanning a large codebase) in its own context window and returns a summary to the parent. The parent's context never sees the verbose intermediate reads. This is a context-management primitive masquerading as a delegation pattern.

_Confidence: high — LangGraph's Checkpointer/Store split is documented at the primary docs level ([S13]); the conceptual distinction is consistent across frameworks._

### Planning and Orchestration

This category covers how an agent (or system of agents) decides what to do next, and how work gets distributed.

The foundational division is Anthropic's **Workflows vs. Agents** distinction. Workflows orchestrate LLM calls through predefined code paths; agents let the LLM direct its own tool use in a loop. Anthropic identifies **five canonical workflow patterns**:

1. **Prompt chaining** — decompose a task into a fixed sequence; each LLM call processes the previous output. Optional programmatic "gates" check intermediate results. Use when: tasks decompose cleanly into fixed subtasks; you want to trade latency for accuracy.
2. **Routing** — classify input and dispatch to a specialized followup. Use when: distinct categories benefit from specialized prompts/tools; classification is reliable. Common version: route easy queries to Haiku (cheap, fast), hard queries to Opus (capable).
3. **Parallelization** — split a task across simultaneous LLM calls. Two forms: **sectioning** (independent subtasks) and **voting** (same task, multiple attempts, aggregate). Use when: subtasks are independent, or multiple perspectives raise confidence.
4. **Orchestrator-workers** — central LLM dynamically breaks down tasks, delegates to worker LLMs, synthesizes results. Use when: subtasks cannot be predicted in advance (e.g., a coding change touching N files where N depends on the task).
5. **Evaluator-optimizer** — one LLM generates, another evaluates and provides feedback in a loop. Use when: clear evaluation criteria exist and iterative refinement helps.

Beyond workflows, **Agents** are LLMs operating in a loop, using tools based on environmental feedback, until a stopping condition (task completion, max iterations, human intervention) fires. Anthropic's three principles for agent design: **simplicity** (don't add complexity until it demonstrably helps), **transparency** (show the agent's planning steps explicitly), and **careful ACI design** (tools and their docs deserve as much engineering as prompts).

**Multi-agent orchestration** introduces additional artifacts:
- **Handoffs** ([E13]) — codified by OpenAI Agents SDK. When a handoff occurs, the receiving agent takes over the conversation and sees the entire previous history (unless an `input_filter` is configured). Distinct from Agent.as_tool: in a handoff, the new agent owns the next response; with as_tool, the calling agent remains in charge.
- **Agent registries** — explicit listings of available specialists with their domains and descriptions. Without a registry, routing becomes guesswork.
- **Escalation rules** — when to bail to a human, when to ask another agent, when to retry.
- **Priority rules** — how the agent chooses among competing tasks.

**Subagents** ([E12]) are a hybrid: they're invoked from inside the parent's session (via a `Task` tool in Claude Agent SDK) but run in their own isolated context window and return only summaries. They are cheaper than handoffs to a separate agent run but more expensive than tool calls — Anthropic's own documentation puts multi-agent workflows at roughly 4–7× the tokens of a single-agent session, and full multi-session "Agent Teams" at ~15×. The architecturally sound use case is **read-heavy bounded research**: large-file exploration, codebase scanning, dependency review. Less suitable: parallel writing (coordination overhead defeats the gains) and autonomous decision-making (Opus 4.6 specifically has been observed to over-spawn subagents).

The strongest cross-framework consensus on orchestration: **start with the simplest pattern that works**. Single LLM call with retrieval beats prompt chaining beats agent loop beats multi-agent system, in that order of preference, and you should only escalate when you can measure that you need to.

_Confidence: high — primary Anthropic and OpenAI sources directly document these patterns ([S4], [S5], [S10], [S12])._

### Guardrails, Outputs, and Evaluation

These three categories together make an agent **reliable** — and they are the layers most often deferred until production failure forces them in.

**Guardrails** ([E14]) are validation and safety checks. OpenAI Agents SDK codifies four enforcement points, and the same model generalizes well:
- **Input guardrails** — run on the initial user input, before the agent starts. Catch malicious prompts, off-topic queries, policy violations. Can run in parallel with the agent (lower latency, but may waste tokens if tripped late) or blocking (higher latency, no wasted tokens).
- **Output guardrails** — run on the agent's final response before it reaches the user. Catch hallucinations, PII leakage, brand-tone violations, format errors.
- **Tool guardrails** — run before and/or after each function-tool invocation. Validate arguments, sanitize outputs, enforce rate limits. Tool guardrails do **not** apply to handoffs themselves; for that, use input/output guardrails on the relevant agents.
- **Handoff filters** — control what conversation history transfers to a specialist agent (e.g., `remove_all_tools` strips prior tool calls; useful when the specialist should reason from a clean slate).

Common guardrail artifacts: `GUARDRAILS.md` (overall safety posture and behavior boundaries), `PERMISSIONS.md` (what tools are allowed in which contexts), `RISK_TIERS.md` (low/medium/high categorization), `APPROVALS.md` (when human approval is required), `COMPLIANCE.md` (regulatory constraints), `PRIVACY.md` (PII handling). These artifacts are typically always-on but small.

**Outputs/Schemas** turn the agent's free-text generation into structured data the rest of the system can rely on. The dominant pattern in 2025–2026 is **schema-constrained generation**: define the desired output shape as a Pydantic model (Python) or Zod schema (TypeScript), let the framework convert it to JSON Schema, pass it to the model.

Two strategies:
- **Native structured output** (`response_format` / "JSON Schema response format") — supported on OpenAI, Anthropic, Google, xAI Grok. The model is constrained at decoding time to produce output matching the schema. Most reliable when available. LangChain calls this `ProviderStrategy`.
- **Tool-calling fallback** — for models without native support. The output schema becomes a tool definition the agent must "call." LangChain calls this `ToolStrategy`. Pydantic AI defaults to this and registers each member of a union as a separate tool to maximize correctness.

Important constraints: OpenAI's strict mode supports only a subset of JSON Schema (constraints like `minimum`/`maximum` on numbers, `pattern` on strings are stripped); Gemini cannot use tools simultaneously with structured output. Pydantic-AI sanitizers exist specifically to bridge these gaps.

Output artifacts: `OUTPUT_FORMATS.md` (catalog of structured shapes the agent produces), `schemas/*.json` or `schemas/*.py` (the actual schemas), report templates, status formats, handoff brief templates.

**Evaluation** is how you measure whether the agent is doing a good job. The current state of the art separates three layers:
1. **Session-level** — did the user's goal get met? Measured via task success, resolution rate, user satisfaction.
2. **Trajectory-level** — was the path efficient? Tool-call accuracy, argument correctness, step efficiency, plan adherence, retrieval quality. A correct final answer from a 12-step trajectory that should have been 4 steps is still a failure mode.
3. **Leaf-level** — single-turn LLM metrics: groundedness, factuality, safety, format compliance, answer relevancy.

Each layer needs different instrumentation, and all three sit on top of **tracing**: capturing every step the agent takes (tool selection, tool arguments, model responses, memory reads, memory writes, state transitions, decision branches) into a nested span tree. The current ecosystem standardizes on **OpenTelemetry**-native traces (so framework-specific tools can interoperate). Native adapters exist for OpenAI Agents SDK, LangGraph, Mastra, Pydantic AI, LangChain, CrewAI, Vercel AI SDK.

Evaluation artifacts: `EVALS.md` (test cases and grading criteria), `RUBRIC.md` (scoring rules, often with LLM-as-judge prompts), `TEST_CASES.md` (representative scenarios with expected behaviors), `BENCHMARKS.md` (performance baselines), `ERROR_LOG.md` (production failures and fixes), `QA_CHECKLIST.md` (pre-release review). Trace logs themselves are typically a service (LangSmith, Braintrust, Langfuse, Confident AI, Arize) rather than a markdown artifact, but their schema and query patterns are part of this category.

The strongest practitioner-level finding: **trajectory evaluation is what separates working agents from broken ones in production**, because traditional APM (request rate, latency, error rate) cannot detect an agent that loops, calls the wrong tool, or hallucinates inside a 200-status response. [S19, S27]

_Confidence: high — Guardrails and Output sources are primary ([S11], [S14], [S15]); evaluation guidance is well-established across multiple secondary sources but less standardized at the spec level._

### Runtime and Learning/Iteration

**Runtime** answers "where and how does the agent actually execute?" — the workshop. It covers configuration, model selection, environment variables, sandboxing, dependencies, deployment, and versioning.

Common runtime artifacts:
- `CONFIG.json` / `CONFIG.md` — agent settings, default model, default temperature
- `MODEL_CONFIG.md` — model choice, fallback chain, cost/capability tier mapping
- `.env` — secrets, API keys, environment variables (never committed)
- `WORKSPACE/` — files the agent can read/write
- `SANDBOX/` — isolated execution environment
- `DEPENDENCIES.md` — required packages, system tools
- `INSTALL.md` — setup instructions
- `DEPLOYMENT.md` — how to run/publish
- `VERSION.md` / `CHANGELOG.md` — what changed

**Sandbox agents** are a primitive in both Anthropic's Claude Agent SDK and OpenAI's Agents SDK. They run inside isolated workspaces with manifest-defined files, sandbox-client choice, and resumable sandbox sessions. Important when agents need filesystem write access, shell execution, or package installation. Both vendors offer hosted sandbox runtimes (Anthropic's Claude Managed Agents, launched 2026-04-08; OpenAI's hosted agent runtime via Agent Builder) and self-hosted modes.

A practical Runtime concern that often gets undersized: **permission scoping**. Both Claude Code and Claude Agent SDK ship per-tool allowlists/denylists. A research subagent can be read-only (`allowedTools: ["Read", "Glob", "Grep"]`). A code-review subagent can have Bash plus Grep but no Edit or Write. Permission scoping is more architecturally important than prompt rules — a tool that isn't in the allowlist cannot be called even if the model wants to call it.

**Learning/Iteration** is how the agent improves over time and how the system around it evolves. This is the category least standardized in tooling because it crosses multiple layers (skill content, eval suites, guardrail rules, identity files all evolve together).

Common artifacts:
- `CHANGELOG.md` — what changed and when, per agent or per artifact
- `RETROSPECTIVE.md` — lessons from past runs, both at the agent level and per skill
- `BACKLOG.md` / `IMPROVEMENTS.md` — known issues, planned enhancements
- Annotation queues (a feature of LangSmith, Braintrust, Confident AI) — human review of traces, feeding back into eval datasets

The most important Learning pattern is **eval-driven iteration**: production traces feed an evaluation dataset; failing traces become labeled test cases; fixes are validated against the dataset before shipping; the cycle repeats. Without this loop, agent improvements are vibes-based and regress unpredictably. Anthropic's published Skills-creation guidance starts with this principle: "Start with evaluation. Identify specific gaps in your agents' capabilities by running them on representative tasks and observing where they struggle. Then build skills incrementally to address these shortcomings."

A subtler Learning concern is **artifact decay**. Files that document repository structure or build commands go stale quickly; LLM-generated context files in particular have been shown to actively hurt success rates over time as the repo evolves. The maintenance discipline that keeps an agent improving is the same discipline that keeps documentation alive in any engineering org: ownership, review cycles, automated checks.

_Confidence: mixed — Runtime patterns are well-documented at the SDK level ([S5], [S9]); Learning/Iteration is less standardized and relies more on secondary practitioner sources._

## Conflicts, Assumptions & Uncertainty

**Source conflicts** — where credible sources disagree.

- **Filename conventions for Operating Style.** Hermes Agent / Nous Research uses `SOUL.md` loaded as system-prompt slot #1, followed by IDENTITY.md, USER.md, AGENTS.md, MEMORY.md ([S28]). ClawSouls / Soul Spec uses `SOUL.md` plus `IDENTITY.md` exported into CLAUDE.md ([S29]). OpenClaw treats them as a multi-file set ([S21]). There is no settled standard. Treat as a coherent design pattern, not a binding convention.
- **AGENTS.md vs CLAUDE.md precedence.** Practitioner guides disagree on whether CLAUDE.md should take precedence over AGENTS.md when both exist. The Amit Ray "Hierarchy Guide" places CLAUDE.md at the top ([S24]); HiveTrail and Augment Code emphasize using AGENTS.md as the canonical source with CLAUDE.md as a symlink ([S25], [S17]). Until Anthropic adds native AGENTS.md support, the practical answer is: pick one as canonical and symlink or import the other.
- **Whether context files help or hurt.** ETH Zurich research (cited by [S17]) found that LLM-generated context files reduced task success rates ~3% on average; human-curated files gave ~4% gain but at 20%+ inference cost overhead. Other practitioner sources are uniformly positive on context files. The conflict is real and resolvable only by measurement on your specific tasks.

**Interpretive assumptions** — calls the researcher made.

- **Treated the 15-category taxonomy from the user's source document as a working organizational frame, not as canon.** The categories are real; each maps to codified concepts somewhere; but their grouping (e.g., "Identity" vs. "Operating Style" as separate categories) is a useful pedagogical split, not an industry-standard partition. Alternative groupings (e.g., merging Identity + Operating Style into "Persona," or collapsing Memory + State into "Stateful Context") are equally defensible.
- **Treated SKILL.md and "Capability Module" as effectively interchangeable.** The agentskills.io spec uses "Skill"; the source document used "Capability Module" as a generalized category. They refer to the same thing in current ecosystem usage.
- **Treated MCP's control-source trichotomy as the cleanest formal vocabulary for distinguishing artifact types.** This is an editorial choice — the trichotomy is real and codified, but generalizing it from MCP's server-feature primitives to a universal lens on all artifacts is a synthesis call, not a sourced framework.
- **Reported the OpenAI Agents SDK's primitive count as four (Agents, Tools, Handoffs, Guardrails) with Sessions as a related concept.** OpenAI's marketing materials count "four primitives" but the SDK's actual primitive set includes Sessions in some surfaces. This is a vocabulary inconsistency in the source material rather than a deliberate omission.

**Areas of thin evidence.**

- **The Operating Style / persona-file category.** Multiple competing conventions exist; none is a formal standard; all sources are practitioner-blog rather than primary spec. Expect this to change.
- **Learning/Iteration patterns.** Less codified than other categories. Most guidance is folk wisdom from practitioner blogs; framework-level standards for "how an agent learns over time" do not yet exist beyond eval-driven iteration cycles.
- **Multi-agent orchestration token-cost claims.** The 4–7× and 15× multipliers come from a single Augment Code analysis ([S22], [S30]) citing Anthropic's own documentation; the underlying Anthropic source could not be independently verified. Treat the numbers as directionally correct but not precise.

## Open Questions & Gaps

1. **What is the right granularity for splitting Identity vs. Operating Style?** A clearer convention than the current SOUL/IDENTITY/USER/AGENTS/MEMORY stack would reduce confusion. Would need: a settled standard from a major framework or foundation, ideally with empirical evidence of slot-order impact.
2. **How should artifacts handle versioning across breaking framework changes?** When a SKILL.md author publishes v1 and the underlying SDK changes its tool-loading semantics, what's the migration story? Would need: a SemVer or similar discipline applied to the Agent Skills spec.
3. **What is the right boundary between Memory (durable) and Knowledge (general)?** A fact about *this user* clearly belongs in Memory; a fact about *the world* clearly belongs in Knowledge. But "this team uses Pixi instead of pip" sits between. Would need: better practitioner consensus or framework guidance.
4. **Are there published benchmarks comparing single-prompt vs. multi-artifact agent designs on identical tasks?** Most empirical evidence is anecdotal. Would need: rigorous comparison studies on standardized tasks (SWE-bench-style), holding the model constant.
5. **What is the failure mode of progressive disclosure when skill descriptions are poorly written?** Anecdotal evidence suggests poor descriptions cause skills to not trigger; how often, and how badly? Would need: published telemetry from major agent platforms.

## Staleness Indicators

How the consuming agent will know this brief is becoming wrong:

- **Time-based:** review after the `refresh_after` date (2026-11-16). Agent artifact conventions have been evolving on roughly a 3–6-month cadence; a 6-month horizon is appropriate.
- **Event-based:** if any of the following occur, this brief is likely partially invalidated:
  - **A new major version of the Agent Skills standard releases** → likely affects [F2], [F3], [F4], and the entire Capability artifacts section. Check agentskills.io changelog.
  - **A new MCP specification version supersedes 2025-06-18** → likely affects [F5], [F6], and the Resource/Tool/Prompt distinction in the Tools/Knowledge/Prompts section. Check modelcontextprotocol.io.
  - **Claude Code adds native AGENTS.md support** → resolves a Conflict item and changes precedence guidance in Identity section. Check Claude Code changelog.
  - **A second-generation Agent Skills spec adds a new layer between activation and execution** → would change [F3] and the progressive disclosure model.
  - **OpenAI publishes major changes to the Agents SDK primitive set** (e.g., adding a Memory primitive alongside Sessions) → affects [F8] and the Memory/State section.
  - **A persona-file standard achieves cross-vendor adoption** → resolves the open question in Identity/Operating Style and likely deprecates [CF11].
- **Signal-based:** if the agent's user reports that a framework's behavior diverges from what this brief describes, or if live tool calls return unexpected schemas (e.g., MCP servers responding with new `capabilities`), treat the relevant section as suspect and prefer the live data.

## Decision Heuristics for the Agent

How the consuming agent should USE this brief:

**DO**
- Cite from Canonical Facts ([F1]–[F15]) as authoritative ground truth.
- Cite from Core Findings ([CF1]–[CF13]) with appropriate confidence; LOAD-BEARING findings carry more weight than SUPPORTING.
- When building a new artifact, first identify which of the 15 categories it belongs to, then check this brief's section for that category to pick a sensible filename and structure.
- Default to **Markdown plus YAML frontmatter** for any new artifact unless a specific format is required (e.g., JSON schemas, `.env`).
- Default to **plain Markdown filenames using the conventions cited** (`SKILL.md`, `AGENTS.md`, `CLAUDE.md`, `MEMORY.md`, etc.) rather than inventing new names. When in doubt about persona files, use `SOUL.md` and note in a project README that the convention is emerging.
- Apply progressive disclosure: when a SKILL.md would exceed ~5,000 tokens or ~500 lines, split into `references/` and point to them from SKILL.md.
- When generating a skill description, include **both what the skill does and when to use it**, with trigger keywords — this is the basis on which the agent will (or won't) load it.
- When defining a tool, **invest in the description, parameter names, and examples** as much as the implementation. Anthropic spent more time on SWE-bench tools than on prompts.
- When asked about structured outputs, default to **Pydantic (Python) or Zod (TypeScript)** with native provider structured-output mode where supported, tool-calling fallback otherwise.
- When asked about multi-agent designs, push back if the user hasn't validated a single-agent version first. Multi-agent multiplies cost 4–7×.
- Defer to live tools and primary documentation for any topic where this brief's `refresh_after` date has passed, or where the user is working with a framework version newer than what was current at research time (2026-05-16).
- Flag uncertainty when answering from `mixed`-confidence sections (Identity/Operating Style, Learning/Iteration, multi-agent cost) or when the question touches a Conflict.
- When the user asks for an artifact in a category labeled `scope_out` (clinical/regulated tilt, deployment infra, framework-specific tutorials), say so explicitly and offer to either work within general-purpose conventions or point to a v2 brief that addresses the tilt.

**DO NOT**
- Do not cite Detailed Analysis paragraphs as facts; they are interpretation.
- Do not treat [INFERENCE]-tagged claims as established truth.
- Do not extrapolate beyond `scope_in` without explicitly flagging the extrapolation.
- Do not present this brief's framings (Mental Model tensions, control-source trichotomy, 15-category taxonomy) as universally accepted — they are an organizing frame synthesized from multiple sources, not a single industry consensus.
- **Do not confuse Skills with Tools.** A skill is *instructions* for how to do a kind of work; a tool is *an action* the agent can take. Skills can invoke tools; they are not interchangeable. This is the most frequently conflated pair in the domain.
- **Do not confuse Memory with State.** State is per-conversation, automatic, structural. Memory is per-user, explicit, curated. Conflating them produces agents that either forget everything across sessions or remember irrelevant noise.
- **Do not put task-specific instructions in CLAUDE.md or AGENTS.md.** Those are always-on Identity files with a ~150–200 instruction budget; task instructions belong in Skills.
- **Do not invent new artifact filenames when an established convention exists.** Use `SKILL.md` not `CAPABILITY.md`; `AGENTS.md` not `PROJECT.md`; `MEMORY.md` not `NOTES.md`.
- Do not advise multi-agent architecture without strong justification — the token cost is real and the coordination failures are common.
- Do not skip evaluation artifacts. The single most common gap in published agent retrospectives is "we didn't have trajectory eval until production broke."

## Sources

- **[S1]** Anthropic. *Equipping agents for the real world with Agent Skills.* Anthropic Engineering Blog. 2025. https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills. _Type: primary. Credibility: first-party from the originator of the Agent Skills standard._
- **[S2]** Anthropic. *Agent Skills — Claude API Docs.* Claude API documentation. Accessed 2026-05-16, last updated ~1 week prior to access. https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview. _Type: primary. Credibility: official product documentation._
- **[S3]** Agent Skills Standard. *Agent Skills Overview.* agentskills.io. Standard released 2025-12-18. https://agentskills.io/home. _Type: primary. Credibility: the canonical open-standard specification._
- **[S4]** Anthropic. *Building effective agents.* Anthropic Engineering Blog. 2024-12-19. https://www.anthropic.com/engineering/building-effective-agents. _Type: primary. Credibility: foundational primary document defining the workflow patterns adopted across the industry._
- **[S5]** Anthropic. *Building agents with the Claude Agent SDK.* Anthropic Engineering Blog. 2025-09-29. https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk. _Type: primary. Credibility: first-party SDK announcement and architectural overview._
- **[S6]** Model Context Protocol. *Resources — Server Features.* MCP Specification 2025-06-18. https://modelcontextprotocol.io/specification/2025-06-18/server/resources. _Type: primary. Credibility: canonical protocol specification._
- **[S7]** Model Context Protocol. *Prompts — Server Features.* MCP Specification 2025-06-18. https://modelcontextprotocol.io/specification/2025-06-18/server/prompts. _Type: primary. Credibility: canonical protocol specification._
- **[S8]** Model Context Protocol. *Tools — Server Features.* MCP Specification 2025-06-18. https://modelcontextprotocol.io/specification/2025-06-18/server/tools. _Type: primary. Credibility: canonical protocol specification._
- **[S9]** OpenAI. *Agents SDK Overview.* OpenAI Developer Documentation. 2026. https://developers.openai.com/api/docs/guides/agents. _Type: primary. Credibility: first-party SDK documentation._
- **[S10]** OpenAI. *Handoffs — OpenAI Agents SDK.* openai.github.io/openai-agents-python. Accessed 2026-05-16. https://openai.github.io/openai-agents-python/handoffs/. _Type: primary. Credibility: first-party SDK reference._
- **[S11]** OpenAI. *Guardrails — OpenAI Agents SDK.* openai.github.io/openai-agents-python. Accessed 2026-05-16. https://openai.github.io/openai-agents-python/guardrails/. _Type: primary. Credibility: first-party SDK reference._
- **[S12]** OpenAI. *A practical guide to building agents.* openai.com Business Resources. 2025. https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/. _Type: primary. Credibility: first-party engineering guidance._
- **[S13]** LangChain. *Persistence — LangGraph Documentation.* docs.langchain.com. Accessed 2026-05-16. https://docs.langchain.com/oss/python/langgraph/persistence. _Type: primary. Credibility: first-party framework documentation._
- **[S14]** LangChain. *Structured output.* docs.langchain.com. 2026-04-06. https://docs.langchain.com/oss/python/langchain/structured-output. _Type: primary. Credibility: first-party framework documentation._
- **[S15]** Pydantic. *Output — Pydantic AI.* ai.pydantic.dev. Accessed 2026-05-16. https://ai.pydantic.dev/output/. _Type: primary. Credibility: first-party framework documentation._
- **[S16]** HumanLayer. *Writing a good CLAUDE.md.* HumanLayer Blog. 2025-11-25. https://www.humanlayer.dev/blog/writing-a-good-claude-md. _Type: secondary. Credibility: detailed practitioner analysis citing Claude Code internals._
- **[S17]** Augment Code. *How to Build Your AGENTS.md (2026).* Augment Code Guides. 2026-03-31. https://www.augmentcode.com/guides/how-to-build-agents-md. _Type: secondary. Credibility: practitioner guide citing the AGENTS.md standard and ETH Zurich research._
- **[S18]** SwirlAI Newsletter. *Agent Skills: Progressive Disclosure as a System Design Pattern.* 2026-03-11. https://www.newsletter.swirlai.com/p/agent-skills-progressive-disclosure. _Type: secondary. Credibility: detailed practitioner analysis with quantitative measurements of skill token costs._
- **[S19]** Braintrust. *Agent observability: The complete guide for 2026.* 2026. https://www.braintrust.dev/articles/agent-observability-complete-guide-2026. _Type: secondary. Credibility: vendor-published but technically substantive guide to tracing/eval._
- **[S20]** Focused.io. *Persistent Agent Memory in LangGraph: Cross-Thread State and Memory Stores.* 2026-03-11. https://focused.io/lab/persistent-agent-memory-in-langgraph. _Type: secondary. Credibility: technical deep-dive on the Checkpointer/Store distinction._
- **[S21]** Stanza. *OpenClaw SOUL.md — Agent Persona Guide.* 2026-02-24. https://www.stanza.dev/concepts/openclaw-soul-persona. _Type: secondary. Credibility: convention-defining content for one of the emerging SOUL.md ecosystems._
- **[S22]** Penligent. *Inside Claude Code, The Architecture Behind Tools, Memory, Hooks, and MCP.* 2026-04-02. https://www.penligent.ai/hackinglabs/inside-claude-code-the-architecture-behind-tools-memory-hooks-and-mcp/. _Type: secondary. Credibility: technical analysis citing primary Anthropic documentation._
- **[S23]** User-provided document. *Ontology of agentic AI concepts.* Synthesized taxonomy document supplied by user as starting input, 2026-05-16. _Type: secondary (synthesis). Credibility: integrates citations to primary sources [S1], [S4], MCP Resources/Prompts specs, OpenAI Agents SDK, LangChain — all independently re-verified in this brief._
- **[S24]** Amit Ray. *Claude.md vs Agents.md vs Memory.md, Skills.md, Context.md & The Hierarchy (2026 Guide).* amitray.com. 2026-04-14. https://amitray.com/claude-md-vs-agents-md-memory-md-skills-md-context-md-guide-2026/. _Type: secondary. Credibility: practitioner synthesis of the multi-file convention stack; cited for the explicit precedence-order argument._
- **[S25]** HiveTrail. *AGENTS.md vs CLAUDE.md: The AI Developer's Guide to Context Standards.* hivetrail.com Blog. 2026 (recent). https://hivetrail.com/blog/agents-md-vs-claude-md-cross-tool-standard. _Type: secondary. Credibility: detailed comparison of the two conventions with primary-document citation._
- **[S26]** CopyMarkdown. *CLAUDE.md, AGENTS.md, GEMINI.md Explained.* copymarkdown.com. 2026. https://copymarkdown.com/agents-md-explained/. _Type: secondary. Credibility: clear practitioner exposition of why Markdown won as the artifact format._
- **[S27]** FutureAGI. *Agent Evaluation Frameworks in 2026: 7 Tools Compared for Real Agents.* futureagi.com Blog. 2026. https://futureagi.com/blog/agent-evaluation-frameworks-2026. _Type: secondary. Credibility: vendor-published but technically substantive comparison of the eval ecosystem; informs the session/trajectory/leaf model._
- **[S28]** Nous Research. *Personality & SOUL.md — Hermes Agent Docs.* hermes-agent.nousresearch.com. 2026. https://hermes-agent.nousresearch.com/docs/user-guide/features/personality. _Type: secondary. Credibility: convention-defining content for one of the emerging SOUL.md ecosystems (Hermes / Nous Research)._
- **[S29]** ClawSouls. *How to Add a Persona to Claude Code Using Soul Spec.* blog.clawsouls.ai. 2026-02-21. https://blog.clawsouls.ai/en/guides/claude-code-soul/. _Type: secondary. Credibility: another emerging SOUL.md / persona-file convention; cited as evidence of unsettled standard._
- **[S30]** ksred. *Claude Code Agents & Subagents: What They Actually Unlock.* ksred.com. 2026-03-16. https://www.ksred.com/claude-code-agents-and-subagents-what-they-actually-unlock/. _Type: secondary. Credibility: practitioner analysis citing Anthropic's published documentation; source of the multi-agent token-cost multipliers._

## Changelog

- **v1.0 (2026-05-16):** Initial brief. General-purpose, framework-agnostic. A planned v2 will add a clinical / regulated-work domain tilt as a parallel artifact (not a supersession).
