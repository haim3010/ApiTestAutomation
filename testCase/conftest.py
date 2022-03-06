import pytest
from selenium import webdriver

@pytest.fixture(autouse=True)
def setup(request):
    driver = webdriver.Chrome(executable_path="C:\\Users\\haim\\PycharmProjects\\AutomationProject\\Driver\\chromedriver.exe")
    driver.implicitly_wait(30)
    driver.get("https://www.n12.co.il/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
