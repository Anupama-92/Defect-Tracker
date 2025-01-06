import time

import pytest

from AutomationSuite.ChorusTest import ChorusTest
from AutomationSuite.Data.GlobalData import AppItems
from AutomationSuite._Fragments.BaseFragments.base_fragments import BasePageFragments
from AutomationSuite._Fragments.DTFragments.DTList import DTListPage


@pytest.mark.chorus
@pytest.mark.dt
@pytest.mark.dt_homepage
@pytest.mark.usefixtures("microsoft_login")
class TestDTHomePage(ChorusTest):

    def test_dt_dt_homepage_smoke_test(self, microsoft_login):
        # Navigating to the Defect Tracker APP
        BasePageFragments().navigate_to_app(AppItems().DT_app)
        expected_modules = [self.s.modules.defect_list]
        observed_modules = BasePageFragments().get_modules(switch=True)
        # Comparing the modules found with the expected.
        self.h.verify_comparison(expected=expected_modules, actual=observed_modules, fail_message="Modules not matched")
        # Waiting till the page loaded
        time.sleep(3)
        DTListPage().select_project()
