from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# -------------------------------
# Launch Browser
# -------------------------------
driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://demoqa.com/automation-practice-form")

wait = WebDriverWait(driver, 10)

# Wait until page loads
wait.until(EC.visibility_of_element_located((By.ID, "firstName")))

# -------------------------------
# Fill Basic Details
# -------------------------------
driver.find_element(By.ID, "firstName").send_keys("Zubair")
driver.find_element(By.ID, "lastName").send_keys("Siddiqui")
driver.find_element(By.ID, "userEmail").send_keys("zubair@gmail.com")

# Gender
driver.find_element(By.XPATH, "//label[text()='Male']").click()

# Mobile Number
driver.find_element(By.ID, "userNumber").send_keys("9876543210")

# -------------------------------
# Date of Birth
# -------------------------------
driver.find_element(By.ID, "dateOfBirthInput").click()

Select(
    driver.find_element(By.CLASS_NAME, "react-datepicker__month-select")
).select_by_visible_text("August")

Select(
    driver.find_element(By.CLASS_NAME, "react-datepicker__year-select")
).select_by_visible_text("1995")

driver.find_element(
    By.XPATH,
    "//div[contains(@class,'react-datepicker__day') and text()='15']"
).click()

# -------------------------------
# Subjects
# -------------------------------
subject = driver.find_element(By.ID, "subjectsInput")

subject.send_keys("Maths")
subject.send_keys(Keys.ENTER)

# -------------------------------
# Hobbies
# -------------------------------
sports = driver.find_element(
    By.XPATH,
    "//label[text()='Sports']"
)

driver.execute_script(
    "arguments[0].scrollIntoView({block:'center'});",
    sports
)

time.sleep(1)

sports.click()

# -------------------------------
# Picture Upload
# -------------------------------
driver.find_element(
    By.ID,
    "uploadPicture"
).send_keys(
    r"D:\2. Techbees\selenium-rpa\files\profile.jpg"
)

# -------------------------------
# Current Address
# -------------------------------
driver.find_element(By.ID, "currentAddress").send_keys(
    "New Delhi, India"
)

# -------------------------------
# Scroll to Submit Button
# -------------------------------
submit = driver.find_element(By.ID, "submit")

driver.execute_script(
    "arguments[0].scrollIntoView({block:'center'});",
    submit
)

time.sleep(1)

# -------------------------------
# Submit Form
# -------------------------------
submit.click()

# -------------------------------
# Verify Submission
# -------------------------------
title = wait.until(
    EC.visibility_of_element_located(
        (By.ID, "example-modal-sizes-title-lg")
    )
)

print("=" * 50)
print(title.text)
print("=" * 50)

if title.text == "Thanks for submitting the form":
    print("FORM SUBMITTED SUCCESSFULLY")
else:
    print("FORM SUBMISSION FAILED")

input("\nPress Enter to close browser...")

driver.quit()
