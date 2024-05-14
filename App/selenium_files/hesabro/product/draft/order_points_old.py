
# from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from .xpath import get_xpath
# from ...settings.xpath import get_xpath
from selenium_files.settings_selenium import xpath_hesabro 
import time
import pandas as pd
import os
from selenium.webdriver.common.keys import Keys
# from .merchandise import 
# from selenium_files.settings_selenium.main_defs import    
from selenium_files.settings_selenium.main_defs import write_in_element,search_fieldProduct_navbar,clear_txt, select_product_inSearchFeild
from selenium_files.settings_selenium.app_address import urls_hesabro
# from ...settings_selenium.browser import write_in_element
from python_files.settings_python import DateJuToJa as djtj
class Order_point():
    merchandise = "عنوان کالا"
    # order_point= "حد سفارش"
    order_point = 'کف سفارش'
    # buy_price = "old sale price"
    id = "کد کالا"    
    branch = "عنوان شرکت"
		# عنوان کالا	کد کالا	جمع واحد	مقدار	تعداد روز فعال شعبه	مجموع تعداد فروش	ماه	
		

def get_index_order_point_file(df):
    thisItter = -1
    thisClass = Order_point()
    for col in df.columns:
        thisItter += 1
        if col == thisClass.id:
            thisClass.id = thisItter # type: ignore
        elif col == thisClass.branch:
            thisClass.branch = thisItter

        # elif col == thisClass.buy_price:
        #     thisClass.buy_price = thisItter # type: ignore
        elif col == thisClass.merchandise:
            thisClass.merchandise = thisItter # type: ignore
        elif col == thisClass.order_point:
            thisClass.order_point = thisItter # type: ignore
        # elif col == thisClass.buy_price:
        #     thisClass.buy_price = thisItter # type: ignore
    return thisClass

def update_product_order_point(driver,id,order_point): 
    # if act== "exit_product":
        is_true = True
        # is_search_fieldProduct = search_fieldProduct_navbar(driver)
        # while search_fieldProduct(driver)
        # _product_input = driver.switch_to.active_element
        
        # select_product_inSearchFeild(driver, main_url, id, _product_input)
        # write_in_element(id,_product_input)
        # _product_input.send_keys(Keys.ENTER)
        # time.sleep(3.5)
        this_product = f'{urls_hesabro.product.product_view_detail}{id}'
        driver.get(this_product)
        time.sleep(2.4)
        # _product_input.send_keys(Keys.ENTER)
        # time.sleep(3.5)
        driver.implicitly_wait(2)
        # while driver.current_url!=main_url:
        if driver.current_url != main_url:
            try:
                element = WebDriverWait(driver, 10).until(
                    
                EC.presence_of_element_located((By.XPATH, f"{xpath_hesabro.product_view.tabs.details.act_button}")))
                element.click()
            except:
                is_true = False
            try:
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, f"{xpath_hesabro.product_view.tabs.details.update_btn}")))
                    
                element.click()
            except:
                is_true = False
            try:
                time.sleep(2)
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, f"{xpath_hesabro.product_view.tabs.details.update_page.more_details}")))
                
                element.click()
                # driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                time.sleep(1)
                element = driver.find_element(By.TAG_NAME,"html")
                for i in range(12):
                    time.sleep(0.4)
                    element.send_keys(Keys.DOWN)
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, f"{xpath_hesabro.product_view.tabs.details.update_page.order_point}")))
                    # EC.presence_of_element_located((By.XPATH, f"{get_xpath('merchandise','order_point')}")))
                element.click()
                clear_txt(element)
                # for i in range(20):
                #     time.sleep(0.04)
                #     element.send_keys(Keys.BACKSPACE)
                # time.sleep(1)
                # for i in range(20):
                #     time.sleep(0.04)
                #     element.send_keys(Keys.DELETE)
                # time.sleep(1)
                element.clear()
                write_in_element(order_point,element)
                
                time.sleep(1)
            except Exception as e:
                print(e)
                is_true = False
            
        
            try:
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, f"{xpath_hesabro.product_view.tabs.details.update_page.btn_submit}")))
                    # EC.presence_of_element_located((By.XPATH, f"{get_xpath('merchandise','btn_submit')}")))
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
    
    

def set_order_point(driver,dfData):
    print("please wait until see 'done'...")
    thisPath = os.getcwd()
    # chPath = f"{thisPath}/merchandises"
    # os.chdir(chPath)
    todayIs = djtj.getDateTimeForFileName()
    # lsData = []
    # for i in range(1,11):
    #     print("start read file")
    #     sheetName = str(i)
    #     while len(sheetName)<3:
    #         sheetName = "0" +sheetName
    #     sheetName = "sh"+ sheetName
    #     dfData = pd.read_excel("..//dist/order point/order point.xlsx",sheet_name=sheetName)
    #     lsData.append(dfData)
    #     # thisIndex = get_index_order_point_file(dfData)
    #     # print("start export file")
    #     # branch = dfData.iat[0,thisIndex.branch]
    #     # dfData.to_excel(f" {branch} -{todayIs}.xlsx",index= False)
    #     # print("export complete")
    #     # testers_avalible = True
    # dfData = pd.concat(lsData)
    # dfData.to_excel("order point all brs.xlsx")
    # return False
    counter = 0
    # dfData = pd.read_excel("..//dist/order point/orderPoint0209.xlsx")
    thisIndex = get_index_order_point_file(dfData)
    # ls_true = []
    # ls_false = []
    ls_ans = []
    while len(dfData):
        # driver.get(main_url)
        time.sleep(3)
        counter += 1
        merchandise = dfData.iat[0,thisIndex.merchandise]
        order_point = f"{int(dfData.iat[0,thisIndex.order_point])}"
        
        id = f"{int(dfData.iat[0,thisIndex.id])}"
        
        print(counter)
        # is_True = update_product_order_point(driver,main_url,id,order_point)
        is_True = update_product_order_point(driver,merchandise,order_point)
        dfData = dfData.loc[dfData[Order_point.merchandise]!= (merchandise)]
        # dfData = dfData.loc[dfData[Order_point.id]!= int(id)]
        if is_True:
            ls_ans.append({"id":id, "product":merchandise,"order point":order_point,"is_True":True})
            dfData.to_excel("order-mod.xlsx",index= False)
        else:
            ls_ans.append({"id":id, "product":merchandise,"order point":order_point,"is_True":False})
            # import random as r
            # sl = r.randint(2,6)
            # print(f"please wait for {sl} seconds ...")
            # time.sleep(sl)
        df_ans = pd.DataFrame(ls_ans)
        df_ans.to_excel("ans orderPoint.xlsx",index=False)
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
