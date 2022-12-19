from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


class Channel:
    def __init__(self, element, driver):
        self._element = element
        self._driver = driver
        self._ingredients = None
        self._time = None
        self._picture = None

    def extract_data(self):

        WebDriverWait(self._driver, 120).until(EC.presence_of_element_located((By.XPATH, './/main[contains(@id,"content")]')))
        time.sleep(5)

        self._time = self._driver.find_element(By.XPATH, './/div[@class="total-time"]').text
        self._ingredients = self._driver.find_element(By.XPATH, './/ul[@class="recipe-ingredients__list recipe-ingredients__collection splitColumns"]').text
        self._picture = self._driver.find_element(By.XPATH, './/div[contains(@class,"recipe-image")]//img[1]').get_attribute("src")
        print(self._time, self._ingredients, self._picture)

        self._driver.close()
        self._driver.switch_to.window(self._driver.window_handles[-1])

    def to_dict(self):
        return {
            'time': self._time,
            'ingredients': self._ingredients,
            'picture': self._picture
        }