---
title: Regular Expressions
tags:
    - Standard Library
    - Core Library
    - RegEx
---

# Regular Expressions

Topaz features a fast, predictable, and memory-safe regular expression engine based on a non‑backtracking (Thompson-style) NFA execution model. Matching runs in linear time with respect to the input length for a fixed pattern. More precisely the runtime is $O(n\cdot m)$, where $n$ is the input length and $m$ is the pattern size (so for a compiled or reasonably small pattern this is linear in $n$).

## Supported Syntax

The table below summarizes all regex constructs, character classes, anchors, and quantifiers supported by the engine.

| Category              | Pattern                                                             | Description & Examples                                                                                                                                                                          |
|:----------------------|:--------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Literals**          | `abc`                                                               | Matches exact character sequences (e.g., `abc`).                                                                                                                                                |
| **Any Character**     | `.`                                                                 | Matches any single character except newline (`\n`).                                                                                                                                             |
| **Character Classes** | `[a-z0-9]`<br>`[^aeiou]`                                            | Matches any single character within the brackets.<br>Negated class: matches any character **not** in the brackets.                                                                              |
| **Shorthands**        | `\d` / `\D`<br>`\w` / `\W`<br>`\s` / `\S`                           | Digit / Non-digit (`0-9`).<br>Word / Non-word character (`[a-zA-Z0-9_]`).<br>Whitespace / Non-whitespace (`\t`, `\n`, `\r`, space).                                                             |
| **POSIX Classes**     | `[[:alpha:]]`<br>`[[:digit:]]`...                                   | POSIX character classes (must be used inside bracketed character classes `[...]`). See [POSIX Character Classes](#posix-character-classes) for full details.                                    |
| **Anchors**           | `^` / `$`<br>`\b` / `\B`                                            | Start / End of input text (or start / end of **line** when multiline `(?m)` is active).<br>Word boundary / Non-word boundary.                                                                   |
| **Alternation**       | `cat                                                                | dog                                                                                                                                                                                             |bird` | Matches either `cat`, `dog`, or `bird`. |
| **Groups & Captures** | `(...)`<br>`(?:...)`<br>`(?<name>...)`                              | Capturing group (indexed numerical capture).<br>Non-capturing group (grouping without memory overhead).<br>Named capturing group (accessible by key, e.g., `(?<year>\d{4})` or `(?<name>...)`). |
| **Inline Modifiers**  | `(?i)` / `(?i:...)`<br>`(?m)` / `(?m:...)`<br>`(?im)` / `(?im:...)` | Case-insensitive mode (global or scoped to subpattern).<br>Multiline mode: `^` and `$` match start/end of each line (`\n`).<br>Combined inline flags (e.g., case-insensitive + multiline).      |
| **Greedy Repetition** | `*`<br>`+`<br>`?`<br>`{n}` / `{n,}` / `{n,m}`                       | Matches **0 or more** times.<br>Matches **1 or more** times.<br>Matches **0 or 1** time (optional).<br>Matches exactly `n`, at least `n`, or between `n` and `m` times.                         |
| **Lazy Repetition**   | `*?`, `+?`, `??`                                                    | Non-greedy equivalents. Matches as few characters as possible to satisfy the pattern.                                                                                                           |
| **Escapes**           | `\.`, `\*`, `\n`, `\t`                                              | Escapes special regex metacharacters or inserts control characters.                                                                                                                             |

### POSIX Character Classes

POSIX character classes allow you to match specific categories of characters. In Topaz regex expressions, POSIX classes are evaluated within bracketed character sets (e.g., `[[:alnum:]_]`).

| Class Name   | Equivalent / Description                                          |
|:-------------|:------------------------------------------------------------------|
| `[:alnum:]`  | Alphanumeric characters: `[a-zA-Z0-9]`                            |
| `[:alpha:]`  | Alphabetic characters: `[a-zA-Z]`                                 |
| `[:ascii:]`  | ASCII characters: `[\x00-\x7F]`                                   |
| `[:blank:]`  | Space and tab characters: `[ \t]`                                 |
| `[:cntrl:]`  | Control characters: `[\x00-\x1F\x7F]`                             |
| `[:digit:]`  | Digits: `[0-9]`                                                   |
| `[:graph:]`  | Visible characters (anything except space and control characters) |
| `[:lower:]`  | Lowercase letters: `[a-z]`                                        |
| `[:print:]`  | Printable characters (including space)                            |
| `[:punct:]`  | Punctuation and symbol characters                                 |
| `[:space:]`  | All whitespace characters: `[\t\n\v\f\r ]`                        |
| `[:upper:]`  | Uppercase letters: `[A-Z]`                                        |
| `[:word:]`   | Word characters: `[a-zA-Z0-9_]`                                   |
| `[:xdigit:]` | Hexadecimal digits: `[0-9a-fA-F]`                                 |

## Design & Safety

The engine explicitly excludes:

- **Backreferences** (e.g., `\1`, `\2`).
- **Lookarounds** (lookahead `(?=...)`, lookbehind `(?<=...)`, and their negative variants).

This exclusion is a deliberate safety assumption.  Because the matcher does not backtrack, classical exponential backtracking attacks (e.g., against `(a+)+b`) are not possible, making the engine resistant to ReDoS vectors that rely on backtracking. Note that costs are still proportional to pattern size. Extremely large patterns or heavy repeated use will consume CPU, but with predictable, bounded complexity.

## Additional Notes

- $O(m)$ extra memory to hold compiled instructions and per-match state ($m$ - pattern size).
- Compile and reuse patterns when matching repeatedly to amortize parse/compile cost.
- Storage and work scale with the number of capturing groups. Avoid unnecessary captures for high-throughput paths.
- Very large or programmatically generated patterns increase $m$ and thus CPU/memory cost. Prefer simpler or modular patterns.
- Benchmark patterns in your workload and prefer compiled reuse in servers or hot loops.