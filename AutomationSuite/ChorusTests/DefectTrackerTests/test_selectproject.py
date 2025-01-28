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
        # Navigate to the Defect Tracker App
        BasePageFragments().navigate_to_app(AppItems().DT_app)

        # Wait for the iframe and switch to it
        SelectProject().wait_for_load(switch=True)
        

        # Select the project from the dropdown
        SelectProject().run(select_project=Selectproject.aws_services_amazon)

        # Wait for the auto-suggestions to load and click the correct option (if needed)
        SelectProject().click_element(
            element_locator=SelectProject().select_project1, selector="xpath"
        )

        # (Optional) Verify successful selection
        assert Selectproject.aws_services_amazon in SelectProject().get_element_value(
            SelectProject().select_project(), selector="xpath"
        )



