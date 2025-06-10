import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


#fixture to crete and close browser
@pytest.fixture()
def driver():
    # show the path to your driver
    service = Service("/Users/ks/PycharmProjects/ui_test_practice/chromedriver")
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()  # expand the browser window
    driver.get("https://manojkumar4636.github.io/Selenium_Practice_Hub/home.html")
    time.sleep(3)  # wait for 3 sec to see the home page
    yield driver
    driver.quit()

#fixture to start the home page
#@pytest.fixture()
#def home_page(driver):
    #driver.get("https://manojkumar4636.github.io/Selenium_Practice_Hub/home.html")
    #time.sleep(3)  # wait for 3 sec to see the home page
    #return driver

#fixture to transfer to Button page
@pytest.fixture()
def button_page(driver):
    driver.get("https://manojkumar4636.github.io/Selenium_Practice_Hub/pages/Button.html")
    time.sleep(3)  #wait for 3 sec to see button page
    return driver

#fixture to transfer to Drop down page
@pytest.fixture()
def dropdown_page(driver):
    driver.get("https://manojkumar4636.github.io/Selenium_Practice_Hub/pages/Dropdown.html")
    time.sleep(3)   #wait for 3 sec to see dropdown page
    return driver
