# from xpath import get_xpath
from selenium_files.settings_selenium import xpath_hesabro
from selenium_files.settings_selenium.app_address import urls_hesabro
# from browser import Browser,write_in_element
from selenium_files.settings_selenium.main_defs import write_in_element, clear_txt
from selenium.webdriver.common.keys import Keys
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def _coin_form_finder(driver):
    # is_showed = True
    try:
        _coin_form = driver.find_element(by="xpath",value=f"//form[@id='ajax-create-or-update-coin']")
    except:
        try:
            time.sleep(1)
            _coin_form = driver.find_element(by="xpath",value=f"//form[@id='ajax-create-or-update-coin']")
            ########print("coin add form step:2")
        except:
            try:
                time.sleep(2)
                _coin_form = driver.find_element(by="xpath",value=f"//form[@id='ajax-create-or-update-coin']")
                ########print("coin add form step:3")
            except:
                try:
                    time.sleep(3)
                    _coin_form = driver.find_element(by="xpath",value=f"//form[@id='ajax-create-or-update-coin']")
                    ########print("coin add form step:3")
                except:
                    # is_showed =False
                    pass
        
    return _coin_form
                ########print("coin add form step:4")
def _is_clickable_input_coin(driver,coin,_coin_form):
    is_clickable = True
    
    if is_clickable:
        try:
            _coin_input= _coin_form.find_element(by="xpath",value=f".//input[@id='customercoin-amount'][@name='CustomerCoin[amount]']")
            _coin_input.click()
            write_in_element(coin,_coin_input)
        except:
            is_clickable = False
    return is_clickable
def ico_add_coin(driver, tbl):
    is_ico_add_coin = True
    try:
        tbl_th = tbl.find_elements(by="xpath",value=f"//th")
        _coin_add = tbl_th[-1]
        th_a = _coin_add.find_element(by='xpath',value='.//a')
        th_a_span = _coin_add.find_element(by='xpath',value='.//span')
        #driver.execute_script("return arguments[0].scrollIntoView();", th_a_span)
        time.sleep(0.5)
        th_a_span.click()
        time.sleep(1.3)
        # element = WebDriverWait(driver, 10).until(
        # EC.presence_of_element_located((By.XPATH, f"{get_xpath('user_detail','coin')}"))    )
        # element.click()
    except:
        is_ico_add_coin = False
    
    return is_ico_add_coin



def search_fieldMobile(driver):
    is_search_fieldMobile =False
    while is_search_fieldMobile == False:
        try:
            _search = driver.find_element(by="xpath",value=f"{get_xpath('search','mobile')}")
            #driver.execute_script("return arguments[0].scrollIntoView();", _search)
            _search.click()
            is_search_fieldMobile = True
            time.sleep(1)
        except:
            pass
    return is_search_fieldMobile
    
def user_details_coin(driver):
    is_tab_coin =True
    # try:
        # time.sleep(2)
        # driver.implicitly_wait(3)
        # _coin= driver.find_element(by="xpath",value=get_xpath('user_detail','coin'))
        # _coin.click()
    try:
        element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f"{get_xpath('user_detail','coin')}"))    )
        #driver.execute_script("return arguments[0].scrollIntoView();", element)
        element.click()
    except:
        is_tab_coin = False
    # except:
    #     try:
    #         time.sleep(2)
    #         _coin= driver.find_element(by="xpath",value=get_xpath('user_detail','coin'))
    #         _coin.click()
    #     except:
    #         try:
    #             time.sleep(2)
    #             _coin= driver.find_element(by="xpath",value=get_xpath('user_detail','coin'))
    #             _coin.click()
    #         except:
    #             is_tab_coin =False
    # if is_tab_coin:
    #     time.sleep(1.3)
    return is_tab_coin
def change_address(driver, thisUrl):
    driver.get(thisUrl)
    while driver.current_url != thisUrl:
        driver.get(thisUrl)
        time.sleep(2)
    # #######print(driver.current_url)
def count_first_charge(driver,Initial_charge):
    count = 0
    tbl= driver.find_element(by="xpath",value=get_xpath('user_detail','coin_table'))
    # for tr in tbl:
    #     #######print(tr.text)
    trs=tbl.find_elements(by="xpath",value=get_xpath('user_detail','coin_table_tr'))
    # # inner_for = True
    # row_count = 0
    # rows = len(trs)
    # # #######print(trs.text)
    for r in trs:
        driver.execute_script("return arguments[0].scrollIntoView();", r)
        # #######print(f"r is {r.text}")
        # row_count += 1
        # tds = 0
        try:
            tds = r.find_element(by="xpath",value=f".//td[text()='{Initial_charge}']")# or td data-col-seq=4 = firstcharge
            
            #driver.execute_script("return arguments[0].scrollIntoView();", tds)
            if tds.text == Initial_charge:
                count += 1
        except:
            pass
                # #######print(count)
            # #######print(tds.text)
    # #######print(count)
    # #######print(f"row count: {row_count}")
    # #######print(f"rows: {rows}")
    return count
    
def _remove_first_charge(driver,Initial_charge,coin_address):
    # for i in range(4):

        # is_tab_coin = user_details_coin(driver)

        # if is_tab_coin:
            # charge_checked = False
            # counter=1
            # while charge_checked==False:
                        #######print("start removing")
            # try:
            #     base_tbl= driver.find_element(by="xpath",value=get_xpath('user_detail','coin_table'))
            #     base_trs=base_tbl.find_elements(by="xpath",value=get_xpath('user_detail','coin_table_tr'))
            #     rowCount = len(base_trs)
            #     if rowCount>4:
            #         rowCount = 4
                
            #     for i in range(rowCount):
            #         #######print(f"start loop removing with {rowCount} iter")
                    try:
                        tbl= driver.find_element(by="xpath",value=get_xpath('user_detail','coin_table'))
                        trs=tbl.find_elements(by="xpath",value=get_xpath('user_detail','coin_table_tr'))
                        # inner_for = True
                        
                        for r in trs:
                                #######print(f"start loop removing with rows")
                            # try:
                                
                                # tds = r.find_element(by="xpath",value=f"//td[contains(text(),'{Initial_charge}')]")# or td data-col-seq=4 = firstcharge
                                # #######print(tds.text)
                                # //td[contains(text(),'شارژ همیار')]
                                # if len(tds):
                                tds = r.find_elements(by="xpath",value=f"//td")
                                for item in tds:
                                    #######print(f"this is an item : {item.text}")
                                    ########print(f"initial charge : {Initial_charge}")
                                    if item.text == Initial_charge:
                                        ########print("td and initial charge are equal!")
                                        rem_td = tds[-1]
                                        # driver.execute_script("return arguments[0].scrollIntoView();", rem_td)
                                        # time.sleep(0.02)
                                        rem_td.find_element(by='xpath',value=f"//i[@class='ti-trash grid-btn grid-btn-delete']").click()#[@title='{del_title}']
                                        ########print("befor 3.5")
                                        time.sleep(3.5)
                                        ########print("after 3.5")
                                        # test = input("press key to continio...")
                                        driver.implicitly_wait(4)
                                        alert_del = driver.switch_to.active_element
                                        alert_del.send_keys(Keys.ENTER)
                                        inner_for = user_details_coin(driver)
                                        time.sleep(3.5)
                                        # alert_del.find_element(by='xpath',value=f".//button[text()='بله']").click()
                                        # r.find_element(by="xpath",value=f"//td[@title='{del_title}']").click
                                    # break
                                # break
                            # except Exception as e:
                            #     # ########print(e)

                            #     pass
                    except:
                        pass
    #         except:
    #             pass
    #     # time.sleep(3)
    # # driver.implicitly_wait(3)
    #         # user_details_coin(driver)
                        ########print(f"exit removing ")
                        change_address(driver,coin_address)
    # _coin= driver.find_element(by="xpath",value=get_xpath('user_detail','coin'))
    # _coin.click()    
def _add_first_charge(driver,coin,main_url):
    # for i in range(3):
        # time.sleep(1)
        # driver.implicitly_wait(6)
        #########print("start for add charge")
        is_tab_coin = user_details_coin(driver)
        
        # charge_checked = False
        # counter=1
        # while charge_checked==False:
            # try:y
        # time.sleep(1)
        if is_tab_coin:
            try:
                tbl= driver.find_element(by="xpath",value=f"//table")
            except:
                try:
                    time.sleep(1)
                    tbl= driver.find_element(by="xpath",value=f"//table")
                    #########print("table step:2")
                except:
                    try:
                        time.sleep(1)
                        tbl= driver.find_element(by="xpath",value=f"//table")
                        #########print("table step:3")
                    except:
                        time.sleep(4)
                        tbl= driver.find_element(by="xpath",value=f"//table")
                        ########print("table step:4")
            
            is_icon=False
            while is_icon==False:
                is_icon = ico_add_coin(driver,tbl)     
            _coin_form = _coin_form_finder(driver)
            # win = driver.switch_to.active_element
            
            is_clickable_input_coin = _is_clickable_input_coin(driver,coin,_coin_form)
            while is_clickable_input_coin==False:
                 is_clickable_input_coin = _is_clickable_input_coin(driver,coin,_coin_form)
            
            
            _radio_add = False
            while _radio_add == False:
                try:
                        
                    _coin_div_radio = _coin_form.find_element(by="xpath", value = ".//div[@id='customercoin-coin_type']")
                    _coin_add_radio = _coin_div_radio.find_element(by="xpath",value=f".//input[@id='i0']")#//label[@for='i1']
                    # _coin_add_radio = _coin_radio[1]
                    # _coin_add_radio.value=1
                    time.sleep(0.04)
                    _coin_add_radio.send_keys(Keys.SPACE)
                    _radio_add = True
                except:
                    _radio_add = False
            
            _text_area = False
            while _text_area == False:
                try:
                    _coin_textarea_des = _coin_form.find_element(by="xpath", value = ".//textarea[@id='customercoin-comment']")
                    write_in_element("شارژ همیار",_coin_textarea_des)
                    _text_area = True
                except:
                    _text_area = False
                    # _coin_textarea_des.send_keys(Keys.ENTER)
            
            time.sleep(0.04)
            _ok_button = False
            while _ok_button == False:
                try:
                    _coin_form.find_element(by="xpath", value = ".//button[text()='ایجاد']").click()
                    time.sleep(2)
                    _ok_button = True
                except:
                    _ok_button = False
                

def coin_setter(mobile, driver, main_url, coin, hamyar_condition):
    is_search_fieldMobile = search_fieldMobile(driver)
    if is_search_fieldMobile:
        # #######print(f"is searched = {is_search_fieldMobile}")
        # _input = _input.find_element(by="xpath",value=".//span[@class='input.select2-search select2-search--dropdown',@aria-control='select2-shortcutCustomerName-results']")
        _mobile_input = driver.switch_to.active_element
        
        write_in_element(mobile,_mobile_input)
        _mobile_input.send_keys(Keys.ENTER)
        time.sleep(3.5)
        
        _mobile_input.send_keys(Keys.ENTER)
        time.sleep(3.5)
        driver.implicitly_wait(2)
        if driver.current_url!=main_url:
            address_id = driver.current_url
            index_id = address_id.find("=")
            this_id = address_id[index_id+1:]
            Initial_charge = "شارژ اولیه"
            coin_address = get_address("user_detail","coin",this_id)
            #######print("strat get coin address")
            while driver.current_url != coin_address:

                # driver.get(coin_address)
                try:
                    element = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, f"{get_xpath('user_detail','coin')}")))
                    element.click()
                except:
                    pass
            #######print("end get coin address")
            # count_first_charge(driver,Initial_charge)   
            # 

            count = count_first_charge(driver,Initial_charge)   
            #######print(f"count in hesabro charge in start: {count}")    
            while count:
                #######print(f"count in hesabro charge: {count}")
                _remove_first_charge(driver,Initial_charge,coin_address) 
                count = count_first_charge(driver,Initial_charge) 

            # count = count_first_charge(driver,Initial_charge)  
            if hamyar_condition: # با توجه به اینکه هر 10 یوزر یکمرتبه فایل ذخیره می شود در نتیجه بعد ازقطع شدن قطعا بعد از 10یوزر نیازی به بررسی شارژهای قبلی نیست
                hamyar_charge = "شارژ همیار"      
                count = count_first_charge(driver,hamyar_charge)        
                while count:
                    #######print(f"count in hamyar charge: {count}")
                    _remove_first_charge(driver,hamyar_charge,coin_address)   
                    count = count_first_charge(driver,hamyar_charge) 

            if int(coin)>0:
                _add_first_charge(driver,coin,main_url)    
            
            return True
        else:
            return False
    else:
        return False
    # return is_search_fieldMobile
            
        

  