import threading
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
from selenium.webdriver.chrome.options import Options
from time import sleep
import time
import pandas as pd


CSV_FILE_NAME = "data.csv"

data= pd.read_csv(CSV_FILE_NAME)

count = len(data)
email_list = data.Email
password_list = data.Password
instantly_login = data.Instantly
instantly_password = data.PW

def process_row(index,ssl_verified,warmup_enabled,connected):

    chrome_options = Options()
    #  chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--window-size=1920,1080")  # Approximate a maximized window size

    if not connected:
        try:
            print("CONNECTING - START - " + email_list[index])
            driver = webdriver.Chrome(options=chrome_options)
            ## driver.maximize_window()

            driver.get("https://app.instantly.ai/auth/login")



            # EMAIL_ADDRESS = "cs@spitzsolutions.com"
            # PASSWORD = "^zRM8AFvhL@gRYG&"

            my_email = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type=\"email\"]")))
            my_email.send_keys(instantly_login[index])

            my_password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type=\"password\"]")))
            my_password.send_keys(instantly_password[index])

            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type=\"submit\"]"))).click()
            sleep(10000)

            # Add new email button
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="simplebar-scroll-node"]/div/div/div[1]/div[2]/div/button[2]'))).click()
            sleep(3)
            # WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class=\"jss29\"]")))


            try:
                WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div[2]/div/div/div/div[2]/div[2]/p'))).click()
            except:
                WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div[2]/div/div/div/div[2]/div[2]/p'))).click()
            sleep(3)

            
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,  ' //*[@id="__next"]/div[2]/div/div[4]/div/button'))).click()

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
            connected = True
            print("CONNECTING - SUCCESSFUL - " + email_list[index])
            return ssl_verified, warmup_enabled, connected


        except Exception as error:
            print("CONNECTION - FAL & RETRY - " + email_list[index])
            connected = False
            return ssl_verified, warmup_enabled, connected

    # if not ssl_verified:
    #     try:
    #         print("CONFIGURING - START - " + email_list[index])
    #         driver = webdriver.Chrome(options=chrome_options)
    #         ##driver.maximize_window()

    #         driver.get("https://app.instantly.ai/auth/login")

    #         my_email = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type=\"email\"]")))
    #         my_email.send_keys(instantly_login[index])

    #         my_password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type=\"password\"]")))
    #         my_password.send_keys(instantly_password[index])

    #         WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type=\"submit\"]"))).click()

    #         #find search field
    #         search_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[class=\"MuiInputBase-input MuiInput-input\"]")))

    #         search_field.send_keys(email_list[index])
    #         sleep(2)
    #         search_field.send_keys(Keys.BACKSPACE)
    #         sleep(2)

    #         # click email account
    #         found_account =  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="simplebar-scroll-node"]/div/div/div[2]/div/div[2]'))).click()

    #         sleep(1)

    #         #click settings
    #         settings_found = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="account_details_filter"]/div/div/ul/li[2]/a'))).click()

    #         # Sending Limit
    #         variable = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="account_details_main"]/div/div[5]/div[1]/div/input')))
    #         variable.send_keys(Keys.BACKSPACE)
    #         variable.send_keys(Keys.BACKSPACE)
    #         variable.send_keys("200")
    #         sleep(1)

    #         # Wait_Time
    #         variable = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="account_details_main"]/div/div[5]/div[2]/div/input')))
    #         variable.send_keys(Keys.BACKSPACE)
    #         variable.send_keys("5")
    #         sleep(1)

    #         # Increase Per Day
    #         variable = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="account_details_main"]/div/div[10]/div[1]/div/div/input')))
    #         variable.send_keys(Keys.BACKSPACE)
    #         variable.send_keys("4")
    #         sleep(1)

    #         # Click Show advanced settings
    #         variable = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="account_details_main"]/div/div[11]/button'))).click()
    #         sleep(1)

    #         # Warm Custom Domain
    #         variable = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="account_details_main"]/div/div[12]/div[2]/div[1]/div[3]/div[2]/div/button[2]')))
    #         driver.execute_script("arguments[0].scrollIntoView();", variable)
    #         variable.click()
    #         sleep(2)

    #         # Click Custom Domain Tracking Enabled
    #         variable = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="account_details_main"]/div/div[7]/div/div[1]/span')))
    #         driver.execute_script("arguments[0].scrollIntoView();", variable)
    #         variable.click()

    #         sleep(2)

    #         # Click Custom Domain Tracking Enabled
    #         variable = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="account_details_main"]/div/div[7]/div/div[2]/input')))
    #         domain = "inst." + email_list[index].split('@')[1]
    #         variable.send_keys(domain)

    #         # Click Custom Domain Tracking Enabled
    #         variable = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="account_details_main"]/div/div[7]/div/div[2]/button/span[1]'))).click()

    #         sleep(10)

    #         ## Checking if SSL verified
    #         start_time = time.time()  # Record the start time

    #         while not ssl_verified and time.time() - start_time < 15:
    #             # Attempt to find the SSL Verified text
    #             try:
    #                 ssl_element = WebDriverWait(driver, 2).until(
    #                     EC.presence_of_element_located((By.XPATH, "//small[text()='SSL Verified']"))
    #                 )

    #                 ## SAVE THE SETTINGS
    #                 variable = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'btn-primary') and text()='Save']")))
    #                 print("CONFIGURING - SUCCESSFUL - " + email_list[index])
    #                 variable.click()

    #                 sleep(3)

    #                 driver.quit()

    #                 ssl_verified = True  # SSL Verified found, break the loop

    #                 return ssl_verified, warmup_enabled, connected

    #             except TimeoutException:
    #                 # If not found, sleep for a short time and then retry until 15 seconds are up
    #                 time.sleep(1)

    #         if not ssl_verified:
    #             # If SSL Verified wasn't found in 15 seconds, print a message and start over
    #             print(f"SSL Verification not found for {email_list[index]} within 15 seconds.")
    #             driver.quit()  # Close the browser
    #             ssl_verified = False
    #             return ssl_verified, warmup_enabled, connected


    #     except Exception as error:
    #         print("CONFIGURING - FAILED & RETRYING - " + email_list[index])
    #         ssl_verified = False
    #         return ssl_verified, warmup_enabled, connected
    #         # ... (rest of your code that should execute after SSL verification) ...

    # if not warmup_enabled:
    #     try:
    #         print("WARMUP - START - " + email_list[index])
    #         driver = webdriver.Chrome(options=chrome_options)
    #         ##driver.maximize_window()

    #         driver.get("https://app.instantly.ai/auth/login")

    #         my_email = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type=\"email\"]")))
    #         my_email.send_keys(instantly_login[index])

    #         my_password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type=\"password\"]")))
    #         my_password.send_keys(instantly_password[index])

    #         WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type=\"submit\"]"))).click()

    #         #find search field
    #         search_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[class=\"MuiInputBase-input MuiInput-input\"]")))
    #         search_field.send_keys(email_list[index])
    #         sleep(2)
    #         search_field.send_keys(Keys.BACKSPACE)
    #         sleep(2)


    #         ## click the warmup
    #         variable =  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="simplebar-scroll-node"]/div/div/div[2]/div/div[2]/div/div[4]/div/a[1]')))

    #         sleep(2)
    #         variable.click()

    #         sleep(5)

    #         try:
    #             element = WebDriverWait(driver, 2).until(
    #                 EC.presence_of_element_located((By.XPATH, "//span[text()='Yes, I understand']/preceding-sibling::input[@type='checkbox']"))
    #             )
    #             element.click()

    #             sleep (2)

    #             element = WebDriverWait(driver, 2).until(
    #                 EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Continue')]"))
    #             )

    #             element.click()

    #             sleep(3)
    #             print("WARMUP - SUCCESSFUL - " + email_list[index])
    #             warmup_enabled = True
    #             return ssl_verified, warmup_enabled, connected
    #         except:
    #             print("WARMUP - SUCCESSFUL - " + email_list[index])
    #             warmup_enabled = True
    #             return ssl_verified, warmup_enabled, connected

    #     except Exception as error:
    #         print("WARMUP - WENT WRONG & RETRYING - " + email_list[index])
    #         warmup_enabled = False
    #         return ssl_verified, warmup_enabled, connected




def thread_worker(start_index, end_index):
    index = start_index
    while index < end_index:
        email = data.Email[index]

        # Initialize the flags outside the loop
        ssl_verified = False
        warmup_enabled = False
        connected = False

        # Retry loop
        # while not (ssl_verified and warmup_enabled and connected):
            # Call process_row and update the flags based on the returned values
            # ssl_verified, warmup_enabled, connected = process_row(index, ssl_verified, warmup_enabled, connected)
        process_row(index, ssl_verified, warmup_enabled, connected)


        # Check the flags after the loop
        if ssl_verified and warmup_enabled and connected:
            print(f"{email} - FULL SETUP COMPLETE")

        # Increment index to move to the next email address
        index += 1





# Number of threads
num_threads = 1

# Determine the number of rows per thread
num_rows = len(data)
rows_per_thread = num_rows // num_threads

# Creating and starting threads
threads = []
for i in range(num_threads):
    start_index = i * rows_per_thread
    end_index = start_index + rows_per_thread
    if i == num_threads - 1:
        end_index = num_rows  # Ensure the last thread covers the remainder
    thread = threading.Thread(target=thread_worker, args=(start_index, end_index))
    threads.append(thread)
    thread.start()

# Waiting for all threads to complete
for thread in threads:
    thread.join()