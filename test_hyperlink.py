from selenium.webdriver.common.by import By
from pages.radio_page import RadioPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_hyperlink(driver):
    # 1. find hyperlink button and click:
    hyperlink_icon = driver.find_element(By.XPATH, "//body")
    hyperlink_icon.click()
    time.sleep(3)

    assert "link" in driver.current_url.lower()
    print("transfer to page 'link' is successful!")

    # 2. navigate to Go to Home hyperlink and click
    go_to_home_link_button = driver.find_element(By.XPATH, "//a[text()='Go to Home Page']")
    go_to_home_link_button.click()
    time.sleep(3)
    assert "home" in driver.current_url.lower()
    print("Returned to home page successful!")
