import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    # options.add_argument("--headless") # Раскомментируй для работы без окна браузера

    # webdriver-manager сам скачает нужный драйвер под твою версию Chrome
    service = Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()