def test_conduit11():
    # Conduit_TC_011_Reg
    # Saját blogbejegyzés létrehozása, módosítása
    # Előfeltételek:
    # 1- A gazdagép elérhető
    # 2- A gazdagépen  fut a Conduit
    # 3- Chrome Verzió: 91.0.4472.77 (Hivatalos verzió) (64 bites)
    # 4- OS: Windows 10
    # 5- Bejelentkezett felhasználó: Email: testuser1@example.com Password: Abcd123$
    # 6- Szükséges a TC_001 és a TC_002 tesztek sikeres lefutása
    # Követelmény: Req.id: R07
    from selenium import webdriver
    import time
    import random
    import string
    from selenium.webdriver.chrome.options import Options
    from webdriver_manager.chrome import ChromeDriverManager

    options = Options()
    # options.add_argument('--headless')

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    # Oldal betöltése
    driver.get("http://localhost:1667")
    time.sleep(1)

    # Random cím
    def get_title(lowers_count):
        lowers = ''.join((random.choice(string.ascii_lowercase) for i in range(lowers_count)))
        titles = "A" + " " + lowers
        return titles

    # Random szöveg
    def get_text(lowers_count):
        lowers = ''.join((random.choice(string.ascii_lowercase) for i in range(lowers_count)))
        return lowers

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

    # Blogbejegyzés létrehozás függvény
    def create_article(article_a, about_a, text_a, tag_a):
        new_article = driver.find_element_by_xpath('//a[@href="#/editor"]')
        new_article.click()
        time.sleep(2)
        article_title = driver.find_element_by_xpath('//input[@placeholder="Article Title"]')
        article_title.send_keys(article_a)
        about = driver.find_element_by_xpath("//form/fieldset/fieldset[2]/input")
        about.send_keys(about_a)
        text_area = driver.find_element_by_xpath("//textarea")
        text_area.send_keys(text_a)
        tags = driver.find_element_by_xpath('//input[@placeholder="Enter tags"]')
        tags.send_keys(tag_a)
        publish_article = driver.find_element_by_xpath("//button")
        publish_article.click()
        time.sleep(1)

    # Blog cím módosítás függvény
    def edit_article_title(new_title):
        edit_article = driver.find_element_by_xpath('//div[@class="banner"]/div/div/span/a/i')
        edit_article.click()
        time.sleep(1)
        article_title = driver.find_element_by_xpath('//input[@placeholder="Article Title"]')
        article_title.clear()
        article_title.send_keys(new_title)
        submit_button = driver.find_element_by_xpath("//button[@class='btn btn-lg pull-xs-right btn-primary']")
        submit_button.click()
        time.sleep(2)

    # Blogbejegyzés törlése függvény
    def delete_article():
        delete_button = driver.find_element_by_xpath('//button[@class="btn btn-outline-danger btn-sm"]')
        delete_button.click()

    # Blog tesztadat
    test_list = [get_title(5), get_text(10), get_text(3), get_title(5)]

    # Bejelentkezés tesztadat
    email_data = ["testuser1@example.com"]
    password_data = ["Abcd123$"]

    # Bejelentkezés függvény meghívás
    login(email_data[0], password_data[0])

    # Blogbejegyzés létrehozás függvény meghívás
    create_article(test_list[0], test_list[0], test_list[1], test_list[2])

    # Létrehozott blogbejegyzés adat helyesség vizsgálata
    title = driver.find_element_by_xpath("//h1")
    text = driver.find_element_by_xpath("//p")
    tag = driver.find_element_by_xpath('//a[@class="tag-pill tag-default"]')

    assert title.text == test_list[0]
    assert text.text == test_list[1]
    assert tag.text == test_list[2]

    # Blog cím módosítás függvény meghívás
    edit_article_title(test_list[3])

    # Blog cím módosításának ellenőrzése
    text = test_list[3]
    assert title.text == text

    # Blogbejegyzés törlése függvény meghívása
    delete_article()

    driver.close()
