---
name: kb-answer-open-questions
description: Work through the open questions in the InCharge knowledge base - list them by who is likely to know (so they get asked in batches), and when the user reports an answer ("Q034: Matt says...") update the affected articles, tick the question and move it to Answered. Use when the user asks what to ask someone, wants to review open questions, or gives an answer to one.
---

# Answer Open Questions

Open questions live in one table, `$ACCT_MYNOTES/OPEN_QUESTIONS.md`. Each
article's own "Open Questions" section keeps the context; the table is the
working list. **Nothing in an article or in the table changes until the user
approves**, except as noted under "Retire".

Table columns (Open): `Done | ID | Question | Who may know (suggested) | Article | Raised | Answer`.
Answered table: `Done | ID | Question | Answered by | Article | Raised | Answer`.
IDs are `Q001`, `Q002`, ... and are never reused.

## 1. Triage: "what should I ask Carrie?"

- Read the Open table and group the rows by the names in "Who may know". A row
  with two names appears under both.
- Show, per person, a short list: ID, question, and the article it comes from.
  Put questions that block several articles or a decision first.
- "Who may know" is a suggestion from the articles and the department
  directory (`$TOOLS_PRODCTVTY/shared-knowledge/org-glossary.md`). Correct it
  if the user says someone else is the right person. Do not invent a person
  where none is indicated; leave "Who may know" empty instead.
- Offer to draft a short message or agenda for that person. Do not send it.

## 2. Record an answer: "Q034: Matt says it comes from..."

1. **Find the row** by ID or by matching the question. If several questions
   share one answer, handle them together.
2. **Find every article affected.** Start from the row's article, then search
   `$KB_ROOT/02_Knowledge-Articles` and the other open questions for the same
   fact (for example a conflict between articles needs one answer applied to
   all of them).
3. **Propose, then wait.** One message showing, for each article:
   - the question as it stands in the article's Open Questions section
   - where the answer goes (Current State, Business Rules and Exceptions, ...)
     and the exact new text
   - the change to remove the open question, `Last updated`, and a Change Log
     line naming who answered and when
   - for the table: the row moving to Answered with the answer, the person and
     the date
   Ask the user to approve, edit or reject.
4. **Linked articles.** An answer from a person is not in the original document
   and these articles say the original governs. Add it labeled
   "Answered by <name> on <date>; not in the original document", never as if
   the original said it. If the original is the user's own document, suggest
   updating it, so `kb-update-linked-docs` can refresh the article later.
5. **If the answer contradicts an existing statement**, replace the old
   statement (as in `kb-article-builder`), archive the previous article version
   to `_Superseded-Archived`, and show the before/after.
6. **If the answer creates a to-do**, suggest a row for
   `$ACCT_MYNOTES/FOLLOWUP_ITEMS.md` and add it only if the user says yes.
7. **If the answer raises a new question**, add it as a new row with the next ID.
8. After approval, write exactly what was approved and report in one short
   message.

## 3. Retire: "Q012 doesn't matter any more"

With the user's reason, move the row to Answered with `Answered by` set to the
user, the answer "Retired: <reason>", and remove it from the article's Open
Questions section. Show the change first if it touches an article.

## Adding new questions

When `kb-article-builder` or `kb-update-linked-docs` writes an article, it
adds that article's open questions to the Open table with the next free ID,
the date, a link to the article, and a suggested "Who may know". If you add a
question here by hand-off ("add a question for Carrie about ..."), also add it to
the article's Open Questions section after approval.
