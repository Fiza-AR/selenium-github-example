from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Navigate to Login Page
    driver.get("https://the-internet.herokuapp.com/login")
    time.sleep(2)  # Allow page to load

    # Find Elements
    username = driver.find_element(By.ID, "username")
    password = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

    # Input Incorrect Credentials
    username.send_keys("wronguser")
    password.send_keys("wrongpass")
    login_button.click()
    time.sleep(2)  # Wait for error message

    # Validate Error Message
    error_message = driver.find_element(By.ID, "flash").text

    if "Your username is invalid!" in error_message:
        print("[X] Login failed as expected with invalid credentials.")
    else:
        print("[!] Unexpected behavior: Login did not fail as expected.")

finally:
    # Close browser
    driver.quit()
