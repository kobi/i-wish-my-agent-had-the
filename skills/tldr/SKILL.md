---
name: tldr
description: ONLY activate when explicitly requested with "tldr", "give me a summary", or a direct --skill tldr invocation. Never summarize automatically at the end of a task or during normal conversation.
---

# TL;DR

**Explicit invocation only.** Do not activate this skill unless the user directly asks for a TL;DR, TLDR or invokes `--skill tldr`.

Condense the current session into a terse, copy-pasteable update for a standup, PR description, or handoff. Include only what is supported by the session; do not invent completion or decisions.

Use exactly these three sections, in this order:

## Done

What was actually completed, one line per item.

## Decisions

Choices made along the way and why, one line per item. Write `None` if there were no meaningful decisions.

## Next

What remains unresolved or needs follow-up, one line per item. Write `None` if nothing remains.

Do not add a preamble, conclusion, or conversation recap. Keep every line short and make the result ready to paste as-is.
