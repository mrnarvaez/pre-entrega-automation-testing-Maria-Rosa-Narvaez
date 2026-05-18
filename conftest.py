import pytest
from selenium import webdriver
from datetime import datetime


@pytest.fixture
def driver():

    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):

    outcome = yield
    report = outcome.get_result()

    # Solo cuando falla el test
    if report.when == "call" and report.failed:

        driver = item.funcargs["driver"]

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        screenshot_name = f"screenshots/screenshot_{timestamp}.png"

        driver.save_screenshot(screenshot_name)

        print(f"\nCaptura guardada: {screenshot_name}")