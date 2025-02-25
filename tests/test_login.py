from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# No specific path needed — the runner knows where chromedriver is
service = Service()  
driver = webdriver.Chrome(service=service)

driver.get("https://the-internet.herokuapp.com/login")
print("Opened login page")

driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# Confirm login success
success_message = driver.find_element(By.CSS_SELECTOR, ".flash.success").text
if "You logged into a secure area!" in success_message:
    print("Login successful ✅")
else:
    print("Login failed ❌")

time.sleep(2)  # Just to view before closing
driver.quit()
