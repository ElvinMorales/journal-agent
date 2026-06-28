# Security

This project handles artifact patterns for sensitive journal workflows. Do not
include private journal data, real names, secrets, crisis notes, medical details,
or third-party private information in public issues, pull requests, examples, or
logs.

## Reporting Sensitive Issues

If you find committed private data, credentials, or a safety issue that should
not be public, report it privately through the repository owner's preferred
private contact channel or GitHub private vulnerability reporting if enabled.
Do not open a public issue with the sensitive content.

## Scope

Please report:

- Accidental exposure of private journal data or identifiers.
- Secrets or credentials committed to the repository.
- Gaps that could cause private data to be written outside ignored `private/`
  paths.
- Safety-boundary failures that could encourage diagnosis, treatment planning,
  medication guidance, crisis counseling, self-harm methods, or other harmful
  advice.

This repository is not an emergency or crisis-support channel. If someone may be
in immediate danger, contact local emergency services or a crisis resource in
the person's location.

## Future Controller Boundary

`docs/future-mcp-vps-controller-contract.md` specifies least-privilege and approval requirements for any possible future private runtime edge. It is not an implementation. Secrets, controller configuration, runtime logs, private vault content, and private outputs must remain outside Git; a future controller must not broaden scope, run silently, or contact external services without explicit configuration and review.

## Private Vault Initializer Boundary

`scripts/init-private-vault.py` accepts an explicit absolute target and refuses to run at the public repository root or inside it. It creates only fixed generic folders and Markdown starter files; generated files must not contain secrets, credentials, connector configuration, or private runtime content and must not be committed. Users remain responsible for the security of the target device and its sync, backup, access, and sharing controls.
