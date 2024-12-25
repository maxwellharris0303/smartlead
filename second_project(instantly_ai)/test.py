from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *

url = "https://www.compass24.nl/helley-hansen-heren-crew-hooded-midlayer-zeiljas-353926/mannen-xxl-blauw"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)