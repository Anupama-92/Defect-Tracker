class BaseLocators:
    app = "//div[@class='ic-title' and contains(text(),'%s')]"
    iframe = "applicationId"
    modules = "//a[@id='ngb-nav-0']"
    select_project = "//input[@id='mat-input-0' and @placeholder='Select Project']"
    module = "//span[normalize-space()='AWS SERVICES - AMAZON']"

