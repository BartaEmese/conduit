def test_conduit06():
    # Conduit_TC_006_Reg
    # Kijelentkezés
    # Előfeltételek:
    # 1- A gazdagép elérhető
    # 2- A gazdagépen  fut a Conduit
    # 3- Chrome Verzió: 91.0.4472.77 (Hivatalos verzió) (64 bites)
    # 4- OS: Windows 10
    # 5- Bejelentkezett felhasználó: Email: testuser1@example.com Password: Abcd123$
    # 6- Szükséges a TC_001 és a TC_002 tesztek sikeres lefutása
    # Követelmény: Req.id: R03
    from selenium import webdriver
    import time
    from selenium.webdriver.chrome.options import Options
    from webdriver_manager.chrome import ChromeDriverManager

    options = Options()
    # options.add_argument('--headless')
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    # oldal betöltése
    driver.get("http://localhost:1667")

    # Bejelentkezéshez szükséges adatok
    email_data = ["testuser1@example.com"]
    password_data = ["Abcd123$"]

    # Bejelentkezés függvény
    def login(email_l, password_l):
        sign_in = driver.find_element_by_xpath('//a[@href="#/login"]')
        sign_in.click()
        email = driver.find_element_by_xpath('//input[@placeholder="Email"]')
        email.send_keys(email_l)
        password = driver.find_element_by_xpath('//input[@placeholder="Password"]')
        password.send_keys(password_l)
        button = driver.find_element_by_xpath('//button[@class="btn btn-lg btn-primary pull-xs-right"]')
        button.click()
        time.sleep(2)

    # Kijelentkezés függvény
    def logout():
        log_out = driver.find_element_by_xpath('//a[@active-class="active"]')
        log_out.click()
        time.sleep(2)

    # Bejelentkezés függvény meghívása tesztadatokkal
    login(email_data[0], password_data[0])

    test_user1 = driver.find_element_by_xpath('//li[@class="nav-item"]//a[@href="#/@testuser1/"]')

    # Ellenőrizzük a bejelentkezett felhasználó megjelenését
    assert test_user1.text == "testuser1"
    assert test_user1.is_displayed()
    time.sleep(3)

    # Kijelentkezés függvény meghívása
    logout()

    # Ellenőrizzük, hogy a felhasználó már nincs bejelentkezve
    test_user1_check = driver.find_elements_by_xpath('//li[@class="nav-item"]//a[@href="#/@testuser1/"]')
    assert len(test_user1_check) == 0

    driver.close()
