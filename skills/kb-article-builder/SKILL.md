---
name: kb-article-builder
description: Take a text file (meeting notes, summary, transcript, process notes) and return a knowledge-base-ready file - the original content with the standard eight-field metadata block added and a new title based on what the content is about. Use when someone hands over a text file and wants KB metadata or a KB-ready version of it.
---

# KB Article Builder

Input: one text file. Output: the same content, titled and with metadata
added, ready for the knowledge base. This skill does **not** restructure,
summarize, or reinterpret the content.

Metadata rules and controlled values: `references/metadata-standard.md` (quick version). The complete SOP for the later full pipeline is `references/InCharge_Meeting_to_Knowledge_Base_Standard.md`.

## Steps

1. **Read the whole file.**
2. **Write a new title** from what the content is actually about: system or
   product name plus the process or topic. Not a generic meeting title and
   not the old filename.
3. **Generate the eight metadata fields**, in this order: Title, Category,
   Document Type, Keywords, Status, Primary Process Contact, Related Teams,
   Short Description.
   - Use only what the file supports. Unsupported value → `Needs confirmation`. Never guess contacts or teams.
   - Category: `Business Function > Process Area`, prefixed `Proposed:` unless the user gives a taxonomy.
   - Status: `Draft - Process Discovery` for unvalidated process-discovery content.
4. **Write the output file:** metadata block first, then `# <new title>`, then
   the original content unchanged (drop only an existing top-level title
   that the new one replaces). Name the file after the new title, in the same
   folder as the input. Leave the original file untouched.
5. **Reply briefly:** the new file path, the metadata, and which fields are
   `Needs confirmation`.

## Output layout

```markdown
---
Title: ...
Category: ...
Document Type: ...
Keywords: ...
Status: ...
Primary Process Contact: ...
Related Teams: ...
Short Description: ...
---

# <new title>

<original content, unchanged>
```
