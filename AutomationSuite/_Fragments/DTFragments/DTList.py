from AutomationSuite._Fragments.BaseFragments.base_fragments import BasePageFragments
from AutomationSuite._Locators.DTLocators.dt_locator import dtListPageLocators


class CRMCompanyPage(BasePageFragments):

    def __init__(self):
        BasePageFragments.__init__(self)

    @staticmethod
    def selectproject():
        return dtListPageLocators().select_project