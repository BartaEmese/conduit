# Conduit_TC_011_Reg
# Saját blogbejegyzés szerkesztése (módosítása)
# Előfeltételek:
# 1- A gazdagép elérhető
# 2- A gazdagépen  fut a Conduit
# 3- Chrome Verzió: 91.0.4472.77 (Hivatalos verzió) (64 bites)
# 4- OS: Windows 10
# 5- Bejelentkezett felhasználó: Email: testuser1@example.com Password: Abcd123$
# 6- Szükséges a TC_001 és a TC_002 teszt sikeres lefutása
# Követelmény: Req.id: R07

from selenium import webdriver
import time
import random
import string

driver = webdriver.Chrome()
driver.get("http://localhost:1667")
time.sleep(1)


def get_title(lowers_count):
    lowers = ''.join((random.choice(string.ascii_lowercase) for i in range(lowers_count)))
    titles = "A" + " " + lowers
    return titles


def get_text(lowers_count):
    lowers = ''.join((random.choice(string.ascii_lowercase) for i in range(lowers_count)))
    return lowers


test_list = [get_title(5), get_text(10), get_text(3)]

sign_in = driver.find_element_by_xpath('//a[@href="#/login"]').click()
email = driver.find_element_by_xpath('//input[@placeholder="Email"]').send_keys("testuser1@example.com")
password = driver.find_element_by_xpath('//input[@placeholder="Password"]').send_keys("Abcd123$")
button = driver.find_element_by_xpath('//button[@class="btn btn-lg btn-primary pull-xs-right"]').click()
time.sleep(3)

new_article = driver.find_element_by_xpath('//a[@href="#/editor"]')
new_article.click()
time.sleep(1)
article_title = driver.find_element_by_xpath('//input[@placeholder="Article Title"]')
time.sleep(2)
article_title.send_keys(test_list[0])
about = driver.find_element_by_xpath("//form/fieldset/fieldset[2]/input")
about.send_keys(test_list[0])
text_area = driver.find_element_by_xpath("//textarea")
text_area.send_keys(test_list[1])
tags = driver.find_element_by_xpath('//input[@placeholder="Enter tags"]')
tags.send_keys(test_list[2])
publish_article = driver.find_element_by_xpath("//button").click()
time.sleep(1)

title = driver.find_element_by_xpath("//h1")
text = driver.find_element_by_xpath("//p")
tag = driver.find_element_by_xpath('//a[@class="tag-pill tag-default"]')

assert title.text == test_list[0]
assert text.text == test_list[1]
assert tag.text == test_list[2]

time.sleep(1)
edit_article = driver.find_element_by_xpath('//div[@class="banner"]/div/div/span/a/i').click()
time.sleep(1)
article_title.clear()
article_title.send_keys("Ez az új cím")
submit_button = driver.find_element_by_xpath("//button[@class='btn btn-lg pull-xs-right btn-primary']").click()
time.sleep(2)
article_title2 = driver.find_element_by_xpath('//h1[text()="Ez az új cím"]')
text = "Ez az új cím"
assert article_title2.text == text

delete_button = driver.find_element_by_xpath('//button[@class="btn btn-outline-danger btn-sm"]')
delete_button.click()

articles = driver.find_elements_by_xpath('//div[@class="article-preview"]')

# driver.close()
