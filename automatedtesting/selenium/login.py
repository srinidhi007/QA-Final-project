# #!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def login(driver, username, password):
    print(f"Logging in as '{username}'")
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    WebDriverWait(driver, 10).until(EC.url_to_be("https://www.saucedemo.com/inventory.html"))
    if driver.current_url == "https://www.saucedemo.com/inventory.html":
        print("Login successful")
        return True
    else:
        print("Login failed")
        return False

def add_products_to_cart(driver):
    print("Adding products to cart")
    products = driver.find_elements(By.CSS_SELECTOR, ".inventory_item")
    for product in products:
        product_name = product.find_element(By.CSS_SELECTOR, ".inventory_item_name").text
        print(f"Adding '{product_name}' to cart")
        product.find_element(By.CSS_SELECTOR, "button.btn_primary.btn_inventory").click()

def remove_products_from_cart(driver):
    print("Removing products from cart")
    driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()
    products = driver.find_elements(By.CSS_SELECTOR, ".cart_item")
    for product in products:
        product_name = product.find_element(By.CSS_SELECTOR, ".inventory_item_name").text
        print(f"Removing '{product_name}' from cart")
        product.find_element(By.CSS_SELECTOR, "button.cart_button").click()

# Create the driver with the Chrome WebDriver path
driver = webdriver.Chrome("C:\\Users\\CHIN086\\Downloads\\chromedriver_win32\\chromedriver.exe")

# Execute the test suite
try:
    username = "standard_user"  # Change to desired username
    password = "secret_sauce"   # Change to desired password

    if login(driver, username, password):
        add_products_to_cart(driver)
        remove_products_from_cart(driver)
finally:
    # Quit the driver
    driver.quit()



