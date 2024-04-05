
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
from selenium_files.settings_selenium.main_defs import write_in_element, change_chk #...
from python_files.settings_python import DateJuToJa as djtj #....
# from ...settings import xpath

class active_inSiteCols():
    product_name = "product_name"
    page_title = "page_title"
    slug = "slug"
    des = "des"
    act = "act"

def get_index_active_inSite(df):
    thisItter = -1
    thisClass = active_inSiteCols()
    for col in df.columns:
        thisItter += 1
        if col == thisClass.product_name:
            thisClass.product_name = thisItter # type: ignore
        elif col == thisClass.page_title:
            thisClass.page_title = thisItter

        elif col == thisClass.slug:
            thisClass.slug = thisItter # type: ignore
        elif col == thisClass.des:
            thisClass.des = thisItter # type: ignore
        elif col == thisClass.act:
            thisClass.act = thisItter # type: ignore
        # elif col == thisClass.buy_price:
        #     thisClass.buy_price = thisItter # type: ignore
    return thisClass
       
def _run_active_product_in_site(driver,main_url,thisData): 
    # if act== "exit_product":
    is_true = True
    scales = [10, 15, 20, 30, 50]
    pre = "نیش"
    # thisData = active_inSiteCols()
    
    act_chk = thisData.act
    for scale in scales:
        driver.get(main_url)
        time.sleep(4)
        
        product_name = f"{pre} {thisData.product_name} {scale}"
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
            _product_input.send_keys(Keys.ENTER)
            time.sleep(3.5)
            
            _product_input.send_keys(Keys.ENTER)
            time.sleep(3.5)
            driver.implicitly_wait(2)
            if driver.current_url != main_url:
                is_exist_product = True
            if tryCount >= 3:
                break
                # while driver.current_url!=main_url:
        if is_exist_product:   
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
                time.sleep(2)
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, f"{xpath_hesabro.product.update_form.site_price}")))
                element.click()
                element.clear()
                for iter in range(100):
                    element.send_keys(Keys.BACK_SPACE)
                    element.send_keys(Keys.DELETE)
                time.sleep(2)
                write_in_element(store_price,element)
            except:
                is_true = False
            
            try:
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, f"{xpath_hesabro.product.update_form.site_chekbox}")))
                time.sleep(2)
                change_chk(element, act_chk)
                time.sleep(2)
            except:
                is_true = False
            
            try:
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, f"{xpath_hesabro.product.update_form.select_Supplier}")))
                time.sleep(2)
                element.click()
                time.sleep(2)
            except:
                is_true = False
            
            try:
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, f"{xpath_hesabro.product.update_form.select_Supplier_site}")))
                time.sleep(2)
                element.click()
                time.sleep(2)
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
    
    element =driver.find_element(By.XPATH,xpath_hesabro.shop.product.tbody)
                # element[1].click()
    trs = element.find_elements(By.TAG_NAME, "tr")
    for tr_index in trs:
        tds = tr_index.find_elements(By.TAG_NAME, "td")
       
        category =(tds[2].text)
        print(category)
        if category == "نیش پرفیوم انحصاری" or category == "نیش پرفیوم تجاری":
            print(category , tds[5])
            if product_name == tds[5]:
                
                edit_ico = tds[9]
                edit_ico = edit_ico.find_elements(By.TAG_NAME,"a")
                edit_ico = edit_ico[3]
                edit_ico.click()
                
                break
    time.sleep(3)
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"{xpath_hesabro.shop.product.edit_p.slug}")))
        element.click()
        element.clear()
        write_in_element(slug, element)
    except:
        is_true = False
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"{xpath_hesabro.shop.product.edit_p.page_title}")))
        element.click()
        element.clear()
        write_in_element(page_title, element)
    except:
        is_true = False
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"{xpath_hesabro.shop.product.edit_p.des}")))
        element.click()
        element.clear()
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
    return is_true

def run_active_products_inSite(driver,main_url,dfData):
    print("please wait until see 'done'...")
    # thisPath = os.getcwd()
    p_ul = "https://hesabro.ir/@hm/shop/product/index"
    todayIs = djtj.getDateTimeForFileName()
    # counter = 0
    # dfData = pd.read_excel("..//dist/order point/order point.xlsx")
    thisIndex = get_index_active_inSite(dfData)
    ThisCols = active_inSiteCols()
    while len(dfData):
        thisData = active_inSiteCols()
        thisData.product_name = dfData.iat[0, thisIndex.product_name]
        thisData.slug = dfData.iat[0,thisIndex.slug]
        thisData.page_title = dfData.iat[0, thisIndex.page_title]
        thisData.des = dfData.iat[0, thisIndex.des]
        thisData.act = dfData.iat[0, thisIndex.act]
        
        is_True = _run_active_product_in_site(driver,main_url,thisData)
        
        is_act = _run_active_shop(driver,p_ul,thisData)
        dfData = dfData.loc[dfData[ThisCols.product_name] != thisData.product_name]
        # if is_True:
        #     dfData = dfData.loc[dfData[ThisCols.product_name] != thisData.product_name]
        #     dfData.to_excel(f"ثبت نشده های فرایند فعال سازی در سایت مای هانی مون {todayIs}.xlsx",index= False)
        # else:
        #     import random as r
        #     sl = r.randint(20,80)
        #     print(f"please wait for {sl} seconds ...")
        #     time.sleep(sl)
                
       
