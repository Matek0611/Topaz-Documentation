---
tags:
    - Standard Library
    - Core Library
    - RegEx
---

# Auxiliary types

## `RegExMatch`

It is a type representing a collection of the match captures.

```topaz
type
  RegExMatch = map of (UnicodeString, UnicodeString);
```

## `RegExMatches`

This type serves as a base for the output matches of the regular expression search. 

```topaz
type
  RegExMatches = array of RegExMatch;
```
