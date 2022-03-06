import logging


class LoggerYit:
    @staticmethod
    def Logger():
        logger = logging.getLogger("YitLog")
        logger.setLevel(logging.DEBUG)
        fileHandler = logging.FileHandler("C:\\Users\\haim\\PycharmProjects\\AutomationProject\\Logs\\yit.log")
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s : %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        return logger

