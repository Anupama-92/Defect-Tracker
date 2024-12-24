class Fragments(object):

    @property
    def chorus_loginpage(self):
        try:
            return self.__chorus_loginpage
        except AttributeError:
            from AutomationSuite._Fragments.ChorusFragments.chorus_login_page import ChorusLoginPage
            self.__chorus_loginpage = ChorusLoginPage()
            return self.__chorus_loginpage

    @property
    def chorus_dashboardpage(self):
        try:
            return self.__chorus_dashboardpage
        except AttributeError:
            from AutomationSuite._Fragments.ChorusFragments.chorus_dashboard_page import ChorusDashboardPage
            self.__chorus_dashboardpage = ChorusDashboardPage()
            return self.__chorus_dashboardpage


    @property
    def base_fragments(self):
        try:
            return self.__base_fragments
        except AttributeError:
            from AutomationSuite._Fragments.BaseFragments.base_fragments import BasePageFragments
            self.__base_fragments = BasePageFragments()
            return self.__base_fragments
