from time import sleep
from AutomationSuite._Locators.BaseLocators.base_locators import BaseLocators
from AutomationSuite._Wrapper.Shared.Constants import Constants
from AutomationSuite._Wrapper.Shared.WebElements import WebElement



class BasePageFragments(WebElement):

    def __init__(self):
        WebElement.__init__(self)

    @staticmethod
    def app_item():
        return BaseLocators().app