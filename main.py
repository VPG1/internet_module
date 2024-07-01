from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from local_storage.local_storage import LocalStorage


def print_line():
    print("".join(["-" for i in range(100)]))


service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

url = 'https://google.com'

try:
    driver.get(url)

    print_line()

    # cookie
    print("Куки нет:", driver.get_cookie("name1"))

    driver.add_cookie({"name": "name1", "value": "value1"})  # add cookie
    print("Добавили куки:", driver.get_cookie("name1"))

    driver.delete_cookie("name1")  # delete cookie
    print("Удалили куки:", driver.get_cookie("name1"))

    print_line()

    # local storage
    local_storage = LocalStorage(driver)

    print("Нет в local storage:", local_storage.get("name1"))

    local_storage.set("name1", "value1")
    print("Добавили в local storage:", local_storage.get("name1"))

    local_storage.remove("name1")
    print("Удалили из local storage:", local_storage.get("name1"))

    print_line()

finally:
    driver.close()
    driver.quit()
