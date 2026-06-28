"""GoatControl integration."""

from .const import DOMAIN


async def async_setup(hass, config):
    """Set up GoatControl."""
    hass.data.setdefault(DOMAIN, {})
    return True