def test_conduit04():
    # Conduit_TC_005_Reg
    # Bejelentkezés- már létező felhasználó helyes és helytelen adatainak megadásával
    # Előfeltételek:
    # 1- A gazdagép elérhető
    # 2- A gazdagépen  fut a Conduit
    # 3- Chrome Verzió: 91.0.4472.77 (Hivatalos verzió) (64 bites)
    # 4- OS: Windows 10
    # 5- Szükséges a TC_001 és a TC_002 tesztek sikeres lefutása
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
    # Oldal betöltése
    driver.get("http://localhost:1667")

    # Elemek megkeresése és törlése függvény
    def find_by_xpath(xpath):
        element = driver.find_element_by_xpath(xpath)
        element.clear()
        return element

    # Bejelentkezés függvény
    def login_f(email_l, password_l):
        email_f = find_by_xpath('//input[@placeholder="Email"]')
        email_f.send_keys(email_l)
        print(email_f.get_attribute("value"))
        password = find_by_xpath('//input[@placeholder="Password"]')
        password.send_keys(password_l)
        time.sleep(2)
        add_button.click()
        time.sleep(2)

    # Log in link elem
    login = driver.find_element_by_xpath('//a[@href="#/login"]')

    # register_data_test.csv beolvasása
    with open('testproject/register_data_test.csv', encoding="UTF-8") as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=",")
        next(csv_reader)
        login.click()

        add_button = driver.find_element_by_xpath('//button[@class="btn btn-lg btn-primary pull-xs-right"]')

        email_value = ["", "testuser1@example", "@example.com"]

        # Bejelentkezés függvény üres és helytelen email és password-del csv-ből
        for row in csv_reader:
            time.sleep(2)
            print(row)
            login_f(row[0], row[1])

            # Alert gomb elem
            alert_button = driver.find_element_by_xpath('//button[@class="swal-button swal-button--confirm"]')
            time.sleep(1)

            # Alert gomb megjelenésének vizsgálata
            if alert_button.is_displayed():
                time.sleep(2)
                alert_title = driver.find_element_by_xpath('//div[@class="swal-title"]')
                alert_text = driver.find_element_by_xpath('//div[@class="swal-text"]')

                # Alert helyességének vizsgálata a beírt email (row[0]) címek alapján
                if row[0] == email_value[0]:
                    time.sleep(1)
                    assert alert_title.text == "Login failed!"
                    assert alert_text.text == "Email field required."
                elif row[0] == email_value[1]:
                    assert alert_title.text == "Login failed!"
                    assert alert_text.text == "Invalid user credentials."
                elif row[0] == email_value[2]:
                    assert alert_title.text == "Login failed!"
                    assert alert_text.text == "Email must be a valid email."
                    time.sleep(2)
                alert_button.click()
            else:
                break

        # Bejelentkezés függvény meghívás helyes email és password-el
        login_f("testuser1@example.com", "Abcd123$")

        # A bejelentkezett felhasználó név ellenőrzése
        testuser1 = driver.find_element_by_xpath('//li[@class="nav-item"]//a[@href="#/@testuser1/"]')
        assert testuser1.is_displayed()

    driver.close()
