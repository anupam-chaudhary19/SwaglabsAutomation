import configparser

config = configparser.RawConfigParser()
config.read("/Users/Anupam/PycharmProjects/SwaglabsAutomation/Configuration/config.ini")

class Readconfig:

    @staticmethod
    def getApplicationURL():
        url = config.get("https://www.saucedemo.com/")
        return url

    @staticmethod
    def getUsername():
        username = config.get('common values', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common values', 'password')
        return password
