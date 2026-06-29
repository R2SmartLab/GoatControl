"""GoatControl integration."""

import asyncio
import logging

import async_timeout
import voluptuous as vol

from deebot_client.commands.json.clean import CleanAreaV2, CleanMode
from homeassistant.helpers import config_validation as cv

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

SERVICE_START_AREA = "start_area"
ATTR_AREA = "area"
ATTR_ENTITY_ID = "entity_id"
DEFAULT_ENTITY_ID = "lawn_mower.mahcedes"

START_AREA_SCHEMA = vol.Schema(
    {
        vol.Required(ATTR_AREA): cv.string,
        vol.Optional(ATTR_ENTITY_ID, default=DEFAULT_ENTITY_ID): cv.string,
    }
)

_command_lock = asyncio.Lock()


async def async_setup(hass, config):
    """Set up GoatControl."""
    hass.data.setdefault(DOMAIN, {})

    async def async_start_area(call):
        """Handle the start_area action."""
        area = call.data[ATTR_AREA]
        entity_id = call.data[ATTR_ENTITY_ID]
        _LOGGER.info(
            "Requested GoatControl start_area for entity_id=%s area=%s",
            entity_id,
            area,
        )

        if _command_lock.locked():
            _LOGGER.warning(
                "Ignoring GoatControl start_area for entity_id=%s area=%s because a command is already running",
                entity_id,
                area,
            )
            return

        async with _command_lock:
            try:
                component = hass.data.get("lawn_mower")
                if component is None:
                    _LOGGER.error(
                        "Cannot start GoatControl area %s: lawn_mower component is unavailable",
                        area,
                    )
                    return

                for ent in component.entities:
                    if ent.entity_id == entity_id:
                        device = ent._device
                        command = CleanAreaV2(CleanMode.SPOT_AREA, area)
                        _LOGGER.info(
                            "Sending CleanAreaV2 to entity_id=%s area=%s",
                            entity_id,
                            area,
                        )
                        async with async_timeout.timeout(8):
                            result = await device.execute_command(command)
                        _LOGGER.info("CleanAreaV2 command result: %s", result)
                        return

                _LOGGER.error(
                    "Cannot start GoatControl area %s: entity %s was not found",
                    area,
                    entity_id,
                )
            except Exception:
                _LOGGER.exception(
                    "Unexpected error while starting GoatControl area %s for entity %s",
                    area,
                    entity_id,
                )

    hass.services.async_register(
        DOMAIN,
        SERVICE_START_AREA,
        async_start_area,
        schema=START_AREA_SCHEMA,
    )

    return True
