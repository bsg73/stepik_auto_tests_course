import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    driver = webdriver.Chrome()
    driver.get("https://suninjuly.github.io/math.html")
    x_element = driver.find_element(By.CSS_SELECTOR, "[id='input_value']")
    x = x_element.text
    y = calc(x)
    txt = driver.find_element(By.ID, "answer")
    txt.send_keys(str(y))
    chk=driver.find_element(By.ID,"robotCheckbox")
    chk.click()
    rbt=driver.find_element(By.ID,"robotsRule")
    rbt.click()
    btn=driver.find_element(By.TAG_NAME,"button")
    btn.click()
    time.sleep(5)
finally:
    driver.quit()

print(calc(1000))
