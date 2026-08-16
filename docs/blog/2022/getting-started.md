---
date: 2022-05-29
description: First notes.
---

# Getting Started

I’ve decided to start building a new interpreted programming language from scratch.
While the ecosystem is full of great tools, I felt there was a sweet spot missing, 
i.e. a language that combines the developer experience of a dynamic interpreter with 
modern capabilities like native hardware acceleration, straightforward UI development, 
and modern architectural primitives.

Here are the three core pillars driving its design:

* Building a graphical user interface shouldn't require installing massive third-party dependencies,
fighting foreign function interfaces (FFI), or configuring complex build pipelines.
The standard library includes a native, lightweight and cross-platform GUI toolkit. You can launch desktop windows, layout visual elements, 
and wire up events directly from standard scripts without adding a single external package.
* Unlocking parallel computation on the GPU usually means writing separate shader code (GLSL/HLSL/CUDA),
managing context switching, and dealing with tedious memory buffers. In this language, 
GPU execution is built into the language syntax. You can define functions intended for the GPU natively in your code, 
letting the interpreter handle compilation and dispatch to graphics hardware under the hood.
* Traditional Object-Oriented class hierarchies often end up rigid, prone to deep inheritance issues, 
and difficult to refactor. This language discards class inheritance entirely in favor of a compositional model built around two key primitives:
    * `component` - modular data and state containers.
    * `feature` - reusable behaviors, capabilities, and functions that attach to components.

In the future I'll be documenting the interpreter's development, syntax design, and performance milestones as I build it out.