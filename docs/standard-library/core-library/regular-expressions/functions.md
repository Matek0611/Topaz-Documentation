---
tags:
    - Standard Library
    - Core Library
    - RegEx
---

# Functions

## `Match`

Determines whether the specified regular expression pattern finds a match within the input text.

```topaz
function Match((APattern, AText): UnicodeString): Boolean;
```

### Parameters

1. `APattern` - the regular expression pattern to match.
2. `AText` - the target input string to evaluate.

### Result

Returns `true` if the pattern matches the input text. Otherwise, `false`.

## `Search`

Searches the input text for all occurrences that match the regular expression pattern and captures their details.

```topaz
function Search((APattern, AText): UnicodeString): RegExMatches;
```

### Parameters

1. `APattern` - the regular expression pattern to search for.
2. `AText` - the target input string to scan.

### Returns

A [`RegExMatches`][RegExMatches] structure containing detailed information about all matched substrings and their captured groups.

## `Replace`

Replaces occurrences of a regular expression pattern within the input string with a specified replacement string.

```topaz
function Replace(
    (APattern, AText, AReplacement): UnicodeString,
    ACount: LongInteger := 0
): UnicodeString;
```

### Parameters

1. `APattern` - the regular expression pattern to match.
2. `AText` - the input string in which to perform the replacement.
3. `AReplacement` - the replacement string to substitute for each match.
4. *Optional* `ACount` - the maximum number of replacements to make. If set to a value less than 1 (default), all occurrences of the pattern are replaced.

### Returns

A new `UnicodeString` with the specified pattern occurrences replaced by the substitution string.

## Examples

The following example demonstrates how to validate, extract, and reformat dates using the functions mentioned above:

```topaz linenums="1"
// 1. Validate if a string contains an ISO date (YYYY-MM-DD)
PrintLine(Core.Regex.Match('\d{4}-\d{2}-\d{2}', 'Event date: 2026-08-02'));
// Output: true

// 2. Extract matches and named groups (year, month, day)
PrintLine(Core.Regex.Search('(?<year>\d{4})-(?<month>\d{2})-(?<day>\d{2})', 'Today is 2026-08-02, next week is 2026-08-09.')); 
// Output: 
// [
//   #[`1`: `2026-08-02`, `year`: `2026`, `day`: `02`, `month`: `08`], 
//   #[`year`: `2026`, `day`: `09`, `month`: `08`, `2`: `2026-08-09`]
// ]

// 3. Reformat ISO dates (YYYY-MM-DD) to European format (DD/MM/YYYY)
PrintLine(Core.Regex.Replace('(\d{4})-(\d{2})-(\d{2})', 'today is 2026-07-10', '$3/$2/$1'));
// Output: today is 10/07/2026
```

[RegExMatches]: ./types.md