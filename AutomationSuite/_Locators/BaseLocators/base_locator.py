class BaseLocators:
    app = "//div[@class='ic-title' and contains(text(),'%s')]"
    table_1st_row = "//div[@class='tableFixHead']/table/tbody/tr[contains(@class,'even_col')][1]"
    table_no_data = ("//div[@class='tableFixHead']/div[contains(@class,'text-center')]/div/div/h6[contains(text(),"
                     "'No Data Found')]")
    modules = "//div[@id='navbarSupportedContent']/ul/li/a"
    module = "//a[@id='ngb-nav-0']"
    sub_module = "//div[@id='navbarSupportedContent']/ul/li/ul/li/a[contains(text(),'{0}')]"
    row_in_div = "//div[@class='tableFixHead']/table/tbody/tr/td/div[contains(text(),'{0}')]"
    row_in_a = "//div[@class='tableFixHead']/table/tbody/tr/td/a[contains(text(),'{0}')]"
    row_in_td = "//div[@class='tableFixHead']/table/tbody/tr/td[contains(text(),'{0}')]"
    toggle_switch = "//div[@class='tableFixHead']/table/tbody/tr/td/ui-switch"
    popup_yes_btn = "//div[@class='row']//button[contains(text(),'Yes')]"
    popup_close_btn = "//div[@class='row']//button[contains(text(),'Close')]"
    success_text = "//div[@role='alert' and contains(text(),'success') or contains(text(),'Success')]"
    multi_select_dropdown_select_all = "//div[contains(text(),'Select All')]"
    multi_select_dropdown_search = "//input[@placeholder='Search']"
    multi_select_dropdown_option = "//li/div[contains(text(),'{0}')]"

