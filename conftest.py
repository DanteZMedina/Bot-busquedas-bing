import pytest
import os
from datetime import datetime
from drivers.driver_factory import get_driver


@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call":
        html = item.config.pluginmanager.getplugin("html")
        if html is None:
            return

        extras = getattr(rep, "extra", [])

        driver = item.funcargs.get("driver")
        if driver:
            screenshots_dir = os.path.join("reports", "screenshots", "bing")
            os.makedirs(screenshots_dir, exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_path = os.path.join(
                screenshots_dir,
                f"{item.name}_{timestamp}.png"
            )

            driver.save_screenshot(screenshot_path)

            extras.append(html.extras.png(screenshot_path))
            rep.extra = extras
