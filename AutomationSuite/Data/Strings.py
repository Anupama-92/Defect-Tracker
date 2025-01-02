class Strings(object):

    @property
    def modules(self):
        try:
            return self.__modules
        except AttributeError:
            from AutomationSuite.Data.DTData import Modules
            self.__modules = Modules()
            return self.__modules
