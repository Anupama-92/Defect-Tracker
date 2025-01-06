from AutomationSuite.Data.DTData import Modules
from AutomationSuite._Fragments.BaseFragments.base_fragments import BasePageFragments
from AutomationSuite._Locators.DTLocators.dt_locator import dtListPageLocators
from AutomationSuite._Wrapper.Shared.Constants import Constants


class DTListPage(BasePageFragments):

    def __init__(self):
        BasePageFragments.__init__(self)

    @staticmethod
    def select_project():
        return dtListPageLocators().select_project

    def navigate_to_module(self, module):
        self.click_sub_module(module_name=Modules().select_project, sub_module_name=sub_module)


class SelectProject(DTListPage):
    def wait_for_load(self, timeout=Constants.long_throttle,switch=False):
        if switch:
            self.switch_to_frame_by_index(0)
            self.h.verify(lambda: self.verify_element_present(self.select_project(), selector="id"), timeout=timeout,
                      fail_message="Screen failed to load")

    def run(self, select_project=None, timeout=Constants.default_throttle):
        self.wait_for_load(timeout)
        if select_project is not None:
            self.send_keys_to_element(element_locator=self.select_project(), selector="id", keys=select_project)