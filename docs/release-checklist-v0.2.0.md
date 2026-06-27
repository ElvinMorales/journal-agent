# v0.2.0 Release Checklist

Use this checklist after the release-readiness PR merges and before creating a `v0.2.0` tag or GitHub release. It records release gates; it does not itself authorize a release action.

## Documentation Completeness

- [ ] `README.md` explains the public file-first scaffold and manual private-first workflow.
- [ ] `docs/release-notes/v0.2.0.md` accurately describes the release-candidate state.
- [ ] `docs/v0.2-usable-product-handoff.md` gives a public reader a practical start path.
- [ ] Workflow, private runtime, proposal review, architecture, lifecycle, and future-controller docs agree.
- [ ] `CHANGELOG.md`, `BACKLOG.md`, and `docs/roadmap-v0.2.0.md` reflect issue #17 without claiming a tag exists.
- [ ] `ARTIFACT_MAP.md` and `docs/taxonomy-mapping.md` retain and map the original 14 buckets.

## Link and Navigation Check

- [ ] README links to the handoff, private runtime guide, workflow, proposal review guide, release notes, and this checklist.
- [ ] Every relative link in changed Markdown resolves to an existing repository path.
- [ ] No document references a renamed or missing file.
- [ ] Release docs follow the existing `docs/release-notes/` convention.

PowerShell spot check for Markdown links can supplement manual review; directory links and anchors still require human inspection.

## Public / Private Safety

- [ ] Public files contain only reusable control-plane artifacts, blank templates, or clearly synthetic examples.
- [ ] No real entry, selected excerpt, private reflection, filled Memory, live State, real pending proposal, private vault file, therapy note, crisis note, export, log, database, screenshot, local path, secret, credential, or identifying detail is included.
- [ ] The private notes system remains the data plane and outside Git.
- [ ] Public examples derived from private use are independently synthetic or deliberately redacted and reviewed.
- [ ] No document claims privacy or confidentiality beyond actual user-controlled storage and tooling.

Run:

```powershell
git ls-files private
git grep -n -i "real journal\|actual entry\|my journal\|therapy note\|crisis note\|diagnosis\|medication\|password\|secret\|token\|api_key\|confidential\|proprietary\|C:\\\\Users\|/Users/"
```

`git ls-files private` should list only `.gitkeep` placeholders. Review grep matches manually; expected safety warnings are not failures.

## Memory / State Boundary

- [ ] Memory is described as durable, minimal, and explicitly user-approved.
- [ ] State is described as temporary and includes a review, stale, or expiration trigger.
- [ ] Memory and State use separate proposals, schemas, destinations, and approval decisions.
- [ ] No document permits silent State-to-Memory promotion.
- [ ] Proposal creation, proposal review, exact-wording approval, and manual application remain distinct.
- [ ] No proposal is treated as an automatic or implied write.

## Proposal Schema Validation

- [ ] Memory and State proposal schemas remain separate and valid.
- [ ] Synthetic proposal fixtures validate against their intended schemas.
- [ ] JSON examples parse successfully.

Run:

```powershell
python scripts/validate-json-schemas.py
Get-ChildItem examples -Recurse -Filter *.json | ForEach-Object {
  python -m json.tool $_.FullName > $null
}
```

## Synthetic Examples and Evals

- [ ] All walkthroughs, fixtures, and eval inputs are clearly synthetic.
- [ ] Journal Mirror evals cover selected-context privacy and tentative reflection.
- [ ] Proposal evals cover classification, required fields, approval, discard, and State expiration.
- [ ] Safety evals cover clinical refusal and crisis routing without method details or numeric scoring.
- [ ] Future-controller evals remain design-boundary checks and do not imply executable behavior.
- [ ] Eval results are qualitative boundary evidence, not clinical validation or effectiveness claims.

## Runtime Non-Implementation Check

- [ ] No live runtime, hosted service, app backend, MCP server, VPS controller, plugin, connector, vault reader, or background job was added.
- [ ] No executable controller example or runtime configuration was added.
- [ ] No automatic Memory or State persistence was added.
- [ ] The future controller contract is labeled design-only.
- [ ] No document implies current vault access or broad notes search.

Review the changed scope:

```powershell
git diff --name-only main...HEAD
git diff --cached --name-only
```

If changes are not staged, the second command may be empty. Review all listed paths manually.

## Clinical / Safety Boundary Check

- [ ] The project is described as a reflection companion, not therapy, medical advice, crisis counseling, or a clinical product.
- [ ] No diagnosis, disorder labeling, treatment planning, medication guidance, clinical claim, or therapeutic-effectiveness claim is added.
- [ ] No numerical suicide or self-harm risk score is used.
- [ ] Crisis indicators stop ordinary reflection and prioritize immediate safety, trusted human support, and local emergency or crisis resources.
- [ ] Public materials contain no self-harm method detail.

Run and review matches manually:

```powershell
git grep -n -i "method\|means\|weapon\|dose\|dosage\|cut\|hanging\|overdose"
```

High-level safety-boundary wording may be expected. Remove procedural or enabling detail.

## Git Hygiene Check

- [ ] Working changes are intentional and release-readiness-only.
- [ ] No merge conflict markers remain.
- [ ] No nested repository exists.
- [ ] No unexpected untracked file would be included.
- [ ] `.gitattributes` applies the intended text normalization policy without a broad line-ending-only diff.
- [ ] `.agents/` is ignored and `git ls-files .agents` returns no tracked content.
- [ ] No release tag or GitHub release has been created as part of the readiness PR.

Run:

```powershell
git status --short --branch
git diff --check
git diff --cached --name-status
git diff --cached --check
git ls-files .agents
git grep -n "<<<<<<<\|=======\|>>>>>>>"
git clean -nd
$rootGit = (Resolve-Path .git).Path
Get-ChildItem -Force -Directory -Recurse -Filter .git |
  Where-Object { $_.FullName -ne $rootGit } |
  Select-Object FullName
```

`git clean -nd` is a dry run. Inspect its output; do not delete files as part of this check.

## Release Action Checklist

- [ ] Merge the focused release-readiness PR after review and validation.
- [ ] Pull the merged `main` branch and rerun every command in this checklist.
- [ ] Confirm GitHub Actions and required checks pass.
- [ ] Confirm `docs/release-notes/v0.2.0.md` still matches the merged state.
- [ ] Confirm issue #17 is closed or ready to close.
- [ ] Decide whether to create the `v0.2.0` tag and GitHub release.
- [ ] If approved, create the tag and release as a separate post-merge action.
- [ ] Leave optional controller implementation planning and additional sanitized eval/example work as separate follow-ups.
