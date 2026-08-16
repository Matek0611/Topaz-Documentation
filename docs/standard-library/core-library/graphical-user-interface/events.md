---
tags:
    - Standard Library
    - Core Library
    - GUI
    - Development
---


### Base Events

| Name | Parameters | Description |
|------|------------|-------------|
|`Create`|`const Target: GUIComponent`|It is triggered immediately after the target component is created.|
|`Destroy`|`const Target: GUIComponent`|It is triggered just before the target component is destroyed.|
|`HitTest`|`const Target: GUIComponent`, `(X, Y): Integer`|Determines and returns what part of the component corresponds to a particular screen coordinate. This can happen, for example, when the cursor moves, when a mouse button is pressed or released.|
|`CloseQuery`|`const Target: GUIComponent`|Returns a closing action of the target (`0`/`'none'` - do nothing, `1`/`'delete'` - remove component (default behavior), `2`/`'hide'` - hide component).|

### Drawing Events

| Name | Parameters | Description |
|------|------------|-------------|
|`Paint`|`const Target: GUIComponent`|Implements a custom handler used to draw the target control.|

### Component Bounds Events

| Name | Parameters | Description |
|------|------------|-------------|


### Mouse Events

| Name | Parameters | Description |
|------|------------|-------------|
||||

### Touch Events

| Name | Parameters | Description |
|------|------------|-------------|

## Example

Sample window with the red surface and custom title.

```topaz
// todo
```
