# SIPOC: What It Is and How It Leads to a Swim-Lane Map

**Prepared for:** Suzan Oslin
**Date:** September 28, 2026
**Sources:** General process-improvement practice (outside this knowledge base) and the web pages linked in section 7. The worked example in section 5 is built from this folder's notes, mainly [Billing.docx](<Order-to-Cash/Billing.docx>) and [Order-to-Cash-Notes-Josh.docx](<Order-to-Cash/Order-to-Cash-Notes-Josh.docx>).

---

## 1. The short answer on "suppliers are the swim lanes"

A SIPOC and a swim-lane map are **two different tools, used one after the other**:

1. **SIPOC first.** It is a one-page table. It sets the boundaries of a process and lists everyone who feeds it and everyone who depends on it. It does *not* show who does each step.
2. **Swim-lane map second.** This is a detailed flowchart. Each horizontal band (a "lane") belongs to one person, team or system, and every step sits in the lane of whoever does it.

The link between them: **the people and groups you list in the SIPOC's Supplier (and Customer) columns are your starting list of lanes for the swim-lane map.** You don't have to work out who belongs on the map, because the SIPOC already told you.

That is almost certainly what Delphine meant by "Supplier as swim lanes." Your note had "??" after it, so it's worth confirming with her (see section 6). In section 5 you can see it happen: every lane in the swim-lane sketch comes from the SIPOC's Supplier or Customer column.

One refinement: a lane is strictly for **whoever performs a step**. Most suppliers do perform steps, so they become lanes. A supplier that only hands something over and does nothing else (for example, Avalara returning a tax rate) can be merged into a "Systems" lane or left off.

---

## 2. What a SIPOC is

SIPOC stands for **Suppliers, Inputs, Process, Outputs, Customers**. It is a five-column table that describes a process at a high level. It dates from the total quality management programs of the late 1980s and is now standard in Lean Six Sigma and business process management.

| Column | Question it answers | Example (service billing) |
|---|---|---|
| **S**uppliers | Who provides what the process needs? | Service team, Sales Support, the customer |
| **I**nputs | What do they provide? | Completed Work Order, signed quote or PO |
| **P**rocess | What are the 5–7 main steps? | Verify → build invoice → post → send |
| **O**utputs | What does the process produce? | Posted invoice, AR open item |
| **C**ustomers | Who receives the outputs? | Customer AP department, cash application |

**What it is good for:**
- Agreeing on where a process starts and stops before anyone maps details.
- Making sure no stakeholder is forgotten.
- Showing where inputs arrive late or incomplete. That's where rework comes from, and it's exactly what your onboarding plan asks you to trace ("What information does Doricia need to bill correctly? Where does it originate?").

**What it is not good for:** showing handoffs, delays, decisions or who does each step. That's the swim-lane map's job.

Delphine's description in your notes matches the standard one: *Supplier, Inputs (what), Process (5–10 steps), Outputs, Customers (who am I serving, what is the value).*

---

## 3. How to build one

Although the name runs S → I → P → O → C, you usually **fill it in from the middle out**:

1. **Name the process and set its boundaries.** Write down the trigger that starts it and the event that ends it. For example: *starts when a Work Order is marked Ready to Invoice; ends when the invoice is delivered and the WO is set to Invoiced.*
2. **Process column.** List 5–7 high-level steps, each as a verb and a noun ("Verify billing data"). Resist detail; that goes in the swim-lane map.
3. **Outputs.** What does the process produce? Include records and status changes as well as documents.
4. **Customers.** Who receives each output? Include internal customers.
5. **Inputs.** What does each step need?
6. **Suppliers.** Who or what provides each input?
7. **Check it with the people who do the work.** A SIPOC built alone at a desk is usually missing something.

**COPIS variation:** some teams fill it in backwards, starting from Customers and working upstream. This keeps the focus on what the customer needs. It's useful when the goal is "what does Carrie actually need to manage the team?"

**Tips:**
- Keep it to one page. If the Process column needs more than about 7 steps, you are probably describing two processes.
- Name roles and systems, not only individuals (for example, "Billing (Doricia)" rather than just "Doricia"), so the SIPOC stays true when people change.
- List systems as suppliers when they provide data (Salesforce, BC, Avalara). At InCharge a lot of the rework comes from system inputs that arrive incomplete.
- Pain points, workarounds and ideas don't belong in the SIPOC. Keep them in a separate list using your onboarding capture questions (Process, Pain, Why, Opportunity, Value).

---

## 4. From SIPOC to swim-lane map

| | SIPOC | Swim-lane map |
|---|---|---|
| **Level of detail** | High level, 5–7 steps | Detailed, often 15–40 steps |
| **Format** | Table | Flowchart in horizontal lanes |
| **Shows** | Scope, stakeholders, inputs and outputs | Who does each step, handoffs, decisions, waits, loops |
| **Best for** | Agreeing scope before mapping | Finding rework, delays and unclear ownership |
| **When** | First | Second |

**Steps to convert:**

1. Take everyone in the Supplier and Customer columns, plus anyone who performs a Process step. Each becomes a lane.
2. Put the external parties (customer, vendor) in the top or bottom lane, and group systems into one lane if they don't need separate lanes.
3. Break each high-level SIPOC step into the detailed steps you observed, and place each one in the lane of whoever does it.
4. Draw arrows. **Every time an arrow crosses from one lane into another, that is a handoff.** Handoffs are where work waits, gets lost or comes back for correction, so they are usually where the improvement opportunities are.

---

## 5. Worked example: service billing at InCharge

This is a **first draft** built from your notes on shadowing Doricia. Check it with her and with Sales Support before relying on it.

### 5.1 SIPOC

**Process:** Service billing.
**Starts:** a Work Order appears on the ServiceMax "O2C Ready to Invoice" list.
**Ends:** the invoice is delivered to the customer and the Work Order is set to Invoiced in Salesforce.

| Suppliers | Inputs | Process | Outputs | Customers |
|---|---|---|---|---|
| Service team / RSS | Completed Work Order marked Ready to Invoice; WO number | 1. Pull Ready-to-Invoice WOs, oldest first | Posted sales invoice in BC | Customer AP department (external) |
| Customer | Signed quote or PO; tax-exemption certificate; required reference numbers | 2. Verify authorization and billing data (PO or quote, amounts match across SF, BC and quote, tax status) | Open AR item on the customer account | Cash application (Walter) and collections |
| Sales Support (RSS, Katrina) | Verified billing opportunity; billing amount; AP contact | 3. Complete the BC sales order (references, prices, quantities, tax, project code, site name) | Invoice delivered by PayFabric link, email with documents, or customer portal upload | Service / RSS and regional GMs (receive rejections and corrections) |
| Salesforce → BC integration | Project number (billing opportunity number); BC sales order; customer card | 4. Preview and post the invoice | Work Order status set to Invoiced in Salesforce | Finance / record-to-report (revenue) |
| Shipping | Shipped items; WO reference on released orders | 5. Deliver the invoice | Corrections sent back to Service when data is wrong | Analytics and leadership (revenue by WO and line of business) |
| Avalara | Tax calculation | 6. Update the Work Order status in Salesforce | | Carrie (billing workload and capacity) |

The columns in this table are read top to bottom, not across. Each row doesn't correspond to the others; for example, Shipping doesn't supply step 5.

### 5.2 Swim-lane sketch from the SIPOC

The lanes below come straight from the SIPOC's Supplier and Customer columns. Read down the table in step order. Each step sits in the lane of whoever does it. **→** marks a handoff to a different lane.

| # | Customer | Service / RSS | Sales Support | Billing (Doricia) | Systems (SF, BC, PayFabric) |
|---|---|---|---|---|---|
| 1 | Signs quote or issues PO → | | | | |
| 2 | | | | | Opportunity Closed/Won → BC sales order created |
| 3 | | Completes WO, marks Ready to Invoice → | | | |
| 4 | | | Checks PO, quote and tax documents → | | |
| 5 | | | | Pulls WO from Ready-to-Invoice list | |
| 6 | | | | Verifies amounts match across SF, BC and quote | |
| 7 | | ← *If data is wrong: sent back for correction* | | Finds a problem → | |
| 8 | | | | Completes BC sales order, previews and posts | |
| 9 | | | | Sends invoice → | PayFabric emails payment link |
| 10 | ← Receives invoice (or it's uploaded to their portal) | | | | |
| 11 | | | | Sets WO to Invoiced in Salesforce | |

**What the sketch already shows:**

- **Every lane came from the SIPOC.** That's Delphine's point.
- **There are at least five handoffs** before the customer is invoiced, plus a loop back to Service when data is wrong (step 7). Your notes say "a lot of rejections coming from Service," so that loop is worth measuring.
- **The Systems lane is thin** compared with the human lanes. That fits the main finding of the O2C assessment: people, not systems, are carrying the integration.

A full swim-lane map would expand steps 6 and 8 into the detailed checks in your notes: price overwrites, locked SKUs, tax codes, site names, blanket POs and portal uploads.

---

## 6. Questions to confirm with Delphine

1. **"Suppliers as swim lanes":** did you mean that the SIPOC's suppliers (and customers) become the lanes of the detailed map? Or should the SIPOC itself be drawn with one band per supplier?
2. **Level:** should there be one SIPOC per process (service billing, EPC billing, cash application, AP invoice processing), or one per line of business?
3. **Systems:** should systems (Salesforce, BC, Avalara) be listed as suppliers, or only people and teams?
4. **Tool and format:** Visio, Lucidchart, Miro, Excel or PowerPoint? Is there an InCharge template, like the Installed Product Lifecycle diagram?

---

## 7. Visual examples and templates

**SIPOC examples with pictures:**
- [EdrawMax: SIPOC diagram examples](https://edrawmax.wondershare.com/examples/sipoc-diagram-examples.html). Nine illustrated examples, including a coffee shop and setting up a laptop for a new employee (a SIPOC paired with its own flowchart).
- [GoLeanSixSigma: Infographic, What is a SIPOC?](https://goleansixsigma.com/what-is-a-sipoc-example/). A one-page illustrated explainer. I couldn't open this page to check it, but it is a well-known training source.
- [GoLeanSixSigma: SIPOC](https://goleansixsigma.com/sipoc/). Definitions and a walkthrough.

**SIPOC templates you can copy:**
- [Miro SIPOC template](https://miro.com/templates/sipoc/)
- [Lucid SIPOC diagram template](https://lucid.co/templates/sipoc-diagram)
- [FigJam SIPOC template](https://www.figma.com/templates/sipoc-diagram/). You already have a Figma connector, so I could build yours in FigJam.
- [Visual Paradigm SIPOC templates](https://online.visual-paradigm.com/diagrams/templates/sipoc-diagram/)
- [Accounts payable SIPOC example (ConceptDraw)](https://www.conceptdraw.com/examples/sipoc-for-accounts-payable). The page itself shows little, but it links to an AP-specific example.

**Swim-lane examples with pictures:**
- [Lucid: What is a swimlane diagram?](https://lucid.co/diagram/swimlane/tutorial). Two illustrated examples showing steps in their lanes and the connections between lanes.
- [Venngage: Swimlane process maps guide](https://venngage.com/blog/swimlane-process-map/). Several illustrated templates, including sales order processing, which is close to your order-to-cash work.

**On how SIPOC and swim lanes fit together (text):**
- [Umbrex: Swimlane process map](https://umbrex.com/resources/frameworks/process-improvement-frameworks/swimlane-process-map/). Describes SIPOC as the precursor to the swim-lane map, and says each lane can be a role, team, department, system, vendor or customer.
- [Wikipedia: SIPOC](https://en.wikipedia.org/wiki/SIPOC). History, the build steps and the COPIS variation.
