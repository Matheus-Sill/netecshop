
import os
import pytest
from selenium import webdriver

URL = "https://cristianomacedo19.github.io/netecshop/app.html"


@pytest.fixture
def navegador():
    opcoes = webdriver.FirefoxOptions()

    if os.getenv("HEADLESS") == "1":
        opcoes.add_argument("-headless")

    driver = webdriver.Firefox(options=opcoes)
    driver.set_window_size(1280, 900)
    driver.get(URL)

    yield driver

    driver.quit()
