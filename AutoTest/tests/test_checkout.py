import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_full_checkout_path(driver):
    driver.get("https://www.saucedemo.com/")
    wait = WebDriverWait(driver, 10)

    # 1. Авторизация
    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # 2. Добавление товара в корзину (например, рюкзак)
    add_to_cart_button = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack")))
    add_to_cart_button.click()
    time.sleep(3)

    # 3. Переход в корзину
    shopping_cart_link = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
    shopping_cart_link.click()

    wait.until(EC.url_contains("cart.html"))
    assert "cart.html" in driver.current_url
    assert "cart.html" in driver.current_url
    assert driver.find_element(By.CLASS_NAME, "inventory_item_name").text == "Sauce Labs Backpack"

    # 4. Нажимаем Checkout
    driver.find_element(By.ID, "checkout").click()
    time.sleep(3)

    # 5. Заполнение данных покупателя
    wait.until(EC.visibility_of_element_located((By.ID, "first-name"))).send_keys("Ivan")
    driver.find_element(By.ID, "last-name").send_keys("Ivanov")
    driver.find_element(By.ID, "postal-code").send_keys("123456")
    time.sleep(3)

    driver.find_element(By.ID, "continue").click()

    # 6. Проверка страницы Overview (финальный просмотр перед оплатой)
    assert "checkout-step-two.html" in driver.current_url
    time.sleep(3)

    # 7. Нажимаем Finish
    driver.find_element(By.ID, "finish").click()

    # 8. Финальная проверка
    complete_header = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "complete-header")))

    expected_message = "Thank you for your order!"
    assert complete_header.text == expected_message, f"Ожидалось '{expected_message}', но получили '{complete_header.text}'"

    print("\nЗаказ успешно оформлен!")
    time.sleep(3)