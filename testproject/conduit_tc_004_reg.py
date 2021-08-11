# Conduit_TC_005_Reg
# Bejelentkezés- már létező felhasználó helyes és helytelen adatainak megadásával
# Előfeltételek:
# 1- A gazdagép elérhető
# 2- A gazdagépen  fut a Conduit
# 3- Chrome Verzió: 91.0.4472.77 (Hivatalos verzió) (64 bites)
# 4- OS: Windows 10
# 5- Szükséges a TC_001 és a TC_002 teszt sikeres lefutása
# 6- Teszt adat:
#    username,email,password
#   "" ,"" (üres)
#  testuser1@example.com,Abcd123
#  @example.com,Abcdefg$
#  testuser1@example.com,Abcd123$
# Követelmény: Req.id: R02
from selenium import webdriver
import time
import csv
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument('--headless')

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get("http://localhost:1667")


def find_by_xpath(xpath):
    element = driver.find_element_by_xpath(xpath)
    return element


login = driver.find_element_by_xpath('//a[@href="#/login"]')

with open('register_data.csv', encoding="UTF-8") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    next(csv_reader)
    login.click()

    add_button = driver.find_element_by_xpath('//button[@class="btn btn-lg btn-primary pull-xs-right"]')

    email_value = ["", "testuser1@example", "@example.com", "testuser1@example.com"]

    for row in csv_reader:
        print(row)
        email = find_by_xpath('//input[@placeholder="Email"]')

        email.send_keys(row[0])
        print(email.text)
        password = find_by_xpath('//input[@placeholder="Password"]')
        password.send_keys(row[1])
        time.sleep(2)
        add_button.click()
        time.sleep(2)

        alert_button = driver.find_element_by_xpath('//button[@class="swal-button swal-button--confirm"]')
        if alert_button.is_displayed():
            time.sleep(2)
            alert_title = driver.find_element_by_xpath('//div[@class="swal-title"]')
            alert_text = driver.find_element_by_xpath('//div[@class="swal-text"]')
            if email.text == email_value[0]:
                time.sleep(1)
                assert alert_title.text == "Login failed!"
                assert alert_text.text == "Email field required."
            elif email.text == email_value[1]:
                assert alert_title.text == "Login failed!"
                assert alert_text.text == "Invalid user credentials."
            elif email.text == email_value[2]:
                assert alert_title.text == "Login failed!"
                assert alert_text.text == "Email must be a valid email."
                time.sleep(2)
            alert_button.click()

        else:
           pass



