import time

from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#  Открыть браузер
options = ChromeOptions()

options.add_argument('headless')
options.add_argument("--disable-extensions")
options.add_argument('window-size=1920x935')
driver = Chrome(options = options)

def test_google_search():
    #  Переход на страницу
    driver.get('https://catalogplitki.ru')
    tel = driver.find_element_by_id('tel')
    name = driver.find_element_by_id('name')
    #  Ввод текста
    tel.send_keys(Keys.HOME + '87127848311')
    name.send_keys('sasha')
    message = driver.find_element_by_id('message')
    submit = driver.find_element_by_id('submit')
    rul_checkbox = driver.find_element_by_id('rul_checkbox')
    print(submit.text)
    rul_checkbox.click()
    submit.click()
    time.sleep(5)
    #  Проверка результатов
    result = driver.find_elements(
        by=By.CSS_SELECTOR,
        value='#rso .srg div.g'
    )

    if message.is_displayed():
        print("Element found")
    else:
        print("Element not found")

test_google_search()
