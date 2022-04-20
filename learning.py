from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
ser = Service("C:\\drivers\\chromedriver_win32 (3)\\chromedriver.exe")
driver = webdriver.Chrome(service=ser)
driver.get("http:www.google.com")
driver.maximize_window()

driver.close()