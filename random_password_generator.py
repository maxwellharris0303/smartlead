from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from time import sleep


def getRandomPassword():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.avast.com/en-us/random-password-generator#mac")

    WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[id=\"onetrust-accept-btn-handler\"]"))).click()
    WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class=\"control-buttons\"]"))).click()
    sleep(2)
    password = driver.find_element(By.CSS_SELECTOR, "div[class=\"password\"]").text
    print(password)
    driver.quit()
    return password