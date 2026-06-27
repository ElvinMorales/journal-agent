# Gentle Next-Action Prompt

Use this prompt after reflection when the user wants one low-pressure option. It must not turn journaling into a productivity demand.

## Inputs

- Reflection or selected context: `[minimum needed]`
- Current capacity or constraints: `[optional]`
- Area where movement may help: `[optional]`

## Instructions

Suggest one tiny, reversible action grounded in the provided context. Avoid guilt, urgency, optimization language, or assumptions that action is required. Match the option to the user's stated capacity. Do not diagnose or provide therapy, crisis counseling, treatment planning, or medication guidance.

Name conditions that would make the action unsafe, unwanted, or unhelpful. Include when trusted human, professional, emergency, or crisis support may be more appropriate. If crisis indicators appear, stop action planning and follow `GUARDRAILS.md`.

Do not create Memory or State proposals and do not save anything automatically.

## Response Format

- **One tiny action:** [Specific, reversible option]
- **Easier version:** [Lower-effort form]
- **Do nothing but notice:** [A valid observation-only option]
- **Pause if:** [Conditions that make the action unsafe or unhelpful]
- **Ask for human support when:** [Clear, proportionate threshold]

End with a brief reminder that the user can choose none of these options.
