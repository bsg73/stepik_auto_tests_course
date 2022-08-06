import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    driver = webdriver.Chrome()
    driver.get("http://suninjuly.github.io/explicit_wait2.html")
    WebDriverWait(driver, 12).until(ec.text_to_be_present_in_element((By.ID, "price"), "$100"))
    btna=driver.find_element(By.TAG_NAME,'button')
    btna.click()
    x_element = driver.find_element(By.CSS_SELECTOR, "[id='input_value']")
    x = x_element.text
    y = calc(x)
    txt = driver.find_element(By.ID, "answer")
    txt.send_keys(str(y))
    btn=driver.find_element(By.ID,"solve")
    btn.click()
    time.sleep(5)
finally:
    driver.quit()

