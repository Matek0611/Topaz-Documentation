---
icon: material/function
tags:
    - COP
    - Language Reference
---

# Functions

## Functions and Procedures

### Syntax

```bnf
<Identifier List> ::= "(" <Identifier> ["," <Identifier>]* ")"
<Function Parameter> ::= ["const" | "ref"] (<Identifier List> | <Identifier>) ":" <Type Expression> [ ":=" <Basic Expression> ]
<Function Parameters> ::= "(" [<Function Parameter> ["," <Function Parameter>]*] ")"
<Function Attributes> ::= {"@Abstract" | "@Async" | "@Native" | "@VarArgs" | "@MapArgs" | <External Attribute> | <Hint Attribute> | <Custom Attribute>}
<Function Prototype> ::= <Function Attributes> "function" <Identifier> <Function Parameters> [":" <Type Expression>] ";"
<Function Body> ::= [<Statement> | ("exit" [["*"] <Expression>] ";") ]
<Function Declaration> ::= <Function Prototype> <Function Body> "end" ";"
```

## Methods

### Syntax

```bnf
<Method Prototype> ::= <Function Attributes> "method" <Identifier> <Function Parameters> [":" <Type Expression>] ";"
<Method Declaration> ::= <Method Prototype> <Function Body> "end" ";"
```

## Constructors

### Syntax

```bnf
<Constructor Prototype> ::= <Function Attributes> "constructor" [<Identifier>] <Function Parameters> [":" <Type Expression>] ";"
<Constructor Declaration> ::= <Constructor Prototype> <Function Body> "end" ";"
```

## Destructors

### Syntax

```bnf
<Destructor Prototype> ::= <Function Attributes> "destructor" [<Identifier>] <Function Parameters> [":" <Type Expression>] ";"
<Destructor Declaration> ::= <Destructor Prototype> <Function Body> "end" ";"
```

## Generators

### Syntax

```bnf
<Generator Prototype> ::= <Function Attributes> "generator" <Identifier> <Function Parameters> [":" <Type Expression>] ";"
<Generator Declaration> ::= <Generator Prototype> <Function Body> "end" ";"
```
