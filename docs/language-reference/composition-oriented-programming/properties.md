---
icon: material/tag-outline
tags:
    - COP
    - Language Reference
---

# Properties

## Syntax

```bnf
<Property Getter> ::= "get" (<Block Statement> | <Expression>)
<Property Setter> ::= "set" (<Block Statement> | <Expression>)
<Property> ::= "property" <Identifier> ["[" {<Identifier> ["," <Identifier>]} "]"] [":" <Type Expression>] (<Property Getter> [<Property Setter>] | <Property Setter>) ";"
```