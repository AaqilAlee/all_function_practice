import imaplib, email, re, time

import select
import wait
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.action_chains import ActionChains


# --- Start browser ---
service = Service(r"F:\drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()

# select author
username = driver.find_element(By.ID, "name")
username.send_keys("mamun")

user_mail = driver.find_element(By.ID, "email")
user_mail.send_keys("mytestautomation@gmail.com")

phone_number = driver.find_element(By.ID, "phone")
phone_number.send_keys("0123456789")

address = driver.find_element(By.ID, "textarea")
address.send_keys("Mirpur 10")

gender = driver.find_element(By.ID, "male")
gender.click()

# select checkbox
days = ["sunday", "monday"]  # days to select
all_days = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]

for day in all_days:
    checkbox = driver.find_element(By.ID, day)
    if day in days:
        if not checkbox.is_selected():
            checkbox.click()
    else:
        if checkbox.is_selected():
            checkbox.click()

# select country
select_element = driver.find_element(By.ID, "country")
# Create a Select object
dropdown = Select(select_element)

# Select Canada by visible text
dropdown.select_by_visible_text("Canada")

# Pause to see the result
time.sleep(2)

# Optional: verify which option is selected
selected = dropdown.first_selected_option.text
print("Selected country:", selected)



#<-------- select colors ------->
select_element = driver.find_element(By.ID, "colors")

# Create a Select object
dropdown = Select(select_element)

# Select "Green" by visible text
dropdown.select_by_visible_text("Green")

# Optional: Verify which options are selected
selected = [opt.text for opt in dropdown.all_selected_options]
print("Selected colors:", selected)

#<-------- select animal ------->
select_element = driver.find_element(By.ID, "animals")

# Create a Select object
dropdown = Select(select_element)

# Select "Green" by visible text
dropdown.select_by_visible_text("Cheetah")

# Optional: Verify which options are selected
selected = [opt.text for opt in dropdown.all_selected_options]
print("Selected colors:", selected)


# Scroll into view
# driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", next_page)
# Optional: hover over the element before clicking
# actions = ActionChains(driver)
# actions.move_to_element(next_page).perform()
# next_page.click()


# name of area
# select_area = wait.until(
#     EC.presence_of_element_located(
#         (By.NAME, "billing_area")
#     )
# )
# # select_element.click()
# dropdown = Select(select_area)
# dropdown.select_by_value("221")


# delivery checkbox
# delivery_checkbox = wait.until(
#     EC.presence_of_element_located(
#         (By.XPATH, "//input[@id='gift_paper']")
#     )
# )
# delivery_checkbox.click()


time.sleep(4)
driver.quit()