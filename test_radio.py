from selenium.webdriver.common.by import By
from pages.radio_page import RadioPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_radio_button_page(driver):
    page = RadioPage(driver)

#1. open radio button page
    page.open()

# select "Yes"
    page.select_yes()

    #confirm that "Yes" is selected
    assert page.is_yes_selected()
    print("answer 'Yes' is selected successfully")



