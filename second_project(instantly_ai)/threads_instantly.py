from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from concurrent.futures import ThreadPoolExecutor
from time import sleep

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

def concurrent_run_bots(brower_count, email_list_array, password_list_array):
    print(brower_count)
    print(len(email_list_array))
    print(len(password_list_array))
    # Set the number of browsers you want to start
    num_browsers = brower_count

    def perform_task(email_list, password_list):
        print(email_list, password_list)
        # browser.get('https://app.smartlead.ai/')
        index = 0
        while(index < len(email_list)):
            try:
                chrome_options = webdriver.ChromeOptions()
                # chrome_options.add_argument("--headless")  # Run in headless mode
                chrome_options.add_argument("--window-size=1920,1080")  # Approximate a maximized window size
                driver = webdriver.Chrome(options=chrome_options)
                # driver.maximize_window()
                driver.get("https://app.instantly.ai/auth/login")

                # EMAIL_ADDRESS = "cs@spitzsolutions.com"
                # PASSWORD = "^zRM8AFvhL@gRYG&"

                my_email = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type=\"email\"]")))
                my_email.send_keys(EMAIL_ADDRESS)

                my_password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type=\"password\"]")))
                my_password.send_keys(PASSWORD)

                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type=\"submit\"]"))).click()

                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class=\"MuiButtonBase-root MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium css-kjttz\"]"))).click()
                sleep(3)
                # WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class=\"jss29\"]")))
                try:
                    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div[2]/div/div/div/div[2]/div[2]/h6'))).click()
                except:
                    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div/div/div[2]/div/div[2]/h6'))).click()
                sleep(3)

                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div[2]/div/div[4]/div/button'))).click()

                driver.switch_to.window(driver.window_handles[1])

                email_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type=\"email\"]")))
                email_element.send_keys(email_list[index])
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type=\"submit\"]"))).click()

                password_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type=\"password\"]")))
                password_element.send_keys(password_list[index])

                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type=\"submit\"]"))).click()
                sleep(1.5)
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type=\"submit\"]"))).click()

                sleep(3)
                driver.quit()


            except:
                try:
                    driver.quit()
                except:
                    pass
            index += 1



    # Create a thread pool executor with the number of desired workers
    with ThreadPoolExecutor(max_workers=num_browsers) as executor:
        # Submit the tasks to the executor
        executor.map(perform_task, email_list_array, password_list_array)



# concurrent_run_bots(2, [["aaa", "sdfdf"], "sss", "sdfwer"], ["dfger", "werwe", "fdgdfgert"])