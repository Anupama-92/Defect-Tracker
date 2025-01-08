import time

import pytest

from AutomationSuite.ChorusTest import ChorusTest
from AutomationSuite.Data.GlobalData import AppItems
from AutomationSuite._Fragments.BaseFragments.base_fragments import BasePageFragments
from AutomationSuite._Fragments.DTFragments.DTList import DTListPage, SelectProject
from AutomationSuite.Data.DTData import Selectproject

@pytest.mark.chorus
@pytest.mark.dt
@pytest.mark.dt_homepage
@pytest.mark.usefixtures("microsoft_login")
class TestDTProjectPage(ChorusTest):

    def test_dt_projectpage_smoke_test(self, microsoft_login):
        # Navigating to the Defect Tracker APP
        BasePageFragments().navigate_to_app(AppItems().DT_app)
        SelectProject().wait_for_load()

        # print("Testing")
        # #BasePageFragments().switch_to_frame()
        # SelectProject().wait_for_load()
        # time.sleep(3)
        # #SelectProject().click_element(element_locator=SelectProject().select_project())
        # SelectProject().run(select_project="AWS SERVICES - AMAZON")



