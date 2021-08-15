def test_conduit01():
    # Conduit_TC_001_Reg
    # Kezdő képernyő vizsgálata és regisztráció üres beviteli mezővel
    # Előfeltételek:
    # 1- A gazdagép elérhető
    # 2- A gazdagépen  fut a Conduit
    # 3- Chrome Verzió: 91.0.4472.77 (Hivatalos verzió) (64 bites)
    # 4- OS: Windows 10
    # Követelmény: Req.id: R01
    import csv
    from selenium import webdriver
    import time

    from selenium.webdriver.chrome.options import Options
    from webdriver_manager.chrome import ChromeDriverManager

    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    # Oldal betöltése
    driver.get("http://localhost:1667")

    # Vizsgáljuk a kezdőoldal elemeinek  meglétét
    assert driver.find_element_by_xpath("//div[@class='container']//a[contains(text(),'conduit')]").is_displayed()
    assert driver.find_element_by_xpath("//li[@class='nav-item']//a[contains(text(),'Home')]").is_displayed()
    assert driver.find_element_by_xpath("//li[@class='nav-item']//a[contains(text(),'Sign in')]").is_displayed()
    assert driver.find_element_by_xpath("//li[@class='nav-item']//a[contains(text(),'Sign up')]").is_displayed()
    assert driver.find_element_by_xpath("//li[@class='nav-item']//a[contains(text(),'Global Feed')]").is_displayed()
    assert driver.find_element_by_xpath("//div[@class='sidebar']").is_displayed()
    assert driver.find_element_by_xpath('//div[@class="cookie__bar__buttons"][1]/button[1]').is_displayed()
    assert driver.find_element_by_xpath('//div[@class="cookie__bar__buttons"][1]/button[2]').is_displayed()
    assert driver.find_element_by_xpath('//div[@class="cookie__bar__content"]/div/a').is_displayed()

    # Tag-ek kilistázása
    tags_list = []
    tags = driver.find_elements_by_xpath('//div[@class="tag-list"]/a')
    for tag in tags:
        tags_list.append(tag.text)
    print(tags_list)

    with open('tags.txt', 'w', newline='', encoding='UTF-8') as csvtags:
        writer = csv.writer(csvtags)
        writer.writerow(tags_list)

    # Sign up gomb megnyomása után vizsgáljuk a beviteli mezők meglétét
    sing_up = driver.find_element_by_xpath('//a[@href="#/register"]')
    sing_up.click()
    time.sleep(2)

    sing_up_button = driver.find_element_by_xpath("//button")

    assert driver.find_element_by_xpath("//form/fieldset[1]/input").is_displayed()
    assert driver.find_element_by_xpath("//form/fieldset[2]/input").is_displayed()
    assert driver.find_element_by_xpath("//form/fieldset[3]/input").is_displayed()
    assert sing_up_button.is_displayed()

    # Üresen hagyott beviteli mezőkel rákattintunk a Sign up gomra és vizsgáljuk a felugró ablak szövegének helyességét
    sing_up_button.click()
    time.sleep(2)

    assert driver.find_element_by_xpath('//div[@class="swal-title"]').text == "Registration failed!"
    assert driver.find_element_by_xpath('//div[@class="swal-text"]').text == "Username field required."

    driver.close()
