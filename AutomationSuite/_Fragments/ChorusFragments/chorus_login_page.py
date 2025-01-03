import time

from AutomationSuite._Fragments.BaseFragments.base_fragments import BasePageFragments
from AutomationSuite._Locators.ChorusLocators.LoginPageLocators.loginpage_locators import ChorusLoginPageLocators
from AutomationSuite._Wrapper.Shared.Constants import Constants


class ChorusLoginPage(BasePageFragments):

    def __init__(self):
        BasePageFragments.__init__(self)

    @staticmethod
    def email_id_field():
        return ChorusLoginPageLocators().email_id_field

    @staticmethod
    def next_btn():
        return ChorusLoginPageLocators().next_btn

    @staticmethod
    def password_field():
        return ChorusLoginPageLocators().password_field

    @staticmethod
    def sign_in_btn():
        return ChorusLoginPageLocators().sign_in_btn

    @staticmethod
    def dont_show_again():
        return ChorusLoginPageLocators().dont_show_again_checkbox

    @staticmethod
    def forget_password_link():
        return ChorusLoginPageLocators().forget_password_link

    @staticmethod
    def yes_btn():
        return ChorusLoginPageLocators().yes_btn

    @staticmethod
    def no_btn():
        return ChorusLoginPageLocators().no_btn

    def wait_for_load(self, timeout=Constants.long_throttle):
        self.h.verify(lambda: self.verify_element_present(self.email_id_field(), selector="id"), timeout=timeout,
                      fail_message="Login screen failed to load")

    def run_login(self, email_id=None, next_btn=True, password=None, sign_in=True, dont_show=False,
                  forget_password=False,
                  yes_btn=True, no_btn=False, timeout=Constants.default_throttle):
        self.wait_for_load(timeout)
        if email_id is not None:
            self.send_keys_to_element(element_locator=self.email_id_field(), selector="id", keys=email_id)
            time.sleep(1)
        if next_btn:
            self.click_element(element_locator=self.next_btn(), selector="id")
            time.sleep(2)
        if password is not None:
            self.send_keys_to_element(element_locator=self.password_field(), selector="id", keys=password)
        if sign_in:
            self.click_element(element_locator=self.sign_in_btn(), selector="id")
            time.sleep(2)
        if dont_show:
            self.click_element(element_locator=self.dont_show_again(), selector="id")
        if forget_password:
            self.click_element(element_locator=self.forget_password_link(), selector="id")
        if yes_btn:
            self.click_element(element_locator=self.yes_btn(), selector="id")
        if no_btn:
            self.click_element(element_locator=self.no_btn(), selector="id")
