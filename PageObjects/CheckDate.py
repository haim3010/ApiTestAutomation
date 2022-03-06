from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class Date:
    date_path = "date"

    def __init__(self, driver):
        self.driver = driver

    def checkDate(self):
       txt = self.driver.find_element(by=By.CLASS_NAME,value="date").text
       txt = txt.split()
       return txt[1]
