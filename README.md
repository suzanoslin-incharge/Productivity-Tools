# InCharge Claude Tools

Shared Claude Code skills and agents for InCharge Energy. This repo is a
**Claude Code plugin**: anyone at the company can install it and get the same
skills, agents, and shared reference knowledge in their own Claude Code
sessions.

## Layout

```
.claude-plugin/
  marketplace.json      Plugin manifest (see caveat below)
skills/
  <skill-name>/
    SKILL.md             The recipe Claude follows. Required.
    references/          Knowledge only THIS skill needs.
    scripts/              (optional) helper scripts the skill can run.
agents/
  <agent-name>.md         Subagent definitions (system prompt, tool
                            restrictions, model). Use for autonomous
                            multi-step work, not bounded recipes.
shared-knowledge/
  org-glossary.md          Terms, roles, line-of-business shorthand
  systems-landscape.md     Systems of record and what each owns
```

## Where knowledge goes

- **Only one skill needs it** → that skill's own `references/` folder.
- **Several skills need it** (org glossary, systems list, roles, people) →
  `shared-knowledge/`. Each `SKILL.md` that needs it says so explicitly
  ("Before starting, read `../../shared-knowledge/org-glossary.md`").
- **Deep, evolving domain notes** (like a personal working folder such as
  Accounting-MyNotes) generally stay where they are. Pull a *curated* summary
  into `shared-knowledge/` only when a skill should load it automatically —
  don't sync the whole working folder in.

## Adding a new skill

1. `skills/<name>/SKILL.md` with YAML frontmatter (`name`, `description`) and
   the recipe as the body.
2. Put anything long or reference-only under `skills/<name>/references/` —
   SKILL.md should stay short; the model loads references only when needed.
3. If it needs shared knowledge, say so in the body and confirm the file
   exists in `shared-knowledge/`.
4. Add an entry for it in `.claude-plugin/marketplace.json` if it should be
   independently toggleable; otherwise it's included automatically as part
   of this plugin.
5. Open a PR. Anyone who has this plugin installed gets the update next time
   they pull / Claude Code refreshes the plugin.

## Adding a new agent

Use an agent (not a skill) when the task needs autonomous multi-step tool
use, delegation, or a deliberately restricted toolset — e.g., a
"process-discovery" agent that reads raw meeting notes and drafts a SIPOC +
swim-lane map on its own. A bounded, repeatable recipe (like "build a SIPOC
from information I already have") is a skill.

## Installing this plugin (once pushed to GitHub)

```
# from inside any Claude Code session
/plugin marketplace add <org>/incharge-claude-tools
/plugin install accounting-process-tools
```

**Caveat:** the exact `marketplace.json` schema and `/plugin` commands should
be checked against the current Claude Code plugin docs before company-wide
rollout — plugin tooling has moved fast and this file is a reasonable
starting shape, not a verified-against-latest-docs guarantee.

## Status

- [x] Repo scaffolded locally
- [ ] Pushed to GitHub (`gh repo create <org>/incharge-claude-tools --private --source=. --push`)
- [x] First skill: `sipoc-builder`
- [ ] `shared-knowledge/org-glossary.md` reviewed by Delphine
