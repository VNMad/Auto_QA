import pytest
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture
def driver():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


def test_payment_methods(driver):
    driver.get("https://itcareerhub.de/ru")
    sleep(2)
    payment_button = driver.find_element(By.LINK_TEXT,"Способы оплаты")
    payment_button.click()
    sleep(2)
    driver.save_screenshot("payment_methods.png")
