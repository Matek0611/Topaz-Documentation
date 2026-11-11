---
icon: material/lightning-bolt-outline
tags:
    - COP
    - Language Reference
---

# Events

## Syntax 

```bnf
<Event Attributes> ::= "@Async" | "@VarArgs" | "@MapArgs"
<Event Kind> ::= "function" | "method"
<Event Prototype> ::= {<Event Attributes>} <Event Kind> <Function Parameters> [":" <Type Expression>]
<Event Type Expression> ::= "event" <Event Prototype> ";"
<Event Declaration> ::= "type" <Event Type Expression>
<Event Expression> ::= "^" <Event Prototype> ";" <Function Body> "end"
```

