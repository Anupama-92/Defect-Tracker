import time

from AutomationSuite.Data.LoginData import logins
from AutomationSuite._Fragments.ChorusFragments.chorus_dashboard_page import ChorusDashboardPage
from AutomationSuite._Fragments.ChorusFragments.chorus_login_page import ChorusLoginPage
from AutomationSuite._Wrapper.Shared.Util.TestLog import cogtestlog
from AutomationSuite.cog_config import COGConfig
from AutomationSuite.server.cog_webdriver_frontend import CogWebDriverFrontEnd


class Login(object):

    def open_portal(self):
        global url
        browser = COGConfig().browser_type
        if COGConfig().site_mode.get('default') is None or '':
            url = COGConfig().chorus_web_ui_config.get("qa", None)
        elif COGConfig().site_mode.get('default') == 'dev':
            url = COGConfig().chorus_web_ui_config.get("dev", None)
        elif COGConfig().site_mode.get('default') == 'qa':
            url = COGConfig().chorus_web_ui_config.get("qa", None)
        elif COGConfig().site_mode.get('default') == 'prod':
            url = COGConfig().chorus_web_ui_config.get("prod", None)
        cogtestlog().info(f"Navigating to the {url}")
        web_driver = CogWebDriverFrontEnd()
        web_driver.open_url(browser=browser, url=url)

    def portal_login(self, login_email, login_password, skip_login=False, skip_open_url=False):

        error_message = 'Unable to login.  Run manually to confirm.'
        if not skip_open_url:
            self.open_portal()

        if not skip_login:
            ChorusLoginPage().run_login(email_id=login_email, password=login_password)
            ChorusDashboardPage().wait_for_load()
            time.sleep(2)

    def chorus_login(self, login_member=None):
        if login_member is None:
            login_member = COGConfig().portal_login
        if login_member not in logins:
            email = COGConfig().login_credentials.get("email")
            password = COGConfig().login_credentials.get("password")
            Login().portal_login(login_email=email,
                                 login_password=password)
        else:
            login_credentials = logins[login_member]
            Login().portal_login(login_email=login_credentials.email,
                                 login_password=login_credentials.password)
