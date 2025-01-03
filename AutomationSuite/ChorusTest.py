import logging

from AutomationSuite.Data.Strings import Strings
from AutomationSuite._Fragments.Fragments import Fragments
from AutomationSuite._Wrapper import helper
from AutomationSuite._Wrapper.Shared.Constants import Constants
from AutomationSuite._Wrapper.Shared.Util.Utils import Utils
from AutomationSuite.cog_config import COGConfig


class ChorusTest(object):

    @classmethod
    def setup_method(cls):
        cls._config = COGConfig().get_config()
        cls.utils = Utils()
        cls.const = Constants()
        cls.f = Fragments()
        cls.logger = logging.getLogger('automation')
        cls.cog_config = COGConfig()
        cls.h = helper
        cls.s = Strings()

    @classmethod
    def __get_helper(cls):
        try:
            return cls.__helper
        except AttributeError:
            from AutomationSuite._Wrapper import helper
            cls.__helper = helper
            return cls.__helper
