from AutomationSuite._Fragments.BaseFragments.base_fragments import BasePageFragments
from AutomationSuite._Locators.DTLocators.dt_locator import dtListPageLocators


class DTListPage(BasePageFragments):

    def __init__(self):
        BasePageFragments.__init__(self)

    @staticmethod
    def select_project():
        return dtListPageLocators().select_project


class SelectProject(DTListPage):
    def wait_for_load(self, timeout=Constants.long_throttle):
        self.h.verify(lambda: self.verify_element_present(self.firstname(), selector="id"), timeout=timeout,
                      fail_message="Add Contact screen failed to load")

    def run(self, select_project = None, timeout=Constants.default_throttle):
        self.wait_for_load(timeout)
        if select_project is not None:
            self.select_dropdown_option_by_visible_text(element_locator=self.type(), selector="id", visible_text=select_project)