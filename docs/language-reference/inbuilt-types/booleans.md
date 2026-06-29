---
tags:
    - Build-in Type
---

## `Boolean`

| Property | Value |
| -------- | ----- |
| Size     | 1 byte (8 bits) |
| Values   | `false` or `true` |

The simple type `Boolean` is a logical data type. Its value can be assigned to many data types. 
For instance, `true` equals `1`, `0` equals `false`, and `Boolean(-5)` equals `true`.

## Literals

```topaz
var IsRunning: Boolean := false;
var SomeFlag: Boolean := 2; // converted to true
const Truth := true; // inferred as boolean
```

## Logical operations and conversions

All comparison operations result in logical values.

[See comparison operators :material-arrow-top-right:](/language-reference/operations/comparison/){ .md-button }

