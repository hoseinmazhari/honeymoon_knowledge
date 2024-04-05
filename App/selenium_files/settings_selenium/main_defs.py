
import time
from . import xpath_hesabro
from selenium.webdriver.common.keys import Keys
def search_fieldProduct_navbar(driver):
    is_search_fieldProduct =False
    while is_search_fieldProduct == False:
        try:
            # _search = driver.find_element(by="xpath",value=f"{get_xpath('search','merchandise')}")
            _search = driver.find_element(by="xpath",value=f"{xpath_hesabro.navbar.searchbar.merchandise}")
            #driver.execute_script("return arguments[0].scrollIntoView();", _search)
            _search.click()
            is_search_fieldProduct = True
            time.sleep(1)
        except:
            pass
    return is_search_fieldProduct

def write_in_element(text,element):
    for _char in text:
        element.send_keys(_char)
        # t= random.random()
        t= 0.04
        time.sleep(t)
        
def change_chk(element, act_chk):
    is_checked = element.is_selected()
    if act_chk == True or act_chk =="True":
        if is_checked != True:
            element.send_keys(Keys.SPACE)
    elif act_chk == False or act_chk == "False":
        if is_checked != False:
            element.send_keys(Keys.SPACE)