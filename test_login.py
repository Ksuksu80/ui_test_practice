from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# show the path to your driver
service = Service("/Users/ks/PycharmProjects/ui_test_practice/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://google.com")
print(driver.title)
# wait 3 sec and close browser
time.sleep(3)
driver.quit()