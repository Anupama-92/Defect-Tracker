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
    def table_1st_row():
        return BaseLocators().table_1st_row

    @staticmethod
    def table_no_data():
        return BaseLocators().table_no_data

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
    def row_in_div():
        return BaseLocators().row_in_div

    @staticmethod
    def row_in_td():
        return BaseLocators().row_in_td

    @staticmethod
    def row_in_a():
        return BaseLocators().row_in_a

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

    @staticmethod
    def multi_select_dropdown_select_all():
        return BaseLocators().multi_select_dropdown_select_all

    @staticmethod
    def multi_select_dropdown_search():
        return BaseLocators().multi_select_dropdown_search

    @staticmethod
    def multi_select_dropdown_option():
        return BaseLocators().multi_select_dropdown_option

    def navigate_to_app(self, app_name):
        menu_name_path = self.app_item() % f"{app_name}"
        self.click_element(element_locator=menu_name_path)

    def grid_wait_for_load(self, ready_state=None, switch=False):
        """
        Standard table_wait_for_load for a table. By default, it verifies that one of the three criteria is true.
        If a specific ready_state value is provided, it only checks
        one validation rule.

        * Please note that loading & loaded are case-sensitive & must be lowed case *

        1.) 'loaded' = at least 1 row and cell with data is loaded.
        2.) 'no results' = "No Data Found" text is displayed in list view
        3.) 'loading' = means the list view autoloads, but you aren't sure that there are records or no records found
        """
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
        print("Testing")
        sleep(1)
        if switch:
            self.switch_to_frame_by_name_or_id("applicationId")
            print("Switched to Iframe")
        self.click_element(element_locator=self.module().format(module_name))

    def click_sub_module(self, module_name, sub_module_name, switch=False, selector="xpath"):
        sleep(1)
        if switch:
            self.switch_to_frame_by_index(0)
        self.hover_to_module(module_name)
        self.click_element(element_locator=self.sub_module().format(sub_module_name), selector=selector)

    def click_on_row_name_in_grid(self, row_name=None):
        fail_message = "Row not found"
        if row_name is not None:
            if self.h.verify(lambda: self.verify_element_present(self.row_in_div().format(row_name)),
                             timeout=Constants.default_throttle, fail_message=fail_message):
                self.scroll_to_element(element_locator=self.row_in_div().format(row_name))
                self.click_element(element_locator=self.row_in_div().format(row_name))
            elif self.h.verify(lambda: self.verify_element_present(self.row_in_a().format(row_name)),
                               timeout=Constants.default_throttle, fail_message=fail_message):
                self.scroll_to_element(element_locator=self.row_in_div().format(row_name))
                self.click_element(element_locator=self.row_in_a().format(row_name))
            elif self.h.verify(lambda: self.verify_element_present(self.row_in_td().format(row_name)),
                               timeout=Constants.default_throttle, fail_message=fail_message):
                self.scroll_to_element(element_locator=self.row_in_div().format(row_name))
                self.click_element(element_locator=self.row_in_td().format(row_name))

    def click_toggle_switch_in_grid(self, click=True):
        if click:
            self.click_element(element_locator=self.toggle_switch())

    def handle_crm_popup(self, click_yes=True, click_close=False):
        if click_yes:
            self.click_element(element_locator=self.popup_yes_btn())
        if click_close:
            self.click_element(element_locator=self.popup_close_btn())

    def verify_success(self, timeout=Constants.long_throttle):
        self.h.verify(lambda: self.verify_element_present(self.success_alert()), timeout=timeout,
                      fail_message="Success toast failed to load or Operation is not successful")

    def verify_success_alert_disappeared(self, timeout=Constants.long_throttle):
        self.h.verify(lambda: self.verify_element_disappeared(self.success_alert()), timeout=timeout,
                      fail_message="Success toast failed to disappear or Operation is not successful")
