from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Use ChromeDriverManager to auto-manage ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Navigate to website
driver.get("https://the-internet.herokuapp.com/login")

# Example interaction
username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

username.send_keys("tomsmith")
password.send_keys("SuperSecretPassword!")
login_button.click()

# Check for successful login
success_message = driver.find_element(By.ID, "flash").text
if "You logged into a secure area!" in success_message:
    print("Login Successful: You logged into a secure area!")
else:
    print("Login Failed")

# Close browser
driver.quit()
