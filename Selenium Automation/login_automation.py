from selenium import webdriver
from selenium.webdriver.common.by import By
import time

print("=" * 50)
print("LOGIN AUTOMATION")
print("=" * 50)

# Launch Chrome
driver = webdriver.Chrome()
driver.maximize_window()

# Open website
driver.get("https://the-internet.herokuapp.com/login")
print("Website Opened")

username = driver.find_element(By.ID, "username")
time.sleep(2)
password = driver.find_element(By.ID, "password")
time.sleep(2)
login_button = driver.find_element(By.CSS_SELECTOR, "button.radius")
print("Elements Located Successfully")

username.send_keys("tomsmith")
password.send_keys("SuperSecretPassword!")
print("Credentials Entered")
login_button.click()
time.sleep(3)

print("Login Button Clicked")
message = driver.find_element(By.ID, "flash")
print(message.text)

if "You logged into a secure area!" in message.text:
    print("LOGIN SUCCESSFUL")
else:
    print("LOGIN FAILED")

time.sleep(3)
logout = driver.find_element(By.CSS_SELECTOR, "a.button")
logout.click()
print("Logged Out Successfully")

time.sleep(3)
driver.quit()
print("Browser Closed")
