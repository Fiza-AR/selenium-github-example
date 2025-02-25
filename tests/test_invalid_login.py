from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Setup
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Navigate to Login Page
driver.get("https://the-internet.herokuapp.com/login")

# Define multiple invalid credentials
invalid_credentials = [
    {"username": "wronguser", "password": "wrongpass"},
    {"username": "", "password": "password"},  # Empty username
    {"username": "tomsmith", "password": ""},  # Empty password
    {"username": "", "password": ""}           # Both fields empty
]

# Loop through each invalid scenario
for creds in invalid_credentials:
    username = driver.find_element(By.ID, "username")
    password = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

    # Clear fields before each attempt
    username.clear()
    password.clear()

    username.send_keys(creds["username"])
    password.send_keys(creds["password"])
    login_button.click()

    # Validate Error Message
    error_message = driver.find_element(By.ID, "flash").text

    # Check for empty password separately
    if creds["password"] == "":
        if "Your password is invalid!" in error_message or "Your username is invalid!" in error_message:
            print(f"[FAILED] Login failed as expected with empty password: {creds}")
        else:
            print(f"[WARNING] Unexpected behavior with empty password: {creds}")
    elif "Your username is invalid!" in error_message:
        print(f"[FAILED] Login failed as expected with: {creds}")
    else:
        print(f"[WARNING] Unexpected behavior with: {creds}")

# Close browser
driver.quit()
