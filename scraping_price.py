from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver import ActionChains
from time import sleep
import requests
import quickstart

quickstart.main()
gyms_url = quickstart.getGymsUrlList()
print(gyms_url)

options = webdriver.ChromeOptions()
options.add_argument('--headless=new')

driver = webdriver.Chrome(options=options)
driver.maximize_window()

index = 0
for gym_url in gyms_url:
    # url = "http://www.24hourfitness.com/Website/Club/00510"
    try:
        driver.get(gym_url)

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class=\"pp-price\"]")))
        price = driver.find_elements(By.CSS_SELECTOR, "div[class=\"pp-price\"]")

        print(len(price))
        price_data = []
        if len(price) == 8:
            price_data.append(price[0].text.splitlines(0)[0])
            price_data.append(price[1].text.splitlines(0)[0])
            price_data.append(price[2].text.splitlines(0)[0])
            price_data.append(price[3].text.splitlines(0)[0])
            price_data.append(price[4].text.splitlines(0)[0])
            price_data.append(price[5].text.splitlines(0)[0])
            price_data.append(price[6].text.splitlines(0)[0])
            price_data.append(price[7].text.splitlines(0)[0])
        if len(price) == 6:
            price_data.append(price[0].text.splitlines(0)[0])
            price_data.append(price[1].text.splitlines(0)[0])
            price_data.append("")
            price_data.append(price[2].text.splitlines(0)[0])
            price_data.append(price[3].text.splitlines(0)[0])
            price_data.append("")
            price_data.append(price[4].text.splitlines(0)[0])
            price_data.append(price[5].text.splitlines(0)[0])
        print(price_data)
        quickstart.main()
        RANGE_NAME = f"24hourfitness!C{index + 3}:J"
        quickstart.insertData(RANGE_NAME, price_data)
    except:
        pass
    index += 1
