# service_handler.py

import logging
import subprocess

from homeassistant.core import HomeAssistant, ServiceCall

from .const import DOMAIN, SERVICE_SEND_COMMAND

_LOGGER = logging.getLogger(__name__)

async def async_setup_services(hass: HomeAssistant):
    async def handle_send_command(call: ServiceCall):
        command = call.data.get("command")
        if command:
            _LOGGER.debug(f"Executing command: {command}")
            try:
                subprocess.run(command, shell=True, check=True)
                _LOGGER.info(f"Command executed successfully: {command}")
            except subprocess.CalledProcessError as e:
                _LOGGER.error(f"Command failed: {command}")
                _LOGGER.error(e)
        else:
            _LOGGER.error("No command provided to execute.")

    hass.services.async_register(
        DOMAIN, SERVICE_SEND_COMMAND, handle_send_command
    )

async def async_unload_services(hass: HomeAssistant):
    hass.services.async_remove(DOMAIN, SERVICE_SEND_COMMAND)
