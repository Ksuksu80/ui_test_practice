from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import time

def test_dropdown(driver):
    #1. transfer to drop down page
    dropdown_button = driver.find_element(By.XPATH, "//img[@alt='ListBox']")
    dropdown_button.click()
    time.sleep(2)

    # Assertion: URL change
    assert "dropdown" in driver.current_url.lower()
    print("transfer to page 'dropdown' is successful!")

    #2.select training program using index
    dropdown_a = driver.find_element(By.XPATH, "//select[@id='dropdown1']")
    dropdown_a.click()
    # wrap in Select for choosing the option in dropdown
    select = Select(dropdown_a)
    time.sleep(2)

    # select by Index (2 - this is second option in the list)
    select.select_by_index(2)
    time.sleep(2)

    print(" option is selected by index 2 (second option in the list)")

    #3. find the second dropdown field and view options
    dropdown_b = driver.find_element(By. XPATH, "//select[@name='dropdown2']")
    dropdown_b.click()

    #wrap in Select for choosing  the option by Text
    select = Select(dropdown_b)
    time.sleep(2)

    # select the option 1 by Text(option number 1 in the list)
    select.select_by_visible_text("Selenium")
    time.sleep(2)
    print(" option is selected by text 'Selenium' (first option in the list)")

    #4. Find third dropdown and click to view options
    dropdown_c = driver.find_element(By.XPATH, "//select[@id='dropdown3']")
    dropdown_c.click()
    time.sleep(2)

    #wrap in Select
    select = Select(dropdown_c)
    time.sleep(2)

    select.select_by_value("3")
    time.sleep(3)
    print(" option is selected by value '3' (third option in the list)")

    #4. count options in dropdown 4. find dropdown 4 and click on it
    dropdown_d = driver.find_element(By. XPATH, "//select[@class='dropdown']")
    dropdown_d.click()
    time.sleep(2)

    #count options in dropdown
    select_d = Select(dropdown_d)
    option_count = len(select_d.options)
    print(f"number of options in dropdown: {option_count}")

    # 5. select an option with sendkeys. find dropdown 5
    dropdown_e = driver.find_element(By.XPATH, "//div[6]//select[1]")

    #use sendKeys to select option in the list
    dropdown_e.send_keys("Appium")
    time.sleep(2)

    #to confirm that the right option is selected
    select= Select(dropdown_e)
    selected_option=select.first_selected_option
    assert selected_option.text==("Appium")
    print(f"option selected:{selected_option.text}")











