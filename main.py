import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from utility.categories import Category
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument('--incognito')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
chrome_options.add_argument('--mute-audio')



url = 'https://www.tasteofhome.com/recipes/cuisines/'
driver = webdriver.Chrome(options=chrome_options)


driver.get(url)


WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, './/nav[contains(@class,"main-navigation")]')))

driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

categories = []
item_elements = driver.find_elements(By.XPATH, './/div[@class="owl-stage-outer"]//div[@class="item"]')
for index, item_element in enumerate(item_elements):
# for item_element in item_elements:
    category = Category(item_element, driver=driver)
    category.extract_data()
    categories.append(category)

    if index == 5:
        break


driver.close()


output = [
    category.to_dict()
    for category in categories
]

with open('output.json', 'w') as json_file:
    json.dump(output, json_file, indent=2)