from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_button(driver):
    # 1.find Button icon on home page

    button_icon = driver.find_element(By.XPATH, "//img[@alt='Buttons']")
    button_icon.click()
    time.sleep(3)

   #wait for button to appear
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@id='home']")))

    assert "button" in driver.current_url.lower()
    print("transfer to page 'Button' is successful!")

    #click button to go home
    home_button = driver.find_element(By.XPATH, "//button[@id='home']")
    home_button.click()
    # wait to return to home page
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//div[@class='block-content']//ul" )))
    time.sleep(3)

    assert "home" in driver.current_url.lower()
    print("Returned to home page successful!")


    #2. find position of button (x,y) координаты
def test_position_button(button_page):

    # wait for button to appear
    WebDriverWait(button_page, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@id='home']")))
    position_button = button_page.find_element(By.XPATH, "//button[@id='position']")

    # get position
    x = position_button.location['x']
    y = position_button.location['y']

    assert x > 0 and y > 0, "numbers should be positive"
    print("position finding is successful")

    print(f"Button position - X: {x}, Y: {y}")

    #3. define color of the button

    button_color=button_page.find_element(By.ID,"color")
    button_color = WebDriverWait(button_page, 10).until (EC.presence_of_element_located((By.ID, "color")))
    rgba_color = button_color.value_of_css_property("background-color")
    print("button color is:", rgba_color)
    expected_color="rgba(144, 238, 144, 1)"
    assert rgba_color == expected_color, f"Expected {expected_color}, but got {rgba_color}"

    #4. what size is the button
    size_button = button_page.find_element(By.XPATH, "//button[@id='size']")
    time.sleep(2)
    size= size_button.size
    width = size['width']
    height = size['height']
    print(f"Button size - Width: {width}, Height: {height}")

    assert width >0 and height >0, "the size of button should be positive"

