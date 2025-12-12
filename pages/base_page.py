from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def wait_for_title(self, title):
        self.wait.until(EC.title_contains(title))

    def wait_for_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
