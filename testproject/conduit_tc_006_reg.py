# Conduit_TC_006_Reg
# Kijelentkezés
# Előfeltételek:
# 1- A gazdagép elérhető
# 2- A gazdagépen  fut a Conduit
# 3- Chrome Verzió: 91.0.4472.77 (Hivatalos verzió) (64 bites)
# 4- OS: Windows 10
# 5- Bejelentkezett felhasználó: Email: testuser1@example.com Password: Abcd123$
# 6- Szükséges a TC_001 és a TC_002 teszt sikeres lefutása
# Követelmény: Req.id: R03
from selenium import webdriver
import time
import random
import string
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument('--headless')

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get("http://localhost:1667")

sign_in = driver.find_element_by_xpath('//a[@href="#/login"]').click()
email = driver.find_element_by_xpath('//input[@placeholder="Email"]').send_keys("testuser1@example.com")
password = driver.find_element_by_xpath('//input[@placeholder="Password"]').send_keys("Abcd123$")
button = driver.find_element_by_xpath('//button[@class="btn btn-lg btn-primary pull-xs-right"]').click()
time.sleep(2)
test_user1 = driver.find_element_by_xpath('//a[@href="#/@testuser1/"]')
print(test_user1.text, test_user1.is_displayed())

assert test_user1.text == "testuser1"
assert test_user1.is_displayed()
time.sleep(3)
log_out = driver.find_element_by_xpath('//a[@active-class="active"]').click()
time.sleep(2)

nav_items = driver.find_elements_by_xpath('//li[@class="nav-item"]')
# assert nav_items not in driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[4]/a')




# driver.close()
