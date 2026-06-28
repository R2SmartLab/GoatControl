# 🐐 GoatControl

Control Ecovacs GOAT mowing areas directly from Home Assistant.
GoatControl provides a simple and reliable way to start individual mowing areas, build automations and integrate Ecovacs GOAT robots into advanced smart home workflows.

## Features

- ✅ Start individual mowing areas
- ✅ Home Assistant service integration
- ✅ Webhook support
- ✅ Fast execution
- ✅ Designed for automation
- 🚧 openHAB support (planned)
- 🚧 HACS installation (planned)

## Example

```yaml
action: goat_area.start_area
data:
  area: "129"
```

## Roadmap

- [x] Start individual areas
- [ ] Area name support
- [ ] Entity selector
- [ ] Status sensors
- [ ] Schedule support
- [ ] HACS integration
- [ ] openHAB integration
- [ ] Documentation

## Compatibility

- Home Assistant
- Ecovacs GOAT Series

## License

MIT License


Developed by **R²SmartLab**

Building practical automation solutions.
