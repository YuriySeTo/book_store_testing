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
Shop = driver.find_element_by_css_selector("#menu-item-40 a")
Shop.click()
HTML5 = driver.find_element_by_css_selector(".post-181 h3")
HTML5.click()
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
Logout = WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".product_title.entry-title"), "HTML5 Forms"))
driver.quit()

################################################################################

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
Shop = driver.find_element_by_css_selector("#menu-item-40 a")
Shop.click()
HTML = driver.find_element_by_css_selector(".cat-item.cat-item-19 a")
HTML.click()
Count = driver.find_elements_by_class_name('woocommerce-LoopProduct-link')
if len(Count) == 3:
   print("На странице три товара")
else:
   print("Ошибка")
driver.quit()

################################################################################

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
Shop = driver.find_element_by_css_selector("#menu-item-40 a")
Shop.click()
Default = driver.find_element_by_css_selector('[value="menu_order"]')
Default_Ui = Default.get_attribute("selected")
if Default_Ui is not None:
    print("Совпадает")
else:
    print("Ошибка")
from selenium.webdriver.support.select import Select
element = driver.find_element_by_class_name('orderby')
select = Select(element)
select.select_by_visible_text("Sort by price: high to low")
Default_1 = driver.find_element_by_css_selector('[value="price-desc"]')
Default_Ui_1 = Default_1.get_attribute("selected")
if Default_Ui_1 is not None:
    print("Совпадает")
else:
    print("Ошибка")
driver.quit()

################################################################################

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
Shop = driver.find_element_by_css_selector("#menu-item-40 a")
Shop.click()
Android = driver.find_element_by_css_selector(".post-169 h3")
Android.click()
element_600 = driver.find_element_by_css_selector(".price > del > span")
element_600_text = element_600.text
assert element_600_text == "₹600.00"
element_450 = driver.find_element_by_css_selector(".price > ins > span")
element_450_text = element_450.text
assert element_450_text == "₹450.00"
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
Cart = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".attachment-shop_single")))
Cart_1 = driver.find_element_by_class_name('attachment-shop_single').click()
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
Close = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.pp_close")))
Close_1 = driver.find_element_by_class_name('pp_close').click()
driver.quit()

#########################################################################################

import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
Shop = driver.find_element_by_css_selector("#menu-item-40 a")
Shop.click()
HTML = driver.find_element_by_css_selector('a[href="/shop/?add-to-cart=182"]')
HTML.click()
element_1 = driver.find_element_by_class_name("cartcontents")
element_1_text = element_1.text
assert element_1_text == "1item"
element_180 = driver.find_element_by_css_selector(".amount:nth-child(3)")
element_180_text = element_180.text
assert element_180_text == "₹180.00"
SC = driver.find_element_by_class_name('cartcontents')
SC.click()
element_180_1 = driver.find_element_by_css_selector(".cart-subtotal .woocommerce-Price-amount ")
element_180_text_1 = element_180_1.text
assert element_180_text_1 == "₹180.00"
element_183 = driver.find_element_by_css_selector(".order-total .woocommerce-Price-amount")
element_183_text = element_183.text
assert element_183_text == "₹183.60"
driver.quit()

##########################################################################################

import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
Shop = driver.find_element_by_css_selector("#menu-item-40 a")
Shop.click()
driver.execute_script("window.scrollBy(0, 300);")
HTML = driver.find_element_by_css_selector('a[href="/shop/?add-to-cart=182"]')
HTML.click()
time.sleep(3)
JS = driver.find_element_by_css_selector('a[href="/shop/?add-to-cart=180"]')
JS.click()
SC = driver.find_element_by_class_name('cartcontents')
SC.click()
time.sleep(3)
Del = driver.find_element_by_css_selector('a[data-product_id="182"]')
Del.click()
time.sleep(3)
Undo = driver.find_element_by_css_selector('.woocommerce-message > a')
Undo.click()
Quanty_1 = driver.find_element_by_css_selector('[name="cart[045117b0e0a11a242b9765e79cbf113f][qty]"]')
Quanty_1.clear()
Quanty_2 = driver.find_element_by_css_selector('[name="cart[045117b0e0a11a242b9765e79cbf113f][qty]"]')
Quanty_2.send_keys("3")
UPB = driver.find_element_by_css_selector('.actions .button:nth-child(2)')
UPB.click()
element_3 = driver.find_element_by_xpath('//input[@value=3]')
element_3_text = element_3.text
assert element_3_text == "3"
time.sleep(3)
AP = driver.find_element_by_css_selector('.coupon .button')
AP.click()
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
Book_1 = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((
By.CSS_SELECTOR, '.woocommerce-error > li'), "Please enter a coupon code."))
driver.quit()

######################################################################################################

import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
Shop = driver.find_element_by_css_selector("#menu-item-40 a")
Shop.click()
driver.execute_script("window.scrollBy(0, 300);")
HTML = driver.find_element_by_css_selector('a[href="/shop/?add-to-cart=182"]')
HTML.click()
time.sleep(3)
SC = driver.find_element_by_class_name('cartcontents')
SC.click()
PTC = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-button"))).click()
First_Name = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#billing_first_name")))
First_Name.send_keys("Ivan")
Last_Name = driver.find_element_by_id('billing_last_name')
Last_Name.send_keys("Ivanov")
Email = driver.find_element_by_id('billing_email')
Email.send_keys("1@1.co")
Phone = driver.find_element_by_id('billing_phone')
Phone.send_keys("+79001006004")
Country_1 = driver.find_element_by_id('s2id_billing_country')
Country_1.click()
Country_2 = driver.find_element_by_id('s2id_autogen1_search')
Country_2.send_keys("Russia")
Country_3 = driver.find_element_by_class_name('select2-match')
Country_3.click()
Address = driver.find_element_by_id('billing_address_1')
Address.send_keys("Russia")
Town = driver.find_element_by_id('billing_city')
Town.send_keys("UFA")
State = driver.find_element_by_id('billing_state')
State.send_keys("UFANSKIY")
Postcode = driver.find_element_by_id('billing_postcode')
Postcode.send_keys("128500")
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(3)
Check = driver.find_element_by_id('payment_method_cheque')
Check.click()
Check = driver.find_element_by_id('place_order')
Check.click()
TY = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((
By.CSS_SELECTOR, '.woocommerce-thankyou-order-received'), "Thank you. Your order has been received."))
PM = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((
By.CSS_SELECTOR, 'tr:nth-child(3) > td'), "Check Payments"))
driver.quit()