from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from time import sleep
import time
from selenium.webdriver.common.keys import Keys
import pandas as pd
import threads_smart

NUMBER_OF_THREAD = int(input("Enter number of threads: "))
CSV_FILE_NAME = "smartlead upload.csv"

data= pd.read_csv(CSV_FILE_NAME)
print(data)

emails = data.Email
passwords = data.Password

email_list = []
password_list = []
index = 0
for _ in range(len(emails)):
    email_list.append(emails[index])
    password_list.append(passwords[index])
    index += 1

# NUMBER_OF_THREAD = 1

# Determine the number of rows per thread
num_rows = len(data)
rows_per_thread = num_rows // NUMBER_OF_THREAD

# Creating and starting threads
# threads_smart = []
email_list_array = []   
password_list_array = []
for i in range(NUMBER_OF_THREAD):
    start_index = i * rows_per_thread
    end_index = start_index + rows_per_thread
    if i == NUMBER_OF_THREAD - 1:
        end_index = num_rows  # Ensure the last thread covers the remainder

    # threads_smart.concurrent_run_bots()
    email_list_array.append(email_list[start_index:end_index])
    password_list_array.append(password_list[start_index:end_index])
    
    # thread = threading.Thread(target=thread_worker, args=(start_index, end_index))
    # threads.append(thread)
    # thread.start()
# print(email_list_array)
# print(password_list_array)
threads_smart.concurrent_run_bots(NUMBER_OF_THREAD, email_list_array, password_list_array)

print("Done!")