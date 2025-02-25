from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Set up ChromeDriver service
service = Service("C:\Users\hafizah\selenium-github-example\drivers\chromedriver.exe")  # Path to your chromedriver

# Initialize Chrome
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

# Close browser
driver.quit()
