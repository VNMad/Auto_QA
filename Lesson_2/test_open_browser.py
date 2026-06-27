from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import pytest


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
    

def test_berlin(driver):
    driver.get("https://itcareerhub.de/ru")
    driver.refresh()
    driver.get("https://www.berlin.de")
    driver.save_screenshot("./berlin.png")
    sleep(2)
    driver.refresh()
    driver.back()
    sleep(2)
    driver.forward()
    driver.refresh()
    sleep(2)
