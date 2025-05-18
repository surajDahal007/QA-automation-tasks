from selenium import webdriver
import time

# Open chrome
driver = webdriver.Chrome()

# visit website
driver.get('https://www.facebook.com')

# print title
print(driver.title)

# close chrome
time.sleep(5)
driver.quit()