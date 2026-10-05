# productivity-tools

Suzan Oslin's repo of Claude skills and shared reference files for accounting process improvement at InCharge Energy. Personal preferences (fonts, writing style, approvals) are in `~/.claude/CLAUDE.md`. The same rules apply here.

## What is in the repo

- `skills/`: `kb-article-builder`, `kb-update-linked-docs`, `kb-answer-open-questions`, `map-sipoc-builder`, `map-swimlane-builder`. Each skill has a `SKILL.md`; the kb skills also share a `README.md` and `references/`.
- `shared-knowledge/`: `org-glossary.md` (department directory) and `systems-landscape.md`. Names and roles here are corrected only when Suzan confirms them. Delphine Hartsel has not yet reviewed the glossary.
- `agents/`: agent definitions.

The skills are installed by symlinks in `~/.claude/skills/` that point at `skills/` here. Edits take effect in a new session.

## The knowledge base is not in this repo

The knowledge base and trackers live in OneDrive and are reached through environment variables: `$KB_ROOT` (the `_KB` folder), `$ACCT_MYNOTES` (Accounting-MyNotes) and `$TOOLS_PRODCTVTY` (this repo). Never copy knowledge base content into the repo. See `$ACCT_MYNOTES/CLAUDE.md` for the knowledge base rules.

## Git

- Commit and push straight to `main` when Suzan asks. Do not create a branch unless she asks for one. If a change looks risky enough to deserve a branch (for example one that could break the installed skills), say so and let her decide.
- Commit only when asked. Write a short message that says what changed and why.
- The repo tracks only skills, shared-knowledge and agents.

## Editing skills

- When a change touches how the trackers (`OPEN_QUESTIONS.xlsx`, `FOLLOWUP_ITEMS.xlsx`) are read or written, update `kb-article-builder`, `kb-answer-open-questions` and the README together so they agree.
- Keep every skill's approval rule: nothing in the knowledge base is written until Suzan approves the proposal.
- Any file a skill generates follows the 12-point minimum font rule.
