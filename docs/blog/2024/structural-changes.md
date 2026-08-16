---
date: 2024-04-16
description: Massive overhaul of the language codebase.
---

# Structural Changes

Over the past few weeks, I've undertaken a major architectural overhaul of the Topaz programming language.
While the high-level language semantics remain familiar, the under-the-hood execution pipeline and codebase 
organization have undergone a fundamental redesign.

Here is a look at what changed, why it matters, and where the language is heading.

## From Stack-Based to Register-Based Execution

Previously, the language relied on evaluating an Abstract Syntax Tree (AST) through a classic stack-based interpreter. 
While stack machines are straightforward to build (operations constantly *PUSH* and *POP* values off a central stack), 
they suffer from high instruction counts and redundant memory access patterns.

To increase execution throughput and cut dispatch overhead, the runtime has been re-architected 
into a **Register-Based Bytecode Interpreter**.

Operations that previously required three or four stack instructions (e.g., pushing two operands, adding, and storing)
are now encoded in a single 16-bytes register virtual code (see [`TTopazXVirtualCode`](https://github.com/Matek0611/Topaz-Interpreter/blob/main/modules/topaz.bytecode.types.pas)).
Fetching fewer instructions means fewer iterations through the core VM loop, yielding better runtime performance.

**New virtual code structure:**

| Instruction | Properties | Metadata | Destination | First Source | Second Source |
|-------------|------------|----------|-------------|--------------|---------------|
| 1 byte      | 1 byte     | 2 bytes  | 4 bytes     | 4 bytes      | 4 bytes       |

## Source Module Rearrangement & Core Types

In tandem with the VM rewrite, the underlying repository structure received a clean refactor 
to enforce modularity and facilitate future compiler passes.
Moreover, standard library features and core runtime routines have been modularized, 
making it significantly easier to register new native functions. 
In addition, the internal type system has been extended to handle primitive operations directly within virtual register slots, 
reducing unnecessary heap allocations.