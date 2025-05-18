# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()

# driver.maximize_window()

# driver.get("https://www.wikipedia.org")

# search_box = driver.find_element(By.ID, 'searchInput')
# search_box.send_keys("Python (programming language)")
# search_box.submit()

# time.sleep(4)

# paragraph = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/p[1]')

# # print(driver.title)
# print(paragraph.text)

# driver.quit()


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

# 1. Open Wikipedia
driver.get("https://www.wikipedia.org")

# 2. Find the search input and enter text
search_input = driver.find_element(By.ID, "searchInput")
search_input.send_keys("Python (programming language)")
search_input.submit()

# 3. Wait for results to load
time.sleep(3)

# 4. Get the first paragraph
first_para = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/p[2]')
print("First paragraph:\n", first_para.text)

# 5. Close browser
driver.quit()
