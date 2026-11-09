---
name: bg
description: Run any prompt, task or slash command in the background, save the result to a file and give Suzan a link to it. Use for /bg, "run this in the background", "do this while I work" or any request to run something without waiting for it.
---

# Background run (/bg)

Runs one task as a background job so Suzan can keep working. The task can be any prompt or command, including another skill (for example `/bg /kb-answer-questions ...`). The result is saved to a file and she gets a link to it when it is done.

## Steps

1. **Get the prompt.** Use the text Suzan gives after the skill name or in her message. If there is none, ask for it, once.
2. **Pick the file.** Folder: `$ACCT_MYNOTES/Productivity/Background-Results/` (create it if it does not exist). Name: `Topic-Words_Result_yyyy-mm-dd.md` (no spaces, hyphens within a phrase, underscores between parts, ISO date last, per the filename standard). If the file exists, add `_2`, `_3` and so on. Never overwrite. Every request gets its own file, so one result can be handed back later by name.
3. **Start the task.** Launch one background subagent (Agent tool, general-purpose). Give it:
   - Suzan's prompt, word for word.
   - Any context it needs from this session. It knows nothing else.
   - The exact file path to write the result to.
   - The rules below.
4. **Tell Suzan in one line** that it is running and which file it will write. Then carry on with whatever else she asks. Do not wait for it and do not poll.
5. **When the task finishes,** check the file exists and is not empty. Reply with the link, a two-line summary of what is in it, and one line: "To write the proposal, say: proposal from `<file name>`." If the task failed or the file is empty, say so and what you will try.

## Rules for the subagent

- Do exactly what the prompt asks, including running a skill it names. Follow the rules in `~/.claude/CLAUDE.md` and the project `CLAUDE.md` as if Suzan were watching.
- **Approvals.** The task cannot ask Suzan anything. Anything her rules say needs her approval first (sending email or Teams messages, editing knowledge base articles or trackers, deleting, moving or renaming files, installing software, git commits) is **not done**. Instead the task writes the proposal in the result file, with defaults filled in, and stops. The exception is an action the prompt itself says is approved (for example "I approve", or a plain "yes" quoted in the prompt). A skill's own approval step works the same way: the task stops at the proposal.
- Before writing to any file Suzan may have open, check for a `~$` lock file and `lsof`, and do not write if it is open. Say so in the result file.
- Write the result file as markdown, in plain English, the result first, then detail, as Suzan would write to a colleague. If the task changed any files, list each one with its path.
- End the file with a **Next step** section: what a proposal from this result would cover, and what Suzan would be asked to approve. This is what she picks up later when she says "proposal from that file".
- Do not mention Claude, AI, a subagent or the tools used anywhere in the file.
- Dates are yyyy-mm-dd. Spell out an acronym the first time it appears.
- Keep current state and future state apart and label each.
- If something cannot be found or checked, say so. Do not guess.

## Link format

Give the link as a markdown link with the full path, for example `[Topic-Words_Result_2026-11-05.md](/Users/suzanoslin/Library/CloudStorage/OneDrive-InChargeService/Accounting-MyNotes/Productivity/Background-Results/Topic-Words_Result_2026-11-05.md)`. Name the file in the link text, not the word "here".
