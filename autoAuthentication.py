from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Edge()

browser.get("https://tree.buct.edu.cn/index_20.html")

try:
    browser.implicitly_wait(10)
    browser.find_element(By.XPATH,'//*[@id="username"]').send_keys('2024050276')
    browser.find_element(By.XPATH,'//*[@id="password"]').send_keys('@Jtbx2mtblj')
    browser.find_element(By.XPATH,'//*[@id="login-account"]').click()
except Exception:
    print('Authentication finish!')