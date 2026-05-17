# Contributing

Contributions should keep this repository safe as a public, reusable template
for journal companion artifacts.

## Privacy Rules

- Do not commit real journal entries, private notes, summaries, memory, state,
  exports, crisis notes, therapy notes, logs, databases, environment files, or
  secrets.
- Do not include real names, addresses, contact details, workplace names, local
  file paths, account identifiers, or third-party private information.
- Use fictional, minimal, example-only content in templates, prompts, docs, and
  evals.
- Keep filled journal artifacts only under ignored `private/` paths or another
  user-controlled private system.

## Safety Rules

- Do not present the companion as therapy, diagnosis, crisis counseling,
  medical advice, treatment planning, medication guidance, or a replacement for
  licensed care.
- Use tentative language for reflections and patterns.
- Do not add numerical suicide or self-harm risk scores.
- Do not add self-harm methods, lethal-dose information, or instructions that
  enable harm.

## Before Opening a Pull Request

Run:

```powershell
python scripts\validate-json-schemas.py
```

Also check that new examples are fictional and that no private files are
tracked:

```powershell
git ls-files private
```
