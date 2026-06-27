# Recent Pattern Review Prompt

Use this prompt with a small, user-selected set of entries or excerpts. The selection is a sample, not access to a complete journal history.

## Inputs

- Selected entries or excerpts: `[paste only in the private session]`
- Date range or ordering: `[optional]`
- Review question: `[optional]`
- Propose State updates: `yes | no` (default: `no`)
- Propose Memory candidates: `yes | no` (default: `no`)

## Instructions

Compare only the selected material. Identify repeated themes, what changed, what stayed similar, possible triggers, possible supports, and open loops. Cite the entry labels or dates that support each observation when available. Separate repeated evidence from single mentions and include counterexamples or improvements.

Use tentative, non-clinical language. A small sample is not proof of a fixed trait, diagnosis, trauma history, or enduring pattern. Do not provide therapy, crisis counseling, treatment planning, or medication guidance. If crisis indicators appear, stop ordinary pattern review and follow `GUARDRAILS.md`.

Only propose State when requested and useful for temporary goals, open questions, or near-term context. Only offer a Memory candidate when explicitly requested, directly supported across the selection, likely durable, and minimally worded. Do not save anything automatically or promote State to Memory.

## Response Format

### Repeated Themes

- [Theme, supporting entries, and confidence limits]

### What Changed

- [Change across the selected entries]

### What Stayed Similar

- [Similarity without trait language]

### Possible Triggers or Supports

- [Tentative trigger or support and evidence]

### Open Loops

- [Unresolved question or situation]

### Uncertainty

[Missing context, alternative explanations, and sample limits.]

### Possible State Updates (only if requested)

- [Temporary proposal with review/stale trigger]

### Conservative Memory Candidates (only if requested)

- [Durable candidate, evidence, uncertainty, and why user review is needed]

End by reminding the user that nothing was saved and each proposal can be edited or discarded.
