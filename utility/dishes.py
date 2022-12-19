from selenium.webdriver.common.by import By
from utility.channels import Channel
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Dish:
    def __init__(self, element, driver):
        self._element = element
        self._driver = driver
        self._title = None
        self._link = None
        self._channels = []

    def extract_data(self):
        title_element = self._element.find_element(By.TAG_NAME, 'h2')
        self._title = title_element.text
        link_element = self._element.find_element(By.TAG_NAME, 'a')
        self._link = link_element.get_attribute('href')
        print(self._title, self._link)

        self._driver.execute_script(f'window.open("{link_element.get_attribute("href")}")')
        self._driver.switch_to.window(self._driver.window_handles[-1])

        WebDriverWait(self._driver, 120).until(
            EC.presence_of_element_located((By.XPATH, './/div[@class="hamburger-wrapper"]')))

        channel_elements = self._driver.find_elements(By.XPATH, './/main[@class="recipe-template"]')
        for channel_element in channel_elements:
            channel = Channel(channel_element, self._driver)
            channel.extract_data()
            self._channels.append(channel)


    def to_dict(self):
        return {
            'dish': self._title,
            'link': self._link,
            'instructions': [
                channel.to_dict()
                for channel in self._channels
            ]
        }
