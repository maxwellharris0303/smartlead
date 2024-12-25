from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from concurrent.futures import ThreadPoolExecutor
from time import sleep

LOGIN_EMAIL = "admin@alphoric.com"
LOGIN_PWD = "%LH3T@VwvzpI"

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
                driver.get("https://app.smartlead.ai/")

                WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[class=\"q-field__native q-placeholder\"]")))

                login_elements = driver.find_elements(By.CSS_SELECTOR, "input[class=\"q-field__native q-placeholder\"]")
                login_elements[0].send_keys(LOGIN_EMAIL)
                login_elements[1].send_keys(LOGIN_PWD)

                WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class=\"q-btn q-btn-item non-selectable no-outline q-btn--unelevated q-btn--rectangle bg-primary text-white q-btn--actionable q-focusable q-hoverable q-btn--no-uppercase full-width\"]"))).click()
                WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[class=\"q-item q-item-type row no-wrap q-item--clickable q-link cursor-pointer q-focusable q-hoverable flex items-center no-wrap app-project-route\"]")))

                # sleep(10000)
                sleep(3)
                email_accounts_element = driver.find_elements(By.CSS_SELECTOR, "a[class=\"q-item q-item-type row no-wrap q-item--clickable q-link cursor-pointer q-focusable q-hoverable flex items-center no-wrap app-project-route inactive\"]")
                print(len(email_accounts_element))
                email_accounts_element[1].click()

                WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class=\"q-btn q-btn-item non-selectable no-outline q-btn--unelevated q-btn--rectangle bg-primary text-white q-btn--actionable q-focusable q-hoverable q-btn--no-uppercase q-ml-md\"]"))).click()

                WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class=\"q-item q-item-type row no-wrap q-item--clickable q-link cursor-pointer q-focusable q-hoverable email-connect-card\"]")))

                select_email_provider = driver.find_elements(By.CSS_SELECTOR, "div[class=\"q-item q-item-type row no-wrap q-item--clickable q-link cursor-pointer q-focusable q-hoverable email-connect-card\"]")[2]
                select_email_provider.click()
                
                while(True):
                    try:
                        email_input = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-report-event=\"Signin_Email_Phone_Skype\"]")))
                        email_input.clear()
                        email_input.send_keys(email_list[index])
                        break
                    except:
                        pass
                    sleep(3)
            
                next_button = driver.find_element(By.CSS_SELECTOR, "input[data-report-event=\"Signin_Submit\"]")
                next_button.click()

                while(True):
                    try:
                        password_input = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type=\"password\"]")))
                        password_input.clear()
                        password_input.send_keys(password_list[index])
                        break
                    except:
                        pass
                    sleep(3)

                next_button = driver.find_element(By.CSS_SELECTOR, "input[data-report-event=\"Signin_Submit\"]")
                next_button.click()

                # new_pwd = random_password_generator.getRandomPassword()

                # current_password_input = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id=\"currentPassword\"]")))
                # new_password_input = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id=\"newPassword\"]")))
                # confirm_password_input = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id=\"confirmNewPassword\"]")))

                # current_password_input.send_keys(password_list[index])
                # new_password_input.send_keys(new_pwd)
                # confirm_password_input.send_keys(new_pwd)

                # next_button = driver.find_element(By.CSS_SELECTOR, "input[type=\"submit\"]")
                # next_button.click()
                sleep(5)
                try:
                    accept_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id=\"idSIButton9\"]")))
                    accept_button.click()
                except:
                    later_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id=\"btnAskLater\"]")))
                    later_button.click()
                    # sleep(3)
                    accept_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id=\"idSIButton9\"]")))
                    accept_button.click()

                sleep(5)

                WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class=\"q-btn q-btn-item non-selectable no-outline q-btn--flat q-btn--rectangle text-primary q-btn--actionable q-focusable q-hoverable\"]"))).click()
                
                sleep(3)
                WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type=\"number\"]")))

                username = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "h4[class=\"email-account-text\"]"))).text
                # print(username)
                correct_username = username.split("(")[0].strip()
                print(correct_username)
                

                input_count = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type=\"number\"]")))

                input_day_elements = driver.find_elements(By.CSS_SELECTOR, "input[class=\"q-field__native q-placeholder\"]")
                
                # driver.execute_script(f'document.querySelectorAll("input.q-field__native.q-placeholder]")[0].value = "{MESSAGE_PER_DAY}";')
                # for _ in range(14):
                #     keyboard.press('tab')
                #     keyboard.release('tab')
                # keyboard.write(MESSAGE_PER_DAY)
                # for _ in range(3):
                #     keyboard.press('tab')
                #     keyboard.release('tab')
                #     keyboard.write(correct_username)
                # keyboard.press('tab')
                # keyboard.release('tab')
                # input_day_elements[0].clear()
                
                # length = len(input_day_elements[0].get_attribute('value'))
                # for i in range(length):
                #     input_count.send_keys(Keys.BACKSPACE)

                # input_day_elements[0].send_keys(MESSAGE_PER_DAY)
                # input_day_elements[1].clear()
                # input_day_elements[1].send_keys(MINIMUM_TIME_GAP)

                # text_area = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[class=\"fr-element fr-view\"]")))
                # driver.execute_script("arguments[0].innerHTML = arguments[1];", text_area, correct_username)
                # text_area.send_keys(Keys.RETURN)
                # text_area.send_keys(Keys.BACKSPACE)

                # sleep(2)

                WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class=\"q-checkbox__bg absolute\"]")))
                # checkbox_elements = driver.find_elements(By.CSS_SELECTOR, "div[class=\"q-checkbox__bg absolute\"]")
                # checkbox_elements[0].click()

                
                # reply_to_address_element = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[class=\"q-field__input q-placeholder col\"]")))
                # reply_to_address_element.send_keys(REPLY_TO_ADDRESS)

                # ind = False
                # while(ind == False):
                #     replyInput = (By.CSS_SELECTOR, "input[class=\"q-field__input q-placeholder col\"]")
                #     reply_to_address_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(replyInput))
                #     try:
                #         reply_to_address_element.click()
                #         reply_to_address_element.clear()
                #         reply_to_address_element.send_keys(REPLY_TO_ADDRESS)
                #         reply_dropdown = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class=\"q-item__section column q-item__section--main justify-center\"]")))
                #         reply_dropdown.click()
                #         ind = True
                #     except:
                #         # If the element becomes stale, re-locate it and try again
                #         try:
                #             reply_to_address_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(replyInput))
                #             reply_to_address_element.click()
                #             reply_to_address_element.clear()
                #             reply_to_address_element.send_keys(REPLY_TO_ADDRESS)
                #             reply_dropdown = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class=\"q-item__section column q-item__section--main justify-center\"]")))
                #             reply_dropdown.click()
                #             ind = True
                #         except: pass

                
                # sleep(2)
                # signature_field_parent = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class=\"fr-element fr-view\"]")))
                # signature_field = signature_field_parent.find_element(By.CSS_SELECTOR, ":first-child")
                
                # driver.execute_script("arguments[0].innerText = arguments[1];", signature_field, correct_username)
                # sleep(3)
                save_button = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[class="q-btn q-btn-item non-selectable no-outline q-btn--unelevated q-btn--rectangle bg-primary text-white q-btn--actionable q-focusable q-hoverable q-btn--no-uppercase"]')))
                # save_button = driver.find_element(By.CSS_SELECTOR, "button[class=\"q-btn q-btn-item non-selectable no-outline q-btn--unelevated q-btn--rectangle bg-primary text-white q-btn--actionable q-focusable q-hoverable q-btn--no-uppercase\"]")
                save_button.click()
                sleep(2)
                # sleep(1000)
                current_url = driver.current_url
                driver.quit()
                sleep(2)
                # test.firefox_run(current_url, correct_username)

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