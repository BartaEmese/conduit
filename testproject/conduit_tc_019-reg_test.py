def test_conduit19():
    # Conduit_TC_019_Reg
    # Egy oldalon megjelenő maximális blogbejegyzés vizsgálata
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
    from selenium.webdriver.chrome.options import Options
    from webdriver_manager.chrome import ChromeDriverManager

    options = Options()
    #options.add_argument('--headless')

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    try:
        # Oldal betöltése
        driver.get("http://localhost:1667")
        time.sleep(1)


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


        # Bejelentkezés tesztadat
        email_data = ["testuser1@example.com"]
        password_data = ["Abcd123$"]

        # Bejelentkezés függvény meghívás
        login(email_data[0], password_data[0])

        # testuser1 felhasználó blogbejegyzéseinek kikeresése
        testuser1 = driver.find_element_by_xpath('//li[@class="nav-item"]//a[@href="#/@testuser1/"]')
        testuser1.click()
        time.sleep(7)
        article_title = driver.find_elements_by_xpath('//div[@class="article-preview"]')
        time.sleep(3)
        print(len(article_title))
        # Ellenőrzés: egy oldalon megjelenő blogbejegyzés max 10 db
        assert len(article_title) <= 10

    finally:
        driver.close()
