import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_error_message_with_wrong_password(driver):
    # 1. Сайт
    driver.get("https://www.saucedemo.com/")
    wait = WebDriverWait(driver, 10)
    time.sleep(1)

    # 2. Ввод логина
    username_input = wait.until(EC.element_to_be_clickable((By.ID, "user-name")))
    username_input.send_keys("standard_user")
    time.sleep(1)

    # 3. Ввод НЕВЕРНОГО пароля
    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("wrong_sauce")
    time.sleep(1)

    # 4. Нажатие на кнопку Login
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()
    time.sleep(1)

    # 5. Поиск сообщения об ошибке
    # На SauceDemo ошибка появляется в теге h3 с атрибутом data-test="error"
    error_container = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "h3[data-test='error']"))
    )

    # Текст ошибки, который должен появиться
    expected_error_text = "Epic sadface: Username and password do not match any user in this service"

    # Проверка (Assertion)
    assert error_container.text == expected_error_text, \
        f"Ожидался текст '{expected_error_text}', но получили '{error_container.text}'"

    # Финал
    print("\nТест пройден: ошибка отобразилась корректно.")
    time.sleep(3)