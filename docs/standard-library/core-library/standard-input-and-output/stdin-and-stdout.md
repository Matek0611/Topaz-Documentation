---
tags:
    - Standard Library
    - Core Library
    - IO
---

# Standard Input/Output Utilities

## `Print`
Outputs one or more values to the standard output stream without appending a newline character.

```topaz
@VarArgs
function Print();
```

### Parameters

One or more expressions or values of any type to display.

### Returns

None.

## `PrintLine`

Outputs one or more values to the standard output stream, followed by a newline character.

```topaz
@VarArgs
function PrintLine();
```

### Parameters

One or more expressions or values of any type to display.

### Returns

None.

## `Scan`

Reads a single character from the standard input stream.

```topaz
function Scan(): WideChar;
```

### Parameters

None.

### Returns

The next captured input character as a WideChar.

## `ScanLine`

Reads an entire line of text from the standard input stream until a newline character is encountered.

```topaz
function ScanLine(): UnicodeString;
```

### Parameters

None.

### Returns

Returns the captured line of input as a Unicode string.