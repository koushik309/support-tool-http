import sys
import os
import pytest

# Dynamically add steps/labgrid to Python's import path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'steps', 'labgrid')))

from steps.labgrid.labgrid_support_device import SupportToolRESTDevice
from steps.labgrid.labgrid_support_driver import SupportToolRESTDriver



@pytest.fixture 
def driver():
    # Create the Labgrid resource and bind the driver
    device = SupportToolRESTDevice("support_tool", url="http://localhost:5000")
    driver = SupportToolRESTDriver(device, url=device.url)
    
    # Activate the driver (performs health check)
    driver.on_activate()
    yield driver
    driver.on_deactivate()

def test_upgrade(driver):
    payload = {
        "device_id": "MD001",
        "target_version": "2.1.0",
        "options": {"force": True}
    }
    result = driver.upgrade(payload)
    assert result["status"] == "success"
    assert result["version"] == "2.1.0"

def test_downgrade(driver):
    payload = {
        "device_id": "MD001",
        "target_version": "1.2.0"
    }
    result = driver.downgrade(payload)
    assert result["status"] == "success"
    assert result["version"] == "1.2.0"
