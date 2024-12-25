from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
from selenium.webdriver import ActionChains
from time import sleep
import time
import quickstart
import pandas as pd

CSV_FILE_NAME = "Sample Instantly.csv"

data= pd.read_csv(CSV_FILE_NAME)
# print(data)

file_path = "login.txt"  # Replace with the actual path to your text file

with open(file_path, 'r') as file:
    # Read the contents of the file
    contents = file.read()

# Find the email and password using string manipulation
email_start = contents.find('email="') + len('email="')
email_end = contents.find('"', email_start)
EMAIL_ADDRESS = contents[email_start:email_end]

password_start = contents.find('password="') + len('password="')
password_end = contents.find('"', password_start)
PASSWORD = contents[password_start:password_end]

# Print the email and password
print("Email:", EMAIL_ADDRESS)
print("Password:", PASSWORD)

# quickstart.main()
# count = quickstart.getColumnCount()
# email_list = quickstart.getEmailList()
# password_list = quickstart.getPasswordList()
# print(count)
count = len(data)
email_list = data.Email
password_list = data.Password
# print(email_list[0])
# print(password_list[0])


index = 0
while index < count:
    try:
        driver = webdriver.Chrome()
        driver.maximize_window()

        driver.get("https://app.instantly.ai/auth/login")

        ssl_verified = False  # Flag to track SSL verification status

        # EMAIL_ADDRESS = "cs@spitzsolutions.com"
        # PASSWORD = "^zRM8AFvhL@gRYG&"

        my_email = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type=\"email\"]")))
        my_email.send_keys(EMAIL_ADDRESS)

        my_password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type=\"password\"]")))
        my_password.send_keys(PASSWORD)

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type=\"submit\"]"))).click()

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class=\"MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButtonBase-root css-kjttz\"]"))).click()
        sleep(3)
        # WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class=\"jss29\"]")))
        try:
            WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div/div/div[2]/div[2]/h6'))).click()
        except:
            WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div/div/div[2]/div/div[2]/h6'))).click()
        sleep(3)

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class=\"MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButtonBase-root  css-d8wzva\"]"))).click()

        driver.switch_to.window(driver.window_handles[1])

        email_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type=\"email\"]")))
        email_element.send_keys(email_list[index])
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type=\"submit\"]"))).click()

        password_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type=\"password\"]")))
        password_element.send_keys(password_list[index])
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type=\"submit\"]"))).click()
        sleep(1.5)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type=\"submit\"]"))).click()

        sleep(1.5)



        ### Additional Script to finalize the Configuration.--- IMPORTANT SHIFT


        driver.quit()

        driver = webdriver.Chrome()
        driver.maximize_window()

        driver.get("https://app.instantly.ai/auth/login")

        my_email = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type=\"email\"]")))
        my_email.send_keys(EMAIL_ADDRESS)

        my_password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type=\"password\"]")))
        my_password.send_keys(PASSWORD)

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type=\"submit\"]"))).click()

        #find search field
        search_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[class=\"MuiInputBase-input MuiInput-input\"]")))
        print("Found the email")
        search_field.send_keys(email_list[index])

        # click email account
        found_account =  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="simplebar-scroll-node"]/div/div/div[2]/div/div[2]'))).click()

        sleep(1)

        #click settings
        settings_found = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="account_details_filter"]/div/div/ul/li[2]/a'))).click()

        # Sending Limit
        variable = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="account_details_main"]/div/div[5]/div[1]/div/input')))
        variable.send_keys(Keys.BACKSPACE)
        variable.send_keys(Keys.BACKSPACE)
        variable.send_keys("200")
        sleep(1)

        # Wait_Time
        variable = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="account_details_main"]/div/div[5]/div[2]/div/input')))
        variable.send_keys(Keys.BACKSPACE)
        variable.send_keys("5")
        sleep(1)

        # Increase Per Day
        variable = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="account_details_main"]/div/div[10]/div[1]/div/div/input')))
        variable.send_keys(Keys.BACKSPACE)
        variable.send_keys("4")
        sleep(1)

        # Click Show advanced settings
        variable = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="account_details_main"]/div/div[11]/button'))).click()
        sleep(1)

        # Warm Custom Domain
        variable = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="account_details_main"]/div/div[12]/div[2]/div[1]/div[3]/div[2]/div/button[2]')))
        driver.execute_script("arguments[0].scrollIntoView();", variable)
        variable.click()
        sleep(2)

        # Click Custom Domain Tracking Enabled
        variable = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="account_details_main"]/div/div[7]/div/div[1]/span')))
        driver.execute_script("arguments[0].scrollIntoView();", variable)
        variable.click()
        print("Clicked custom domain tracking enabled - biatch.")
        sleep(2)

        # Click Custom Domain Tracking Enabled
        variable = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="account_details_main"]/div/div[7]/div/div[2]/input')))
        domain = "inst." + email_list[index].split('@')[1]
        print(domain)
        variable.send_keys(domain)

        # Click Custom Domain Tracking Enabled
        variable = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="account_details_main"]/div/div[7]/div/div[2]/button/span[1]'))).click()

        sleep(10)

        ## Checking if SSL verified
        ssl_verified = False  # Flag to track SSL verification status
        start_time = time.time()  # Record the start time

        while not ssl_verified and time.time() - start_time < 15:
            # Attempt to find the SSL Verified text
            try:
                ssl_element = WebDriverWait(driver, 2).until(
                    EC.presence_of_element_located((By.XPATH, "//small[text()='SSL Verified']"))
                )
                ssl_verified = True  # SSL Verified found, break the loop
            except TimeoutException:
                # If not found, sleep for a short time and then retry until 15 seconds are up
                time.sleep(1)

        if not ssl_verified:
            # If SSL Verified wasn't found in 15 seconds, print a message and start over
            print(f"SSL Verification not found for {email_list[index]} within 15 seconds.")
            driver.quit()  # Close the browser
            continue  # Continue the loop, which will retry for the same index

        # ... (rest of your code that should execute after SSL verification) ...

        print("SSL VERIFIED!!")

        ## SAVE THE SETTINGS
        variable = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'btn-primary') and text()='Save']")))
        print("Save button found")
        variable.click()

        ## Switch to Warmup
        variable = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="account_details_filter"]/div/div/ul/li[1]/a')))
        driver.execute_script("arguments[0].scrollIntoView();", variable)
        variable.click()
        sleep(1)

        ## Click Warmup
        variable = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="account_details_main"]/div/div/button[2]')))
        variable.click()

        print("Warmup Enabled")

        sleep(3)

    except Exception as error:
        print(f"An error occurred: {error}")
    finally:
        if ssl_verified:
            # Only increment index if SSL was verified
            index += 1
        driver.quit()  # Ensure the driver is closed in case of an error or successful completion
