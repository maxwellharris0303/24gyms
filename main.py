from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver import ActionChains
from time import sleep
import requests

driver = webdriver.Chrome()
driver.maximize_window()

url = "https://www.24hourfitness.com/search?query=Gyms+near+me&tabOrder=.%2Findex.html%2Clocations%2Cfaqs%2Cproducts%2Cclasses%2Clinks&facetFilters=%7B%22c_marketArea%22%3A%5B%5D%2C%22address.region%22%3A%5B%5D%7D&filters=%7B%7D&search-offset=0&referrerPageUrl=https%3A%2F%2Fwww.24hourfitness.com%2F&verticalUrl=locations.html"
driver.get(url)

WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "iframe[title=\"Gym Search\"]")))

iframe_element = driver.find_element(By.CSS_SELECTOR, "iframe[title=\"Gym Search\"]")
driver.switch_to.frame(iframe_element)

gyms_url = []

while(True):
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[class=\"HitchhikerLocationStandard-titleLink js-Hitchhiker-title\"]")))
    gyms_elements = driver.find_elements(By.CSS_SELECTOR, "a[class=\"HitchhikerLocationStandard-titleLink js-Hitchhiker-title\"]")
    print(len(gyms_elements))

    for gym_element in gyms_elements:
        gyms_url.append(gym_element.get_attribute('href'))
        with open('url.txt', 'a') as file:
            file.write(gym_element.get_attribute('href') + "\n")

    try:
        next_page_button = driver.find_element(By.CSS_SELECTOR, "a[aria-label=\"Go to the next page of results\"]")
        next_page_button.click()
        sleep(5)
    except:
        break

print(gyms_url)
print(len(gyms_url))