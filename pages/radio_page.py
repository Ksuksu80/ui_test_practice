from selenium.webdriver.common.by import By
import time

class RadioPage:
    def __init__(self, driver):
        self.driver = driver
        self.radio_button_page_icon = (By.XPATH, "//img[@alt='Radio Button']")
        self.yes_radio_label = (By.XPATH, "//label[normalize-space()='Yes']")
        self.yes_radio_input = (By.ID, "yes")

    def open(self):
        self.driver.find_element(*self.radio_button_page_icon).click()
        time.sleep(2)

    def select_yes(self):
        self.driver.find_element(*self.yes_radio_label).click()
        time.sleep(2)

    def is_yes_selected(self):
        return self.driver.find_element(*self.yes_radio_input).is_selected()