from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

print("="*50)
print("SEARCH AUTOMATION")
print("="*50)

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.wikipedia.org")

time.sleep(2)
search_box = driver.find_element(By.ID,"searchInput")

search_box.send_keys("Artificial Intelligence")
time.sleep(2)

search_box.send_keys(Keys.ENTER)
print(driver.title)

if "Artificial intelligence" in driver.title:
    print("SEARCH SUCCESSFUL")
else:
    print("SEARCH FAILED")

time.sleep(3)
input("Press Enter to close")
driver.quit()
