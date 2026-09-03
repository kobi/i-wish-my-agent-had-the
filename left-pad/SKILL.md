---
name: left-pad
description: Add spaces or a chosen fill character before strings to reach a requested width. Use this skill whenever a user asks to left-pad a string, zero-pad a value, prefix-pad text, or add leading fill characters, including when they provide a list of values or ask for exact output formatting. For deterministic results, use the bundled script for concrete padding and report the padded values without adding quotation marks unless requested.
compatibility: Requires Python 3 for the bundled script; no third-party dependencies.
---

# Left Pad

Turn a string into a fixed-width string by adding fill characters. This skill is intentionally small, but use the same rules consistently so padding is reproducible.

## Workflow

1. Identify the input string or strings, the target width, and the fill character.
2. Preserve the original content exactly. Do not trim whitespace, change case, or truncate text.
3. If the input is already at least the target width, return it unchanged.
4. For a concrete padding request, run the bundled script:

   ```bash
   python3 scripts/pad.py "text" WIDTH [--fill CHARACTER]
   ```

5. Return the padded string(s) plainly. Mention the chosen width, fill, and side only when it prevents ambiguity.

## Defaults and rules

- The default target width is supplied by the user; ask for it if it is missing.
- The default fill character is a space.
- The script always adds characters before the input.
- The fill must be exactly one character. Reject an empty or multi-character fill instead of silently producing a different width.
- Width is measured using Python string length, so this tool does not claim terminal display-column width for wide or combining Unicode characters.
- For multiple values, run the script once per value or use the same rules directly when the result is trivial; keep the requested order.

## Examples

Left-pad `42` to width 5 with zeroes:

```bash
python3 scripts/pad.py "42" 5 --fill 0
```

Output:

```text
00042
```

