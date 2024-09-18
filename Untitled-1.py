from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Replace with the path to your ChromeDriver
driver_path =''




# Create a Service object
service = Service(executable_path=driver_path)

# Initialize the browser (Chrome)
driver = webdriver.Chrome(service=service)

# Open Facebook login page
driver.get('https://www.facebook.com/')

# Allow the page to load
time.sleep(3)

# Locate the username and password fields
username_field = driver.find_element(By.ID, "email")
password_field = driver.find_element(By.ID, "pass")

# Input credentials
username_field.send_keys('email')
password_field.send_keys('pass')

# Locate and click the login button
login_button = driver.find_element(By.NAME, "login")
login_button.click()

# Wait for the page to load after login
time.sleep(5)

# Print the title of the current page to confirm login
print("Logged in! Current page title is:", driver.title)

# Close the browser
driver.quit()
