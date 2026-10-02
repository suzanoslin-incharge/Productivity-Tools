# SIPOC: What It Is and How It Leads to a Swim-Lane Map

A SIPOC scopes a process. A swim-lane map details it. This guide covers how to build the first and how to turn it into the second. For the swim-lane method itself, see [swimlane-process-map.md](../../map-swimlane-builder/references/swimlane-process-map.md).

---

## 1. How a SIPOC relates to swim lanes

A SIPOC and a swim-lane map are **two different tools, used one after the other**:

1. **SIPOC first.** It is a one-page table. It sets the boundaries of a process and lists everyone who feeds it and everyone who depends on it. It does *not* show who does each step.
2. **Swim-lane map second.** This is a detailed flowchart. Each horizontal band (a "lane") belongs to one person, team or system, and every step sits in the lane of whoever does it.

The link between them: **the people and groups in the SIPOC's Supplier and Customer columns are the starting list of lanes for the swim-lane map.** You don't have to work out who belongs on the map, because the SIPOC already told you.

If someone says "suppliers are the swim lanes," this is almost certainly what they mean. It is worth confirming, because a few people mean something different: drawing the SIPOC itself with one band per supplier.

One refinement: a lane is strictly for **whoever performs a step**. Most suppliers do perform steps, so they become lanes. A supplier that only hands something over and does nothing else (for example, a tax service returning a rate) can be merged into a "Systems" lane or left off.

---

## 2. What a SIPOC is

SIPOC stands for **Suppliers, Inputs, Process, Outputs, Customers**. It is a five-column table that describes a process at a high level. It dates from the total quality management programs of the late 1980s and is now standard in Lean Six Sigma and business process management.

| Column | Question it answers | Example (invoicing a completed job) |
| --- | --- | --- |
| **S**uppliers | Who provides what the process needs? | Service team, sales support, the customer |
| **I**nputs | What do they provide? | Completed work order, signed quote or PO |
| **P**rocess | What are the 5–7 main steps? | Verify → build invoice → post → send |
| **O**utputs | What does the process produce? | Posted invoice, open receivable |
| **C**ustomers | Who receives the outputs? | Customer's accounts payable, cash application |

**What it is good for:**

- Agreeing on where a process starts and stops before anyone maps details.
- Making sure no stakeholder is forgotten.
- Showing where inputs arrive late or incomplete. That is where rework comes from. A useful question to ask of any process: what information does the person doing the work need to do it correctly, and where does that information originate?

**What it is not good for:** showing handoffs, delays, decisions or who does each step. That is the swim-lane map's job.

---

## 3. How to build one

Although the name runs S → I → P → O → C, you usually **fill it in from the middle out**:

1. **Name the process and set its boundaries.** Write down the trigger that starts it and the event that ends it. For example: *starts when a work order is marked Ready to Invoice; ends when the invoice is delivered and the work order is set to Invoiced.*
2. **Process column.** List 5–7 high-level steps, each as a verb and a noun ("Verify billing data"). Resist detail; that goes in the swim-lane map.
3. **Outputs.** What does the process produce? Include records and status changes as well as documents.
4. **Customers.** Who receives each output? Include internal customers.
5. **Inputs.** What does each step need?
6. **Suppliers.** Who or what provides each input?
7. **Check it with the people who do the work.** A SIPOC built alone at a desk is usually missing something.

**COPIS variation:** some teams fill it in backwards, starting from Customers and working upstream. This keeps the focus on what the customer needs. It is useful when the goal is "what does the recipient actually need from this process?"

**Tips:**

- Keep it to one page. If the Process column needs more than about 7 steps, you are probably describing two processes.
- Name roles and systems, not only individuals (for example, "Billing (Pat)" rather than just "Pat"), so the SIPOC stays true when people change.
- List systems as suppliers when they provide data (a CRM, an ERP, a tax engine). A lot of rework comes from system inputs that arrive incomplete.
- Pain points, workarounds and ideas don't belong in the SIPOC. Keep them in a separate list.

---

## 4. From SIPOC to swim-lane map

For what a swim-lane map is, when to use one, and how it differs from a SIPOC, see [swimlane-process-map.md](../../map-swimlane-builder/references/swimlane-process-map.md). The one-line summary: a SIPOC scopes a process before mapping; a swim-lane map maps it in detail once scope is agreed.

**The conversion, specific to a SIPOC's columns:**

1. Take everyone in the Supplier and Customer columns, plus anyone who performs a Process step. Each becomes a lane.
2. Put the external parties (customer, vendor) in the top or bottom lane, and group systems into one lane if they don't need separate lanes.
3. Break each high-level SIPOC step into the detailed steps you observed, and place each one in the lane of whoever does it.
4. Draw arrows. **Every time an arrow crosses from one lane into another, that is a handoff.** Handoffs are where work waits, gets lost or comes back for correction, so they are usually where the improvement opportunities are.

Once the lanes and steps are laid out, the `map-swimlane-builder` skill turns them into a Lucidchart-ready CSV or diagram.

---

## 5. Worked example: invoicing a completed service job

This is an **illustration**, not a real company's process. Replace every supplier, system and step with what actually happens in your process.

### 5.1 SIPOC

**Process:** Invoice a completed service job.
**Starts:** a work order appears on the "Ready to Invoice" list.
**Ends:** the invoice is delivered to the customer and the work order is set to Invoiced.

| Suppliers | Inputs | Process | Outputs | Customers |
| --- | --- | --- | --- | --- |
| Service team | Completed work order marked Ready to Invoice | 1. Pull Ready-to-Invoice work orders, oldest first | Posted invoice in the ERP | Customer's accounts payable (external) |
| Customer | Signed quote or PO; tax-exemption certificate; required reference numbers | 2. Verify authorization and billing data (PO or quote, amounts match across systems, tax status) | Open receivable on the customer account | Cash application and collections |
| Sales support | Verified billing amount; customer AP contact | 3. Complete the sales order (references, prices, quantities, tax, project code) | Invoice delivered by payment link, email or customer portal | Service team and regional managers (receive rejections and corrections) |
| CRM-to-ERP integration | Project number; sales order; customer record | 4. Preview and post the invoice | Work order status set to Invoiced | Finance (revenue recognition) |
| Tax service | Tax calculation | 5. Deliver the invoice | Corrections sent back to the service team when data is wrong | Leadership (revenue reporting) |
| | | 6. Update the work order status | | Billing team lead (workload and capacity) |

The columns in this table are read top to bottom, not across. Each row doesn't correspond to the others; for example, the tax service doesn't supply step 5.

### 5.2 Swim-lane sketch from the SIPOC

The lanes below come straight from the SIPOC's Supplier and Customer columns. Read down the table in step order. Each step sits in the lane of whoever does it. **→** marks a handoff to a different lane.

| # | Customer | Service team | Sales support | Billing | Systems (CRM, ERP, payment) |
| --- | --- | --- | --- | --- | --- |
| 1 | Signs quote or issues PO → | | | | |
| 2 | | | | | Opportunity closed/won → sales order created |
| 3 | | Completes work order, marks Ready to Invoice → | | | |
| 4 | | | Checks PO, quote and tax documents → | | |
| 5 | | | | Pulls work order from Ready-to-Invoice list | |
| 6 | | | | Verifies amounts match across systems and quote | |
| 7 | | ← *If data is wrong: sent back for correction* | | Finds a problem → | |
| 8 | | | | Completes sales order, previews and posts | |
| 9 | | | | Sends invoice → | Payment link emailed |
| 10 | ← Receives invoice (or it is uploaded to their portal) | | | | |
| 11 | | | | Sets work order to Invoiced | |

**What the sketch already shows:**

- **Every lane came from the SIPOC.**
- **There are at least five handoffs** before the customer is invoiced, plus a loop back to the service team when data is wrong (step 7). If people say "a lot of rejections come from Service," that loop is worth measuring.
- **The Systems lane is thin** compared with the human lanes. That often means people, not systems, are carrying the integration.

A full swim-lane map would expand steps 6 and 8 into the detailed checks: price overrides, tax codes, reference numbers, blanket POs and portal uploads. This markdown table is a sketch, not a diagram. For an actual Lucidchart version, use the `map-swimlane-builder` skill.

---

## 6. Questions to settle before you start

1. **Suppliers as swim lanes:** does the requester mean that the SIPOC's suppliers and customers become the lanes of the detailed map, or that the SIPOC itself is drawn with one band per supplier?
2. **Level:** one SIPOC per process, or one per line of business or region?
3. **Systems:** should systems be listed as suppliers, or only people and teams?
4. **Tool and format:** Visio, Lucidchart, Miro, Excel or PowerPoint? Is there an existing template to follow?

---

## 7. Visual examples and templates

**SIPOC examples with pictures:**

- [EdrawMax: SIPOC diagram examples](https://edrawmax.wondershare.com/examples/sipoc-diagram-examples.html). Nine illustrated examples, including a coffee shop and setting up a laptop for a new employee (a SIPOC paired with its own flowchart).
- [GoLeanSixSigma: Infographic, What is a SIPOC?](https://goleansixsigma.com/what-is-a-sipoc-example/). A one-page illustrated explainer. Not verified when this guide was written.
- [GoLeanSixSigma: SIPOC](https://goleansixsigma.com/sipoc/). Definitions and a walkthrough.

**SIPOC templates you can copy:**

- [Miro SIPOC template](https://miro.com/templates/sipoc/)
- [Lucid SIPOC diagram template](https://lucid.co/templates/sipoc-diagram)
- [FigJam SIPOC template](https://www.figma.com/templates/sipoc-diagram/)
- [Visual Paradigm SIPOC templates](https://online.visual-paradigm.com/diagrams/templates/sipoc-diagram/)
- [Accounts payable SIPOC example (ConceptDraw)](https://www.conceptdraw.com/examples/sipoc-for-accounts-payable). The page itself shows little, but it links to an AP-specific example.

**Swim-lane examples with pictures:**

- [Lucid: What is a swimlane diagram?](https://lucid.co/diagram/swimlane/tutorial). Two illustrated examples showing steps in their lanes and the connections between lanes.
- [Venngage: Swimlane process maps guide](https://venngage.com/blog/swimlane-process-map/). Several illustrated templates, including sales order processing.

**On how SIPOC and swim lanes fit together (text):**

- [Umbrex: Swimlane process map](https://umbrex.com/resources/frameworks/process-improvement-frameworks/swimlane-process-map/). Describes SIPOC as the precursor to the swim-lane map, and says each lane can be a role, team, department, system, vendor or customer.
- [Wikipedia: SIPOC](https://en.wikipedia.org/wiki/SIPOC). History, the build steps and the COPIS variation.
