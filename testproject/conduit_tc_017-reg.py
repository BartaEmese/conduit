# Conduit_TC_017_Reg
# Meglévő blogbejegyzéshez commentelése
# Előfeltételek:
# 1- A gazdagép elérhető
# 2- A gazdagépen  fut a Conduit
# 3- Chrome Verzió: 91.0.4472.77 (Hivatalos verzió) (64 bites)
# 4- OS: Windows 10
# 5- Bejelentkezett felhasználó: Email: testuser1@example.com Password: Abcd123$
# 6- Szükséges a TC_001 és a TC_002 teszt sikeres lefutása
# Követelmény: Req.id: R08

from selenium import webdriver
import time


def navigate_to_page(xpath):
    element = driver.find_element_by_xpath(xpath)
    return element


driver = webdriver.Chrome()

try:
    driver.get("http://localhost:1667")
    # A testuser bejelentkezése
    navigate_to_page('//a[@href="#/login"]').click()
    navigate_to_page('//input[@placeholder="Email"]').send_keys("testuser1@example.com")
    navigate_to_page('//input[@placeholder="Password"]').send_keys("Abcd123$")
    navigate_to_page('//button[@class="btn btn-lg btn-primary pull-xs-right"]').click()
    time.sleep(2)
    # A tesruser1 saját cikkeinek kiválasztása
    navigate_to_page('//*[@id="app"]/nav/div/ul/li[4]/a').click()
    time.sleep(1)
    # Az első cikk kiválasztása és megklikkelése
    article = navigate_to_page('//*[@id="app"]/div/div[2]/div/div/div[2]/div/div/div[1]/a/h1').click()
    time.sleep(2)

    article_text = navigate_to_page('//*[@id="app"]/div/div[1]/div/h1').text
    print(article_text)


    #assert article_text.


finally:
    pass
# driver.close()
