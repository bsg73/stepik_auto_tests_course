import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    driver = webdriver.Chrome()
    driver.get("http://suninjuly.github.io/selects1.html")
    x_element = driver.find_element(By.ID, "num1")
    x = int(x_element.text)
    y_element = driver.find_element(By.ID, "num2")
    y = int(y_element.text)
    select = Select(driver.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(x+y))

    btn=driver.find_element(By.TAG_NAME,"button")
    btn.click()
    time.sleep(5)
finally:
    driver.quit()
print(x+y)