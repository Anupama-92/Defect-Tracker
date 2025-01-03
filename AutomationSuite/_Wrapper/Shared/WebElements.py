import time

import pyperclip

from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from AutomationSuite.Data.Actionkeys import ActionKeys
from AutomationSuite._Wrapper import helper
from AutomationSuite._Wrapper.Shared.Constants import Constants
from AutomationSuite._Wrapper.Shared.Util.TestLog import cogtestlog
from AutomationSuite.server.cog_webdriver_frontend import CogWebDriverFrontEnd


class WebElement(CogWebDriverFrontEnd):
    _log = cogtestlog()

    def __init__(self):
        CogWebDriverFrontEnd.__init__(self)
        self.h = helper

    @classmethod
    def find_element_by_id(cls, ID):
        if not cls._browser:
            raise ValueError("Browser not initialized. Call set_browser() first.")
        return cls._browser.find_element(By.ID, ID)

    @classmethod
    def find_element_by_xpath(cls, xpath):
        if not cls._browser:
            raise ValueError("Browser not initialized. Call set_browser() first.")
        return cls._browser.find_element(By.XPATH, xpath)

    @classmethod
    def find_element_by_class_name(cls, className):
        if not cls._browser:
            raise ValueError("Browser not initialized. Call set_browser() first.")
        return cls._browser.find_element(By.CLASS_NAME, className)

    @classmethod
    def find_element_by_name(cls, name):
        if not cls._browser:
            raise ValueError("Browser not initialized. Call set_browser() first.")
        return cls._browser.find_element(By.NAME, name)

    @classmethod
    def find_element_by_tag_name(cls, tagName):
        if not cls._browser:
            raise ValueError("Browser not initialized. Call set_browser() first.")
        return cls._browser.find_element(By.TAG_NAME, tagName)

    @classmethod
    def find_element_by_css_selector(cls, css_selector):
        if not cls._browser:
            raise ValueError("Browser not initialized. Call set_browser() first.")
        return cls._browser.find_element(By.CSS_SELECTOR, css_selector)

    @classmethod
    def find_element_by_link_text(cls, linkText):
        if not cls._browser:
            raise ValueError("Browser not initialized. Call set_browser() first.")
        return cls._browser.find_element(By.LINK_TEXT, linkText)

    @classmethod
    def find_element_by_partial_link_text(cls, partial_link_text):
        if not cls._browser:
            raise ValueError("Browser not initialized. Call set_browser() first.")
        return cls._browser.find_element(By.PARTIAL_LINK_TEXT, partial_link_text)

    @classmethod
    def find_elements_by_id(cls, ID):
        if not cls._browser:
            raise ValueError("Browser not initialized. Call set_browser() first.")
        return cls._browser.find_elements(By.ID, ID)

    @classmethod
    def find_elements_by_xpath(cls, xpath):
        if not cls._browser:
            raise ValueError("Browser not initialized. Call set_browser() first.")
        return cls._browser.find_elements(By.XPATH, xpath)

    @classmethod
    def find_elements_by_class_name(cls, className):
        if not cls._browser:
            raise ValueError("Browser not initialized. Call set_browser() first.")
        return cls._browser.find_elements(By.CLASS_NAME, className)

    @classmethod
    def find_elements_by_name(cls, name):
        if not cls._browser:
            raise ValueError("Browser not initialized. Call set_browser() first.")
        return cls._browser.find_elements(By.NAME, name)

    @classmethod
    def find_elements_by_tag_name(cls, tagName):
        if not cls._browser:
            raise ValueError("Browser not initialized. Call set_browser() first.")
        return cls._browser.find_elements(By.TAG_NAME, tagName)

    @classmethod
    def find_elements_by_css_selector(cls, css_selector):
        if not cls._browser:
            raise ValueError("Browser not initialized. Call set_browser() first.")
        return cls._browser.find_elements(By.CSS_SELECTOR, css_selector)

    @classmethod
    def find_elements_by_link_text(cls, link_text):
        if not cls._browser:
            raise ValueError("Browser not initialized. Call set_browser() first.")
        return cls._browser.find_elements(By.LINK_TEXT, link_text)

    @classmethod
    def find_elements_by_partial_link_text(cls, partial_link_text):
        if not cls._browser:
            raise ValueError("Browser not initialized. Call set_browser() first.")
        return cls._browser.find_elements(By.PARTIAL_LINK_TEXT, partial_link_text)

    @classmethod
    def go_back(cls):
        if not cls._browser:
            raise ValueError("Browser not initialized. Call set_browser() first.")
        cls._browser.back()

    @classmethod
    def go_forward(cls):
        if not cls._browser:
            raise ValueError("Browser not initialized. Call set_browser() first.")
        cls._browser.forward()

    @classmethod
    def refresh_page(cls):
        if not cls._browser:
            raise ValueError("Browser not initialized. Call set_browser() first.")
        cls._browser.refresh()

    @classmethod
    def close_browser(cls):
        if not cls._browser:
            raise ValueError("Browser not initialized. Call set_browser() first.")
        cls._browser.close()

    @classmethod
    def quit_browser(cls):
        if not cls._browser:
            raise ValueError("Browser not initialized. Call set_browser() first.")
        cls._browser.quit()

    @classmethod
    def get_page_title(cls):
        if not cls._browser:
            raise ValueError("Browser not initialized. Call set_browser() first.")
        return cls._browser.title

    @classmethod
    def implicitly_wait(cls, seconds):
        if not cls._browser:
            raise ValueError("Browser not initialized. Call set_browser() first.")
        cls._browser.implicitly_wait(seconds)

    @classmethod
    def press_key(cls, key):
        ActionChains(cls._browser).send_keys(key).perform()

    @classmethod
    def press_enter(cls):
        cls.press_key(ActionKeys.ENTER)

    @classmethod
    def press_tab(cls):
        cls.press_key(ActionKeys.TAB)

    @classmethod
    def switch_to_default_content(cls):
        cls._browser.switch_to.default_content()

    @classmethod
    def get_current_window_handle(cls):
        return cls._browser.current_window_handle

    @classmethod
    def accept_alert(cls):
        Alert(cls._browser).accept()

    @classmethod
    def dismiss_alert(cls):
        Alert(cls._browser).dismiss()

    @classmethod
    def get_alert_text(cls):
        return Alert(cls._browser).text

    @classmethod
    def execute_script(cls, script, *args):
        return cls._browser.execute_script(script, *args)

    @classmethod
    def execute_async_script(cls, script, *args):
        return cls._browser.execute_async_script(script, *args)

    @classmethod
    def get_cookies(cls):
        return cls._browser.get_cookies()

    @classmethod
    def add_cookie(cls, cookie_dict):
        cls._browser.add_cookie(cookie_dict)

    @classmethod
    def delete_cookie(cls, cookie_name):
        cls._browser.delete_cookie(cookie_name)

    @classmethod
    def delete_all_cookies(cls):
        cls._browser.delete_all_cookies()

    @classmethod
    def get_window_size(cls):
        return cls._browser.get_window_size()

    @classmethod
    def get_window_position(cls):
        return cls._browser.get_window_position()

    @classmethod
    def set_browser_size(cls, width, height):
        cls._browser.set_window_size(width, height)

    @classmethod
    def maximize_browser_window(cls):
        cls._browser.maximize_window()

    @classmethod
    def set_browser_position(cls, x, y):
        cls._browser.set_window_position(x, y)

    @classmethod
    def scroll_to_bottom(cls):
        cls._browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    @classmethod
    def switch_to_alert(cls):
        return cls._browser.switch_to.alert

    @classmethod
    def get_all_window_handles(cls):
        return cls._browser.window_handles

    @classmethod
    def wait_for_alert(cls, timeout=10):
        if not cls._browser:
            raise ValueError("Browser not initialized. Call set_browser() first.")
        return WebDriverWait(cls._browser, timeout).until(
            EC.alert_is_present()
        )

    @classmethod
    def verify_element_present(cls, element_locator, selector="xpath"):
        try:
            cls.find_element(element_locator, selector=selector)
            cls._log.info(f"Element located by {element_locator} is present.")
            return True
        except NoSuchElementException as e:
            cls._log.error(f"Element located by {element_locator} is not present. {e}")
            return False
        except TimeoutException as e:
            cls._log.error(f"Timeout waiting for element located by {element_locator}. {e}")
            return False
        except Exception as e:
            cls._log.error(f"An unexpected error occurred: {e}")
            return False

    @classmethod
    def verify_element_disappeared(cls, element_locator, selector="xpath", timeout=10):
        try:
            WebDriverWait(cls._browser, timeout).until_not(
                EC.visibility_of_element_located((selector, element_locator))
            )
            cls._log.info(f"Element located by {element_locator} has disappeared.")
            return True
        except TimeoutException as e:
            cls._log.error(f"Timeout waiting for element located by {element_locator} to disappear. {e}")
            return False
        except Exception as e:
            cls._log.error(f"An unexpected error occurred: {e}")
            return False

    @classmethod
    def verify_elements_present(cls, elements_locator, selector="xpath"):
        try:
            cls.is_element_displayed(elements_locator, selector=selector)
            cls._log.info(f"Element located by {elements_locator} is present.")
            return True
        except NoSuchElementException as e:
            cls._log.error(f"Element located by {elements_locator} is not present. {e}")
            return False
        except TimeoutException as e:
            cls._log.error(f"Timeout waiting for element located by {elements_locator}. {e}")
            return False
        except Exception as e:
            cls._log.error(f"An unexpected error occurred: {e}")
            return False

    @classmethod
    def verify_text_in_element(cls, element_locator, expected_text):
        element = cls.find_element(element_locator)
        actual_text = element.text
        try:
            assert expected_text == actual_text
            cls._log.info(f"Text in element is as expected: {expected_text}")
            return True
        except AssertionError:
            cls._log.error(f"Text in element doesn't match. Expected: {expected_text}, Actual: {actual_text}")
            return False

    @classmethod
    def verify_attribute_value(cls, element_locator, attribute, expected_value, selector="xpath"):
        element = cls.find_element(element_locator, selector=selector)
        actual_value = element.get_attribute(attribute)
        try:
            assert expected_value == actual_value
            cls._log.info(f"Attribute '{attribute}' has the expected value: {expected_value}")
            return True
        except AssertionError:
            cls._log.error(
                f"Attribute '{attribute}' value does not match. Expected: {expected_value}, Actual: {actual_value}")
            return False

    @classmethod
    def expect_element_present(cls, element_locator, selector="xpath"):
        try:
            cls.find_element(element_locator, selector=selector)
            cls._log.info(f"Element located by {element_locator} is present.")
        except AssertionError:
            cls._log.error(f"Element located by {element_locator} is not present.")
            raise AssertionError(f"Element located by {element_locator} is not present.")

    @classmethod
    def expect_text_in_element(cls, element_locator, expected_text, selector="xpath"):
        element = cls.find_element(element_locator, selector=selector)
        actual_text = element.text
        try:
            assert expected_text == actual_text
            cls._log.info(f"Text in element is as expected: {expected_text}")
        except AssertionError:
            cls._log.error(f"Text in element doesn't match. Expected: {expected_text}, Actual: {actual_text}")
            raise AssertionError(f"Text in element doesn't match. Expected: {expected_text}, Actual: {actual_text}")

    @classmethod
    def expect_attribute_value(cls, element_locator, attribute, expected_value, selector="xpath"):
        element = cls.find_element(element_locator, selector=selector)
        actual_value = element.get_attribute(attribute)
        try:
            assert expected_value == actual_value
            cls._log.info(f"Attribute '{attribute}' has the expected value: {expected_value}")
        except AssertionError:
            cls._log.error(
                f"Attribute '{attribute}' value does not match. Expected: {expected_value}, Actual: {actual_value}")
            raise AssertionError(
                f"Attribute '{attribute}' value does not match. Expected: {expected_value}, Actual: {actual_value}")

    @classmethod
    def verify_equal(cls, actual, expected, message=None):
        try:
            assert actual == expected, message
            cls._log.info(f"Verification passed: Actual value '{actual}' is equal to Expected value '{expected}'")
        except AssertionError as e:
            cls._log.error(f"Verification failed: {str(e)}")
            return False
        return True

    @classmethod
    def verify_not_equal(cls, actual, not_expected, message=None):
        try:
            assert actual != not_expected, message
            cls._log.info(
                f"Verification passed: Actual value '{actual}' is not equal to Not Expected value '{not_expected}'")
        except AssertionError as e:
            cls._log.error(f"Verification failed: {str(e)}")
            return False
        return True

    @classmethod
    def get_clipboard_data(cls):
        clipboard_data = pyperclip.paste()
        return clipboard_data

    @classmethod
    def set_clipboard_data(cls, data):
        pyperclip.copy(data)

    @classmethod
    def find_element(cls, element_locator, selector="xpath"):
        if not cls._browser:
            raise ValueError("Browser not initialized. Call set_browser() first.")
        if selector == "xpath":
            return cls.find_element_by_xpath(element_locator)
        if selector == "id":
            return cls.find_element_by_id(element_locator)
        if selector == "link text":
            return cls.find_element_by_link_text(element_locator)
        if selector == "partial link text":
            return cls.find_element_by_partial_link_text(element_locator)
        if selector == "name":
            return cls.find_element_by_name(element_locator)
        if selector == "tag name":
            return cls.find_element_by_tag_name(element_locator)
        if selector == "class name":
            return cls.find_element_by_class_name(element_locator)
        if selector == "css selector":
            return cls.find_element_by_css_selector(element_locator)

    @classmethod
    def find_elements(cls, elements_locator, selector='xpath'):
        if not cls._browser:
            raise ValueError("Browser not initialized. Call set_browser() first.")
        if selector == "xpath":
            return cls.find_elements_by_xpath(elements_locator)
        if selector == "id":
            return cls.find_elements_by_id(elements_locator)
        if selector == "link text":
            return cls.find_elements_by_link_text(elements_locator)
        if selector == "partial link text":
            return cls.find_elements_by_partial_link_text(elements_locator)
        if selector == "name":
            return cls.find_elements_by_name(elements_locator)
        if selector == "tag name":
            return cls.find_elements_by_tag_name(elements_locator)
        if selector == "class name":
            return cls.find_elements_by_class_name(elements_locator)
        if selector == "css selector":
            return cls.find_elements_by_css_selector(elements_locator)

    @classmethod
    def click_element(cls, element_locator, selector="xpath"):
        if not cls._browser:
            raise ValueError("Browser not initialized. Call set_browser() first.")
        element = cls.find_element(element_locator, selector)
        element.click()

    @classmethod
    def send_keys_to_element(cls, element_locator, keys, selector="xpath"):
        if not cls._browser:
            raise ValueError("Browser not initialized. Call set_browser() first.")
        element = cls.find_element(element_locator, selector)
        element.send_keys(keys)

    @classmethod
    def wait_for_element_presence(cls, element_locator, timeout=Constants.short_live_throttle, selector="xpath"):
        if not cls._browser:
            raise ValueError("Browser not initialized. Call set_browser() first.")
        if selector == "xpath":
            return WebDriverWait(cls._browser, timeout).until(
                EC.presence_of_element_located((By.XPATH, element_locator)))
        if selector == "id":
            return WebDriverWait(cls._browser, timeout).until(
                EC.presence_of_element_located((By.ID, element_locator)))
        if selector == "link text":
            return WebDriverWait(cls._browser, timeout).until(
                EC.presence_of_element_located((By.LINK_TEXT, element_locator)))
        if selector == "partial link text":
            return WebDriverWait(cls._browser, timeout).until(
                EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, element_locator)))
        if selector == "name":
            return WebDriverWait(cls._browser, timeout).until(
                EC.presence_of_element_located((By.NAME, element_locator)))
        if selector == "tag name":
            return WebDriverWait(cls._browser, timeout).until(
                EC.presence_of_element_located((By.TAG_NAME, element_locator)))
        if selector == "class name":
            return WebDriverWait(cls._browser, timeout).until(
                EC.presence_of_element_located((By.CLASS_NAME, element_locator)))
        if selector == "css selector":
            return WebDriverWait(cls._browser, timeout).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, element_locator)))

    @classmethod
    def wait_for_all_elements_presence(cls, elements_locator, timeout=Constants.short_live_throttle, selector="xpath"):
        if not cls._browser:
            raise ValueError("Browser not initialized. Call set_browser() first.")
        if selector == "xpath":
            return WebDriverWait(cls._browser, timeout).until(
                EC.presence_of_all_elements_located((By.XPATH, elements_locator)))
        if selector == "id":
            return WebDriverWait(cls._browser, timeout).until(
                EC.presence_of_all_elements_located((By.ID, elements_locator)))
        if selector == "link text":
            return WebDriverWait(cls._browser, timeout).until(
                EC.presence_of_all_elements_located((By.LINK_TEXT, elements_locator)))
        if selector == "partial link text":
            return WebDriverWait(cls._browser, timeout).until(
                EC.presence_of_all_elements_located((By.PARTIAL_LINK_TEXT, elements_locator)))
        if selector == "name":
            return WebDriverWait(cls._browser, timeout).until(
                EC.presence_of_all_elements_located((By.NAME, elements_locator)))
        if selector == "tag name":
            return WebDriverWait(cls._browser, timeout).until(
                EC.presence_of_all_elements_located((By.TAG_NAME, elements_locator)))
        if selector == "class name":
            return WebDriverWait(cls._browser, timeout).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, elements_locator)))
        if selector == "css selector":
            return WebDriverWait(cls._browser, timeout).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, elements_locator)))

    @classmethod
    def wait_for_element_clickable(cls, element_locator, timeout=Constants.short_live_throttle, selector="xpath"):
        if not cls._browser:
            raise ValueError("Browser not initialized. Call set_browser() first.")
        if selector == "xpath":
            return WebDriverWait(cls._browser, timeout).until(
                EC.element_to_be_clickable((By.XPATH, element_locator)))
        if selector == "id":
            return WebDriverWait(cls._browser, timeout).until(
                EC.element_to_be_clickable((By.ID, element_locator)))
        if selector == "link text":
            return WebDriverWait(cls._browser, timeout).until(
                EC.element_to_be_clickable((By.LINK_TEXT, element_locator)))
        if selector == "partial link text":
            return WebDriverWait(cls._browser, timeout).until(
                EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, element_locator)))
        if selector == "name":
            return WebDriverWait(cls._browser, timeout).until(
                EC.element_to_be_clickable((By.NAME, element_locator)))
        if selector == "tag name":
            return WebDriverWait(cls._browser, timeout).until(
                EC.element_to_be_clickable((By.TAG_NAME, element_locator)))
        if selector == "class name":
            return WebDriverWait(cls._browser, timeout).until(
                EC.element_to_be_clickable((By.CLASS_NAME, element_locator)))
        if selector == "css selector":
            return WebDriverWait(cls._browser, timeout).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, element_locator)))

    @classmethod
    def wait_for_visibility_of_element(cls, element_locator, timeout=Constants.short_live_throttle, selector="xpath"):
        if not cls._browser:
            raise ValueError("Browser not initialized. Call set_browser() first.")
        if selector == "xpath":
            return WebDriverWait(cls._browser, timeout).until(
                EC.visibility_of_element_located((By.XPATH, element_locator)))
        if selector == "id":
            return WebDriverWait(cls._browser, timeout).until(
                EC.visibility_of_element_located((By.ID, element_locator)))
        if selector == "link text":
            return WebDriverWait(cls._browser, timeout).until(
                EC.visibility_of_element_located((By.LINK_TEXT, element_locator)))
        if selector == "partial link text":
            return WebDriverWait(cls._browser, timeout).until(
                EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, element_locator)))
        if selector == "name":
            return WebDriverWait(cls._browser, timeout).until(
                EC.visibility_of_element_located((By.NAME, element_locator)))
        if selector == "tag name":
            return WebDriverWait(cls._browser, timeout).until(
                EC.visibility_of_element_located((By.TAG_NAME, element_locator)))
        if selector == "class name":
            return WebDriverWait(cls._browser, timeout).until(
                EC.visibility_of_element_located((By.CLASS_NAME, element_locator)))
        if selector == "css selector":
            return WebDriverWait(cls._browser, timeout).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, element_locator)))

    @classmethod
    def wait_for_visibility_of_all_elements(cls, elements_locator, timeout=Constants.short_live_throttle,
                                            selector="xpath"):
        if not cls._browser:
            raise ValueError("Browser not initialized. Call set_browser() first.")
        if selector == "xpath":
            return WebDriverWait(cls._browser, timeout).until(
                EC.visibility_of_all_elements_located((By.XPATH, elements_locator)))
        if selector == "id":
            return WebDriverWait(cls._browser, timeout).until(
                EC.visibility_of_all_elements_located((By.ID, elements_locator)))
        if selector == "link text":
            return WebDriverWait(cls._browser, timeout).until(
                EC.visibility_of_all_elements_located((By.LINK_TEXT, elements_locator)))
        if selector == "partial link text":
            return WebDriverWait(cls._browser, timeout).until(
                EC.visibility_of_all_elements_located((By.PARTIAL_LINK_TEXT, elements_locator)))
        if selector == "name":
            return WebDriverWait(cls._browser, timeout).until(
                EC.visibility_of_all_elements_located((By.NAME, elements_locator)))
        if selector == "tag name":
            return WebDriverWait(cls._browser, timeout).until(
                EC.visibility_of_all_elements_located((By.TAG_NAME, elements_locator)))
        if selector == "class name":
            return WebDriverWait(cls._browser, timeout).until(
                EC.visibility_of_all_elements_located((By.CLASS_NAME, elements_locator)))
        if selector == "css selector":
            return WebDriverWait(cls._browser, timeout).until(
                EC.visibility_of_all_elements_located((By.CSS_SELECTOR, elements_locator)))

    @classmethod
    def wait_for_visibility_of_any_elements(cls, elements_locator, timeout=Constants.short_live_throttle,
                                            selector="xpath"):
        if not cls._browser:
            raise ValueError("Browser not initialized. Call set_browser() first.")
        if selector == "xpath":
            return WebDriverWait(cls._browser, timeout).until(
                EC.visibility_of_any_elements_located((By.XPATH, elements_locator)))
        if selector == "id":
            return WebDriverWait(cls._browser, timeout).until(
                EC.visibility_of_any_elements_located((By.ID, elements_locator)))
        if selector == "link text":
            return WebDriverWait(cls._browser, timeout).until(
                EC.visibility_of_any_elements_located((By.LINK_TEXT, elements_locator)))
        if selector == "partial link text":
            return WebDriverWait(cls._browser, timeout).until(
                EC.visibility_of_any_elements_located((By.PARTIAL_LINK_TEXT, elements_locator)))
        if selector == "name":
            return WebDriverWait(cls._browser, timeout).until(
                EC.visibility_of_any_elements_located((By.NAME, elements_locator)))
        if selector == "tag name":
            return WebDriverWait(cls._browser, timeout).until(
                EC.visibility_of_any_elements_located((By.TAG_NAME, elements_locator)))
        if selector == "class name":
            return WebDriverWait(cls._browser, timeout).until(
                EC.visibility_of_any_elements_located((By.CLASS_NAME, elements_locator)))
        if selector == "css selector":
            return WebDriverWait(cls._browser, timeout).until(
                EC.visibility_of_any_elements_located((By.CSS_SELECTOR, elements_locator)))

    @classmethod
    def wait_for_invisibility_of_element(cls, element_locator, timeout=Constants.short_live_throttle, selector="xpath"):
        if not cls._browser:
            raise ValueError("Browser not initialized. Call set_browser() first.")
        if selector == "xpath":
            return WebDriverWait(cls._browser, timeout).until(
                EC.invisibility_of_element_located((By.XPATH, element_locator)))
        if selector == "id":
            return WebDriverWait(cls._browser, timeout).until(
                EC.invisibility_of_element_located((By.ID, element_locator)))
        if selector == "link text":
            return WebDriverWait(cls._browser, timeout).until(
                EC.invisibility_of_element_located((By.LINK_TEXT, element_locator)))
        if selector == "partial link text":
            return WebDriverWait(cls._browser, timeout).until(
                EC.invisibility_of_element_located((By.PARTIAL_LINK_TEXT, element_locator)))
        if selector == "name":
            return WebDriverWait(cls._browser, timeout).until(
                EC.invisibility_of_element_located((By.NAME, element_locator)))
        if selector == "tag name":
            return WebDriverWait(cls._browser, timeout).until(
                EC.invisibility_of_element_located((By.TAG_NAME, element_locator)))
        if selector == "class name":
            return WebDriverWait(cls._browser, timeout).until(
                EC.invisibility_of_element_located((By.CLASS_NAME, element_locator)))
        if selector == "css selector":
            return WebDriverWait(cls._browser, timeout).until(
                EC.invisibility_of_element_located((By.CSS_SELECTOR, element_locator)))

    @classmethod
    def wait_for_text_to_be_present_in_element(cls, element_locator, text, timeout=Constants.short_live_throttle,
                                               selector="xpath"):
        if not cls._browser:
            raise ValueError("Browser not initialized. Call set_browser() first.")
        if selector == "xpath":
            return WebDriverWait(cls._browser, timeout).until(
                EC.text_to_be_present_in_element((By.XPATH, element_locator), text))
        if selector == "id":
            return WebDriverWait(cls._browser, timeout).until(
                EC.text_to_be_present_in_element((By.ID, element_locator), text))
        if selector == "link text":
            return WebDriverWait(cls._browser, timeout).until(
                EC.text_to_be_present_in_element((By.LINK_TEXT, element_locator), text))
        if selector == "partial link text":
            return WebDriverWait(cls._browser, timeout).until(
                EC.text_to_be_present_in_element((By.PARTIAL_LINK_TEXT, element_locator), text))
        if selector == "name":
            return WebDriverWait(cls._browser, timeout).until(
                EC.text_to_be_present_in_element((By.NAME, element_locator), text))
        if selector == "tag name":
            return WebDriverWait(cls._browser, timeout).until(
                EC.text_to_be_present_in_element((By.TAG_NAME, element_locator), text))
        if selector == "class name":
            return WebDriverWait(cls._browser, timeout).until(
                EC.text_to_be_present_in_element((By.CLASS_NAME, element_locator), text))
        if selector == "css selector":
            return WebDriverWait(cls._browser, timeout).until(
                EC.text_to_be_present_in_element((By.CSS_SELECTOR, element_locator), text))

    @classmethod
    def is_element_displayed(cls, element_locator, selector="xpath"):
        element = cls.find_element(element_locator, selector=selector)
        return element.is_displayed()

    @classmethod
    def is_element_not_displayed(cls, element_locator, selector="xpath"):
        try:
            element = cls.find_element(element_locator, selector=selector)
            return not element.is_displayed()
        except NoSuchElementException:
            # Element not found, consider it as not displayed
            return True

    @classmethod
    def is_element_enabled(cls, element_locator, selector="xpath"):
        element = cls.find_element(element_locator, selector=selector)
        return element.is_enabled()

    @classmethod
    def is_element_not_enabled(cls, element_locator, selector="xpath"):
        try:
            element = cls.find_element(element_locator, selector=selector)
            return not element.is_enabled()
        except NoSuchElementException:
            # Element not found, consider it as not enabled
            return True

    @classmethod
    def clear_element(cls, element_locator, selector="xpath"):
        element = cls.find_element(element_locator, selector=selector)
        element.clear()

    @classmethod
    def get_text(cls, element_locator, selector="xpath"):
        element = cls.find_element(element_locator, selector="xpath")
        return element.text

    @classmethod
    def get_attribute(cls, element_locator, attribute_name, selector="xpath"):
        element = cls.find_element(element_locator, selector=selector)
        return element.get_attribute(attribute_name)

    @classmethod
    def perform_hover(cls, element_locator, selector="xpath"):
        element = cls.find_element(element_locator, selector=selector)
        ActionChains(cls._browser).move_to_element(element).perform()

    @classmethod
    def select_dropdown_option_by_value(cls, element_locator, option_value, selector="xpath"):
        element = cls.find_element(element_locator, selector=selector)
        select = Select(element)
        select.select_by_value(option_value)

    @classmethod
    def select_dropdown_option_by_index(cls, element_locator, index, selector="xpath"):
        element = cls.find_element(element_locator, selector=selector)
        select = Select(element)
        select.select_by_index(index)

    @classmethod
    def select_dropdown_option_by_visible_text(cls, element_locator, visible_text, selector="xpath"):
        element = cls.find_element(element_locator, selector=selector)
        select = Select(element)
        select.select_by_visible_text(visible_text)

    @classmethod
    def drag_and_drop(cls, source_element_locator, target_element_locator, selector="xpath"):
        source_element = cls.find_element(source_element_locator, selector=selector)
        target_element = cls.find_element(target_element_locator, selector=selector)
        ActionChains(cls._browser).drag_and_drop(source_element, target_element).perform()

    @classmethod
    def scroll_to_element(cls, element_locator, selector="xpath"):
        element = cls.find_element(element_locator, selector=selector)
        cls._browser.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(1)

    @classmethod
    def accept_cert(cls):
        cls._browser.get("javascript:document.getElementById('overridelink').click()")
        return "ok"

    @classmethod
    def get_screenshot(cls, filename):
        cls._browser.get_screenshot_as_file(filename)

    @classmethod
    def switch_to_window_by_handle(cls, window_handle):
        cls._browser.switch_to.window(window_handle)

    @classmethod
    def switch_to_frame_by_index(cls, index):
        cls._browser.switch_to.frame(index)

    @classmethod
    def switch_to_frame_by_name_or_id(cls, frame_name_or_id):
        cls._browser.switch_to.frame(frame_name_or_id)

    @classmethod
    def get_texts_of_elements(cls, elements_locator, selector="xpath"):
        elements = cls.find_elements(elements_locator=elements_locator, selector=selector)
        return [element.text for element in elements]

    @classmethod
    def select_all(cls, element_locator, selector="xpath"):
        cls.send_keys_to_element(element_locator=element_locator,selector=selector, keys=Keys.CONTROL + 'a')

    @classmethod
    def clear_input(cls, element_locator, selector="xpath"):
        cls.select_all(element_locator=element_locator, selector=selector)
        element = cls.find_element(element_locator=element_locator, selector=selector)
        element.clear()
