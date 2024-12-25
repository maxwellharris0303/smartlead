import pycountry
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from time import sleep
from selenium.webdriver.common.keys import Keys

from bs4 import BeautifulSoup
import re

country_names = []
for country in pycountry.countries:
    print(country)
    country_names.append(country.name)

# print(country_names)
print(len(country_names))
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless=new')
chrome_options.add_argument("user-data-dir=C:/Profile")
chrome_options.add_argument('--profile-directory=profile')  # Replace with the actual Chrome profile directory
# chrome_options.add_argument('--load-extension=pgojnojmmhpofjgdmaebadhbocahppod.crx')
# chrome_options.add_extension('pgojnojmmhpofjgdmaebadhbocahppod.crx')

# driver = webdriver.Chrome(options=chrome_options)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.google.com/search?q=site%3Ainstagram.com+%22musician%22+%22Cook+Islands%22+%22%40hotmail.com%22&newwindow=1&cs=0&sca_esv=21105454922e231e&biw=1920&bih=953&sxsrf=ACQVn0__kFZDPtTur_aIiLznVbEOIfFJaQ%3A1710336842379&ei=SqvxZe_cFvzVwPAPrsKtgAY&ved=0ahUKEwjvqb6frfGEAxX8KhAIHS5hC2AQ4dUDCBA&uact=5&oq=site%3Ainstagram.com+%22musician%22+%22Cook+Islands%22+%22%40hotmail.com%22&gs_lp=Egxnd3Mtd2l6LXNlcnAiO3NpdGU6aW5zdGFncmFtLmNvbSAibXVzaWNpYW4iICJDb29rIElzbGFuZHMiICJAaG90bWFpbC5jb20iSJUSUL4KWOQPcAJ4AJABAJgBJqAB1gGqAQE3uAEDyAEA-AEBmAIAoAIAmAMAiAYBkgcAoAe7Ag&sclient=gws-wiz-serp#ip=1")

try:
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[id=\"L2AGLb\"]"))).click()
except:
    pass


for country in country_names:
    try:
        input_serach_key = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.TAG_NAME, "textarea")))
        input_serach_key.clear()
        input_serach_key.send_keys(f'site:instagram.com "musician" "{country}" "@gmail.com"')
        input_serach_key.send_keys(Keys.RETURN)
        sleep(2)

        def extract_contact_info(html):
            soup = BeautifulSoup(html, 'html.parser')

            email_addresses = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', soup.get_text())

            email_links = soup.find_all(href=re.compile(r'mailto:'))
            href_email = [re.sub(r'mailto:', '', link.get('href')) for link in email_links]

            email_addresses.extend(href_email)
            
            return email_addresses

        initial_scroll_height = 0
        flag = 0
        while(True):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            scroll_height = driver.execute_script("return Math.max(document.body.scrollHeight, document.documentElement.scrollHeight, document.body.offsetHeight, document.documentElement.offsetHeight, document.body.clientHeight, document.documentElement.clientHeight);")
            if initial_scroll_height != scroll_height:
                initial_scroll_height = scroll_height
            else:
                flag += 1
            if flag >= 5:
                break
            initial_scroll_height = scroll_height
            # Output the scroll height
            # print("Scroll Height:", initial_scroll_height)
            try:
                more_button = driver.find_element(By.CSS_SELECTOR, "a[class=\"T7sFge sW9g3e VknLRd\"]")
                more_button.click()
            except:
                pass
            try:
                driver.find_element(By.CSS_SELECTOR, "div[class=\"ClPXac Pqkn2e\"]")
                break
            except:
                pass
            try:
                driver.find_element(By.CSS_SELECTOR, "div[class=\"ClPXac hoUro Pqkn2e\"]")
                break
            except:
                pass
            sleep(1)

        searh_results = driver.find_elements(By.CSS_SELECTOR, "div[class=\"MjjYud\"]")
        # print(len(searh_results))
        try:
            print(searh_results[0].text)
        except:
            sleep(20)
            pass

        for result in searh_results:
            print(result.find_element(By.TAG_NAME, "a").get_attribute('href'))
            print(extract_contact_info(result.get_attribute('innerHTML')))

            if len(extract_contact_info(result.get_attribute('innerHTML'))) != 0:
                with open('data.txt', 'a', encoding='utf-8') as file:
                    file.write(result.find_element(By.TAG_NAME, "a").get_attribute('href') + "\t" + extract_contact_info(result.get_attribute('innerHTML'))[0] + "\n")
    except:
        pass