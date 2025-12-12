from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from utils.throttling import human_pause


class BingSearchPage(BasePage):

    SEARCH_INPUT = (By.NAME, "q")
    RESULTS = (By.ID, "b_results")

    def open(self):
        self.driver.get("https://www.bing.com")

    def search(self, text):
        box = self.wait.until(EC.element_to_be_clickable(self.SEARCH_INPUT))
        box.clear()

        # Escritura progresiva (realista, no evasiva)
        for ch in text:
            box.send_keys(ch)
            human_pause(0.08, 0.15)

        box.send_keys(Keys.RETURN)
        self.wait.until(EC.presence_of_element_located(self.RESULTS))
