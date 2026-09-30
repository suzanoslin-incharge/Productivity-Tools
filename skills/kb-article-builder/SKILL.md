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
   - Use only what the file supports. Never guess contacts or teams.
   - **If any field is unclear or unsupported by the file, ask the user before writing the output.** List each unclear field with a short question (and a suggested value where one is reasonable), and wait for the answers. Write `Needs confirmation` only if the user declines to answer or says to skip it.
   - Category: `Business Function > Process Area`, prefixed `Proposed:` unless the user gives a taxonomy.
   - Status: `Draft - Process Discovery` for unvalidated process-discovery content.
4. **Write the output file:** `# <new title>` first, then the metadata block
   directly after the title, then the original content unchanged (drop only
   an existing top-level title that the new one replaces). All metadata goes
   in that one block between the title and the content, never elsewhere. Name the file after the new title, in the same
   folder as the input. Leave the original file untouched.
5. **Reply briefly:** the new file path, the metadata, and any fields still
   marked `Needs confirmation`.

## Output layout

```markdown
# <new title>

- **Title:** ...
- **Category:** ...
- **Document Type:** ...
- **Keywords:** ...
- **Status:** ...
- **Primary Process Contact:** ...
- **Related Teams:** ...
- **Short Description:** ...

<original content, unchanged>
```

The metadata is a plain bulleted list, not `---` front matter, so it renders
the same in any KB or markdown viewer and is not mistaken for file-level
front matter.
