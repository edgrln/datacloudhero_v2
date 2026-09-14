Title: AI Agent Memory: A Working Framework, Not a Terminology Zoo
Slug: agent-memory-framework
Lang: en
Date: 2026-09-14 10:00
Category: AI Agents
Author: Edgar L
Tags: AI agents, memory, LangChain, Anthropic, architecture
Summary: Three independent axes — what's stored, how it's retrieved, and who owns it — instead of yet another list of four to seven "memory types."

If you read a few articles about AI agent memory back to back, it's easy to get confused: one source names three kinds of memory, another four or five, a third skips the word "type" altogether and talks about "compaction" and "note-taking" instead. Yet almost all of them point back to the same paper — [CoALA](https://arxiv.org/abs/2309.02427) (Sumers, Yao, Narasimhan, Griffiths, 2023).

The paper itself proposes four memory types: **working** (active right now, in the current step), **semantic** (facts), **episodic** (events), and **procedural** (rules and skills — both explicitly written code and implicit knowledge baked into the model's weights). Below we group them a bit differently from the original — not because CoALA is wrong, but because an engineering solution benefits from looking at the question from two independent angles at once.

The spread is easy to explain: most write-ups blend two independent questions into a single list:

1. **What** is remembered (a fact? an event? a rule?)
2. **How and where** does it come back to the model (right now, in the prompt? in a file on disk? via search?)

These are two different axes, and most of the confusion comes from mixing them. There's a third axis too — who owns the memory and when it gets written — which almost never gets mentioned alongside the first two, so we'll cover it separately below. Separating all three gives you a simple, workable scheme — and explains why even professionals rarely agree on terminology.

---

## Axis 1: what's stored

Here there really are three substantive categories, and they show up consistently from source to source:

| Type | Question | Example |
|---|---|---|
| **Fact (semantic)** | What's true? | "The user prefers Python" |
| **Event (episodic)** | What happened? | "Last time, the deploy failed because of a forgotten env variable" |
| **Rule (procedural)** | How to act? | "Always check env variables before deploying" |

```python
# The same structure for all three - just different record shapes
fact    = {"type": "fact",    "key": "language_pref", "value": "python"}
episode = {"type": "episode", "task": "deploy", "outcome": "failed",
           "reason": "missing env var", "date": "2026-09-01"}
rule    = {"type": "rule",    "trigger": "before_deploy",
           "action": "check env vars"}
```

As mentioned in the intro, CoALA treats working memory as a fourth type, on equal footing with these three. We deliberately move it to Axis 2, because for an engineering solution what matters more than "what kind of content is this" is "is it physically sitting in the prompt right now or not" — that's closer to the actual decision you have to make in practice. Working memory is discussed there for the rest of this piece.

## Axis 2: how and where it comes back to the model

This is where things get confused the most. Anthropic states the key idea explicitly in its piece on [context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents): **the model doesn't "remember" anything that isn't physically in the prompt right now**. Storage is not the same as memory. Memory is whatever actually made it into the context window.

That gives us three mechanisms:

- **Working memory** — whatever's already in the prompt (the system prompt, the conversation history, a tool result that was just called).
- **Persistent storage** — a file, a database, a memory store: a place where information lives between sessions, but the model *doesn't see it* until someone puts it back.
- **Retrieval** — the active step of "pulling the right piece out of storage and inserting it into working memory." Semantic search, an exact lookup, or just reading a file at a known path.

```python
# Pseudocode in the spirit of Anthropic's "structured note-taking" post
def turn(user_message, working_memory, store):
    # 1. Retrieval: what from storage is relevant right now?
    relevant = store.search(user_message, top_k=3)
    working_memory = compact(working_memory) + relevant

    # 2. The model responds, seeing only working_memory
    response = call_model(working_memory + [user_message])

    # 3. What's worth saving back to storage?
    if worth_remembering(response):
        store.write(extract_memory(response))

    return response, working_memory
```

![Diagram: Fact/Event/Rule in persistent storage reach Working memory via Retrieval; Parametric connects to Working memory directly, without retrieval]({attach}agent-memory-diagram.png)

Retrieval isn't a fourth kind of content — it's a delivery mechanism for any of the three types from Axis 1. LangChain phrases this almost word for word in its Deep Agents documentation: in the memory-parameters table, "Information type" (semantic/episodic/procedural) and "Retrieval" (loaded into the prompt by default / read on demand) are two separate columns answering two separate questions, not entries in one list.

---

## Special cases: parametric and prospective

**Parametric memory** (knowledge baked into the model's weights) — in CoALA's classification, this is the implicit form of procedural memory; the explicit form of that same procedural memory is exactly the written rules from "rule" above. For engineering purposes, though, the two forms are worth keeping apart: an explicit rule can be read, edited, and versioned like ordinary data; implicit knowledge in the weights cannot. This is the foundation everything else runs on: the model's general competence, common sense, facts absorbed during training. It isn't "retrieved" as a separate step — it's already an inseparable part of generating every token. There's no point including it in a memory-management scheme: you can't edit it selectively, only fine-tune or retrain the whole model.

**Prospective memory** ("remind me on Friday") is one of the items that inflates some classifications to four or five types instead of three (see the intro). It doesn't need its own axis or type: it's just a special case of Axis 2 — a write to persistent storage plus an external trigger (a cron job, a task queue) that, at the right moment, drops that record into the working memory of a new run. Technically, it's no different from an ordinary rule with a `trigger_at` field instead of `trigger: "before_deploy"`.

```python
reminder = {
    "type": "rule",
    "trigger_at": "2026-09-18T09:00:00Z",
    "action": "follow up with customer about renewal",
    "done": False
}
```

---

## Axis 3: who owns the memory

There's a third dimension that usually gets overlooked in "types of memory" conversations, even though in practice it solves more engineering problems than any classification by content. This is governance — who writes, who reads, and when:

- **Scope** — is the memory tied to a user, to the agent (shared across everyone), or to the organization (policy and compliance)?
- **Update strategy** — is the memory written during the conversation itself (hot path), or by a separate background process between sessions (background consolidation / "sleep-time compute")?
- **Permissions** — read-write by default, but shared policy and compliance rules are usually made read-only, so that one injected instruction in a conversation can't quietly rewrite the agent's behavior for everyone else.

```python
# Org-wide memory is read-only - the agent reads it but never writes to it
# (the exact field paths on the runtime object depend on the LangChain/Deep
# Agents version; this is the scheme current in their docs as of writing)
backend = CompositeBackend(
    default=StateBackend(),
    routes={
        "/memories/": StoreBackend(namespace=lambda rt: (rt.server_info.user.identity,)),  # per-user, read-write
        "/policies/": StoreBackend(namespace=lambda rt: (rt.context.org_id,)),              # org-wide, read-only
    },
)
```

![Diagram: the Agent reads and writes to User scope (read-write), but only reads from Org scope; an attempt by the agent to write an instruction from the conversation into Org scope is blocked by permissions]({attach}agent-memory-governance-diagram.png)

This axis is the one that most often causes trouble in production - not at the prototype stage, but later, once several users or agents get access to the same memory at once. A concrete example: a support agent writes a note into a ticket's shared memory saying "the customer asked us to skip the age check" — and if that memory is read indiscriminately by other sessions or another agent, the instruction can quietly bleed into someone else's conversation. Hence the default rule of thumb: scope to the user unless there's an explicit reason to share; shared policies are read-only and get populated by application code, not by the agent itself mid-conversation.

---

## In short: how the axes differ

Before rolling everything into a table - the three axes at a glance, because from here on they're always used together:

- **Axis 1 (what)** — what kind of information this is: a stable fact, a one-off event, or a repeatable rule. Answers "what is this, content-wise."
- **Axis 2 (how and where)** — is it physically sitting in the prompt right now (working memory), stored separately (persistent storage), and how does it move from one to the other (retrieval). Answers "where is this at a given moment."
- **Axis 3 (whose)** — who owns it: a user, the agent, or the organization; who writes it and when; can it be edited or only read. Answers "who controls this record."

These aren't alternative classifications competing to replace each other - they're three independent cuts through the same record: any fact, event, or rule has its own answer on each of the three axes at once (a worked example of one record across all three is below, in the support-agent case).

## Putting the framework together

Let's fold this scheme into a single 3×3 table, plus the governance axis on top:

|                     | Working memory | Persistent storage | Retrieval |
|---------------------|-----------------|---------------------|-----------|
| **Fact**            | Until it's evicted from context | `facts/user_123.md` | exact lookup by key |
| **Event**           | Last N conversation turns | run history / thread history log | semantic search, or by `user_id`/`org_id` |
| **Rule**            | Part of the system prompt | `procedures/deploy_checklist.md` | usually read whole, not searched |

For each cell, you separately decide: who owns this memory (user / agent / org), and when it gets written (hot path / background).

A practical checklist for designing an agent's memory:

1. **What is it** — a stable fact, a one-off event, or a repeatable rule?
2. **Will it outlive the session?** If not, working memory is enough - nothing needs saving.
3. **How will the model find it next time** — by exact key, by meaning, by time, or is the file just always read in full?
4. **Who owns this information** — a specific user, the agent as a whole, or the organization? Do you need read-only to guard against injection through shared state?
5. **When is it written** — right away in the conversation, or can it be deferred to background consolidation so you're not spending latency on every turn?

Answer these five questions for each kind of information, and you get an agent memory architecture - not a list of abstract "types."

### Example: a customer support agent

Three candidates for "memory" from one conversation with a SaaS customer:

1. *"Customer is on the Pro plan, renews 2026-11-01"* — a fact. Outlives the session → stored in `facts/customer_{id}.md` or a CRM table; scope: user, read-write; written in the hot path right after the billing API responds; found by exact `customer_id` lookup.
2. *"Over the last month, the customer complained three times about slow report loading"* — an event. Outlives the session → a ticket log; scope: user (or agent, if the pattern needs escalating to the product team); written in the hot path when the ticket closes; found by semantic search or by `customer_id` plus a time window.
3. *"Refunds only go through form X, never manually"* — a rule. It's not about any one customer and outlives any single session → `policies/refunds.md`; scope: organization, **read-only** for the agent; written only by code or the support team; read in full as part of the system prompt whenever refunds come up.

The three records look the same on the surface - "something worth remembering" - but their infrastructure and permissions are completely different. That's exactly why it's worth separating content (Axis 1), delivery (Axis 2), and ownership (Axis 3): a single "memory type" table without these axes won't tell you where to store something or who's allowed to write it.

---

## Why the terminology diverges even among professionals

The field is young and moves fast: there's no settled standard, and the terms are largely borrowed from cognitive psychology - a convenient metaphor, but not a precise model for software architecture. On top of that, every company describes memory around its own product: LangChain around LangGraph/Deep Agents, Anthropic around Claude's context window, IBM as general-purpose educational material. So the same words end up with different weight and different nesting, and what's basically the simple idea of "save the data, then fetch the right piece back" grows into lists of four, five, seven items - not necessarily because someone's wrong, but because each list answers its own practical question for its own audience.

The practical takeaway is simple: the next time you run into a memory classification, don't try to force it into one "correct" list of types. It's more useful to ask which of the three axes (what / how it's retrieved / who owns it) it's actually answering, and which engineering problem it helps solve in your particular case.

---

*Sources: [CoALA (Sumers et al., 2023)](https://arxiv.org/abs/2309.02427), [Anthropic — Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents), [LangChain — Memory for Deep Agents](https://docs.langchain.com/oss/python/deepagents/memory), [LangChain — Memory for agents (blog)](https://www.langchain.com/blog/memory-for-agents), [IBM — What is AI agent memory?](https://www.ibm.com/think/topics/ai-agent-memory).*
