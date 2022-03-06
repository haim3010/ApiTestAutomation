import logging
import time
import pytest
from PageObjects.CheckHeader import Test1
from PageObjects.CheckDate import Date
from PageObjects.CheckWeather import Weather
from utilities.customLogger import LoggerYit

from datetime import date
today = date.today()
today = today.strftime('%d.%m.%y')
mainPage = "C:\\Users\\haim\\PycharmProjects\\AutomationProject\\Screenshots\\"

@pytest.mark.usefixtures("setup")
class TestYit():
    logger = LoggerYit.Logger()
    def test_header(self):
        self.logger.info("*******Test_01_checking_header*******")
        test1 = Test1(self.driver)
        header =  test1.is_enable()
        assert header == True
        self.logger.info("*******Test checking header passed*******")
        self.driver.save_screenshot(mainPage + "TestHeader.png")

        test1.politics()
        isPolitic =  test1.checkPolitics()
        self.driver.save_screenshot(mainPage + "TestPolitic.png")
        if isPolitic == 'פוליטי':
            assert True
            self.logger.info("*******Test checking politics passed*******")
        else:
            self.logger.error("*******Test checking politic failed*******")
            assert False

    def test_date(self):
        self.logger.info("*******Test_02_checking_date*******")
        dates = Date(self.driver)
        check_date = dates.checkDate()
        self.driver.save_screenshot(mainPage + "TestDate.png")

        if check_date == today:
            assert True
            self.logger.info("*******Test checking date passed*******")
        else:
            self.logger.error("*******Test checking date failed*******")
            assert False

    time.sleep(10)

    def test_weather(self):
        self.logger.info("*******Test_03_checking_weather*******")
        weather = Weather(self.driver)
        weather.Click()
        header = weather.get_weather()
        self.driver.save_screenshot(mainPage + "TestWeather.png")
        if header == "תחזית ליממה הקרובה":
            assert True
        else:
            self.logger.error("*******Test checking header failed*******")
            assert False

        eilat = weather.eilat_weather()

        if eilat == 'אילת':
            assert True
            self.logger.info("*******Test checking date passed*******")
        else:
            self.logger.error("*******Test checking weather failed*******")
            assert False

        telAviv = weather.tel_aviv_weather()
        if telAviv == 'תל אביב - יפו':
            assert True
            self.logger.info("*******Test checking telAviv passed*******")
        else:
            self.logger.error("*******Test checking telAviv failed*******")
            assert False

        Jerusalem = weather.jerusalem_weather()
        if Jerusalem == 'ירושלים':
            assert True
            self.logger.info("*******Test checking Jerusalem passed*******")
        else:
            self.logger.error("*******Test checking Jerusalem failed*******")
            assert False

        Ashdod = weather.ashdod_weather()
        if Ashdod == 'אשדוד':
            assert True
            self.logger.info("*******Test checking Ashdod passed*******")
        else:
            self.logger.error("*******Test checking Ashdod failed*******")
            assert False

        BeerSheva = weather.beer_sheva_weather()
        if BeerSheva == 'באר שבע':
            assert True
            self.logger.info("*******Test checking BeerSheva passed*******")
        else:
            self.logger.error("*******Test checking BeerSheva failed*******")
            assert False

        Haifa = weather.haifa_weather()
        if Haifa == 'חיפה':
            assert True
            self.logger.info("*******Test checking Haifa passed*******")
        else:
            self.logger.error("*******Test checking Haifa failed*******")
            assert False

        Zefat = weather.zefat_weather()
        if Zefat == 'צפת':
            assert True
            self.logger.info("*******Test checking Zefat passed*******")
        else:
            self.logger.error("*******Test checking Zefat failed*******")
            assert False

        Tveria = weather.tveria_weather()
        if Tveria == 'טבריה':
            assert True
            self.logger.info("*******Test checking Tveria passed*******")
        else:
            self.logger.error("*******Test checking Tveria failed*******")
            assert False