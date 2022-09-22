import pandas as pd
import time
import urllib.request
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By

# 웹드라이버 설정
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

path = "chromedriver.exe"

driver = webdriver.Chrome(
    executable_path='C:/Users/user/anaconda3/Scripts/chromedriver.exe')
driver.implicitly_wait(3)
