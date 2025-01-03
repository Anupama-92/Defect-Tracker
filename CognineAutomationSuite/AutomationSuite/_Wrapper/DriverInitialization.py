from selenium.webdriver.remote.webdriver import WebDriver


class DriverInitialization:
    # Class variable to store the driver
    _browser = None

    @classmethod
    def set_driver(cls, driver: WebDriver):
        if not isinstance(driver, WebDriver):
            raise TypeError("Invalid driver type. Must be an instance of WebDriver.")
        cls._browser = driver

    @property
    def browser(self):
        return self._browser