# Graphr system spec — v3.5

**Status:** canonical. Three products implement this: the public site, **Kith**, and **Docket**.
**Supersedes all earlier versions.** Where any other document disagrees with this one, this one wins.
**This file must be byte-identical in all three repos** at `docs/graphr-system.md`. Change it here, bump the version, propagate. Never patch a house rule locally.
**Canonical home: `weldebob/graphr-tokens`, branch `main`, `graphr-system.md`.** No product repo's branch is the source. When copies disagree, graphr-tokens wins; check the version line and md5 against it.

---

## 1. The concept

Graphr comes from **graph theory**, not from charts. A **node** is a thing — a person or an organisation. An **edge** is a *named* relationship between two things.

`Patrick → engaged to → Grace`. `You → owe a reply to → Sofia`.

**Two rules follow, and they are absolute:**

1. **Every edge label is written by a human.** Never generated, never inferred from a surname or a shared employer. A parsed label is shown and confirmed before it is stored. "Related items" is not an edge.
2. **Never draw a graph.** No force-directed visualisations, no network diagrams, no nodes-and-lines as decoration. The concept appears as named relationships in content. If you are drawing a picture of a network, you have misread this document.

---

## 2. The products, and the tier line

| | What it is | Status |
|---|---|---|
| **yourgraphr.com** | Writing and free tools. The hub. | Public |
| **Kith** | The people you know, how you know them, and when to reach out | **Free, always** |
| **Kith with a history** | The same app, keeping every conversation | Paid — **not built as a sale yet** |
| **Docket** | What you owe people | Paid, bundled with the above — **not sold yet** |

**The product boundary:** *Kith tracks how you know someone. Docket tracks what you owe them.* Kith's edges never complete and decay if unattended; Docket's have a due date and are meant to be discharged.

### The tier axis is history, not size

> **Free keeps the current state of a relationship. Paid keeps its history.**

Your parents' birthdays, who is married to whom, that a new friend has two sons — those are **attributes and edges**. They are true until they change, and there is exactly one of each. A conversation on a golf course is **an event with a date**, and there will be forty more.

**Free stores one last-contacted date per person, overwritten each time. Paid stores every interaction, with notes, and never overwrites.** That single schema difference generates the whole feature split — which is why it is a real line and not a withheld one.

| Feature | Tier | Because |
|---|---|---|
| People, edges, circles, occasions, open questions | **free** | attributes and relationships |
| Gone quiet, reminders, export, notes on a person | **free** | needs only the one date |
| Search | paid | you do not search 40 names, you read them. You search *notes*, and free has none |
| Cadence rules | paid | "every six weeks" is a pattern; one date is not a pattern |
| The weekly review | paid | reconstructing a week only matters if the week is kept |
| Organisations, CSV import, filters, sort | paid | work-shaped. Nobody imports a CSV of their family |
| Docket | paid | obligations are a work motion |

**There is no person cap and there never will be.** A thousand people on free is fine — it will be a long list of names and dates, which is exactly what someone with a large family has. **The trigger to upgrade is wanting to remember a conversation**, which is a far more honest moment than hitting a number.

**Free must be able to write things down.** "Has two sons" is the point. What free lacks is a *dated, accumulating, searchable* log — not the ability to record a fact.

### There is no paid tier yet

There is no payment integration and will not be for some time. **Build one free product.** No billing, no trials, no upgrade triggers, no downgrade flow, no prices anywhere. The tier is **a flag on an account, set by hand.**

The boundary must still be designed in from the start — **it is a schema boundary** and retrofitting one is expensive. Write the interaction-history tables (§5) even though nothing reads them yet.

Say on the site: *"Kith is free. A version that keeps a full history of your conversations is coming."* No price, no date, no waitlist theatre.

### Canonical copy — use verbatim, do not paraphrase

> **Kith is a private record of the people you know and how you know them** — not their addresses, but that Patrick is engaged to Grace, that you introduced them, that his father is an old friend of yours.
>
> From a handful of facts you supply — a birthday, a last conversation, a relationship — it works out who is worth reaching out to and why, and tells you on the day.
>
> It invents nothing, guesses nothing about your family, shares nothing with anyone, and lets you take all of it back for thirty days after any change.
>
> It is deliberately narrow: Kith tracks how you know people, Docket tracks what you owe them, and neither will tell you anything you have not told it first.

Four existing lines are also canonical and survive any rewrite: *"An untidy graph still works — it just knows less."* · *"It stays empty. Nothing is invented to fill the day."* · *"Being in a circle is a fact about a person, so it is set on the person."* · *"Everything on this board was caught in one field. Nothing was typed into a form."*

---

## 3. Who it is for

**One sentence covers all of them:** the dates and facts about the people in your life are scattered across a paper calendar, a phone, a memory and a group chat, and **Kith is the one place they live.**

Four shapes of that, none of which is *the* user:

- **The large family.** Sixty people, eighty dates, no work angle at all. The purest free user and probably the most common.
- **The person who has moved.** Two graphs at once — one decaying, one forming. The most acute version, because moving removes all ambient contact in a single week. Time-boxed to roughly eighteen months.
- **The one who keeps everyone together.** Does it from memory today. Most likely to hand the app to five others.
- **The one with a life change.** New baby, divorce, bereavement, new job. The circle reshuffles and the same mechanic applies.

**Never name a segment in product copy.** No "expat", no "for relocating families". Relocation is where the pain is sharpest, not who the product is for — and the moment Kith grows relocation features (visa trackers, city guides, shipping checklists) it becomes a relocation app with a five-year customer life.

### Two values, not one

**Kith tells you** — a reminder fires on a day. Everything in this spec has been designed around this.

**Kith is somewhere to look** — a question arrives and you go and check. *When is the wedding? What is his wife called? When did we last see them?* This is lower-commitment and far more frequent, and it costs nothing extra: **the Occasions page must be designed to be read, not only to fire.** A forward-looking chronological list you can scan.

### Growth, and the one thing to refuse

The first real channel is **a trusted person handing it to a stream of people at the week their need is sharpest** — a relocation consultant, a community organiser. Better than viral invites, because the trust arrives attached. They need only an invite link, plus one legitimate seed: **themselves, as the recipient's first contact**, so the graph is not empty on day one.

**Someone will ask for a coach view** — see how clients are settling in, how many people they have met, who is struggling. **The answer is no, permanently.** Promise 1 admits no exceptions. The moment a client suspects their consultant can see who they have befriended, they stop recording the true things, and a graph nobody is honest with is worth nothing to anyone. A distributor may have **a count of links they handed out** and not one fact about what was done with them.

There is an obvious business in firms paying per client. It is also the exact route by which a coach view gets built. Note it; refuse it for a year.

---

## 4. The promises

Load-bearing. Each is the reason somebody trusts the product with their address book. **None may be softened without an explicit decision from Bob.**

1. **Two Kith users share no state, ever.** No mutual connections, no presence, no "you both know Patrick". An invite is a door, not a join. *(This will be proposed again every six months. The answer is no.)* This holds on **every channel that carries anything between two people** — the personal invitation, the Professional invitation and the card (§3a). Each carries only what the owner ticked on their own card; never anyone else in the graph, circles, notes, edges, `about_you`, a photo, a user id, or anything that lets either side find the other's account.
2. **Every edge label is human-written.** See §1.
3. **Nothing is invented to fill the day** — on screen, in the inbox, on a home screen. Silence is a feature.
4. **Match only, never create**, from any external source. Two exceptions, both requiring a tap from the user: a person the user named in their own voice note or text, and **a person who sent their own details from the user's card** (§3a) — two deliberate acts, one on each side.
5. **Export works and downgrade deletes nothing.** Provenance and 30-day undo on every write, in both apps.
6. **Kith never sends anything. Docket never auto-closes anything.** Both open a door; the user walks through it.
7. **Neither app reaches outward.** Reading the user's own calendar (opt-in) is not reaching outward. Suggesting people, pulling third-party profiles, or contacting anyone is. **The card (§3a) is the one sanctioned public surface**, approved explicitly by Bob on 2026-09-23: the owner deliberately shows it, it exposes only what they ticked, and it accepts one kind of inbound write. It fetches nothing and contacts nobody.

### 3a. The card — the one public surface

- Lives at `kith.yourgraphr.com/c/{token}`. Kith owns the token, the page and the data; the hub has no part in it.
- One token per owner per day, expiring at midnight in the owner's timezone. The owner can end it early.
- Shows only fields ticked `share_personal` or `share_work` on the owner's card. **Never the birthday.**
- Accepts one write: a visitor's own details, which arrive as a **suggestion**, never a person. Rate-limited, honeypot, no CAPTCHA.
- **The owner sees no scan counts or visitor data** of any kind.
- Useful without an account: a vCard download. **The offer to join sits below the card's own content** — never above the details, never a banner or modal, never gating the vCard or the form.
- **The page may read the visitor's own Kith session**, for one purpose: to offer an existing user `Add Bob to your Kith` instead of the sign-up offer. **Nothing about the visitor's account reaches the owner** — a submission is byte-identical whether the visitor is signed in or not, and no "is a Kith user" flag is stored, shown or inferable. That would be presence (promise 1). **No pre-fill from the visitor's card**; the phone's autofill does that job.
- Every user has a card. It is not paywalled and costs no invitation slot.

### 3b. Copy rule — passed away

**Say "passed away", never "died", "death" or "deceased"**, in every user-facing string in every product. Internal names (`died_on`) are exempt.

**Hazard, written down while it is cheap:** if Docket ever becomes multi-seat or company-administered, **the shared person layer must break first**. Everything in §5 assumes one person, one account they own.

---

## 5. The data model

**Graphr owns people. The products own edges.** Dana Whitfield is one record; Kith's notes about her and Docket's obligations to her are separate and **neither product can read the other's**.

### Implementation now: identical schemas, not a shared service

Do **not** build a shared identity service yet. Build the tables below **identically in both repos, from this spec** — same table names, same column names, same semantics. Unifying them later is then a data migration rather than a redesign.

**The schema is defined here, not in whichever repo implements it first.** If it needs to change, change this file first.

```
people
  id              uuid
  kind            'person' | 'org'          -- §6 glyph rule
  display_name    text
  sort_name       text
  died_on         date null
  memorial_mode   'birthday'|'death_day'|'silent'|null
  timezone        text null                 -- see below
  source          text                      -- provenance, §9
  merged_into     uuid null → people.id
  created_at / updated_at / deleted_at      -- deleted_at drives 30-day undo
```

**Birthdays are not a column on `people`.** They are a recurring occasion — see §7. A person page still shows a birthday field; it is backed by the occasions table.

**`timezone` is optional and worth having.** A reminder that says *"it is 9pm for her"*, or that does not fire at 7am your time when it is the middle of her night. Calling at the wrong hour is one of the most common ways a long-distance friendship quietly stops. One field, one line of arithmetic.

```
contact_methods
  id / person_id / channel                  -- 'email'|'phone'|'whatsapp'|'linkedin'|'other'
  label           text                      -- free; 'personal'/'work' suggested
  value           text
  is_preferred    bool                      -- max one true per person
  source / created_at
```

One typed list, never fixed `email_1` / `email_2` fields — the same argument returns immediately for a second phone number.

### Edges are dated

```

**Deliberate contact details are stored as given; pasted text is not.** A contact method the user typed into a person's card, or accepted from a card submission (§3a), is stored verbatim — that is what makes deep links (§13) possible. **Anything arriving in pasted, dictated, forwarded or captured text is still sanitised** before storage: addresses become `[email]`, numbers `[phone]`, and URLs are dropped with a `[n links omitted]` note. A parser may *offer* to add an address it found to a person's card, as a suggestion the user taps; it never writes one silently.

**Copy for the promise, both products:** *"Nothing you paste is kept word for word. Only the contact details you choose to add to a person are stored."* This replaces "no PII is ever stored" and "not a system of record" wherever either is stated.
edges
  id
  subject_type    'person' | 'self'
  subject_id      uuid null                 -- null when type = 'self'
  object_type     'person' | 'self'
  object_id       uuid null
  label           text                      -- stored as typed, displayed uppercase
  started_on      date null
  ended_on        date null                 -- superseded, not deleted
  source / created_at
```

**A superseded edge is dated, not deleted.** When Patrick and Grace marry, `ENGAGED TO` gets an `ended_on` and `MARRIED TO` begins. The person page can then say *engaged Sep 2025, married May 2026* — the first thing in Kith that reads as a history rather than a snapshot, for the cost of one column.

### The ego node

**You are a sentinel, not a row.** You are genuinely a node in your own graph — that is what an ego network means — but you must not be *enumerable*, or every present and future query has to remember to skip you, and the failure mode is silent.

```
owner_profile                    -- exactly one row
  id              int = 1
  display_name    text
  about_you       text null      -- assistant context; never sent with an invite
  timezone        text           -- required

owner_contact_methods            -- same shape as contact_methods, plus:
  travels_with_invite  bool      -- the tick column; only these are shared
```

The owner's own birthday is an occasion like anyone else's, attached to `self`.

**Reciprocity does not apply to ego edges.** Lateral edges write both halves because each half is displayed on a page. The owner has no page, so the reverse half has nowhere to appear. Write the single directed half, mark the pair as ego, skip the second write.

### Merging

Duplicates are **guaranteed**: the pasted calendar creates `Oma Trees`, an import creates `Trees Visser`, and the shared schema means a duplicate now appears in two products. A merge that keeps both sets of edges and is undoable **must exist before any bulk import ships**.

### Paid-tier tables — build now, use later

```
interactions                     -- the history that free does not keep
  id / person_id
  happened_on     date
  channel         text null      -- 'met'|'called'|'emailed'|…
  note            text null
  source / created_at
```

Free writes **one** row per person and overwrites it (or equivalently keeps a `last_contacted_on` derived value). Paid appends. That is the entire tier boundary, and it is why it must exist in the schema from day one.

---

## 6. Node grammar

| Glyph | Means | Spec |
|---|---|---|
| ● filled circle | a **person** | 11px, `border-radius: 50%` |
| ■ filled square | an **organisation** | 12px, no radius |
| ○ hollow dashed circle | a node with **no edges yet** | 11px, `border: 2px dashed #C2D2CC` |
| ◉ ringed circle | **you** | 17px, `2px solid #9A4527` ring, 9px `#23403C` fill |

Fill colour is positional: **clay `#9A4527` = the subject**, **spruce `#23403C` = the object**. This matches the favicon, which is therefore a legend for the system rather than decoration.

An organisation is a legitimate node but a *different kind*. Typing it is what makes "who else do I know at Anthropic" answerable — and it is what stops `MasterCard` reading as a colleague.

---

## 7. Occasions

**Occasions are the spine of Kith.** A birthday is not special; it is one kind of occasion that recurs.

```
occasions
  id
  person_id       uuid null → people.id     -- or the owner, via subject_type
  edge_id         uuid null → edges.id      -- anniversaries belong to the pair
  kind            'birthday'|'wedding'|'anniversary'|'graduation'|'other'
  label           text                      -- what the user typed
  day / month / year   int null             -- any part may be missing
  recurs          bool
  lead_days       int                       -- default per kind
  source / created_at
```

**Any date part may be missing.** Most people know a day and month and not a year. A required year forces users to invent one, omit the date, or bury it in a note — all three break the single fact that produces the most moments. **Never display a computed age unless the year was actually given.** A partial date sorts where it belongs and says plainly that it is incomplete — *"May?"* — because **the uncertainty is the record**, not a blocker to making one.

**`lead_days` is what makes non-birthday occasions useful.** A birthday matters on the day (`0`). A wedding is useless on the day — you needed to buy a gift, book a flight, find a hotel (`42`). Defaulted per kind, editable per occasion. Without it the feature fires too late to be worth anything.

**Anniversaries belong to the edge, not to a person.** If the user knows both Patrick and Grace, a person-attached anniversary fires twice every year. Store it once against the pair, render it *Patrick & Grace*, show it on both pages, fire once.

### An occasion may propose a follow-on — always confirmed

When an occasion passes it may offer a follow-on occasion **and** an edge change. One card, the morning after, one tap, undoable.

| Passed | Proposes |
|---|---|
| Wedding | a recurring anniversary, **and** `ENGAGED TO` → `MARRIED TO` |
| A death | the memorial choice (§8) |
| A birth | a new person, once the name is known |

**Never automatic.** Users record weddings they do not want a perpetual annual reminder about — a colleague's, a cousin's, one noted to be polite. Silently converting every one into a yearly obligation is precisely *inventing things to fill the day*, and it is how a calm app becomes a noisy one over three years. Ask once, at the only moment the answer is obvious.

**Three kinds have follow-ons. Nothing else needs one.**

### The restraint that keeps this from becoming a calendar

**Every occasion hangs off a person, with no exceptions.** Occasions are things that happen to people you know. Not appointments, not your own to-dos, not "dentist Tuesday" — the moment it accepts those it is a worse calendar competing with a good one.

---

## 8. Open questions — a gap is a first-class record

Every other tool treats an incomplete fact as a validation failure. Kith holds the gap deliberately: *she has two sons, I do not know their names, remind me to ask.*

```
open_questions(id, person_id, text, answered_at, created_at)
```

- **Do not model unknown people as nodes.** A node you cannot name is a row nobody can address, and it appears in every count, list and picker as a permanent blank. Hold it as a question; **promote it to a real person the day the name is learned.** Same rule for an occasion about someone not in the graph — attach it to the person you do know.
- **It rides moments that already exist.** The birthday email and the person's card gain a line: *"you meant to ask what her sons are called."* No new notification, no new surface.
- **Never generate the questions.** "You have not recorded her birthday" as an auto-nag turns the app into a form with opinions. The user writes the question in their own words — the same rule as edge labels. An *offer* at the moment of typing "two sons" is fine: *note to ask their names?*
- **This is free-tier.** It is about who someone is, not what happened. For anyone building a new social circle it is the main input method, not a garnish.

**Three features compose without a new idea:** a partial date, an open question and an occasion. *May, do not know the day, ask Marijke.* The question surfaces well before May, the answer completes the date, the reminder then fires with enough lead to act.

---

## 9. The memorial state

Kith is a product about people you love. Some of them will die while it is being used. Handling that badly is a worse failure than any bug in this spec.

- The action is **"Oma has died"** in the person's own menu — plainly worded, hard to hit by accident.
- It is a **state, not a deletion**. Node, edges, notes, occasions: everything stays.
- Three choices: remember on their birthday · remember on the day they died · say nothing but keep everything.
- They leave gone-quiet, cadence and every reach-out prompt. **Nothing about them is ever framed as overdue again.**
- Edges stay true — on Patrick's page she is still `GRANDMOTHER` — but she is not offered as a link target and no reach-out is suggested.
- **No `DECEASED` chip, no grey-out, no black border, no icon.** The wording is the design.
- When it fires: **"Oma Trees would have been 84 today"** — not a reminder to call her.

A record of who someone was, what they told you, and who they connected you to becomes most valuable at exactly the moment a contacts app would delete the row.

---

## 10. Provenance and reversibility

A house promise, not a feature. Every write records where it came from and is undoable for 30 days, in both apps, **using the same words**:

`You added it` · `Came in with an import` · `Captured by voice` · `Pasted in` · `Caught by email` · `From your calendar`

Both apps have a change log listing every change with its origin and an `Undo`. Disconnecting any source offers to remove everything it wrote.

**Confirm before write.** Anything parsed — from a paste, a voice note, an email — is shown as candidate facts *before* it is stored. Where a channel cannot show a confirm screen (the Docket inbox), the confirmation moves to a reply plus a reviewable state; it is never dropped.

**Export must produce a real portable file someone else could read:** people, edges with labels and dates, occasions, open questions, notes, provenance. JSON plus a CSV of people. A PDF would make the promise a lie. You are asking people for their family's birthdays — do not take that before they can get it back out.

---

## 11. AI

> **Every AI feature is a shortcut over a manual path that must exist and be good.**

If something is impossible without a model, it was not a shortcut — it was the feature, paywalled.

### Hosted AI is a per-account flag that Bob sets

```
accounts.hosted_ai   on | off        -- DEFAULT off
```

Bob pays for it on a handful of testing accounts. When the product spreads it goes behind usage pricing, once a payment gateway exists. **It is not a product default, not a user toggle, and not something signing up grants** — if it defaults on, account twenty-one gets it free and it cannot be taken back without an incident.

"Bring your own key" quietly means *this product is for people who know what an API key is*, which excludes almost everybody it is meant for. That is why hosted AI exists at all. At test scale it costs a few dollars a month — a rounding error, not a business decision.

**Six rules follow, and they are not optional:**

1. **Nothing is AI-only.** The manual path is not a fallback, **it is the product**; AI is an accelerant on top. A user without the flag must never see a stub, a locked panel, an upsell or a dead end — the AI affordance simply is not rendered, and the manual one is presented as the normal way, not the degraded one.
2. **No AI in the marketing.** Nothing on the site says *powered by AI* or shows the photo flow. Most visitors will not have it, and copy that promises it makes its absence a downgrade.
3. **Never taken away.** Whoever has the flag keeps it permanently when pricing arrives. Removing a feature from someone who has used it for six months is worse than never giving it.
4. **Meter from the first request** — calls, tokens and cost per account. Usage cannot be priced later without knowing what usage looks like, and it cannot be backfilled.
5. **A hard monthly cap per account.** Over the cap it falls back to the manual path rather than failing, so a bug or an enthusiast cannot produce a surprise bill.
6. **Own key stays, as a preference not a plan.** Buried in Settings, never on a path anyone must walk. It is the honest answer for a user without the flag who wants the shortcut.

**Never name a vendor** in copy — say *an AI service*, and tell anyone who asks.

### What hosted AI unlocks: the photograph

The two-step *photograph it, show it to your assistant, paste the answer* dance exists **only because Kith cannot look at the picture**. With the flag on it collapses to what a non-technical person expects:

> **Take a photo of your calendar.**
> We will read the dates off it and show you what we found before saving anything.
> `CHOOSE A PHOTO`  ·  or type them in

That is the difference between a product someone tries and one they abandon on step one. **The paste and typed paths remain**, as the flow for accounts without the flag and as the fallback over the cap.

**One honest sentence at the moment it happens**, not buried in Settings: *"The photo is read by an AI service and deleted straight after. Nothing else about your graph is sent."* And it must be true — **discard the image the moment the dates are out.**

### Bring your own AI, for accounts without the flag

The user asks whichever assistant they already use and pastes the answer. No key, no token, no per-page cost. Give them the prompt with a copy button — never make them invent the ask.

Settings says what is true:

> Kith does not connect to any of your accounts. When you want help with a list, it gives you the words to ask your own assistant, and you paste the answer back.

**No microphone permission, ever.** The user taps the mic on their own keyboard; the phone transcribes on-device. It is a textarea. A Kith-branded recorder would be a new gesture that does the same job worse and needs a permission dialog this product should never show. **The transcript is always visible and editable before parsing.**

**AI may:** parse text the user typed into candidate facts, shown before writing; draft a message the user will edit and send; summarise notes the user wrote.
**AI may not:** infer an edge label, invent a moment, send anything, or reach outward for context about a person.

**Parsers must be generous and never guess.** Accept messy formats, tabs, bullets, any date order. Resolve relative dates against today and display them as real dates, leaving vague ones unticked with the guess visible. **Never fuzzy-match a mangled name onto a person** — transcription mangles proper nouns above all else, and a wrong date is worse than none. Anything unparseable becomes an unticked row, never an error.

**Localisation:** the first users are Dutch and American. `3 maart` and day-first `11-3` on day one. Time zone is stored explicitly — a birthday email arriving at 7pm the day before is how notifications get switched off.

---

## 12. Notifications

**Email is the notification channel.** It needs no app, no permission, no push infrastructure, and for this content it is a better container than push: it carries context, holds the actions, and waits until dealt with.

- **One email per day, only on days with something.** A day's moments batch into a single message. Three birthdays is one email with three items.
- **No digest, no re-engagement, no email on an empty day.** LinkedIn emails on a schedule and finds something to say; this does the opposite. *"Nothing is invented to fill the day"* applies to the inbox or it means nothing.
- **The buttons are deep links** (`mailto:`, calendar, Teams) so the loop can close without opening the app.
- **Open questions ride along** — *"you meant to ask what her sons are called."*
- **Two addresses on paid** — work moments to the work address. A birthday reminder for someone's mother should not arrive in a corporate mailbox.

---

## 13. Flow of work

Outbound is free of privacy cost and ships immediately. Inbound needs rules first.

| # | Step | Needs | Status |
|---|---|---|---|
| 1 | Deep links — invite, draft, Teams chat | URLs and an `.ics` file | ship |
| 2 | Occasions / due items as a subscribable calendar feed | a signed feed URL, one-way out | ship |
| 3 | Ask-and-paste, inside the weekly review | a prompt and a forgiving parser | ship |
| 4 | Calendar / mail read-back over OAuth | scopes, tokens, a security review | **not planned** |
| 5 | Teams / Outlook side panel | an add-in | later |

**Steps 1–3 are the whole flow-of-work story and none need an integration decision.** Copy and paste needs nobody's approval — for the buyer this targets, an OAuth app may never be installable at all, and match-only stops being a promise and becomes structural.

If step 4 is ever built: **metadata never content**, match-only never create, off by default per source, one overwritten fact per person with no communication history accumulating, provenance like everything else, and calendar before mailbox. Write the permission dialog before the integration — if the honest sentence makes you wince, the scope is wrong.

**Being a website is a distribution decision, not an accident.** No install, no admin consent, no MDM, no app store. Submit the domain to the major filtering vendors for classification, and keep the phone path working so a block is an annoyance rather than an ending.

**Capture is a phone job; review is a desk job.** Both tiers want both. The web must be **complete**; a future app is narrow — capture, notify, today — and never a port of the website to a small screen. **Capture never blocks on parsing:** take the text, store it locally, confirm later.

---

## 14. Colour, type, surfaces

> **Clay is attention. Spruce is action. Phosphor is a figure on glass.**

| Role | Token |
|---|---|
| Attention — overdue, gone quiet, the subject, links | clay `#9A4527` on paper · **`#EE8A62` on glass** |
| Action — buttons, commit | spruce-deep `#23403C` · phosphor `#6FE3C0` on glass |
| Destructive | clay, **and always confirmation-gated** |
| Figures | phosphor `#6FE3C0`, **on glass only** |

**Live bug in all three products:** on-glass clay `#BF5B3B` on `#0E1A18` is **3.3:1**. Use `#EE8A62` (**6.3:1**). Plain clay `#9A4527` on glass is **2.76:1** — worse. A dark-surface link override must apply to **leaf glass surfaces only**; a descendant rule on a wrapper containing paper children inverts the bug.

**Paper** — cream `#F6F0E1` (ground, gutters, insets) · paper `#FFFDF8` (reading surfaces, cards) · rule `#EFE9DB` · border `#E3DCCC` · border-strong `#D8D2C4` · faint tint `#FBF8F0`

**Ink** — ink `#262219` · body `#3A352C` · deck `#453F31` · hint `#4A4437` · muted `#6B6353` *(14px minimum, never a deck or summary)*

**Spruce/glass** — glass `#0E1A18` · glass-2 `#152723` · glass-line `#2C4A44` · spruce `#3D6B64` · spruce-deep `#23403C` · phosphor `#6FE3C0` · phosphor-dim `#9FC4BB` · mint-paper `#E4EDE8` · mint-line `#C2D2CC`

**Clay** — clay `#9A4527` · hover `#7F3A20` · bright `#BF5B3B` *(paper only)* · glow `#EE8A62` *(glass only)* · sand `#D9B98A`

**Spacing** 4px base. **Radius** 0 glass/meters/chips, 3px cards/inputs, 4px panels, nothing above 5px. **Shadows: none, anywhere.**

**Type** — Newsreader (headlines, decks, names at display size), Figtree (body, labels, UI), mono (figures, counts, dates, edge labels).

| Element | Spec |
|---|---|
| Deck / subtitle | Newsreader 400 italic `21px/1.5` `#453F31`, max 56ch |
| Long-form body | Figtree 400 `18px/1.75` `#262219`, max 62ch |
| Card / summary | Figtree 400 `16.5px/1.65` `#3A352C` |
| Dense card body | Figtree 400 `16px/1.6` `#3A352C` |
| Eyebrow | Figtree 700 `11.5px` `0.18em` `#3D6B64` |
| Edge label | Mono 400 `12.5px` `0.08em` `#3D6B64` uppercase |
| Field hint | Figtree 400 `14.5px/1.55` `#4A4437` |

**`font-variant-numeric: tabular-nums` on every mono figure.** Required — live-updating numbers reflow without it.

**The mono face is IBM Plex Mono** — Bob's decision of 15 Sep 2026, first recorded in v1.1 §7, dropped by accident in v3.1 and restored here. Declare it ahead of the system stack, which stays as the fallback tail only: `'IBM Plex Mono', ui-monospace, Menlo, SFMono-Regular, monospace`. Weights 400 and 700.

**Surfaces:** cream is the desk, paper is the page, glass is chrome and figures. Any block reporting a number breaks out full-bleed onto glass. Cream is never a reading surface.

---

## 15. The edge row — the house component

One component, all three products. It replaces every other treatment of a relationship.

```
● Subject ── EDGE LABEL ── ● Object                    [metadata, right-aligned]
```

Single flex row, `gap: 12px`, `align-items: center`, padding `14px 18px`, rows split by `1px #EFE9DB` inside a `1px #E3DCCC` container on `#FFFDF8`.

| Part | Spec |
|---|---|
| Subject node | §6 glyph, clay fill, `flex-shrink: 0` |
| Subject name | Figtree 600 17px `#262219` |
| Connector | `22px × 2px` `#C2D2CC`, `flex-shrink: 0`, `aria-hidden` |
| **Edge label** | Mono 12.5px, `0.08em`, `#3D6B64`, uppercase **in display only** |
| Connector | as above |
| Object node | §6 glyph, spruce fill |
| Object name | Figtree 600 17px **clay `#9A4527`** — it is the link |
| Metadata | `margin-left: auto`, mono 13.5px `#6B6353`, and/or chips |

**Rules.** Direction is real — store it, let the label carry it. Only the metadata slot varies by product. Below ~700px the row wraps and metadata moves to its own line; the connectors stay. The row is an `<li>`; the visible label is the accessible name.

**The ego variant:** the owner renders as ◉ with the name `You` in **ink `#262219`, not clay** — every other object name is clay *because it is a link*, and the owner has no page. Metadata carries an `EGO` chip. Store `Dad`, display `DAD`; never generate `IS YOUR FATHER`.

**A superseded edge** shows its dates in the metadata slot and is visually quieter, never hidden.

| Product | Metadata carries |
|---|---|
| Kith | the date or fact that makes the edge live; `ORG` chip for organisations |
| Docket | derived state + overdue badge + provenance chip |
| Site | `TOOL` / `NOTE` / `SUBSTACK` |

---

## 16. Docket's own model

```
obligations
  id / person_id (nullable — "Renew passport" is legal)
  bucket        'do'|'reply'|'remind'|'discuss'
  project       text null                 -- kept, not shown; see below
  title / due_on / closed_at / source / created_at / deleted_at

captures                                  -- the catch tray; not obligations yet
  id / raw_text / parsed jsonb / source / created_at
  resolved      'accepted'|'dismissed'|null
  obligation_id uuid null                 -- set when accepted
  resolved_at   timestamptz null          -- dismissed rows purge after 30 days

obligation_updates
  id / obligation_id
  happened_on   date
  text          text
  implies_waiting bool
  source / created_at
```

**Do not add a status field.** An item accumulates dated updates — exactly the way it was captured — and its state is *derived* from the most recent one. One mechanism, no state machine, and it reads as a history rather than a form field.

| State | Derivation |
|---|---|
| **Open** | no updates since it was caught |
| **Waiting** | the latest update has `implies_waiting` |
| **Done** | `closed_at` is set |

**The catch tray is not a state.** "Caught, not yet confirmed" and "caught, and you said no" are a confirmation queue, and they live in `captures`, never on an obligation. An obligation exists only once the user has confirmed it. Everything that can't show a confirm screen — the inbox, Reconcile, a paste — lands in the tray.

**Everything on the board is something you owe — including following up.** There is no "what they owe me" direction. Tracking someone else's duty is expressed as your own follow-up: *"Troy finishes onboarding by Friday"* is `REMIND` or `DISCUSS NEXT` with a due date — you owe the check-in. When your own obligation is blocked on someone, that's *Waiting*. This keeps Docket's single axis intact: *Docket tracks what you owe them.*

**Priority:** the `⚠ HIGH` chip is removed. Keep the column; the parser stops setting it; revisit with the `project` column at 200 items.

**Nothing else.** Blocked, in-progress and on-hold are all *waiting* wearing different hats, and each extra state is a decision the user must make on every item.

**Waiting is the state that matters.** An open item is your problem and you know it; a waiting item is invisible until it is too late. *"You have been waiting nine days"* is worth more than anything Docket does with overdue, because nothing else in anyone's working life tracks it. It ages into a nudge, **never an auto-chase**.

### One kind of distinction per tab row

> **Kind is a lane. Time is a sort. Subject is a filter.**

`DO` · `REPLY TO` · `REMIND` · `DISCUSS NEXT` answer *what kind of thing do I owe*, and every item is exactly one of them forever. **Due** answers *when* — an item is a `REPLY TO` **and** due Friday. Put it in that row and either an item appears twice or the lanes stop being exhaustive, and **the moment a lane is not exhaustive you cannot trust the board shows everything.** That is the one thing Docket sells. Due lives in the counts bar, the sort and the morning email.

`Key projects` and `Accounts` answer *what is this about* — a third kind. **Remove the views and do not replace them yet.** With 22 items, grouping by project is a filter nobody needs. **Keep the `project` column and its data**, unshown; revisit at 200.

### The owner in Docket

The sentinel rule (§5) **applies to Docket**, because the person layer is shared: an enumerable owner would leak into Kith the day the schemas merge. Row-level security keys off `owner_profile.user_id = auth.uid()`, not off a `people` row. Obligations reference the owner by `subject_type = 'self'`.

### The inbox address

A Docket email address lets a user forward a thread or cc an update from inside the place the work happened. Three controls, all required:

1. **The address is secret, but need not be ugly.** Three ordinary words — `bob-tuna-lamp@in.yourgraphr.com` — readable, sayable, easy to save as a contact called *Docket*, rotatable in one click.
2. **Verify the sending domain's signature** (DKIM/SPF) and drop anything that fails. **The `From` line on an email is not authenticated** — it is a label the sender chooses — so an allowlist alone means "accept mail from anyone willing to type Bob's address in a box". The allowlist is the second lock, not the only one.
3. **Accept only the owner's own addresses**, and **drop everything else silently.** Never bounce: a bounce confirms the address exists, and a confirmation reply to a forged sender mails a stranger.

The mundane reason matters as much as the malicious one: a guessable address is scraped and spammed within weeks.

---

## 17. What each product owes this spec

| | Site | Kith | Docket |
|---|---|---|---|
| Person schema (§5) | — | ✅ identical | ✅ identical |
| Ego sentinel (§5) | — | ✅ | ✅ same owner |
| Occasions (§7) | — | ✅ | — |
| Open questions (§8) | — | ✅ | — |
| Edge row (§15) | `Connected` block | person page | item rows |
| Node glyphs (§6) | new | new | new |
| Colour law (§14) | clay fix | clay fix + destructive confirm | button → spruce, badges stay clay |
| Type + `tabular-nums` | ✅ | ✅ | ✅ |
| Provenance + undo (§10) | — | ✅ already close | add log + undo |
| Email (§12) | — | ✅ | ✅ |
| Deep links (§13) | — | ✅ | ✅ |

---

## 18. Change log

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-09-15 | First issue. Edge row, node grammar, colour law, owe/know and public/private boundaries. |
| 2.0 | 2026-09-19 | Shared person layer and schema, ego sentinel, two-SKU structure, numbered promises, AI position, email notifications, flow-of-work ladder. |
| 3.0 | 2026-09-20 | Tier axis restated as state-vs-history (§2). No paid tier. Occasions become the spine and absorb birthdays (§7). Open questions (§8). Dated edges and follow-on proposals. Optional per-person time zone. Who it is for, and the coach-view refusal (§3). Docket's tab rule (§16). B2 closed; `Key projects`/`Accounts` closed. |
| 3.1 | 2026-09-20 | **Hosted AI reinstated as a per-account flag Bob sets, with six rules and the photograph path (§11). Docket's inbox address becomes three readable words plus signature verification (§16).** |
| 3.2 | 2026-09-23 | **The card (§3a), approved by Bob as the one public surface; promises 1, 4 and 7 amended to name it. "Passed away" copy rule (§3b).** |
| 3.3 | 2026-09-23 | **Mono face restored as IBM Plex Mono (Bob, 15 Sep), dropped in v3.1 by mistake. Change-log rows put in order.** |
| 3.4 | 2026-09-23 | **§3a: the join offer may sit below the card content (was: only after sending). The card may read the visitor's own session to offer `Add Bob to your Kith`; nothing about the visitor reaches the owner; no pre-fill.** |
| 3.5 | 2026-09-24 | **Canonical home is `graphr-tokens@main`. Deliberate contact details stored, pasted text still sanitised; promise copy reworded. Docket: `captures` table for the catch tray, no direction column (follow-ups are your own obligations), `project` kept unshown, `⚠ HIGH` removed, owner sentinel applies.** |
