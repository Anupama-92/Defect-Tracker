from AutomationSuite.Data.DTData import Modules
from AutomationSuite._Fragments.BaseFragments.base_fragments import BasePageFragments
from AutomationSuite._Locators.DTLocators.dt_locator import dtListPageLocators
from AutomationSuite._Wrapper.Shared.Constants import Constants


class DTListPage(BasePageFragments):

    def __init__(self):
        BasePageFragments.__init__(self)

    @staticmethod
    def select_project():
        print("Testing")
        return dtListPageLocators().select_project

    def navigate_to_sub_module(self, sub_module):
        self.click_sub_module(module_name=Modules().defect_list, sub_module_name=sub_module)


class DefectListPage(DTListPage):
    def wait_for_load(self, timeout=Constants.long_throttle):
        self.h.verify(lambda: self.verify_element_present(self.select_project()), timeout=timeout,
                      fail_message="Project selection failed to load")

    def run(self, select_project=None, timeout=Constants.default_throttle):
        self.wait_for_load(timeout)
        if select_project is not None:
            self.select_dropdown_option_by_value(element_locator=self.select_project(), option_value=select_project)

