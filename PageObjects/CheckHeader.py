from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class Test1:

    header_path = "toolbar"
    politics_path = "//body/nav[1]/ul[1]/li[1]/ul[1]/li[2]/a[1]"
    isPolitics_path = "//h1[contains(text(),'פוליטי')]"


    def __init__(self, driver):
        self.driver = driver

    def is_enable(self):
        self.driver.execute_script("window.scrollBy(0,10000)", "")
        element = WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.CLASS_NAME,self.header_path)))
        element = bool(element)
        return element

    def politics(self):
        self.driver.find_element(by=By.XPATH,value=self.politics_path).click()


    def checkPolitics(self):
        is_politic = self.driver.find_element(by=By.XPATH, value=self.isPolitics_path).text
        return is_politic