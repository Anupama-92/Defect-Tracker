class BasePageFragments(WebElement):

    def __init__(self):
        WebElement.__init__(self)

    @staticmethod
    def app_item():
        return BaseLocators().app