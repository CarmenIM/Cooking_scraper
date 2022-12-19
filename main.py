import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from utility.dishes import Dish
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



url = 'https://www.tasteofhome.com/recipes/cuisines/?_cooking-style=easy'
driver = webdriver.Chrome(options=chrome_options)


driver.get(url)


WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, './/nav[contains(@class,"main-navigation")]')))

driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

dishes = []
item_elements = driver.find_elements(By.XPATH, './/div[@class="category-card-content"]')
for index, item_element in enumerate(item_elements):
# for item_element in item_elements:
    dish = Dish(item_element, driver=driver)
    dish.extract_data()
    dishes.append(dish)

    if index == 20:
        break

driver.close()


output = [
    dish.to_dict()
    for dish in dishes
]

with open('output.json', 'w') as json_file:
    json.dump(output, json_file, indent=2)