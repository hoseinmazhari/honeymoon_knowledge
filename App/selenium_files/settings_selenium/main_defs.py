
import time
from . import xpath_hesabro
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
def select_product_inSearchFeild(driver, main_url, product_name, _product_input):
    is_exist_product = False
    tryCount = 0
    while is_exist_product== False:
        tryCount += 1
        clear_txt(_product_input)
        write_in_element(product_name, _product_input)
        # _product_input.send_keys(Keys.ENTER)
        time.sleep(3.5)
        element = driver.find_element(By.XPATH,xpath_hesabro.navbar.searchbar.merchandise_list)
        lst = element.find_elements(By.TAG_NAME,"li")
        # lst = element
        for item in lst:
            if item == product_name:
            # if pre in item.text:
            #     if product_name1 in item.text  or product_name2 in item.text  :
                    item.click()
                    # for w in range(10):
                    #     print(item.text)
                    # element = driver.active_element
                    # element.send_keys(Keys.ENTER)
                    # item.send_keys(Keys.ENTER)
                    time.sleep(3)
                    break
            # element.send_keys(Keys.DOWN)
        # if driver.current_url == main_url:
            # _product_input.send_keys(Keys.ENTER)
            # time.sleep(3.5)
            
        driver.implicitly_wait(2)
        if driver.current_url != main_url:
            is_exist_product = True
        if tryCount >= 2:
            break
            # while driver.current_url!=main_url:
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
            
def clear_txt(element):
    element.click()
    element.clear()
    input_text = element.get_attribute("value")
    for i in range(len(input_text)):
        element.send_keys(Keys.BACK_SPACE)
        element.send_keys(Keys.DELETE)