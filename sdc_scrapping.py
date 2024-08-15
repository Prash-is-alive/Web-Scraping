from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyperclip
credentials ={
  "email" : "ps94886545@gmail.com",
  "first_name" : "Prashant",
  "last_name" : "Singh",
  "mobile" : "1234567890",
  "course" : "NEET"
}
print(credentials)
import time
driver = webdriver.Chrome()
print("Browsing to the website...")
driver.get("https://sdconline.net")

# signing into the website
# usernameEle = driver.find_element(By.ID, "username")
usernameEle = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
# passwordEle = driver.find_element(By.ID, "password")
passwordEle = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "password"))
    )
usernameEle.clear()
passwordEle.clear()
usernameEle.send_keys("SDCAdmin")
passwordEle.send_keys("sdc151928")
print("logging into the website...")
passwordEle.send_keys(Keys.RETURN)
time.sleep(2)

# Navigate to the new URL
driver.get("https://sdconline.net/wp-admin/user-new.php")
print("browsing to add new user page...")
time.sleep(6)  # Give some time for the page to load

# get all the field elements
print("detecting all the fields...")
emailEle = driver.find_element(By.ID, "email")
first_nameEle = driver.find_element(By.ID, "first_name")
last_nameEle = driver.find_element(By.ID, "last_name")
passEle = driver.find_element(By.ID, "pass1")
mobileNumberEle = driver.find_element(By.ID, "acf-field_5f16d938603a0")
courseDropdownEle = driver.find_element(By.ID, "acf-field_5f16d90b6039f")
branchDropdownEle = driver.find_element(By.ID, "acf-field_600e6e48d2e36")
admissionStatusRadio = driver.find_element(By.ID, "acf-field_60a4c45469ba0-admission")
Course_Duration_From =driver.find_element(By.ID, "acf-field_60a4d396bfebd")
Course_Duration_To =driver.find_element(By.ID, "acf-field_60a4d3ecbfebe")
Add_new_user = driver.find_element(By.ID, "createusersub")

# clear all the values
print("setting default values...")
emailEle.clear()
first_nameEle.clear()
last_nameEle.clear()
passEle.clear()
mobileNumberEle.clear()
courseDropdownEle = Select(courseDropdownEle)
courseDropdownEle.select_by_value(f'XI + HSC + {credentials["course"]}')
branchDropdownEle = Select(branchDropdownEle)
branchDropdownEle.select_by_value("Andheri East")
admissionStatusRadio.click()
Course_Duration_From = Select(Course_Duration_From)
Course_Duration_From.select_by_value("2024")
Course_Duration_To = Select(Course_Duration_To)
Course_Duration_To.select_by_value("2026")


# set the values for all of them:
print("filling information...")
emailEle.send_keys(credentials["email"])
first_nameEle.send_keys(credentials["first_name"])
last_nameEle.send_keys(credentials["last_name"])
passEle.clear() # since the password field again resets to default value
passEle.send_keys("admin123")
mobileNumberEle.send_keys(credentials["mobile"])

Add_new_user.click()
print("creating new user...")
time.sleep(3)
try:
    assert "This username is already registered. Please choose another one" not in driver.page_source
    print("User Created Successfully\n\n")
    print(f'''Suresh Dani's Classes

    Your Portal Has been activated!

    Visit at sdconline.net

    Username: {credentials['email']}
    password: admin123
    ''')
    pyperclip.copy(credentials["mobile"])
    print("Number copied to clipboard!")
except:
    print("user already present")