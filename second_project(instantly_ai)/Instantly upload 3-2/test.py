import threading
from selenium_driverless.sync import webdriver
from selenium_driverless.types.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
from selenium.webdriver.chrome.options import Options
from time import sleep
import time
import pandas as pd


CSV_FILE_NAME = "data_gmail.csv"

data= pd.read_csv(CSV_FILE_NAME)

count = len(data)
email_list = data.Email
password_list = data.Password
instantly_login = data.Instantly
instantly_password = data.PW

chrome_options = webdriver.ChromeOptions()
#  chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--window-size=1920,1080")  # Approximate a maximized window size

driver = webdriver.Chrome(options=chrome_options)
## driver.maximize_window()

driver.get("https://app.instantly.ai/auth/login", wait_load=True)



my_email = driver.find_element(By.CSS_SELECTOR, "input[type=\"email\"]")
my_email.write(instantly_login[0])

my_password = driver.find_element(By.CSS_SELECTOR, "input[type=\"password\"]")
my_password.write(instantly_password[0])

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type=\"submit\"]"))).click()

while(True):
    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="simplebar-scroll-node"]/div/div/div[1]/div[2]/div/button[2]'))).click()
        break
    except:
        pass


WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,  ' //*[@id="__next"]/div[2]/div/div/div/div[1]'))).click()

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,  '//*[@id="__next"]/div[2]/div/div[4]/button'))).click()

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,  '//*[@id="__next"]/div[2]/div/div[3]/div[1]/button'))).click()

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,  '//*[@id="__next"]/div[2]/div/div[3]/div/div/button'))).click()

driver.switch_to.window(driver.window_handles[0])
sleep(3)
email_input = driver.find_element(By.CSS_SELECTOR, "input[type=\"email\"]", timeout=10)
email_input.write(email_list[0])

next_button = driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button', timeout=10)
next_button.click()

sleep(3)
password_input = driver.find_element(By.CSS_SELECTOR, "input[type=\"password\"]", timeout=10)
password_input.write(password_list[0])

next_button = driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button', timeout=10)
next_button.click()
sleep(4)

try:
    understand_button = driver.find_element(By.XPATH, '//*[@id="confirm"]')
    understand_button.click()
except:
    sleep(1)
    try:
        understand_button = driver.find_element(By.XPATH, '//*[@id="confirm"]')
        understand_button.click()
    except:
        pass

sleep(3)
try:
    continue_button = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/div[2]/div/div/div[2]/div/div/button', timeout=2)
    continue_button.click()
except:
    continue_button = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[3]/div/div/div[2]/div/div/button', timeout=10)
    continue_button.click()

sleep(2)

allow_button = driver.find_element(By.XPATH, '//*[@id="submit_approve_access"]/div/button', timeout=10)
allow_button.click()

sleep(3)
driver.quit()
connected = True
print("CONNECTING - SUCCESSFUL - " + email_list[0])