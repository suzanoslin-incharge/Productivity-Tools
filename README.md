# InCharge Productivity Tools

Shared Claude Code skills and agents for InCharge Energy — **general-purpose,
cross-department** tools, not specific to any one team's domain. If a skill
is specific to a department's own processes or data (e.g. accounting/finance
workflows), it belongs in a sibling repo instead — see
[`accounting-tools`](../accounting-tools) for that one.

This repo is a **Claude Code plugin**: anyone at the company can install it
and get the same skills, agents, and shared reference knowledge in their own
Claude Code sessions, regardless of what department they're in.

## What belongs here vs. a domain-specific repo

- **Here**: a skill any team could use for their own work — process mapping
  (SIPOC, swim-lane diagrams), meeting-notes summarizing, and similar. The
  test: would this be just as useful to Product, HR, or Service as it is to
  Accounting? If yes, it's general-purpose.
- **A domain repo instead**: a skill that only makes sense with a specific
  team's data, systems, or vocabulary baked in (e.g. an AP-invoice-exception
  triager, a bank-transaction matcher). Those go in that team's own repo
  (`accounting-tools`, and future ones per department).

`sipoc-builder` and `swimlane-builder` live here for exactly this reason —
they're process-mapping tools usable by any team, even though the first
worked examples we built happened to be accounting processes.

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
  org-glossary.md          InCharge org terms: lines of business, departments,
                             key people, abbreviations
  systems-landscape.md     Systems of record and what each owns
```

`shared-knowledge/` holds company-wide reference material (org glossary,
systems landscape) that several skills can read, for example when
kb-article-builder adds a new taxonomy row. A skill should read these only
when it needs a term or system name, and if a term isn't listed it should ask
rather than assume. Both files are seeds, not verified directories; they were
first built from Accounting's knowledge base, so confirm names and roles
before publishing anything outward-facing.

## Adding a new skill

1. `skills/<name>/SKILL.md` with YAML frontmatter (`name`, `description`) and
   the recipe as the body.
2. Put anything long or reference-only under `skills/<name>/references/` —
   SKILL.md should stay short; the model loads references only when needed.
3. Before adding it here, sanity-check it against "What belongs here" above —
   if it only makes sense for one team's data or systems, it likely belongs
   in that team's own repo instead.
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
/plugin marketplace add <org>/productivity-tools
/plugin install productivity-tools
```

**Caveat:** the exact `marketplace.json` schema and `/plugin` commands should
be checked against the current Claude Code plugin docs before company-wide
rollout — plugin tooling has moved fast and this file is a reasonable
starting shape, not a verified-against-latest-docs guarantee.

## Status

- [x] Repo scaffolded locally (renamed from `incharge-claude-tools` once we
      realized SIPOC/swim-lane are general-purpose, not accounting-specific)
- [ ] Pushed to GitHub (`gh repo create <org>/productivity-tools --private --source=. --push`)
- [x] `sipoc-builder`
- [x] `swimlane-builder` (produces Lucidchart-ready output; see its `references/lucidchart-integration.md`)
- [x] `kb-article-builder` (text file → new title + 8-field metadata, content unchanged; full meeting-to-KB pipeline from the SOP is a later phase)
- [ ] Confirm whether Lucid MCP server access is approved for the account (Team/Enterprise admin decision)
- [ ] Decide whether a private personal-sandbox tier (experimental skills, not yet company-facing) is worth adding — deferred for now
