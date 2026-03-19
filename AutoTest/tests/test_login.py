import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_successful_login_and_products_loaded(driver):
    driver.get("https://www.saucedemo.com/")
    time.sleep(2) 

    wait = WebDriverWait(driver, 10)

    # Ввод логина
    username_field = wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
    username_field.send_keys("standard_user")
    time.sleep(1)

    # Ввод пароля
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    time.sleep(1)

    # Нажатие кнопки
    driver.find_element(By.ID, "login-button").click()
    time.sleep(5)

    # Проверка товаров
    products = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item")))

    print(f"Найдено товаров: {len(products)}")
    time.sleep(3)

    assert len(products) > 0