def test_conduit18():
    # Conduit_TC_018_Reg
    # Adatkezelési nyilatkorat használata
    # Előfeltételek:
    # 1- A gazdagép elérhető
    # 2- A gazdagépen  fut a Conduit
    # 3- Chrome Verzió: 91.0.4472.77 (Hivatalos verzió) (64 bites)
    # 4- OS: Windows 10
    # 5- Szükséges a TC_001 és a TC_002 teszt sikeres lefutása

    from selenium import webdriver
    import time
    import random
    import string

    driver = webdriver.Chrome()
    driver.get("http://localhost:1667")
    time.sleep(2)

    # I decline! és az I accept! gomb elemek megkeresése
    decline = driver.find_element_by_xpath('//div[@class="cookie__bar__buttons"]/button[1]')
    accept = driver.find_element_by_xpath('//div[@class="cookie__bar__buttons"]/button[2]')

    # Ellenőrizzük az elemek megjelenését
    assert decline.is_displayed()
    assert accept.is_displayed()

    # I accept! gomb Megnyomása
    accept.click()
    time.sleep(1)

    # Ellenőrizzük, hogy az elemek már nem láthatók
    cookie_buttons = driver.find_elements_by_xpath('//div[@class="cookie__bar__buttons"]')
    assert len(cookie_buttons) == 0

    # Újra betöltjük az oldalt és ellenőrizzük, hohy az elemek már nem láthatók
    driver.get("http://localhost:1667")
    time.sleep(2)
    cookie_buttons = driver.find_elements_by_xpath('//div[@class="cookie__bar__buttons"]')
    assert len(cookie_buttons) == 0

    driver.close()
