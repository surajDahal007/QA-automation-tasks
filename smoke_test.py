# Smoke testing done in --> https://www.saucedemo.com

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Edge()
driver.maximize_window()

# Visit the URL
driver.get("https://www.saucedemo.com")

# Login
driver.find_element(By.ID, 'user-name').send_keys("standard_user")
driver.find_element(By.ID, 'password').send_keys("secret_sauce")
driver.find_element(By.ID, 'login-button').click()

time.sleep(2)

# Wait for product page to load and add item to cart
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'add-to-cart-sauce-labs-backpack'))
).click()

# Open the cart
driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()

# Wait and click the checkout button
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'checkout'))
).click()

# Fill in checkout form
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'first-name'))
).send_keys('Ram')
driver.find_element(By.ID, 'last-name').send_keys('Dhamal')
driver.find_element(By.ID, 'postal-code').send_keys('44600')

# Continue checkout
driver.find_element(By.ID, 'continue').click()

# Finish checkout
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'finish'))
).click()

# Back to products
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'back-to-products'))
).click()

# Wait and quit
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'inventory_container'))
)

time.sleep(5)

# Logout
driver.find_element(By.ID, 'react-burger-menu-btn').click()
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'logout_sidebar_link'))
).click()

time.sleep(5)

print('Smoke Test successful')

driver.quit()
