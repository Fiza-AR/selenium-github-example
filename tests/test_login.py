from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# Path to ChromeDriver (update this if your path is different)
chrome_driver_path = "C:\\Users\\hafizah\\selenium-github-example\\drivers\\chromedriver.exe"

# ✅ Initialize Chrome WebDriver
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

# ✅ Open the login page
driver.get("https://the-internet.herokuapp.com/login")
print("Opened login page")

# ✅ Maximize browser window
driver.maximize_window()

# ✅ Locate and fill in the username
username_input = driver.find_element(By.ID, "username")
username_input.send_keys("tomsmith")  # Valid username

# ✅ Locate and fill in the password
password_input = driver.find_element(By.ID, "password")
password_input.send_keys("SuperSecretPassword!")  # Valid password

# ✅ Click the login button
login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_button.click()

# ✅ Wait for the page to load
time.sleep(2)

# ✅ Check for successful login message
success_message = driver.find_element(By.CSS_SELECTOR, ".flash.success")
if "You logged into a secure area!" in success_message.text:
    print("Login successful ✅")
else:
    print("Login failed ❌")

# ✅ Close the browser
driver.quit()
