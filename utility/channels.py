from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


class Channel:
    def __init__(self, element, driver):
        self._element = element
        self._driver = driver
        self._title = None




    def extract_data(self):
        link_element = self._element.find_element(By.TAG_NAME, 'a')


        self._driver.execute_script(f'window.open("{link_element.get_attribute("href")}")')
        self._driver.switch_to.window(self._driver.window_handles[-1])



        WebDriverWait(self._driver, 1200).until(
            EC.presence_of_element_located((By.XPATH, './/main[contains(@id,"content")]')))
        time.sleep(5)


        self._title = self._driver.find_element(By.XPATH, './/h1[contains(@class,"title")]').text
        print(self._title)

        self._driver.close()
        self._driver.switch_to.window(self._driver.window_handles[-1])

    def to_dict(self):
        return {
            'Recipe Title': self._title,
        }