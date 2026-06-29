# GoatControl

GoatControl is a Home Assistant custom integration for Ecovacs GOAT robotic mowers.

The current working feature is starting individual mowing areas from Home Assistant. GoatControl can use friendly area names or raw Ecovacs area IDs, making it suitable for dashboards, scripts, automations and webhooks.

## Features

- Start individual mowing areas
- Friendly area names
- Home Assistant action integration
- Command locking
- Timeout handling
- Logging

## Current area mapping

- Mähfläche 1 -> 129
- Mähfläche 2 -> 130

Raw IDs such as `"129"` and `"130"` are still supported.

## Usage example

```yaml
action: goatcontrol.start_area
data:
  area: "Mähfläche 1"
```

## Compatibility

- Home Assistant
- Ecovacs GOAT series
- Tested with entity `lawn_mower.mahhcedes`

## Status

GoatControl is experimental. The current implementation relies on private Home Assistant / Ecovacs internals, so behavior may change when those integrations change.

## License

MIT License

Developed by **R²SmartLab**

Building practical automation solutions.
