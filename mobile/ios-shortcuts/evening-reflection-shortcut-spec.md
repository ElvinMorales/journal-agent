# Evening Reflection Shortcut Spec

Purpose: reduce friction for a no-code evening review from a phone.

This is a specification only. It is not an importable shortcut file.

## Recommended Actions

1. Get current date.
2. Open today's Obsidian daily note.
3. Show a menu:
   - Copy prompt.
   - Open ChatGPT.
   - Open reflection pasteback template.
4. If `Copy prompt` is selected, copy an evening reflection prompt from `mobile/gpt-mobile/copy-paste-prompts.md`.
5. If `Open ChatGPT` is selected, open ChatGPT mobile.
6. If `Open reflection pasteback template` is selected, open the Obsidian note section where the reflection will be pasted.

## Manual Review Step

The shortcut should not automatically send the whole daily note to an AI app. The safer MVP is:

1. User reads today's note.
2. User selects a specific excerpt.
3. User copies it into ChatGPT mobile.
4. User reads the response.
5. User pastes only useful parts back into Obsidian.

## Suggested Prompt

Use the evening prompt in `mobile/gpt-mobile/copy-paste-prompts.md`.

## Safety Boundary

This workflow is for ordinary reflection, not therapy, diagnosis, crisis counseling, medical advice, treatment planning, or medication guidance.

If the selected entry includes crisis indicators, prioritize immediate human support and emergency/crisis resources instead of ordinary analysis.

## Privacy Boundary

- Avoid automatically copying entire notes.
- Avoid screenshots of private entries or responses.
- Do not save generated reflections into the public repo.
