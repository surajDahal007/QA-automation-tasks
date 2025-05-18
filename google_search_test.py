from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# for full screen 
driver.maximize_window()

# visit the URL
driver.get('https://www.google.com')

# find search box by name 
search_box = driver.find_element(By.NAME, "q")

# type selenium automation in search box
search_box.send_keys("Selenium Automation")

# submit search form
search_box.submit()

time.sleep(5)

print(driver.title)

driver.quit()