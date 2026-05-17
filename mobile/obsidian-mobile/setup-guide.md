# Obsidian Mobile Setup Guide

Obsidian Mobile is the recommended private storage layer for phone-first journaling.

## Setup

1. Install Obsidian Mobile.
2. Create or open a private vault.
3. Create folders such as:
   - `Journal/`
   - `Journal/Daily/`
   - `Journal/Reflections/`
   - `Journal/Therapy Prep/`
   - `Inbox/`
4. Add a daily note template based on `daily-note-mobile-template.md`.
5. Add a reflection section based on `reflection-pasteback-template.md`.
6. Test any shortcut automation with non-sensitive sample text before using it for real notes.

## Suggested Daily Note Path

Use a predictable daily note path, such as:

```text
Journal/Daily/YYYY-MM-DD.md
```

This makes iOS Shortcut append actions easier to configure.

## Sync and Device Privacy

- Use a strong phone passcode or password.
- Be careful with iCloud, Obsidian Sync, third-party sync, and backups.
- Avoid shared devices for private journaling.
- Avoid screenshots of private entries.
- Do not install untrusted plugins for sensitive journal data.
- Check whether notification previews might reveal note content.

## Public Repo Boundary

The public GitHub repo is for templates, prompts, schemas, and safety docs. It should not contain filled daily notes, raw entries, private reflections, therapy notes, crisis notes, exports, memory, or identifying details.

## Reflection Loop

1. Write in Obsidian.
2. Copy a selected excerpt.
3. Paste into the custom GPT in ChatGPT mobile.
4. Read the response.
5. Paste only useful reflection back into Obsidian.

## Future Work

A PWA or OpenClaw mobile endpoint could later replace some copy/paste steps. The MVP does not require either one.
