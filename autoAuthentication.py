import time 
from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Edge()

browser.get("https://tree.buct.edu.cn/index_20.html")

browser.find_element(By.XPATH,'//*[@id="username"]').send_keys("账号")
browser.find_element(By.XPATH,'//*[@id="password"]').send_keys('密码')

browser.find_element(By.XPATH,'//*[@id="login-account"]').click()

browser.quit()

time.sleep(3)