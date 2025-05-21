import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://www.wikipedia.org")

# search and submit 
search_box = driver.find_element(By.ID, 'searchInput')
search_box.send_keys("Python (programming language)")
search_box.submit()

time.sleep(4)

# find 2nd paragraph from the main div - it contains the first paragraph
paragraph = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/p[2]')

# print(driver.title)
print(paragraph.text)

driver.quit()
