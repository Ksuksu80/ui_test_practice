
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time


def test_navigate_to_edit_page(driver):

    #2. home page is already open, click by "Edit" button
    edit_button = driver.find_element(By.CSS_SELECTOR, "a[href='pages/Edit.html']")
    edit_button.click()
    time.sleep(4)

    #3. Assertion: URL change
    assert "edit" in driver.current_url.lower()
    print("transfer to page 'Edit' is successful!")

    #4. enter e-mail
    email_input = driver.find_element(By.ID, "email")
    email_input.send_keys("test@example.com")
    time.sleep(2)

    #5. Assertion: value
    assert email_input.get_attribute('value') =="test@example.com"
    print('"email input is successful')

    #6. find append field
    append_input = driver.find_element(By.CSS_SELECTOR, 'input[value="Append "]')
    #add text
    append_input.send_keys(' - additional text')

    #press tab
    append_input.send_keys(Keys.TAB)
    time.sleep(2)

    #7. enter default text
    default_text_input = driver.find_element(By.CSS_SELECTOR, "input[value='TestLeaf']")
    #add default text
    copied_text = default_text_input.get_attribute("value")
    new_text = copied_text + copied_text
    # clear the field
    default_text_input.clear()
    default_text_input.send_keys(new_text)
    time.sleep(2)

    #8. find the field to clear the text
    clear_field = driver.find_element(By.XPATH, "//input[@value='Clear me!!']")
    # now we can clean the text
    clear_field.clear()
    time.sleep(2)

    #9. confirm the field is disabled
    input_field = driver.find_element(By.XPATH, "//input[@disabled='true']")
    assert not input_field.is_enabled(), "field is to be disabled"
    print("field is disabled")
    time.sleep(2)



