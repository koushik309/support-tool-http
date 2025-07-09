import pytest
from labgrid_support_device import SupportToolRESTDevice
from labgrid_support_driver import SupportToolRESTDriver

@pytest.fixture
def driver():
    device = SupportToolRESTDevice("support_tool", url="http://localhost:5000")
    driver = SupportToolRESTDriver(device, url=device.url)
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
