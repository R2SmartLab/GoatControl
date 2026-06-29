# Installation

## Manual installation

1. Copy `custom_components/goatcontrol` into `/config/custom_components/`.
2. Add GoatControl to `configuration.yaml`:

   ```yaml
   goatcontrol:
   ```

3. Run the Home Assistant configuration check:

   ```bash
   ha core check
   ```

4. Restart Home Assistant.

## Updating

Until HACS support is available, update GoatControl manually by replacing the files in `/config/custom_components/goatcontrol` with the latest raw files from GitHub:

- `custom_components/goatcontrol/__init__.py`
- `custom_components/goatcontrol/const.py`
- `custom_components/goatcontrol/manifest.json`
- `custom_components/goatcontrol/services.yaml`

After updating, run `ha core check` and restart Home Assistant.

## Logging

To temporarily increase logging from Home Assistant, call the `logger.set_level` action:

```yaml
action: logger.set_level
data:
  custom_components.goatcontrol: debug
```

You can also add a persistent logger configuration to `configuration.yaml`:

```yaml
logger:
  default: info
  logs:
    custom_components.goatcontrol: debug
```
