import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
My_acc = driver.find_element_by_css_selector("li:nth-child(2)")
My_acc.click()
Email = driver.find_element_by_id('reg_email')
Email.send_keys("1255@123.com")
Password = driver.find_element_by_id('reg_password')
Password.send_keys("Ghbdtnvtldtl")
Register = driver.find_element_by_xpath('//input[@name="register"]')
Register.click()
time.sleep(5)
driver.quit()

################################################################

import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
My_acc = driver.find_element_by_css_selector("li:nth-child(2)")
My_acc.click()
Login = driver.find_element_by_id('username')
Login.send_keys("1255@123.com")
Password = driver.find_element_by_id('password')
Password.send_keys("Ghbdtnvtldtl")
Log = driver.find_element_by_xpath('//input[@name="login"]')
Log.click()
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
Logout = WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element((
By.CSS_SELECTOR, ".woocommerce-MyAccount-navigation-link.woocommerce-MyAccount-navigation-link--customer-logout a"), "Logout"))
driver.quit()