"""GoatControl integration."""

import logging

import voluptuous as vol

from homeassistant.helpers import config_validation as cv

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

SERVICE_START_AREA = "start_area"
ATTR_AREA = "area"

START_AREA_SCHEMA = vol.Schema({vol.Required(ATTR_AREA): cv.string})


async def async_setup(hass, config):
    """Set up GoatControl."""
    hass.data.setdefault(DOMAIN, {})

    async def async_start_area(call):
        """Handle the start_area action."""
        area = call.data[ATTR_AREA]
        _LOGGER.info("Requested GoatControl area: %s", area)

    hass.services.async_register(
        DOMAIN,
        SERVICE_START_AREA,
        async_start_area,
        schema=START_AREA_SCHEMA,
    )

    return True
