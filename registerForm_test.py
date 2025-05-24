# https://demoqa.com/automation-practice-form
# unfinished Business 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()

# visit the URL
driver.get("https://demoqa.com/automation-practice-form")

# fill details
driver.find_element(By.ID, 'firstName').send_keys('Ram')
driver.find_element(By.ID, 'lastName').send_keys('Ram')
driver.find_element(By.ID, 'userEmail').send_keys('ram@mail.com')

# select gender by label not by ID
driver.find_element(By.XPATH, "//label[text()='Male']").click()

driver.find_element(By.ID, 'userNumber').send_keys('9876543210')

# select date
driver.find_element(By.ID, 'dateOfBirthInput').click()
driver.find_element(By.CLASS_NAME, 'react-datepicker__month-select').send_keys('June')
driver.find_element(By.CLASS_NAME, 'react-datepicker__year-select').send_keys('2004')
driver.find_element(By.XPATH, "//div[text()='27']").click()

# select subjects
subjects = driver.find_element(By.ID, 'subjectsInput')
subjects.send_keys('Computer Science')
subjects.send_keys(Keys.ENTER)

# select Hobbies
driver.find_element(By.XPATH, "//label[text()='Sports']").click()

# Insert Picture part
driver.find_element(By.ID, 'uploadPicture').send_keys(r"C:\Users\USER\Desktop\2.png")

# Other i/p fields
driver.find_element(By.ID, 'currentAddress').send_keys("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s")

# select State and City
state = driver.find_element(By.ID, 'react-select-3-input')
state.send_keys('Haryana')
state.send_keys(Keys.ENTER)

city = driver.find_element(By.ID, 'react-select-4-input')
city.send_keys('Panipat')
city.send_keys(Keys.ENTER)

# submit the form 
driver.find_element(By.ID, 'submit').click()
time.sleep(4)

# take screenshot
driver.save_screenshot('create_account_test.png')

print(driver.title)

# over and out
driver.quit()
