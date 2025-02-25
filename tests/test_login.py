from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Correct ChromeDriver path
service = Service(r"C:\Users\hafizah\selenium-github-example\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service)

try:
    # Navigate to website
    driver.get("https://the-internet.herokuapp.com/login")

    # Wait for elements to load
    wait = WebDriverWait(driver, 10)

    # Example interaction
    username = wait.until(EC.presence_of_element_located((By.ID, "username")))
    password = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

    # Input credentials
    username.send_keys("tomsmith")
    password.send_keys("SuperSecretPassword!")
    login_button.click()

    # Validate login success
    success_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".flash.success")))
    print("Login Successful:", success_message.text)

except Exception as e:
    print("Test failed:", e)

finally:
    # Close browser
    driver.quit()
