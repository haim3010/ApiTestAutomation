from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class Weather:

    click_path = "tns1"
    scroll_path = "//h2[contains(text(),'תחזית ליממה הקרובה')]"
    eilat_path = "//strong[contains(text(),'אילת')]"
    tel_aviv_path ="//strong[contains(text(),'תל אביב - יפו')]"
    jerusalem_path ="//strong[contains(text(),'ירושלים')]"
    ashdod_path = "//strong[contains(text(),'אשדוד')]"
    beer_sheva_path = "//strong[contains(text(),'באר שבע')]"
    haifa_path = "//strong[contains(text(),'חיפה')]"
    zefat_path = "//strong[contains(text(),'צפת')]"
    tveria_path = "//strong[contains(text(),'טבריה')]"
    weather_path = '//body[1]/main[1]/div[1]/form[1]/button[1]/span[2]'


    def __init__(self, driver):
        self.driver = driver

    def Click(self):
        self.driver.find_element(by=By.ID,value=self.click_path).click()

    def get_weather(self):
        self.driver.implicitly_wait(30)
        flag = self.driver.find_element(by=By.XPATH, value=self.scroll_path)
        self.driver.execute_script("arguments[0].scrollIntoView();", flag)
        self.driver.implicitly_wait(10)
        check_header = self.driver.find_element(by=By.XPATH, value=self.scroll_path).text
        return check_header

    def eilat_weather(self):
        self.driver.find_element(by=By.XPATH,value=self.eilat_path).click()
        self.driver.implicitly_wait(10)
        eilat = self.driver.find_element(by=By.XPATH, value=self.weather_path).text
        return eilat

    def tel_aviv_weather(self):
        self.driver.find_element(by=By.XPATH,value=self.tel_aviv_path).click()
        self.driver.implicitly_wait(10)
        tel_aviv = self.driver.find_element(by=By.XPATH, value=self.weather_path).text
        return tel_aviv

    def jerusalem_weather(self):
        self.driver.find_element(by=By.XPATH,value=self.jerusalem_path).click()
        self.driver.implicitly_wait(10)
        jerusalem = self.driver.find_element(by=By.XPATH, value=self.weather_path).text
        return jerusalem

    def ashdod_weather(self):
        self.driver.find_element(by=By.XPATH,value=self.ashdod_path).click()
        self.driver.implicitly_wait(10)
        ashdod = self.driver.find_element(by=By.XPATH, value=self.weather_path).text
        return ashdod

    def beer_sheva_weather(self):
        self.driver.find_element(by=By.XPATH,value=self.beer_sheva_path).click()
        self.driver.implicitly_wait(10)
        beer_sheva = self.driver.find_element(by=By.XPATH, value=self.weather_path).text
        return beer_sheva

    def haifa_weather(self):
        self.driver.find_element(by=By.XPATH,value=self.haifa_path).click()
        self.driver.implicitly_wait(10)
        haifa = self.driver.find_element(by=By.XPATH, value=self.weather_path).text
        return haifa

    def zefat_weather(self):
        self.driver.find_element(by=By.XPATH,value=self.zefat_path).click()
        self.driver.implicitly_wait(10)
        zefat = self.driver.find_element(by=By.XPATH, value=self.weather_path).text
        return zefat

    def tveria_weather(self):
        self.driver.find_element(by=By.XPATH,value=self.tveria_path).click()
        self.driver.implicitly_wait(10)
        tveria = self.driver.find_element(by=By.XPATH, value=self.weather_path).text
        return tveria