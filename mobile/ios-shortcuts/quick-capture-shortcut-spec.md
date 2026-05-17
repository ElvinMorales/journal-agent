# Quick Capture Shortcut Spec

Purpose: capture a short journal thought from the phone and save it with a timestamp.

This is a specification only. It is not an importable shortcut file.

## Inputs

- Capture mode: dictate text or type text.
- Optional fields: mood, energy, intensity, or tag.

Keep optional fields lightweight. They are cues for reflection, not clinical measures.

## Recommended Actions

1. Ask for capture mode:
   - Dictate text.
   - Type text.
2. Collect the journal thought.
3. If the text is empty, stop.
4. Get current date and time.
5. Format timestamp as `YYYY-MM-DD HH:mm`.
6. Build a markdown block:

```markdown
## HH:mm

[captured thought]

Mood:
Energy:
Intensity:
```

7. Save or append the block to one of:
   - Today's Obsidian daily note.
   - A mobile capture file such as `Mobile Capture.md`.
8. Optional: open Obsidian.
9. Optional: open ChatGPT mobile for later reflection.

## Obsidian URL Option

If using Obsidian URL actions, configure the shortcut to append to a known vault and file. Test with non-sensitive sample text first.

Example target patterns:

- Daily note: `Journal/YYYY-MM-DD.md`
- Capture inbox: `Inbox/Mobile Capture.md`

Do not place real entries in this public repository while testing.

## Safety Check

If the captured thought includes immediate danger, current intent to self-harm, inability to stay safe, or danger from someone else, stop ordinary automation and seek human support. Use emergency services when danger may be imminent and crisis resources such as 988 in the U.S.

## Privacy Check

- Confirm the destination file is private.
- Confirm sync settings are acceptable.
- Avoid running the shortcut from a shared or unlocked device.
- Avoid adding actions from untrusted apps.
