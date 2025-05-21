import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

# Visit the URL
driver.get("https://practicetestautomation.com/practice-test-login/")

username_field = driver.find_element(By.ID, 'username')
username_field.send_keys("student")

password_field = driver.find_element(By.ID, 'password')
password_field.send_keys('Password123')

# form = driver.find_element(By.ID, 'form')
# form.submit()

login_button = driver.find_element(By.ID, 'submit')
login_button.click()

print("Test completed \n")

time.sleep(4)

print(driver.title)

driver.quit()