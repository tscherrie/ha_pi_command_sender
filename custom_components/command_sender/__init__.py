# __init__.py

from .service_handler import async_setup_services, async_unload_services

async def async_setup(hass, config):
    await async_setup_services(hass)
    return True

async def async_unload_entry(hass, entry):
    await async_unload_services(hass)
    return True
