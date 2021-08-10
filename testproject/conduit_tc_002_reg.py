# Conduit_TC_002_Reg
# Regiszrtáció helyesen és helytelen adatokkal.
# Előfeltételek:
# 1- A gazdagép elérhető
# 2- A gazdagépen  fut a Conduit
# 3- Chrome Verzió: 91.0.4472.77 (Hivatalos verzió) (64 bites)
# 4- OS: Windows 10
# 5- Szükséges a TC_001 teszt sikeres lefutása
# Követelmény: Req.id: R01
import csv
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


# random jelszó
def get_ppass(lowers_count, digits_count, uppers_count):
    lowers = ''.join((random.choice(string.ascii_lowercase) for i in range(lowers_count)))
    digits = ''.join((random.choice(string.digits) for i in range(digits_count)))
    uppers = ''.join((random.choice(string.ascii_uppercase) for i in range(uppers_count)))
    sample_list = list(lowers + digits + uppers)
    random.shuffle(sample_list)
    final_string = ''.join(sample_list)
    return final_string


# random felhasználónév
def get_uname(lowers_count):
    lowers = ''.join((random.choice(string.ascii_lowercase) for i in range(lowers_count)))
    return lowers


# random email cím
def get_email(lowers_count):
    lowers = ''.join((random.choice(string.ascii_lowercase) for i in range(lowers_count)))
    emails = lowers + "" + "@example.com"
    return emails


# elemek kikeresése xpath alapján
def find_and_by_xpath(xpath):
    element = driver.find_element_by_xpath(xpath)
    return element


# Tesztadatok
username_value = ["a", get_uname(8)]
email_value = ["a", get_email(8)]
password_value = ["a", get_ppass(3, 4, 1)]


def registration(username_v, email_v, password_v):
    user_name = find_and_by_xpath('//input[@placeholder="Username"]')
    user_name.send_keys(username_v)
    time.sleep(2)
    u.append(user_name.get_attribute('value'))
    print(user_name.get_attribute('value'))
    email = find_and_by_xpath('//input[@placeholder="Email"]')
    email.send_keys(email_v)
    password = find_and_by_xpath('//input[@placeholder="Password"]')
    password.send_keys(password_v)
    time.sleep(2)
    find_and_by_xpath('//button[@class="btn btn-lg btn-primary pull-xs-right"]').click()
    time.sleep(2)


def alert_button_click():
    alert_button = find_and_by_xpath('//button[@class="swal-button swal-button--confirm"]')
    alert_button.click()
    time.sleep(1)

# Sign up link kikeresése és klikkekése
sign_up = find_and_by_xpath("//a[@href='#/register']")
time.sleep(1)
sign_up.click()
time.sleep(1)

# Input mező megjelenésének ellenőrzése
assert find_and_by_xpath('//input[@placeholder="Username"]').is_displayed()
assert find_and_by_xpath('//input[@placeholder="Email"]').is_displayed()
assert find_and_by_xpath('//input[@placeholder="Password"]').is_displayed()

u = []

# Regisztrációs űrlap kitöltése helytelen tesztadatokkal
registration(username_value[0], email_value[0], password_value[0])

# Ellenőrizzük, a felugró ablak helyességét
assert find_and_by_xpath('//div[@class="swal-title"]').text == "Registration failed!"
assert find_and_by_xpath('//div[@class="swal-text"]').text == "Email must be a valid email."

# Alert gomb megnyomása
alert_button_click()

# Regisztrációs űrlap kitöltése helyes tesztadatokkal
registration(username_value[1], email_value[1], password_value[1])

# Ellenőrizzük, a felugró ablak helyességét
assert find_and_by_xpath('//div[@class="swal-title"]').text == "Welcome!"
assert find_and_by_xpath('//div[@class="swal-text"]').text == "Your registration was successful!"

# Alert gomb megnyomása
alert_button_click()

# Ellenőrizzük a felhasználó megjelenését
username = find_and_by_xpath('//div[@class="container"]/ul/li[4]/a')
assert username.is_displayed()
print(username.text)
assert username.text == u[1]

driver.close()
