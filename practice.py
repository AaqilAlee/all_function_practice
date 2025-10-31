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
time.sleep(2)

# select author
username = driver.find_element(By.ID, "name")
username.send_keys("mamun")

user_mail = driver.find_element(By.ID, "email")
user_mail.send_keys("mytestautomation@gmail.com")

#<-------- search item Start------->

search_item = driver.find_element(By.ID, "Wikipedia1_wikipedia-search-input")
search_item.send_keys("book")

search_button = driver.find_element(By.XPATH, "//input[@class='wikipedia-search-button']")
search_button.click()

#<-------- search item End------->

phone_number = driver.find_element(By.ID, "phone")
phone_number.send_keys("0123456789")

address = driver.find_element(By.ID, "textarea")
address.send_keys("Mirpur 10")


#<-------- dynamic button start------->

button_start = driver.find_element(By.NAME, "start")
button_start.click()
time.sleep(2)
button_stop = driver.find_element(By.NAME, "stop")
button_stop.click()

#<-------- dynamic button start------->

#<-------- gender ------->
gender = driver.find_element(By.ID, "male")
gender.click()

#<-------- Alerts & Popups ------->
# simple_alert = driver.find_element(By.ID, "alertBtn")
# simple_alert.click()

#<-------- select checkbox ------->


#<-------- select country part ------->

select_element = driver.find_element(By.ID, "country")
dropdown = Select(select_element)
dropdown.select_by_visible_text("Canada")
time.sleep(2)

#<-------- select country part end ------->

#<-------- select colors part ------->

select_element = driver.find_element(By.ID, "colors")
dropdown = Select(select_element)
dropdown.select_by_visible_text("Green")


#<-------- select animal part ------->
select_element = driver.find_element(By.ID, "animals")
dropdown = Select(select_element)
dropdown.select_by_visible_text("Cheetah")


#<-------- Locate the date picker 1 ------->
date_field = driver.find_element(By.ID, "datepicker")
date_field.click()

date_input = driver.find_element(By.XPATH, "//a[@data-date='1']")
date_input.click()


#<-------- Locate the date picker 2 ------->
date_field2 = driver.find_element(By.ID, "txtDate")
date_field2.click()

date_input2 = driver.find_element(By.XPATH, "//a[@data-date='23']")
date_input2.click()

#<-------- Locate the date picker 2 end ------->

#<-------- mouse over part ------->
element_to_hover = driver.find_element(By.XPATH, "//button[@class='dropbtn' and text()='Point Me']")
actions = ActionChains(driver)
actions.move_to_element(element_to_hover).perform()
time.sleep(5)

#<-------- mouse over part ------->


#<-------- single File upload ------->
file_upload = driver.find_element(By.ID, "singleFileInput")
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", file_upload)
time.sleep(1)
file_upload.send_keys(r"C:\Users\User\Downloads\cv\Mamun_ali.pdf")

#<-------- Multiple File upload ------->
multi_file_upload = driver.find_element(By.ID, "multipleFilesInput")
files_to_upload =[
    r"C:\Users\User\Downloads\cv\Mamun_ali.pdf",
    r"C:\Users\User\Downloads\cv\intern_Mamun_Ali.pdf"
]
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", multi_file_upload)
time.sleep(1)
multi_file_upload.send_keys("\n".join(files_to_upload))

#<-------- drag and drop part ------->
drag_source = driver.find_element(By.ID, "draggable")
drop_target = driver.find_element(By.ID, "droppable")

# Perform drag and drop action
actions = ActionChains(driver)
actions.drag_and_drop(drag_source, drop_target).perform()

# Wait to see the result
time.sleep(3)

time.sleep(5)
driver.quit()