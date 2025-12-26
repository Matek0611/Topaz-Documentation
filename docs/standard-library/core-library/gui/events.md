---
tags:
    - Standard Library
    - Core Library
    - GUI
---

# GUI events

## Event types

### Base events

| Name | Parameters | Description |
|------|------------|-------------|
|`Create`|None|It is triggered immediately after the component is created.|
|`Destroy`|None|It is triggered just before the component is destroyed.|

### Drawing events

### Component bounds events

### Mouse events

### Touch events

## Event map argument


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
        {"feature": "Touch events", "support": "partial", "version": "26", "timeline": [] }
    ],
    "Linux": [
        {"feature": "Base events", "support": "full", "version": "all", "timeline": [] },
        {"feature": "Drawing events", "support": "full", "version": "all", "timeline": [] },
        {"feature": "Component bounds events", "support": "full", "version": "all", "timeline": [] },
        {"feature": "Mouse events", "support": "full", "version": "all", "timeline": [] },
        {"feature": "Touch events", "support": "no", "version": "all", "timeline": [] }
    ]
}
}}}