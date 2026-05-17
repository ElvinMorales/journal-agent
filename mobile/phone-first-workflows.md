# Phone-First Workflows

This guide is for users who want to journal and receive reflections from a phone without Git, VS Code, terminal commands, or local developer tooling.

## Recommended Architecture

Use each tool for the part it handles best:

| Tool | Role | Private Content? |
|---|---|---:|
| Obsidian Mobile | Private journal storage and user-owned notes | Yes |
| ChatGPT mobile custom GPT | Reflection on selected copied text | Selected excerpts only |
| iOS Shortcuts | Fast capture into notes | Yes, if configured locally |
| Public GitHub repo | Templates, prompts, schemas, safety docs | No raw journal content |

The public repo should remain a clean artifact/template backend. It should not become a diary, therapy notebook, memory store, crisis log, or export archive.

## MVP Daily Flow

1. Capture a thought on the phone.
2. Save it into Obsidian Mobile as a daily note or inbox capture.
3. Later, select a specific entry or excerpt.
4. Copy it into the custom GPT in ChatGPT mobile.
5. Ask for a tentative, non-clinical reflection.
6. Paste useful reflections back into Obsidian under a clearly labeled section.

## Quick Capture Flow

Use the shortcut spec in `ios-shortcuts/quick-capture-shortcut-spec.md` to build a personal iOS Shortcut that:

- Accepts typed text or dictation.
- Adds a timestamp.
- Appends the result to today's note or a mobile capture file.
- Optionally opens Obsidian after capture.

Keep quick captures short. A timestamped sentence is usually enough.

## Evening Reflection Flow

Use `ios-shortcuts/evening-reflection-shortcut-spec.md` to open Obsidian or ChatGPT and reduce friction at the end of the day.

The safe default is still manual review:

1. Open today's Obsidian note.
2. Pick what you want reflected.
3. Copy it to ChatGPT mobile.
4. Paste the response back only after reading it.

## Therapy Prep Flow

Use `ios-shortcuts/therapy-prep-shortcut-spec.md` to open relevant notes or a therapy-prep template.

Therapy-prep notes should remain user-owned and tentative. They can help organize what to discuss with a licensed professional, but they should not present agent conclusions as clinical findings.

## Crisis Handling

Do not use ordinary reflection prompts or shortcuts as the main path for crisis content. If there is immediate danger, current self-harm intent, inability to stay safe, or danger from another person, prioritize:

- Contacting trusted human support now.
- Local emergency services when danger may be imminent.
- Crisis resources such as 988 in the U.S.
- Reducing access to means of harm where safely possible.

## Privacy Defaults

- Lock the phone with a passcode or password.
- Avoid shared devices for journaling.
- Check whether Obsidian sync, iCloud, backups, or third-party sync tools are enabled.
- Avoid screenshots of entries and reflections.
- Avoid untrusted plugins and automation actions that upload sensitive text.
- Keep personal content out of the public GitHub repo.

## Later Options

A PWA or OpenClaw mobile endpoint could provide a more polished phone interface later. For MVP, Obsidian Mobile plus ChatGPT mobile plus optional iOS Shortcuts is enough.
