import time

import pytest

from AutomationSuite.ChorusTest import ChorusTest
from AutomationSuite.Data.GlobalData import AppItems
from AutomationSuite._Fragments.BaseFragments.base_fragments import BasePageFragments
from AutomationSuite._Fragments.DTFragments.DTList import DTListPage, DefectListPage
from AutomationSuite.Data.DTData import Modules,SelectProject
from AutomationSuite._Fragments.DTFragments.dt_homepage import DTHomePage


@pytest.mark.chorus
@pytest.mark.dt
@pytest.mark.dt_homepage
@pytest.mark.usefixtures("microsoft_login")
class TestDTProjectPage(ChorusTest):

    def test_dt_projectpage_smoke_test(self, microsoft_login):
        # Navigate to the Defect Tracker App
        BasePageFragments().navigate_to_app(AppItems().DT_app)
        # DTHomePage().navigate_to_module("loaded", True)
        # Wait for the iframe and switch to it
        BasePageFragments().navigate_to_module(module_name=Modules().defect_list)
        DefectListPage().wait_for_load()
        DefectListPage().run(select_project=SelectProject().c2cc_abc)
        





