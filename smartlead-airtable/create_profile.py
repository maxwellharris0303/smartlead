from selenium import webdriver
from time import sleep

# Set the path to the directory where you want to create the profile
profile_directory = 'C:/Profile/profile'

# Configure Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--user-data-dir=' + profile_directory)
# chrome_options.add_argument('--headless=new')
# Create a new Chrome driver with the specified options
driver = webdriver.Chrome(options=chrome_options)

# Open any website to initialize the profile
driver.get('https://example.com')
sleep(300)
# At this point, the new profile has been created and initialized.
# You can customize the profile further or use it for your specific needs.
driver.quit()