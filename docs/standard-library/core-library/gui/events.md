---
tags:
    - Standard Library
    - Core Library
    - GUI
---

# GUI events

## `GUIEventDetails` type

The `GUIEventDetails` type is an alias for a type `map of (UnicodeString, auto)`. Each key-value pair represents the given GUI element detail as follows:

| Key | Value | Expected Value Type |
|-----|-------|---------------------|
|`Target`|Target component of the event (e.g. a window, a button etc.).|`GUIComponent`|

## `GUIEventType` type 

This is an enumeration that describes all GUI event types. We can distinguish plenty of them, as it is described later in the event categories section. It is worth noting here that when specifying the type, the prefix *et* should be added. For instance: `etCreate`, `etPaint`, `etMouseMoved` etc.

## Event categories



### Generic `GUIProcessEvent` event

The `GUIProcessEvent` acts as the central dispatcher for the lifecycle of a UI component. Since it handles generic events like `Paint`, `Create`, and `Destroy`, it serves as a universal hook that intercepts an event before it is routed to more specialized, dedicated methods. 

Because this event is *generic*, it usually sits at the top of the processing chain. The flow typically looks like this:

1. **Intercept**: GUIProcessEvent is called first. It allows you to perform global logic (like logging or security checks) regardless of whether the event is a simple mouse click or a complex `Paint` command.

1. **Filter**: Inside `GUIProcessEvent`, a switch or if statement checks the `GUIEventType`.

1. **Dispatch specialized methods**: After the generic processing is done, the system calls the specific separate methods (e.g., `Paint()`, `Create()`, or `Destroy()`).

**Declaration**:

```topaz
type GUIProcessEvent = event method (const EventType: GUIEventType; const EventDetails: GUIEventDetails): auto;
```

### Base events

| Name | Parameters | Description |
|------|------------|-------------|
|`Create`|`const Target: GUIComponent`|It is triggered immediately after the target component is created.|
|`Destroy`|`const Target: GUIComponent`|It is triggered just before the target component is destroyed.|
|`HitTest`|`const Target: GUIComponent`, `(X, Y): Integer`|Determines and returns what part of the component corresponds to a particular screen coordinate. This can happen, for example, when the cursor moves, when a mouse button is pressed or released.|
|`CloseQuery`|`const Target: GUIComponent`|Returns a closing action of the target (`0`/`'none'` - do nothing, `1`/`'delete'` - remove component (default behavior), `2`/`'hide'` - hide component).|

### Drawing events

| Name | Parameters | Description |
|------|------------|-------------|
|`Paint`|`const Target: GUIComponent`|Implements a custom handler used to draw the target control.|

### Component bounds events

| Name | Parameters | Description |
|------|------------|-------------|


### Mouse events

| Name | Parameters | Description |
|------|------------|-------------|
||||

### Touch events

| Name | Parameters | Description |
|------|------------|-------------|

## Example

Sample window with the red surface and custom title.

```topaz
type MainWindow = class(GUIWindow)
  public 
    constructor Create();
      // Create event (called later)
      Self.Titlebar.Title := 'My Window';
    end;

    method Paint(Target: GUIComponent);
      // Paint event
      Target.Surface.Fill($FF0000FF); // red filling
    end;

    method ProcessEvent(const EventType: GUIEventType; const EventDetails: GUIEventDetails): auto;
      case EventType of
        etCreate: EventDetails.Target.Titlebar.Color := $AB55CCFF; // changed beforehand
        else inherited ProcessEvent(EventType, EventDetails);
      end;
    end;
end;
```


{{{compatibility:
{
    "Windows": [
        {"feature": "Base events", "support": "full", "version": "10", "timeline": [] },
        {"feature": "Drawing events", "support": "full", "version": "10", "timeline": [] },
        {"feature": "Component bounds events", "support": "full", "version": "10", "timeline": [] },
        {"feature": "Mouse events", "support": "full", "version": "10", "timeline": [] },
        {"feature": "Touch events", "support": "full", "version": "10", "timeline": [] }
    ],
    "macOS": [
        {"feature": "Base events", "support": "full", "version": "26", "timeline": [] },
        {"feature": "Drawing events", "support": "full", "version": "26", "timeline": [] },
        {"feature": "Component bounds events", "support": "full", "version": "26", "timeline": [] },
        {"feature": "Mouse events", "support": "full", "version": "26", "timeline": [] },
        {"feature": "Touch events", "support": "partial", "version": "26", "timeline": [[true, "Touch events are implemented with the use of TouchEvent and GestureEvent classes. They will not work both on standard non-touch and touch monitors, due to the limitation of the macOS system.", "2025"]] }
    ],
    "Linux": [
        {"feature": "Base events", "support": "full", "version": "", "timeline": [] },
        {"feature": "Drawing events", "support": "full", "version": "", "timeline": [] },
        {"feature": "Component bounds events", "support": "full", "version": "", "timeline": [] },
        {"feature": "Mouse events", "support": "full", "version": "", "timeline": [] },
        {"feature": "Touch events", "support": "no", "version": "", "timeline": [] }
    ]
}
}}}