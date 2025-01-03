import platform

from selenium import webdriver
from AutomationSuite._Wrapper.DriverInitialization import DriverInitialization
from AutomationSuite._Wrapper.Shared.Util.TestLog import cogtestlog
from AutomationSuite._Wrapper.Shared.Util.logger import COGStaticLogger


class CogWebDriverFrontEnd(DriverInitialization):
    def __init__(self):
        self._log = cogtestlog()

    @classmethod
    def start(cls, browser):
        if "chrome" in browser:
            from selenium.webdriver.chrome.options import Options
            o = Options()
            o.add_argument("--incognito")
            o.add_argument("--start-maximized")
            o.add_argument('--ignore-certificate-errors')
            o.add_argument('--ignore-ssl-errors')

            _browser = webdriver.Chrome(options=o)
        elif "edge" in browser:
            from selenium.webdriver.edge.options import Options as EdgeOptions
            options = EdgeOptions()
            options.use_chromium = True
            options.add_argument("--inprivate")
            options.add_argument("--start-maximized")
            options.add_argument('--ignore-certificate-errors')
            options.add_argument('--ignore-ssl-errors')

            _browser = webdriver.Edge(options=options)
        elif "firefox" in browser:
            from selenium.webdriver.firefox.options import Options as FirefoxOptions
            options = FirefoxOptions()
            # Private browsing mode (equivalent to --in-private)
            options.set_preference("browser.privatebrowsing.autostart", True)
            # Start maximized (equivalent to --start-maximized)
            options.add_argument("--start-maximized")
            # Ignore certificate errors
            options.accept_untrusted_certs = True
            options.assume_untrusted_cert_issuer = True

            _browser = webdriver.Firefox(options=options)
        elif "safari" in browser:
            if platform.system() is 'Darwin':
                from selenium.webdriver.safari.options import Options as SafariOptions
                options = SafariOptions()
                # Private browsing mode (equivalent to --in-private)
                options.set_capability("safari:useAutomaticInspection", False)
                options.set_capability("safari:useTechnologyPreview", False)
                # Ignore certificate errors
                options.set_capability("acceptInsecureCerts", True)
                _browser = webdriver.Safari(options=options)
            else:
                raise ValueError(f"Invalid OS to run: {browser}")
        else:
            raise ValueError(f"Invalid browser name: {browser}")

        _browser.maximize_window()

        COGStaticLogger._browser = _browser

        _mouse = webdriver.ActionChains(_browser)

        _window_handle = _browser.window_handles[0]

        # always switch to the first window
        _browser.switch_to.window(_window_handle)

        DriverInitialization().set_driver(_browser)

    @classmethod
    def open_url(cls, browser, url):
        cls.start(browser)
        cls._browser.get(url)

    @classmethod
    def open_url_in_chrome(cls, url):

        return cls.open_url(browser="chrome", url=url)

    def open_url_in_edge(self, url, request):

        return self.open_url(browser="edge", url=url)

    @property
    def current_url(self):
        return self._browser.current_url

    def set_url(self, url):
        return self._browser.get(url)
