from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://www.baidu.com/')
driver.find_element(By.CSS_SELECTOR, '#kw').send_keys('selenium')

sleep(3)

# 键盘全选操作,ctrl+A
driver.find_element(By.CSS_SELECTOR, '#kw').send_keys(Keys.CONTROL, 'a')
sleep(2)
