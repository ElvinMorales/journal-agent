# Synthetic Runtime Viewer Inputs

The automated viewer tests build a temporary initialized vault containing public-safe synthetic concepts:

- an allowlisted Memory file with a heading and synthetic marker text;
- an allowlisted State file with review/stale and expiration trigger lines;
- separate pending Memory and State proposal JSON records;
- approved/applied proposal metadata without relying on real wording;
- a metadata-only audit event with a synthetic hash and character count; and
- a synthetic session file whose filename, size, and modification time are displayed by default.

The cases also place synthetic raw content under `Journal/Daily`, malformed text in a proposal JSON file, and HTML-like strings in selected fields. Tests verify that the journal folder is not read, malformed content is not leaked, dynamic values are escaped, and optional include flags are required before bounded content appears.

Tests create and remove these vaults under the operating system's temporary directory. No real vault is used. No generated viewer HTML, screenshot, private path, journal entry, filled Memory, live State, real proposal, runtime log, or export is committed.
