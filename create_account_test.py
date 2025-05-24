# https://demo.guru99.com/test/newtours/register.php
# 'Create an account' automation testing
# By Er. Suraj Dahal

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

# visit the URL
driver.get("https://demo.guru99.com/test/newtours/register.php")

# fill in the form 
driver.find_element(By.NAME, 'firstName').send_keys('Ram')
driver.find_element(By.NAME, 'lastName').send_keys('Dangol')
driver.find_element(By.NAME, 'phone').send_keys('9876543210')
driver.find_element(By.NAME, 'userName').send_keys('ram.dangol@hotmail.com')

driver.find_element(By.NAME, 'address1').send_keys('Ram')
driver.find_element(By.NAME, 'city').send_keys('Ram')
driver.find_element(By.NAME, 'state').send_keys('Ram')
driver.find_element(By.NAME, 'postalCode').send_keys('44601')

# for selecting a country by dropdown
driver.find_element(By.NAME, 'country').send_keys('Nepal')

driver.find_element(By.NAME, 'email').send_keys('ram.dangol@hotmail.com')
driver.find_element(By.NAME, 'password').send_keys('password')
driver.find_element(By.NAME, 'confirmPassword').send_keys('password')

time.sleep(4)
driver.find_element(By.NAME, 'submit').click()

time.sleep(4)

print(driver.title)

driver.quit()
