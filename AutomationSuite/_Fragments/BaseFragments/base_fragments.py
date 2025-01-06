from time import sleep
from AutomationSuite._Locators.BaseLocators.base_locator import BaseLocators
from AutomationSuite._Wrapper.Shared.Constants import Constants
from AutomationSuite._Wrapper.Shared.WebElements import WebElement


class BasePageFragments(WebElement):

    def __init__(self):
        WebElement.__init__(self)

    @staticmethod
    def app_item():
        return BaseLocators().app

    @staticmethod
    def switch_to_frame():
        return BaseLocators().iframe

    @staticmethod
    def select_project():
        return BaseLocators().select_project

    @staticmethod
    def modules():
        return BaseLocators().modules

    @staticmethod
    def module():
        return BaseLocators().module

    @staticmethod
    def sub_module():
        return BaseLocators().sub_module

    @staticmethod
    def project_selection():
        return BaseLocators().project_selection

    @staticmethod
    def toggle_switch():
        return BaseLocators().toggle_switch

    @staticmethod
    def popup_yes_btn():
        return BaseLocators().popup_yes_btn

    @staticmethod
    def popup_close_btn():
        return BaseLocators().popup_close_btn

    @staticmethod
    def success_alert():
        return BaseLocators().success_text

    def navigate_to_app(self, app_name):
        menu_name_path = self.app_item() % f"{app_name}"
        self.click_element(element_locator=menu_name_path)

    def switch_to_iframe(self, iframe_locator):
        iframe_element = self.find_element(element_locator=iframe_locator)
        # Switch to the iframe
        self.switch_to.frame(iframe_element)

    def grid_wait_for_load(self, ready_state=None, switch=False):
        fail_message = f'Table wait_for_load failed. Table in page did not load.'

        # Most to all tables are housed within the default frame.
        # Calling this item here to avoid having to call it throughout all tests.
        sleep(2)
        if switch:
            self.switch_to_frame_by_index(0)
        if ready_state == 'loaded':
            self.h.verify(lambda: self.verify_element_present(self.table_1st_row()), timeout=Constants.default_throttle,
                          fail_message=fail_message)
        elif ready_state == 'loading':
            self.h.verify(lambda: self.verify_element_present(self.table_1st_row()) or self.verify_element_present(
                self.table_no_data()),
                          timeout=Constants.default_throttle,
                          fail_message=fail_message)
        elif ready_state == 'no results':
            self.h.verify(lambda: self.verify_element_present(self.table_no_data()),
                          timeout=Constants.default_throttle,
                          fail_message=fail_message)
        else:
            self._log.error(f"Provide the ready_state for the table_wait_for_load.")

    def get_modules(self, switch=False):
        sleep(2)
        if switch:
            self.switch_to_frame_by_index(0)
        return self.get_texts_of_elements(elements_locator=self.modules())

    def hover_to_module(self, module_name, switch=False):
        sleep(1)
        if switch:
            self.switch_to_frame_by_index(0)
        self.perform_hover(element_locator=self.module().format(module_name))

    def navigate_to_module(self, module_name, switch=False):
        sleep(1)
        if switch:
            self.switch_to_frame_by_index(0)
        self.click_element(element_locator=self.module().format(module_name))

    def click_sub_module(self, module_name, sub_module_name, switch=False, selector="xpath"):
        sleep(1)
        if switch:
            self.switch_to_frame_by_index(0)
        self.hover_to_module(module_name)
        self.click_element(element_locator=self.sub_module().format(sub_module_name), selector=selector)

    def verify_success(self, timeout=Constants.long_throttle):
        self.h.verify(lambda: self.verify_element_present(self.success_alert()), timeout=timeout,
                      fail_message="Success toast failed to load or Operation is not successful")

    def verify_success_alert_disappeared(self, timeout=Constants.long_throttle):
        self.h.verify(lambda: self.verify_element_disappeared(self.success_alert()), timeout=timeout,
                      fail_message="Success toast failed to disappear or Operation is not successful")
