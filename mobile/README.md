# Mobile Starter Pack

This folder describes a phone-first workflow for using the journal companion artifacts without Git, VS Code, or command-line tools.

The recommended MVP is:

1. Store private journal notes in Obsidian Mobile or another private notes app you control.
2. Use a custom GPT in the ChatGPT mobile app for reflection.
3. Use iOS Shortcuts for quick capture into a daily note or capture file.
4. Treat this public GitHub repository as the artifact and template backend, not as journal storage.

Do not store raw personal journal entries, private reflections, therapy notes, crisis notes, memory, state, exports, screenshots, secrets, or identifying details in this public repository.

## No-Code Flow

1. Open Obsidian Mobile.
2. Write a short entry in a daily note.
3. Copy only the entry or excerpt you want reflected on.
4. Paste it into the custom GPT with a prompt from `mobile/gpt-mobile/copy-paste-prompts.md`.
5. Review the response for fit and safety.
6. Paste the useful parts back into Obsidian using `mobile/obsidian-mobile/reflection-pasteback-template.md`.

## Safety Scope

This starter pack supports self-reflection. It is not therapy, diagnosis, crisis counseling, medical advice, treatment planning, medication guidance, or a replacement for licensed care.

If a note includes current intent to self-harm, inability to stay safe, danger from someone else, severe intoxication, or another immediate safety concern, do not route it through ordinary automation. Prioritize immediate human support, local emergency services when danger may be imminent, and crisis resources such as 988 in the U.S.

## Privacy Basics

- Use a phone passcode or password and biometric lock when available.
- Be careful with cloud sync settings and shared devices.
- Avoid screenshots of private entries.
- Do not install untrusted Obsidian plugins for sensitive journal data.
- Review any copied text before sending it to a mobile AI app.

## Files

- `phone-first-workflows.md`: overview of the recommended mobile paths.
- `ios-shortcuts/`: iOS Shortcut specifications for quick capture and review preparation.
- `obsidian-mobile/`: setup guide and mobile note templates.
- `gpt-mobile/`: custom GPT workflow, copy-paste prompts, and voice journaling guidance.

## Future Work

A polished PWA or OpenClaw mobile endpoint could reduce copy/paste friction later. It is not required for the MVP.
