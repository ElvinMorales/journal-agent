# Private Obsidian Runtime Starter Guide

## Purpose

This guide helps a user create a private runtime/data plane for the Journal Mirror Agent. The public repository remains the reusable control plane. A private Obsidian vault or similar private notes system remains user-owned, outside this repository, and outside its Git history.

The setup is optional and Obsidian-friendly, not Obsidian-required. Plain folders and Markdown files in any private notes system are enough. No plugin, server, connector, or automated vault access is required. No private journal content belongs in the public repository.

## Public Repo vs Private Vault

| Public repo/control plane | Private vault/data plane |
|---|---|
| Instructions | Raw journal entries |
| Guardrails and privacy rules | Selected excerpts |
| Prompts and schemas | Journal Mirror session notes |
| Synthetic examples | User-approved private reflections |
| Validation scripts | Pending Memory and State proposals |
| Architecture docs | Approved Memory and current State |
| Reusable templates | Private exports |

The public repo describes how the Journal Mirror should behave. The private vault contains the real inputs, outputs, and user-approved runtime records created during use.

## Suggested Private Vault Structure

This generic tree is an example for a private vault only. Do not create or commit it inside this repository.

```text
Private Journal Mirror Vault/
├── Journal/
│   ├── Daily/
│   ├── Freewrites/
│   └── Weekly/
├── Journal Mirror/
│   ├── Sessions/
│   ├── Reflections/
│   ├── Pending Updates/
│   │   ├── memory/
│   │   └── state/
│   └── Approved Updates/
├── Memory/
│   ├── reflection-preferences.md
│   ├── recurring-patterns.md
│   └── values-and-supports.md
├── State/
│   ├── current-session.md
│   ├── active-themes.md
│   └── open-questions.md
└── Exports/
```

- `Journal/` holds natural private writing in whatever organization is useful.
- `Journal Mirror/Sessions/` holds private session records, including the context deliberately selected for a session.
- `Journal Mirror/Reflections/` holds private reflections the user chooses to retain.
- `Journal Mirror/Pending Updates/` keeps proposed Memory and State changes separate while they await review.
- `Journal Mirror/Approved Updates/` may hold a private review trail when the user wants one; it is optional.
- `Memory/` holds small, durable, user-approved context likely to help in future sessions.
- `State/` holds temporary context for a current session, week, question, or open loop.
- `Exports/` holds private, user-reviewed exports. It should not be copied into the public repo.

Folder and file names are suggestions. The important boundaries are that the vault stays private, Memory and State stay separate, and proposals remain pending until reviewed.

## Minimum Starter Setup

The smallest useful setup is:

```text
Journal/
Journal Mirror/Sessions/
Journal Mirror/Pending Updates/memory/
Journal Mirror/Pending Updates/state/
Memory/
State/
Exports/
```

Start manually by creating these folders and ordinary Markdown files in a private notes system. Add `Reflections/` or `Approved Updates/` only if those distinctions become useful. This workflow does not require automation.

## How to Run a Manual Journal Mirror Session

1. Write naturally in the private vault.
2. Select one entry, excerpt, or small group of entries. Use the smallest context that supports the question.
3. Paste only that selected context into `prompts/journal-mirror-session.md`. Use `prompts/freeform-entry-mirror.md` for one unstructured entry or `prompts/recent-pattern-review.md` for a small selected set.
4. Ask for a tentative reflection, clarifying questions, or an optional low-pressure next step with `prompts/gentle-next-action.md`. Request separate Memory and State proposals only when wanted.
5. Save any private reflection only in the private vault.
6. Review each proposed update with `prompts/update-proposal-review.md` before adding it to private Memory or State. Approval for one destination does not approve the other.
7. Edit or discard anything that feels wrong, too broad, too clinical, or not useful.

If crisis indicators appear, stop the ordinary reflection flow and follow `GUARDRAILS.md`: prioritize immediate safety, trusted human support, relevant emergency or crisis resources, and reducing access to harm.

## Memory vs State in the Private Vault

Memory is durable, user-approved context likely to remain useful across future sessions. State is temporary context useful for a current session, week, question, or open loop.

Do not promote State to Memory automatically. Do not save one-off emotions, inferred traits, diagnoses, or raw journal entries as Memory. Prefer notes that are small, editable, and reversible.

```text
Good Memory candidate:
- "The user prefers reflection that starts with validation before pattern analysis."

Poor Memory candidate:
- "The user is always avoidant."

Good State candidate:
- "Current open question: how to make evenings feel less chaotic this week."

Poor State candidate:
- A full pasted journal entry.
```

A proposal may be useful but classified incorrectly. Review both its wording and its destination before saving it.

## Pending Update Review Flow

```text
proposal created
→ saved to Pending Updates
→ user reviews
→ user edits, approves, or discards
→ approved update moves to Memory or State
```

Keep Memory proposals under `Pending Updates/memory/` and State proposals under `Pending Updates/state/`. Moving or copying an approved item into its destination is a deliberate user action. Proposal files contain private runtime context and are private runtime artifacts, not public repo artifacts.

## What Not to Store in the Public Repo

Do not commit or publish:

- Raw journal entries or selected excerpts.
- Private reflections, therapy notes, or crisis notes.
- Filled Memory, live State, or pending updates from real sessions.
- Exports, logs, screenshots, or database files.
- Private vault files or local paths.
- Secrets, credentials, or environment values.
- Employer-specific material or identifying details.
- Self-harm method details in examples or public documentation.

Private storage is not automatically confidential. Review the notes system's device, sync, backup, sharing, and access controls against personal privacy needs.

## Suggested Private File Templates

The following lightweight templates are private-only examples. A user may copy them into a private vault, but must not commit completed copies to this repository.

### `Journal Mirror/Sessions/YYYY-MM-DD-session.md`

```markdown
# Journal Mirror Session — YYYY-MM-DD

## Focus
[Question or reflection goal]

## Selected Context
[Private excerpt selected for this session]

## Reflection
[Tentative reflection kept only if useful]

## Questions or Optional Next Steps
- [Question or small reversible option]

## Update Proposals
- State: [none or link to a separate pending proposal]
- Memory: [none or link to a separate pending proposal]
```

### `Journal Mirror/Pending Updates/memory/YYYY-MM-DD-memory-proposal.md`

```markdown
# Pending Memory Proposal — YYYY-MM-DD

- Proposed text: [small durable context]
- Why it may remain useful: [brief reason]
- Source: [private session reference, not a copied entry]
- Uncertainty: [what may be incomplete or wrong]
- Review decision: pending | edited and approved | approved | discarded
```

### `Journal Mirror/Pending Updates/state/YYYY-MM-DD-state-proposal.md`

```markdown
# Pending State Proposal — YYYY-MM-DD

- Proposed text: [temporary current context]
- Why it is useful now: [brief reason]
- Review or stale trigger: [date, event, or end of session]
- Source: [private session reference, not a copied entry]
- Review decision: pending | edited and approved | approved | discarded
```

### `State/current-session.md`

```markdown
# Current Session

- Current focus: [short description]
- Selected context reference: [private note link or identifier]
- Open question: [one current question]
- Constraints: [topics, retention, or response preferences]
- Review trigger: [end of session or date]
```

## Validation Before Publishing Changes

Before contributing changes to the public repository, confirm:

- [ ] No real entries or selected excerpts.
- [ ] No local paths or private vault files.
- [ ] No screenshots.
- [ ] No filled Memory or live State.
- [ ] No live pending proposals.
- [ ] No logs, exports, databases, or secrets.
- [ ] Only synthetic examples.
