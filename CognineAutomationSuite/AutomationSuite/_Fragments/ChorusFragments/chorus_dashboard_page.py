from AutomationSuite._Fragments.BaseFragments.base_fragments import BasePageFragments
from AutomationSuite._Locators.ChorusLocators.DashboardPageLocators.dashboardpage_locators import \
    ChorusDashboardPageLocators
from AutomationSuite._Wrapper.Shared.Constants import Constants


class ChorusDashboardPage(BasePageFragments):

    def __init__(self):
        BasePageFragments.__init__(self)

    @staticmethod
    def cognine_logo():
        return ChorusDashboardPageLocators().cognine_logo

    @staticmethod
    def DT_label():
        return ChorusDashboardPageLocators().DT_label

    def wait_for_load(self, timeout=Constants.default_throttle):
        self.h.verify(lambda: self.verify_element_present(self.cognine_logo()), timeout=timeout,
                      fail_message="Chorus Dashboard screen failed to load")
