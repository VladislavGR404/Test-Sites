import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


def test_sort_products_by_price_low_to_high(driver):
    driver.get("https://www.saucedemo.com/")
    wait = WebDriverWait(driver, 10)

    # 1. Авторизация
    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # 2. Находим выпадающий список сортировки
    # На сайте это элемент с классом 'product_sort_container'
    sort_select_element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "product_sort_container")))
    select = Select(sort_select_element)

    # 3. Выбираем сортировку "Price (low to high)"
    # Можно выбрать по тексту или по значению (value="lohi")
    select.select_by_value("lohi")
    time.sleep(3)

    # 4. Собираем все цены товаров
    # Цены находятся в элементах с классом 'inventory_item_price'
    price_elements = driver.find_elements(By.CLASS_NAME, "inventory_item_price")

    # Преобразуем текст цен
    prices = []
    for element in price_elements:
        clean_price = float(element.text.replace("$", ""))
        prices.append(clean_price)

    print(f"Цены на странице после сортировки: {prices}")

    # 5. Проверка
    expected_prices = sorted(prices)

    assert prices == expected_prices, f"Сортировка неверна! Ожидалось {expected_prices}, но получили {prices}"

    time.sleep(2)