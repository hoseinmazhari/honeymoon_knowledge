
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from .xpath import get_xpath
# from ...settings.xpath import get_xpath
import time
import pandas as pd
import os
from selenium.webdriver.common.keys import Keys
# from .merchandise import search_fieldProduct
from selenium_files.settings_selenium.main_defs import search_fieldProduct_navbar,write_in_element
# from ...settings_selenium.browser import write_in_element #...
from python_files.settings_python import DateJuToJa as djtj #....
# from ...settings import xpath
class ThisCols():
    name = "عنوان کالا"
    # order_point= "حد سفارش"
    order_point = 'کف سفارش'
    # buy_price = "old sale price"
    id = "کد کالا"    
    branch = "عنوان شرکت"
		# عنوان کالا	کد کالا	جمع واحد	مقدار	تعداد روز فعال شعبه	مجموع تعداد فروش	ماه	
		

def get_index_order_point_file(df):
    thisItter = -1
    thisClass = ThisCols()
    for col in df.columns:
        thisItter += 1
        if col == thisClass.id:
            thisClass.id = thisItter # type: ignore
        elif col == thisClass.branch:
            thisClass.branch = thisItter

        # elif col == thisClass.buy_price:
        #     thisClass.buy_price = thisItter # type: ignore
        elif col == thisClass.name:
            thisClass.name = thisItter # type: ignore
        elif col == thisClass.order_point:
            thisClass.order_point = thisItter # type: ignore
        # elif col == thisClass.buy_price:
        #     thisClass.buy_price = thisItter # type: ignore
    return thisClass
       
def _update_product_order_point(driver,main_url,id,order_point): 
    # if act== "exit_product":
        is_true = True
        is_search_fieldProduct = search_fieldProduct(driver)
        # while search_fieldProduct(driver)
        _product_input = driver.switch_to.active_element
        
        write_in_element(id,_product_input)
        _product_input.send_keys(Keys.ENTER)
        time.sleep(3.5)
        
        _product_input.send_keys(Keys.ENTER)
        time.sleep(3.5)
        driver.implicitly_wait(2)
        # while driver.current_url!=main_url:
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f"{get_xpath('merchandise','act_button')}")))
            element.click()
        except:
            is_true = False
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f"{get_xpath('merchandise','update_btn')}")))
            element.click()
        except:
            is_true = False
        try:
            time.sleep(2)
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f"{get_xpath('merchandise','more_details')}")))
            element.click()
            # driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(1)
            element = driver.find_element(By.TAG_NAME,"html")
            for i in range(12):
                time.sleep(0.4)
                element.send_keys(Keys.DOWN)
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f"{get_xpath('merchandise','order_point')}")))
            element.click()
            for i in range(20):
                time.sleep(0.04)
                element.send_keys(Keys.BACKSPACE)
            time.sleep(1)
            for i in range(20):
                time.sleep(0.04)
                element.send_keys(Keys.DELETE)
            time.sleep(1)
            element.clear()
            write_in_element(order_point,element)
            
            time.sleep(1)
        except Exception as e:
            print(e)
            is_true = False
        
       
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f"{get_xpath('merchandise','btn_submit')}")))
            element.click()
            time.sleep(2)
            while driver.current_url!= main_url:
                driver.get(main_url)
                time.sleep(2)
        except:
            is_true = False
        return is_true
        # is_search_fieldProduct = search_fieldProduct(driver)
        # _product_input = driver.switch_to.active_element
    
        # write_in_element(merchandise,_product_input)
        # _product_input.send_keys(Keys.ENTER)
        # time.sleep(3.5)
        
        # _product_input.send_keys(Keys.ENTER)
        # time.sleep(3.5)
        # driver.implicitly_wait(2)
    
def _change_branch(driver, branch):
    is_true = True
    # is_true = False
    # print(branch)
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath.hesabro.navbar.branch_selector)))
        element.click()
        time.sleep(4)
        
        element = driver.find_elements(By.XPATH, xpath.hesabro.navbar.branch_item_selector)
        counter = -1                    #   f"{xpath.hesabro.navbar.branch_item_selector}[text()= {branch}]")
        for x in element:
            counter += 1
            if branch == x.text:
                thisItem = counter
                break
        element = element[thisItem]
        # element = element[branch]
        element.click()
    except Exception as e:
        print(e)
        is_true = False
    return is_true

def set_order_point_allBrs(driver,main_url):
    print("please wait until see 'done'...")
    thisPath = os.getcwd()
    todayIs = djtj.getDateTimeForFileName()
    counter = 0
    dfData = pd.read_excel("..//dist/order point/order point.xlsx")
    thisIndex = get_index_order_point_file(dfData)
    ls_true = []
    ls_false = []
    while len(dfData):
        branch = dfData.iat[0, thisIndex.branch]
        dfBranch = dfData.loc[dfData[ThisCols.branch]==branch]
        dfData = dfData.loc[dfData[ThisCols.branch]!=branch]
        br_changed = _change_branch(driver, branch)
        if br_changed:
            while len(dfBranch):
                counter += 1
                merchandise = dfBranch.iat[0,thisIndex.name]
                order_point = f"{int(dfBranch.iat[0,thisIndex.order_point])}"
                
                id = f"{int(dfBranch.iat[0,thisIndex.id])}"
                
                # print(counter)

                is_True = _update_product_order_point(driver,main_url,id,order_point)
                if is_True:
                    dfBranch = dfBranch.loc[dfBranch[ThisCols.id]!= int(id)]
                    dfBranch.to_excel(f"ثبت نشده های کف سفارش{branch}.xlsx",index= False)
                else:
                    import random as r
                    sl = r.randint(20,80)
                    print(f"please wait for {sl} seconds ...")
                    time.sleep(sl)
                
        # if is_True:
        #     ls_true.append({testers.id:id,testers.tester:tester,testers.buy_price:buy_price,testers.sale_price:salePrice})
        #     df = pd.DataFrame(ls_true)
        #     df.to_excel("ok_orders.xlsx",index=False)
        # else:
        #     # try:
        #     ls_false.append({testers.id:id,testers.tester:tester,testers.buy_price:buy_price,testers.sale_price:salePrice})
        #     df = pd.DataFrame(ls_false)
        #     df.to_excel("false_orders.xlsx",index=False)
        #     # except:
        #     #     pass
