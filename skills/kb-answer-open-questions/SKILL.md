---
name: kb-answer-open-questions
description: Work with the open questions in the InCharge knowledge base in three ways - ASK (what should I ask Doricia and Josh? returns each person's questions rewritten to stand alone, with context from the article), PROCESS (find questions the user answered by hand in the workbook and move them to Answered and record them in the articles), and INTAKE (the user passes notes, an email, a transcript or a message containing answers; match them to open questions and record them). Nothing is written until the user approves. Use when the user asks what to ask someone, wants to review open questions, says "process my answers", or hands over answers in any form.
---

# Answer Open Questions

Open questions live in one Excel workbook, `$ACCT_MYNOTES/OPEN_QUESTIONS.xlsx`,
so the user can also read and edit it by hand. Each article's own "Open
Questions" section keeps the context; the workbook is the working list.
**Nothing in an article or in the workbook changes until the user approves**,
except as noted under "Retire".

## The three ways to use it

| The user says | Mode | Section |
| --- | --- | --- |
| "What should I ask Doricia and Josh?" / "questions for Carrie" / "what is open on PayFabric?" | **Ask** | 1 |
| "Process my answers" / "I filled in some answers, sync them" | **Process** | 2 |
| "Here are notes / an email / a transcript / what Matt told me: record the answers" (pasted or attached) | **Intake** | 3 |
| "Q034: Matt says ..." (one answer, typed) | Intake with one answer | 3 |
| "Q012 doesn't matter any more" | **Retire** | 5 |

Recording an answer in the articles and the workbook is the same procedure for
Process and Intake (section 4).

Workbook layout. Sheet "Open" (Excel table `OpenQuestions`): `Done | ID | Question | Context | Who may know (suggested) | Related notes | Link | Raised | Answer`.
Sheet "Answered" (table `AnsweredQuestions`): `Done | ID | Question | Context | Answered by | Related notes | Link | Raised | Answer`.
`Question` is written to stand alone. `Context` is 2 to 4 plain sentences: what my notes say, where the gap or conflict is, where it came from (the meeting and its date, or an email), and why it matters when that is supported. Wording: write like a colleague talking to a colleague, in plain everyday words, for people who have not read Suzan's notes (the workbook is shared and is copied into process documents such as a SIPOC). Never write "the article", "the KB", "the source" or "per"; say "my notes" for Suzan's write-up and "the meeting notes" (or name the meeting) for a meeting. Emails can be named normally ("in Priya's email of 2026-09-29"). Do not end a Context with a stock phrase such as "From the 2026-10-05 session" and do not use the label "Why it matters:"; say it in a sentence ("This matters because ..."). Spell out an acronym the first time it appears in each cell. Both were backfilled for every existing question on 2026-10-05. The article's own Open Questions bullet may be worded differently from the workbook question, so match by ID and meaning, not by exact text.
`Done` is blank, or `Yes` when answered. `Related notes` is the title of the KB article in plain text. `Link` is a clickable **local file link** to that article (built as `file:///Users/suzanoslin/Library/CloudStorage/OneDrive-InChargeService/Accounting-MyNotes/` plus the path under `_KB`), which opens the note in Suzan's editor. SharePoint web links to `.md` files do not open in a browser; at migration the links are re-pointed (see the kb-article-builder README, section "Moving everything to SharePoint"). `Raised` is a real date
(`yyyy-mm-dd`). IDs are `Q001`, `Q002`, ... and are never reused.

Read and edit the workbook with `openpyxl` or the `xlsx` skill. Keep the
formatting, never rewrite or reorder other rows, and extend the table range when
adding a row. If the workbook is open in Excel, ask the user to close it first:
an Excel save can overwrite the edit.

## 1. Ask: "what should I ask Doricia and Josh?"

Goal: for each person, a list the user can walk into a conversation with. A
question copied from the workbook often means little on its own ("The note says
'lots to be worked out'"), so every question is rewritten to stand alone and
comes with context.

1. **Find the people.** Match each name the user gave against "Who may know"
   (case-insensitive, first or last name, e.g. "Josh" matches "Joshua
   Barnhill"). Use `$TOOLS_PRODCTVTY/shared-knowledge/org-glossary.md` to
   resolve a first name. If a name matches several people or none, ask. A row
   with two names appears under both people; show it once in full and refer to
   it from the second person's list. The user may also ask by topic, article or
   system ("what is open on PayFabric?"); then group by person within it.
2. **Read the sources of each question.** Start from the workbook's `Question` and `Context` columns, then verify and extend them: open the question's article
   (`$KB_ROOT/02_Knowledge-Articles/...`): the Open Questions bullet, the
   surrounding statements it depends on, and the Sources section. Read the
   source folder's `Source-Metadata.md` for the meeting or document and its
   date. Read only what is needed; do not dump articles.
3. **Rewrite and add context.** For each question show:
   - **Ask:** the workbook `Question` (rewrite it only if it still does not stand alone). Name the system or
     process, what is known, and what is not. Keep the meaning of the original;
     do not add facts that are not in the article or source.
   - **Context:** two or three sentences: what the article says today, where
     the gap or conflict is, and the source with its date.
   - **Why it matters:** what is blocked or uncertain until it is answered (a
     decision, an automation, a conflicting article). Skip if nothing is stated.
   - **ID and article:** `Q081` and the article title.
   The workbook text is not changed by this. If a question is too vague to
   rewrite without guessing, say so and show it as written.
4. **Order and size.** Group by person. Put questions that block several
   articles or a decision first, then the rest by article. If a person has more
   than about 12, show the top ones and give the count of the rest, and offer
   them.
5. **Offer next steps.** A short message or agenda for each person (not sent),
   and "tell me their answers and I will record them" (section 3).
6. Questions with an empty "Who may know" are listed under "No suggested
   person" only when the user asks for them.

If the user likes the rewritten wording, offer to save it back as the question
text in the workbook (needs approval; the ID stays the same).

## 2. Process: answers entered by hand

The user may answer a question by typing in the workbook instead of telling
Claude. This mode finds those and handles them as answers already given. Also
run this check at the start of Intake (section 3) so a hand answer and a new
answer for the same question are not confused. Read-only until the user
approves.

**What counts as answered by hand**
- A row on the "Open" sheet with text in `Answer`, or `Done` = `Yes`.
- A row on the "Answered" sheet whose article has not been brought up to date:
  the question (matched by meaning; the article's wording may differ) is still in the article's Open Questions section, and the
  article's Change Log has no line naming the ID. (A row the user moved by hand
  to "Answered".)
- An `Answer` that starts with `Retired:` is a retirement (section 5).

**What to do**
1. List them in one short table: ID, question, the answer as typed, who answered
   (the `Answered by` cell on the Answered sheet; if there is none, or the row is
   still on "Open", ask) and the date (ask if not stated; default to today only
   if the user says so).
2. `Done` = `Yes` with no answer text: ask what the answer was. Do not guess.
   An answer that is unclear or only partly answers the question: show it and
   ask whether to record it as written, or to keep the question open with a
   note.
3. Do not assume a row is out of sync when the article does not mention the
   question at all. It may have been handled before this check existed. List
   it and ask whether to mark it as already synced.
4. For each confirmed one, go to section 4 using the typed answer. The proposal
   also covers moving the row from "Open" to "Answered" (set `Done` = `Yes`,
   `Answered by`, keep the typed answer) when the user has not moved it already.
5. Say in the report how many hand answers were found and synced.

Do not rewrite or clear the user's typed answer. Move or keep it as is, and
correct only obvious formatting (for example the date).

## 3. Intake: answers from notes, an email, a transcript, a message

The user passes material that may contain answers: pasted text, an attached
file, or a path (`.md`, `.txt`, `.docx`, `.pdf`, an email thread, meeting
notes, a transcript). Read it with the ingest rules in `../kb-article-builder/SKILL.md`.

1. **Say who and when.** Note who gave each answer and when (the speaker, the
   email sender and date, the meeting date). Ask if it is not clear. Do not
   attribute an answer to a person the material does not name.
2. **Match to open questions.** Read the "Open" sheet (with its articles for
   context, as in section 1). For each question the material answers, quote the
   passage. One passage may answer several questions; one question may be
   answered by several people.
3. **Show one match table before anything else:**
   - ID, the question (rewritten to stand alone, as in section 1)
   - the answer as the material states it (a short quote or close paraphrase)
   - who said it, where (file, email, meeting) and the date
   - fit: **answers it fully**, **answers it partly** (say what is still open),
     **conflicts with an existing statement or another answer**, or **unclear**
   Never infer an answer the material does not state. Silence is not an answer.
4. **Also list:** new facts in the material that answer no open question (offer
   to file the material with `kb-article-builder`, since it may deserve its own
   source folder and article update); and new questions it raises (to be added
   as rows with the next ID).
5. **Ask the user to confirm or edit the table.** Partial, conflicting and
   unclear ones need an explicit decision: record as written, keep open with a
   note, or skip.
6. For each confirmed answer, go to section 4. Put the source in the `Answer`
   cell and in the article's Change Log line (for example "per email from
   Matt, 2026-10-06"). If the material is worth keeping, the user can file it
   with `kb-article-builder`; do not copy it into the KB from here.

## 4. Record an answer (shared by Process and Intake)

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
     line that names the question ID, who answered and when (for example
     "2026-10-06: Q034 answered by Matt: ..."); the ID is how Process mode
     later recognises that the article is already up to date
   - for the workbook: the row moving from the "Open" sheet to the "Answered"
     sheet with the answer, the person and the date
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
   `$ACCT_MYNOTES/FOLLOWUP_ITEMS.xlsx` (columns: Done, Action item, Owner,
   Date made, Meeting; append below the last row of the `FollowUps` table) and
   add it only if the user says yes.
7. **If the answer raises a new question**, add it as a new row with the next ID,
   written to stand alone (see "Adding new questions").
8. After approval, write exactly what was approved and report in one short
   message: how many answered, which articles changed, what is still open.

## 5. Retire: "Q012 doesn't matter any more"

With the user's reason (or a typed `Retired: <reason>` answer found in Process
mode), move the row to Answered with `Answered by` set to the user, the answer
"Retired: <reason>", and remove it from the article's Open Questions section.
Show the change first if it touches an article.

## Adding new questions

When `kb-article-builder` or `kb-update-linked-docs` writes an article, it
adds that article's open questions to the "Open" sheet with the next free ID,
the date, a link to the article, and a suggested "Who may know". Each question
is written to stand alone: it names the system or process, says what is known
and what is not, and does not depend on the surrounding text ("The note says
'lots to be worked out'" is not a question) and has a `Context` cell written with it. If you add a question here by
hand-off ("add a question for Carrie about ..."), also add it to the article's
Open Questions section after approval.
