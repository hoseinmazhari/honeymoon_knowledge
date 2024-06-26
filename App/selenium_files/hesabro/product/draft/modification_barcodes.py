
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
from selenium_files.settings_selenium.main_defs import search_fieldProduct_navbar
from selenium_files.settings_selenium.main_defs import write_in_element, change_chk,clear_txt #...
from python_files.settings_python import DateJuToJa as djtj #....
# from ...settings import xpath

class modification_barcodesCols():
    product_name = "عنوان کالا"
    # order_point= "حد سفارش"
    
    id = "کد کالا"    
   

def get_index_modification_barcodesCols(df):
    thisItter = -1
    thisClass = modification_barcodesCols()
    for col in df.columns:
        thisItter += 1
        if col == thisClass.product_name:
            thisClass.product_name = thisItter # type: ignore
        elif col == thisClass.id:
            thisClass.id = thisItter
        
    return thisClass
def change_product_attr(driver,scales,scale)    :
            try:
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, f"{xpath_hesabro.product.view.act_button}")))
                element.click()
            except:
                is_true = False
            try:
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, f"{xpath_hesabro.product.view.update_btn}")))
                element.click()
            except:
                is_true = False
            
            try:
                time.sleep(2)
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, f"{xpath_hesabro.product.update_form.store_price}")))
                element.click()
                store_price = element.get_attribute("value")
            except:
                is_true = False
            try:
                time.sleep(1)
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, f"{xpath_hesabro.product.update_form.site_price}")))
                clear_txt(element)
                time.sleep(1)
                write_in_element(store_price,element)
            except:
                is_true = False
            
            try:
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, f"{xpath_hesabro.product.update_form.site_chekbox}")))
                time.sleep(1)
                change_chk(element, act_chk)
                time.sleep(1)
            except:
                is_true = False
            
            
            try:
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, f"{xpath_hesabro.product.update_form.warranty_selector}")))
                time.sleep(1)
                element.click()
                time.sleep(1)
            except Exception as e:
                print(e)
                is_true = False
            try:
                element =  driver.switch_to.active_element
                element.send_keys(Keys.ENTER)
                # element = WebDriverWait(driver, 10).until(
                #     EC.presence_of_element_located((By.XPATH, f"{xpath_hesabro.product.update_form.warranty_item}")))
                # time.sleep(1)
                # element.click()
                # time.sleep(1)
            except Exception as e:
                print(e)
                is_true = False 
            try:
                element = driver.find_element(By.XPATH,xpath_hesabro.product.update_form.unit_selector)
                # element = WebDriverWait(driver, 10).until(
                #     EC.presence_of_element_located((By.XPATH, f"{xpath_hesabro.product.update_form.unit_selector}")))
                # time.sleep(1)
                element.click()
                time.sleep(1)
            except:
                # try:
                    for u in range(10):
                        print("select Unit not found")
                    # element = driver.find_element(By.XPATH,xpath_hesabro.product.update_form.btn_add_unitScale)
                    element = driver.find_element(By.XPATH,xpath_hesabro.product.update_form.div_add_unitScale)
                    # element = WebDriverWait(driver, 10).until(
                    #     EC.presence_of_element_located((By.XPATH, f"{xpath_hesabro.product.update_form.btn_add_unitScale}")))
                    # time.sleep(1)
                    # element.click
                    time.sleep(1)
                    
                    element = element.find_element(By.TAG_NAME,'button')
                    # element.send_keys(Keys.ENTER)
                    # element = WebDriverWait(driver, 10).until(
                    #     EC.presence_of_element_located((By.XPATH, f"{xpath_hesabro.product.update_form.btn_add_unitScale}")))
                    # time.sleep(1)
                    element.click()
                    time.sleep(4)
                    
                # except:
                #     for u in range(10):
                #         print("select addUnit not found")
                #     is_true =False
                # try:
                    element = driver.find_element(By.XPATH,xpath_hesabro.product.update_form.div_scaleContainer)
                    element = WebDriverWait(element, 10).until(
                        EC.presence_of_element_located((By.XPATH, f"{xpath_hesabro.product.update_form.unit_selector}")))
                    time.sleep(1)
                    element.click()
                    time.sleep(1)
                # except:
                #     is_true =False
                # try:
                    # element = element.find_element(By.TAG_NAME,"option")
                    # element[2].click()
                    element= WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, f"{xpath_hesabro.product.update_form.unit_item}")))
                    time.sleep(1)
                    element.click()
                    time.sleep(1)
                # except:
                #     is_true =False
                # try:
                    element = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, f"{xpath_hesabro.product.update_form.scale_selector}")))
                    time.sleep(1)
                    element.click()
                    time.sleep(1)
                # except:
                #     is_true =False
                # try:
                    item = f"{xpath_hesabro.product.update_form.scale_item}option[{scales.index(scale)+2}]"
                    element = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, f"{item}")))
                    time.sleep(1)
                    element.click()
                    time.sleep(1)
                # except:
                #     is_true =False
                
            try:
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, f"{xpath_hesabro.product.update_form.select_Supplier}")))
                time.sleep(1)
                element.click()
                time.sleep(1)
            except:
                is_true = False
            
            try:
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, f"{xpath_hesabro.product.update_form.select_Supplier_site}")))
                time.sleep(1)
                element.click()
                time.sleep(1)
            except:
                is_true = False
            time.sleep(3)
            
            try:
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, f"{xpath_hesabro.product.update_form.btn_submit}")))
                element.click()
                time.sleep(2)
                # while driver.current_url!= main_url:
                #     driver.get(main_url)
                #     time.sleep(2)
            except:
                is_true = False
            
           
def _run_active_product_in_site(driver,main_url,thisData): 
    # if act== "exit_product":
    is_true = True
    scales = [10,  20, 30, 50, 100, 15]
    # scales = [30, 50, 100, 15]
    pre = "نیش"
    aft = "میل"
    # thisData = active_inSiteCols()
    
    act_chk = thisData.act
    for scale in scales:
        driver.get(main_url)
        time.sleep(4)
        
        product_name = f"{pre} {thisData.product_name} {scale} {aft}"
        product_name1 = f"{thisData.product_name} {scale} {aft}"
        product_name2 = f"{thisData.product_name} - {scale} {aft}"
        
        # is_search_fieldProduct = search_fieldProduct_navbar(driver)
        search_fieldProduct_navbar(driver)
        # while search_fieldProduct(driver)
        _product_input = driver.switch_to.active_element
        tryCount = 0
        is_exist_product = False
        while is_exist_product== False:
            tryCount += 1
            
            _product_input.clear()
            write_in_element(product_name, _product_input)
            # _product_input.send_keys(Keys.ENTER)
            time.sleep(3.5)
            element = driver.find_element(By.XPATH,xpath_hesabro.navbar.searchbar.merchandise_list)
            lst = element.find_elements(By.TAG_NAME,"li")
            # lst = element
            for item in lst:
                if pre in item.text:
                    if product_name1 in item.text  or product_name2 in item.text  :
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
        if is_exist_product:   
            
            change_product_attr(driver,scales,scale)
            
    return is_true
            # is_search_fieldProduct = search_fieldProduct(driver)
            # _product_input = driver.switch_to.active_element
        
            # write_in_element(merchandise,_product_input)
            # _product_input.send_keys(Keys.ENTER)
            # time.sleep(3.5)
            
            # _product_input.send_keys(Keys.ENTER)
            # time.sleep(3.5)
            # driver.implicitly_wait(2)
def _run_active_shop(driver, shopUrl, thisData) :
    is_true = True
    driver.get(shopUrl)
    time.sleep(4)
    # thisData = active_inSiteCols()
    product_name = f"{thisData.product_name}"
    slug = thisData.slug
    page_title = thisData.page_title
    act_chk = thisData.act
    des = thisData.des
    oldName = thisData.oldName
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"{xpath_hesabro.shop.product.search_show}")))
        element.click()
    except:
        is_true = False
    time.sleep(1)
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"{xpath_hesabro.shop.product.product_name}")))
        element.click()
        write_in_element(product_name, element)
    except:
        is_true = False
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"{xpath_hesabro.shop.product.search_btn}")))
        element.click()
    except:
        is_true = False
    time.sleep(2)
    
    
                # element[1].click()
    
    try:
        element =driver.find_element(By.XPATH,xpath_hesabro.shop.product.tbody)
        el_th_ca = element.find_element(By.XPATH,xpath_hesabro.shop.product.thead_category) # element thead category = for sort
        el_th_ca.click()
        time.sleep(2)
        element =driver.find_element(By.XPATH, xpath_hesabro.shop.product.tbody)
        trs = element.find_elements(By.TAG_NAME, "tr")
        find_product = False
        for tr_index in trs:
            tds = tr_index.find_elements(By.TAG_NAME, "td")
        
            category =(tds[2].text)
            print(category)
            if category == "نیش پرفیوم انحصاری" or category == "نیش پرفیوم تجاری":
                for zz in range(10):
                    print(category , tds[5].text)
                    print(oldName)

                if oldName.strip() == tds[5].text.strip():
                    
                        
                    
                        
                        edit_ico = tds[9]
                        edit_ico = edit_ico.find_elements(By.TAG_NAME,"a")
                        edit_ico = edit_ico[3]
                        find_product = True
                        edit_ico.click()
                        
                        break
        time.sleep(3)
        if find_product:
            try:
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, f"{xpath_hesabro.shop.product.edit_p.slug}")))
                clear_txt(element)
                write_in_element(slug, element)
            except:
                is_true = False
            try:
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, f"{xpath_hesabro.shop.product.edit_p.page_title}")))
                clear_txt(element)
                element.click()
                element.clear()
                clear_txt(element)
                write_in_element(page_title, element)
            except:
                is_true = False
            try:
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, f"{xpath_hesabro.shop.product.edit_p.des}")))
                element.click()
                element.clear()
                clear_txt(element)
                write_in_element(des, element)
            except:
                is_true = False
            try:
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, f"{xpath_hesabro.shop.product.edit_p.act}")))
                change_chk(element, act_chk)
            except:
                is_true = False
            try:
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, f"{xpath_hesabro.shop.product.edit_p.save}")))
                element.click()
                time.sleep(3)
                
                # print("Save")
            except:
                is_true = False
    except:
        pass
    return is_true

def run_modification_barcodesCols(driver,main_url,dfData):
    print("please wait until see 'done'...")
    # thisPath = os.getcwd()
    # p_ul = "https://hesabro.ir/@hm/shop/product/index"
    todayIs = djtj.getDateTimeForFileName()
    # counter = 0
    # dfData = pd.read_excel("..//dist/order point/order point.xlsx")
    thisIndex = get_index_modification_barcodesCols(dfData)
    ThisCols = modification_barcodesCols()
    while len(dfData):
        thisData = modification_barcodesCols()
        thisData.product_name = dfData.iat[0, thisIndex.product_name]
        thisData.id = dfData.iat[0,thisIndex.id]
        
        is_True = _run_active_product_in_site(driver,main_url,thisData)
        
        
        dfData = dfData.loc[dfData[ThisCols.id] != thisData.id]
        print(os.getcwd())
        dfData.to_excel("مانده های فعال سازی در سایت.xlsx",index=False)
        # if is_True:
        #     dfData = dfData.loc[dfData[ThisCols.product_name] != thisData.product_name]
        #     dfData.to_excel(f"ثبت نشده های فرایند فعال سازی در سایت مای هانی مون {todayIs}.xlsx",index= False)
        # else:
        #     import random as r
        #     sl = r.randint(20,80)
        #     print(f"please wait for {sl} seconds ...")
        #     time.sleep(sl)
                
       
