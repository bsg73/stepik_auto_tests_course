import os
import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    driver = webdriver.Chrome()
    driver.get("http://suninjuly.github.io/file_input.html")
    name1 = driver.find_element(By.NAME, "firstname")
    name1.send_keys("Serg")
    name2 = driver.find_element(By.NAME, "lastname")
    name2.send_keys("ik")
    name3 = driver.find_element(By.NAME, "email")
    name3.send_keys("ik@gmail.com")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    infile=driver.find_element(By.ID,'file')
    infile.send_keys(file_path)
    btn=driver.find_element(By.TAG_NAME,"button")
    btn.click()

finally:
    time.sleep(3)
    driver.quit()