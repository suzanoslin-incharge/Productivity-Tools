# InCharge Meeting-to-Knowledge-Base Standard

**Owner:** Product Development / Knowledge Management  
**Status:** Working Standard  
**Version:** 1.0  
**Date:** September 2026

---

# Part 1: Meeting to Knowledge Base Article SOP

## Executive Summary

This SOP separates raw meeting evidence from reusable knowledge. Preserve the original meeting artifacts, extract only source-supported information, create topic-based knowledge articles, record decisions separately, and apply standard metadata before publishing.

> **Core principle:** Organize knowledge by business topic or process, not by meeting. Meetings are evidence sources. Knowledge articles are the reusable output.

## 1. Scope and Outcomes

Use this process for Teams meetings, process-discovery sessions, stakeholder interviews, workshops, and recurring operational discussions containing information worth preserving beyond the meeting itself.

Expected outcomes:

- A preserved source package for each meeting
- One or more topic-based knowledge articles
- A Decision Log entry when the meeting contains a confirmed decision
- Consistent metadata for search, SharePoint filtering, and Copilot retrieval

## 2. Repository Structure

### 01 Meeting Sources

**Purpose:** Preserve raw evidence.

**Typical contents:**

- AI summary
- Loop notes
- Transcript
- Recording link
- Attachments
- Meeting metadata

### 02 Knowledge Articles

**Purpose:** Store reusable knowledge by topic or process.

**Typical contents:**

- Current-state process documentation
- Standards
- How-to guides
- Product knowledge
- Lessons learned

### 03 Decision Log

**Purpose:** Preserve organizational decisions.

**Typical contents:**

- Decision statement
- Rationale
- Owner or approving role
- Decision date
- Effective date
- Affected processes or systems
- Source link

## 3. End-to-End Procedure

### Step 1: Identify Meetings Worth Processing

**Purpose:** Process meetings that produce reusable knowledge, a documented process, confirmed decisions, standards, recurring issues, or material product or system guidance.

1. Review the meeting purpose and available recap artifacts.
2. Determine whether the content will remain useful after immediate follow-up is complete.
3. If the meeting contains only scheduling, status reporting, or temporary coordination, preserve the source only.

**Required output:** A decision to create only a source package or to create a source package plus one or more knowledge articles.

### Step 2: Create the Meeting Source Package

**Purpose:** Preserve original evidence before interpreting it.

1. Create one folder using this naming pattern:

   ```text
   YYYY-MM-DD Meeting Title
   ```

2. Save or link the Teams AI summary without changing its meaning.
3. Save or link the Loop notes as the human-curated meeting record.
4. Save the transcript when available.
5. Add links to the recording and supporting files.
6. Create a meeting metadata record containing:
   - Meeting title
   - Date
   - Topics
   - Participants
   - Projects mentioned
   - Source links

**Required output:** A complete, traceable meeting-source folder.

### Step 3: Extract From the AI Summary

**Purpose:** Use the AI summary for orientation and candidate topic identification.

Review:

- Key Takeaways
- Topics
- Action Items
- Listed decisions

Extract candidate:

- Knowledge
- Processes
- Tools
- Terms
- Decisions
- Follow-up questions

Validate important or ambiguous details against Loop notes or the transcript. Ignore greetings, attendance chatter, scheduling, and filler.

**Required output:** A short list of candidate topics and items requiring validation.

### Step 4: Extract From Loop Notes

**Purpose:** Use substantive human-edited notes as the primary curated meeting record.

Sort the content into four working buckets:

1. Facts
2. Processes
3. Best Practices
4. Open Questions

Also:

- Capture decisions separately.
- Capture action items separately.
- Do not present an action item as an established process.
- Preserve supporting links.
- Mark contradictions, uncertainty, and missing owners instead of resolving them by assumption.

**Required output:** A structured extraction worksheet grounded in the meeting notes.

### Step 5: Use the Transcript for Verification

**Purpose:** Consult the transcript when added detail or evidence is needed.

1. Verify wording, sequence, rationale, ownership, and exceptions.
2. Locate relevant passages rather than summarizing the entire transcript.
3. Do not infer intent, policy, dates, or ownership.
4. When sources conflict, document both positions or retain an open question.

**Required output:** Verified details and clearly identified gaps or conflicts.

### Step 6: Separate Knowledge From Meeting Administration

**Purpose:** Keep only content that helps someone understand or perform work later.

Include:

- Stable facts and definitions
- Process steps
- Business rules
- System behavior
- Roles and responsibilities
- Exceptions
- Dependencies
- Best practices
- Confirmed decisions

Exclude:

- Greetings
- Attendance roll
- Scheduling
- Repeated discussion
- Temporary coordination
- Task reminders that do not create reusable knowledge

Move confirmed decisions to the Decision Log. Move follow-up work to the appropriate action-item system.

**Required output:** A clean set of reusable knowledge statements.

### Step 7: Choose the Article Type and Topic

**Purpose:** Create one article per coherent topic or process, not one article per meeting by default.

1. Choose a specific topic title.
2. Select the appropriate document type:
   - Process Discovery Meeting Notes
   - Current State Process Documentation
   - Future State Design
   - Standard Operating Procedure
   - How-To Guide
   - Product Knowledge
   - Decision Record
   - Reference
   - Training Material
3. Split unrelated topics into separate articles.
4. When later meetings cover the same topic, update the existing article and add the new meeting as another source.

**Required output:** A defined article title, scope, and document type.

### Step 8: Draft the Knowledge Article

**Purpose:** Transform extracted content into a stand-alone, reusable article.

1. Write a concise purpose and scope.
2. Describe the current state before proposed changes.
3. Use the sections appropriate to the article type.
4. Separate confirmed information from proposals and unresolved questions.
5. Preserve exact system names, field names, identifiers, and material terminology.
6. Link to source meetings and supporting documents.

**Required output:** A source-grounded article understandable without attending the meeting.

### Step 9: Create or Update the Decision Log

**Purpose:** Preserve confirmed decisions outside the narrative article.

1. Create an entry only when the source clearly records a decision.
2. Record the following when explicitly supported:
   - Decision statement
   - Date
   - Owner or approving role
   - Rationale
   - Effective date
   - Affected processes or systems
   - Source link
3. Do not convert recommendations, action items, or unresolved discussion into decisions.

**Required output:** A traceable decision record, when applicable.

### Step 10: Generate and Apply Metadata

**Purpose:** Improve search, filtering, and retrieval.

Complete these fields:

- Title
- Category
- Document Type
- Keywords
- Status
- Primary Process Contact
- Related Teams
- Short Description

Use `Draft - Process Discovery` only for unvalidated process-discovery content. Use a primary process contact only when supported by the source.

**Required output:** A complete metadata block attached to the draft article.

### Step 11: Validate With the Process Contact

**Purpose:** Confirm accuracy before treating the article as authoritative.

1. Review facts, sequence, roles, exceptions, terminology, and open questions.
2. Record corrections without removing the source evidence.
3. Keep unresolved items clearly labeled.
4. Update the status only after the appropriate review or approval.

**Required output:** A validated draft or approved article with its review state recorded.

### Step 12: Publish, Cross-Link, and Maintain

**Purpose:** Make the article discoverable and traceable.

1. Publish the article in the topic-based knowledge location.
2. Link the article to source meetings and supporting files.
3. Link the source folder back to the published article.
4. Record the version, last-reviewed date, and review owner when those fields are available.
5. Add later meeting sources to the existing article and preserve the change history.

**Required output:** A published, traceable, and maintainable knowledge article.

## 4. Recommended Knowledge Article Structure

```markdown
# [Specific Topic or Process Title]

## Purpose
[Why the article exists and what it helps the reader understand or do.]

## Scope
[What is included and excluded.]

## Overview
[Concise summary of the knowledge.]

## Current State or Process
[Confirmed steps, sequence, systems, roles, inputs, outputs, and dependencies.]

## Business Rules and Exceptions
[Rules, decision points, edge cases, and constraints.]

## Open Questions
[Unresolved items that must not be presented as fact.]

## Decisions
[Confirmed decisions or links to Decision Log records.]

## Sources
[Meeting links, Loop notes, transcript, files, and related articles.]

## Metadata
[Required metadata block.]
```

## 5. Publication Checklist

- [ ] Original artifacts are preserved and linked.
- [ ] Every factual statement is supported by a source.
- [ ] Current state, future state, decisions, actions, and open questions are clearly separated.
- [ ] The article is organized by topic or process.
- [ ] No unsupported owners, dates, rules, or conclusions were added.
- [ ] Metadata is complete.
- [ ] Review status is clear.
- [ ] The article stands alone for a reader who missed the meeting.

## 6. Quick Reference Workflow

```text
Preserve sources
    ↓
Extract candidate knowledge
    ↓
Validate against Loop notes and transcript
    ↓
Separate facts, processes, decisions, actions, and questions
    ↓
Draft a topic-based knowledge article
    ↓
Generate metadata
    ↓
Validate with the process contact
    ↓
Publish and cross-link
```

---

# Part 2: Knowledge Base Metadata Generation Standard

## Executive Summary

Generate metadata only after reviewing the knowledge article and supporting notes. Use source-supported wording, optimize for human search and Copilot retrieval, and never invent owners, teams, statuses, dates, or scope.

## 1. Required Fields

Return all fields in this order:

1. Title
2. Category
3. Document Type
4. Keywords
5. Status
6. Primary Process Contact
7. Related Teams
8. Short Description

## 2. Generation Rules

- Use only information in the supplied article, notes, transcript excerpts, or explicit context.
- Do not infer a process owner or contact. Use `Needs confirmation` when unsupported.
- Do not infer teams merely because they would normally participate.
- Use the most specific valid category.
- If the category taxonomy is unavailable, prefix a proposed value with `Proposed:`.
- Use `Draft - Process Discovery` only for unvalidated process-discovery content.
- Use concise, specific, source-supported keywords.
- Include supported systems, processes, products, acronyms, teams, and common search terms.
- Write the Short Description in one to three factual sentences covering scope, major processes or systems, and important boundaries.

## 3. Field-by-Field Standard

### Title

**Purpose:** Names the article.

**Generation guidance:** Use the system or product name plus the process or topic. Avoid generic meeting titles.

**Fallback:** `Needs confirmation`

### Category

**Purpose:** Places the article in the knowledge hierarchy.

**Generation guidance:** Use this format:

```text
Business Function > Process Area
```

**Fallback:** `Proposed: [category]`

### Document Type

**Purpose:** Identifies the article's purpose and maturity.

**Generation guidance:** Match the content, not the original file format.

**Fallback:** `Reference` or `Needs confirmation`

### Keywords

**Purpose:** Improves search and retrieval.

**Generation guidance:** Use supported systems, processes, products, teams, acronyms, and common search terms. Keep the list concise and remove duplicates.

**Fallback:** Use only the supported core terms.

### Status

**Purpose:** Shows the article's lifecycle and validation state.

**Generation guidance:** Use a controlled value supported by the review state.

**Fallback:** `Needs confirmation`

### Primary Process Contact

**Purpose:** Identifies the best process contact.

**Generation guidance:** Use an explicitly named owner, subject-matter expert, or confirmed contact. Do not guess.

**Fallback:** `Needs confirmation`

### Related Teams

**Purpose:** Supports discovery and routing.

**Generation guidance:** Include teams explicitly involved, affected, responsible, consulted, or referenced.

**Fallback:** `Needs confirmation`

### Short Description

**Purpose:** Explains the article's scope in search results.

**Generation guidance:** Use one to three factual sentences covering scope, major systems or processes, important boundaries, and deferred topics.

**Fallback:** A concise factual summary based only on supported content.

## 4. Recommended Controlled Values

### Document Type

- Process Discovery Meeting Notes
- Current State Process Documentation
- Future State Design
- Standard Operating Procedure
- How-To Guide
- Product Knowledge
- Decision Record
- Reference
- Training Material

### Status

- Draft - Process Discovery
- Draft - Under Review
- Validated
- Approved
- Published
- Superseded
- Archived
- Needs confirmation

## 5. Copy/Paste Metadata Generation Prompt

```text
Generate knowledge base metadata from the supplied article or meeting notes. Use only information explicitly supported by the source. Do not infer owners, teams, dates, decisions, status, or scope. If a required value is unsupported, write "Needs confirmation."

Return exactly these fields in this order:
Title:
Category:
Document Type:
Keywords:
Status:
Primary Process Contact:
Related Teams:
Short Description:

Rules:
- Title: use the system, product, process, or topic name; avoid generic meeting titles.
- Category: use Business Function > Process Area. If uncertain, prefix the value with "Proposed:".
- Keywords: comma-separated, concise, specific, non-duplicative, and source-supported.
- Status: use "Draft - Process Discovery" only for unvalidated process-discovery content; otherwise use a supported status or "Needs confirmation."
- Primary Process Contact and Related Teams: never guess.
- Short Description: one to three factual sentences covering scope, major systems or processes, and important boundaries or deferred topics.
- Output only the completed metadata fields.
```

## 6. Reusable Blank Template

```text
Title: [Enter value]
Category: [Enter value]
Document Type: [Enter value]
Keywords: [Enter value]
Status: [Enter value]
Primary Process Contact: [Enter value]
Related Teams: [Enter value]
Short Description: [Enter value]
```

## 7. Completed Example

**Title:** Business Central Inbound Receiving and Warehouse Put-Away Process  
**Category:** Operations > Warehouse and Inventory Management  
**Document Type:** Process Discovery Meeting Notes  
**Keywords:** Business Central, inbound receiving, warehouse receipts, partial shipments, inventory, non-inventory, warehouse put-away, bin management, JotForm, shipping and receiving, logistics  
**Status:** Draft - Process Discovery  
**Primary Process Contact:** Leeana  
**Related Teams:** Warehouse, Shipping and Receiving, Logistics, Inventory, Accounting  
**Short Description:** Current-state meeting notes on inbound delivery intake through JotForm, inventory and non-inventory receipt posting in Business Central, partial shipment handling, warehouse put-away and bin practices, process ownership, and opportunities to streamline receiving. Purchase-order creation was deferred to a follow-up session.

## 8. Metadata Validation Checklist

- [ ] All eight fields are present and in the standard order.
- [ ] The title describes the knowledge, not merely the meeting.
- [ ] The category follows `Business Function > Process Area`.
- [ ] The document type matches the content's purpose and maturity.
- [ ] Keywords are specific, supported, and non-duplicative.
- [ ] Status reflects the actual review state.
- [ ] The contact and teams are source-supported.
- [ ] The Short Description states scope and boundaries accurately.
- [ ] No unsupported detail was added.
