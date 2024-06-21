
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
from selenium_files.settings_selenium.app_address import Urls_hesabro
class active_inSiteCols():
    # is_proccess_true = "اعمال موفق تغییرات"
    id = "آیدی"
    scale_index = "اندیس حجم"
    scale = "حجم"
    act = "وضعیت"
    # oldName = "oldName"
    # page_title = "page_title"
    # slug = "slug"
    # des = "des"
    # act = "act"

def get_index_active_inSite(df):
    thisItter = -1
    thisCols = active_inSiteCols()
    for col in df.columns:
        thisItter += 1
        if col == thisCols.id:
            thisCols.id = thisItter # type: ignore
        elif col == thisCols.scale:
            thisCols.scale = thisItter
        elif col == thisCols.scale_index:
            thisCols.scale_index = thisItter
        elif col == thisCols.act:
            thisCols.act = thisItter
        # elif col == thisCols.is_proccess_true:
        #     thisCols.is_proccess_true = thisItter
        # elif col == thisCols.oldName:
        #     thisCols.oldName = thisItter
        # elif col == thisCols.page_title:
        #     thisCols.page_title = thisItter
        # elif col == thisCols.slug:
        #     thisCols.slug = thisItter # type: ignore
        # elif col == thisCols.des:
        #    thisCols.des = thisItter # type: ignore
        # elif col == thisCols.act:
        #     thisCols.act = thisItter # type: ignore
        # # elif col == thisCols.buy_price:
        #     thisCols.buy_price = thisItter # type: ignore
    return thisCols
def change_product_attr(driver, thisData, act_chk):
            # scale_index = thisData.scale_index
            scale = thisData.scale
            scale_items = [10, 20, 30, 50, 100, 15, 12]
            scale_index = scale_items.index(scale)
            # time.sleep(6)
            # try:
            #     element = WebDriverWait(driver, 10).until(
            #         # EC.presence_of_element_located((By.XPATH, f"{xpath_hesabro.product.view.act_button}")))
            #         EC.presence_of_element_located((By.XPATH, f"{xpath_hesabro.product_view.tabs.details.act_button}")))
            #     element.click()
            # except:
            #     is_true = False
            # try:
            #     element = WebDriverWait(driver, 10).until(
            #         # EC.presence_of_element_located((By.XPATH, f"{xpath_hesabro.product.view.update_btn}")))
            #         EC.presence_of_element_located((By.XPATH, f"{xpath_hesabro.product_view.tabs.details.update_btn}")))
            #     element.click()
            # except:
            #     is_true = False
            # print(scale_index)
            try:
            # if True
                time.sleep(3)
                element = WebDriverWait(driver, 10).until(
                    # EC.presence_of_element_located((By.XPATH, f"{xpath_hesabro.product.update_form.store_price}")))
                    EC.presence_of_element_located((By.XPATH, f"{xpath_hesabro.product_view.tabs.details.update_page.store_price}")))
                # element = driver.findelement(By.XPATH, '//*[@id="product-price1"]')
                element.click()
                # time.sleep(3)
                store_price = (element.get_attribute("value"))
                # 24,390,000
                # print(store_price)
                # store_price = store_price.replace(",", "")
                # site_price = str(int(store_price)//2)
                # site_price = store_price
                site_price = store_price
            except:
                is_true = False
            try:
                time.sleep(1)
                element = WebDriverWait(driver, 10).until(
                    # EC.presence_of_element_located((By.XPATH, f"{xpath_hesabro.product.update_form.site_price}")))
                    EC.presence_of_element_located((By.XPATH, f"{xpath_hesabro.product_view.tabs.details.update_page.site_price}")))
                clear_txt(element)
                time.sleep(1)
                write_in_element(site_price,element)
            except:
                is_true = False
            try:
                time.sleep(1)
                element = WebDriverWait(driver, 10).until(
                    # EC.presence_of_element_located((By.XPATH, f"{xpath_hesabro.product.update_form.site_price}")))
                    EC.presence_of_element_located((By.XPATH, f"{xpath_hesabro.product_view.tabs.details.update_page.off_price}")))
                clear_txt(element)
                time.sleep(1)
                clear_txt(element)
                # store_price = store_price.replace(",", "")
                # off_price = str(int(store_price)//2)
                # write_in_element(off_price,element)
                
            except:
                is_true = False
            try:
                element = WebDriverWait(driver, 10).until(
                    # EC.presence_of_element_located((By.XPATH, f"{xpath_hesabro.product.update_form.site_chekbox}")))
                    EC.presence_of_element_located((By.XPATH, f"{xpath_hesabro.product_view.tabs.details.update_page.site_chekbox}")))
                time.sleep(1)
                change_chk(element, act_chk)
                time.sleep(1)
            except:
                is_true = False
            
            
            try:
                element = WebDriverWait(driver, 10).until(
                    # EC.presence_of_element_located((By.XPATH, f"{xpath_hesabro.product.update_form.warranty_selector}")))
                    EC.presence_of_element_located((By.XPATH, f"{xpath_hesabro.product_view.tabs.details.update_page.warranty_selector}")))
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
                element = driver.find_element(By.XPATH,xpath_hesabro.product_view.tabs.details.update_page.unit_selector)
                # element = WebDriverWait(driver, 10).until(
                #     EC.presence_of_element_located((By.XPATH, f"{xpath_hesabro.product.update_form.unit_selector}")))
                # time.sleep(1)
                element.click()
                time.sleep(1)
                element= WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, f"{xpath_hesabro.product_view.tabs.details.update_page.unit_item}")))
                 
                element.click()
                time.sleep(2.2)
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, f"{xpath_hesabro.product_view.tabs.details.update_page.scale_selector}")))
                time.sleep(1)
                element.click()
                time.sleep(1)
                item = f"{xpath_hesabro.product_view.tabs.details.update_page.scale_item}{scale_index+2}]"
                # print(item)
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, f"{item}")))
                time.sleep(1)
                element.click()
                time.sleep(1)
            except:
            #         print(e)
            #     # try:
            # if True:
                    # for u in range(10):
                    #     print("select Unit not found")
                    # element = driver.find_element(By.XPATH,xpath_hesabro.product.update_form.btn_add_unitscale_index)
                    element = driver.find_element(By.XPATH,xpath_hesabro.product_view.tabs.details.update_page.div_add_unitScale)
                    # element = WebDriverWait(driver, 10).until(
                    #     EC.presence_of_element_located((By.XPATH, f"{xpath_hesabro.product.update_form.btn_add_unitscale_index}")))
                    # time.sleep(1)
                    element.click()
                    time.sleep(1)
                    
                    # element = element.find_element(By.TAG_NAME,'button')
                    # element.send_keys(Keys.ENTER)
                    # element = WebDriverWait(driver, 10).until(
                    #     EC.presence_of_element_located((By.XPATH, f"{xpath_hesabro.product.update_form.btn_add_unitscale_index}")))
                    # time.sleep(1)
                    # element.click()
                    time.sleep(3)
                    
                # except:
                #     for u in range(10):
                #         print("select addUnit not found")
                #     is_true =False
                # try:
                    # element = driver.find_element(By.XPATH,xpath_hesabro.product_view.tabs.details.update_page.div_scale_indexContainer)
                    # print(scale_index)
                    element = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, f"{xpath_hesabro.product_view.tabs.details.update_page.unit_selector}")))
                    time.sleep(1)
                    element.click()
                    time.sleep(2.3)
                # except:
                #     is_true =False
                # try:
                    # element = element.find_element(By.TAG_NAME,"option")
                    # element[2].click()
                    element= WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, f"{xpath_hesabro.product_view.tabs.details.update_page.unit_item}")))
                    # time.sleep(1)
                    # element = driver.switch_to.active_element
                    # for jj in range(3):

                    #     # element.send_keys(Keys.DOWN)
                    #     element.send_keys(Keys.DOWN)
                    #     time.sleep(1.3)
                    element.click()
                    # element.send_keys(Keys.RETURN)
                    time.sleep(2.2)
                # except:
                #     is_true =False
                # try:
                    element = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, f"{xpath_hesabro.product_view.tabs.details.update_page.scale_selector}")))
                    time.sleep(1)
                    element.click()
                    time.sleep(1)
                # except:
                #     is_true =False
                # try:
                    # /html/body/div[2]/div/div[2]/form/div/div[1]/div[4]/div/div/div/div[2]/div/div[2]/div/div[2]/div/select/option[4]
                    # /html/body/div[2]/div/div[2]/form/div/div[1]/div[4]/div/div/div/div[2]/div/div[2]/div/div[2]/div/select/option[5]
                    # print(scale_index)
                    item = f"{xpath_hesabro.product_view.tabs.details.update_page.scale_item}{scale_index+2}]"
                    # print(item)
                    element = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, f"{item}")))
                    time.sleep(1)
                    element.click()
                    time.sleep(1)
                # except:
                #     is_true =False
                
            try:
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, f"{xpath_hesabro.product_view.tabs.details.update_page.select_Supplier}")))
                time.sleep(1)
                element.click()
                time.sleep(1)
            except:
                is_true = False
            
            try:
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, f"{xpath_hesabro.product_view.tabs.details.update_page.select_Supplier_site}")))
                time.sleep(1)
                element.click()
                time.sleep(1)
            except:
                is_true = False
            time.sleep(3)
            
            try:
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, f"{xpath_hesabro.product_view.tabs.details.update_page.btn_submit}")))
                element.click()
                time.sleep(2)
                # while driver.current_url!= main_url:
                #     driver.get(main_url)
                #     time.sleep(2)
            except:
                is_true = False
            
           
# def _run_active_product_in_site(driver,main_url,thisData): 
#     # if act== "exit_product":
#     is_true = True
#     ls_invalid = []
    # scale_indexs = [10,  20, 30, 50, 100, 15]
    # scale_indexs = [30, 50, 100, 15]
    # pre = "نیش"
    # aft = "میل"
    # thisData = active_inSiteCols()
    
    # act_chk = thisData.act
    # for scale_index in scale_indexs:
    # driver.get(main_url)
    # time.sleep(4)
    
    # product_name = f"{pre} {thisData.product_name} {scale_index} {aft}"
    # product_name1 = f"{thisData.product_name} {scale_index} {aft}"
    # product_name2 = f"{thisData.product_name} - {scale_index} {aft}"
    # product_id = thisData.id
    # is_search_fieldProduct = search_fieldProduct_navbar(driver)
    # search_fieldProduct_navbar(driver)
    # while search_fieldProduct(driver)
    # _product_input = driver.switch_to.active_element
    # tryCount = 0
    # is_exist_product = False
    # while is_exist_product== False:
    #     tryCount += 1
        
    #     _product_input.clear()
    #     write_in_element(product_name, _product_input)
    #     # _product_input.send_keys(Keys.ENTER)
    #     time.sleep(3.5)
    #     element = driver.find_element(By.XPATH,xpath_hesabro.navbar.searchbar.merchandise_list)
    #     lst = element.find_elements(By.TAG_NAME,"li")
    #     # lst = element
    #     for item in lst:
    #         thisItem = item.text
    #         try:
    #             while "  " in thisItem:
    #                 thisItem = thisItem.replace("  ", " ")
    #         except: 
    #             pass
    #         if pre in thisItem:
    #             if product_name1 in thisItem  or product_name2 in thisItem  :
    #                 item.click()
    #                 # for w in range(10):
    #                 #     print(item.text)
    #                 # element = driver.active_element
    #                 # element.send_keys(Keys.ENTER)
    #                 # item.send_keys(Keys.ENTER)
    #                 time.sleep(3)
    #                 break
    #         # element.send_keys(Keys.DOWN)
    #     # if driver.current_url == main_url:
    #         # _product_input.send_keys(Keys.ENTER)
    #         # time.sleep(3.5)
            
    #     driver.implicitly_wait(2)
    #     if driver.current_url != main_url:
    #         is_exist_product = True
    #     if tryCount >= 2:
    #         ls_invalid.append({"product":product_name,"is_search":False})
    #         is_true = False
    #         break
    #         # while driver.current_url!=main_url:
    # if is_exist_product:   
        
    # change_product_attr(driver, scale_indexs, scale_index, act_chk)
    # dfInvalid = pd.DataFrame(ls_invalid)
    # return is_true
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

def run_active_products_inSite(driver,main_url,dfData):
    print("please wait until see 'done'...")
    # thisPath = os.getcwd()
    # p_ul = "https://hesabro.ir/@hm/shop/product/index"
    # todayIs = djtj.getDateTimeForFileName()
    # counter = 0
    # dfData = pd.read_excel("..//dist/order point/order point.xlsx")
    thisIndex = get_index_active_inSite(dfData)
    ThisCols = active_inSiteCols()
    # ls_invalid = []
    while len(dfData):
        thisData = active_inSiteCols()
        # thisData.product_name = dfData.iat[0, thisIndex.product_name]
        # thisData.slug = dfData.iat[0,thisIndex.slug]
        # thisData.page_title = dfData.iat[0, thisIndex.page_title]
        # thisData.des = dfData.iat[0, thisIndex.des]
        # thisData.act = dfData.iat[0, thisIndex.act]
        # thisData.oldName = dfData.iat[0, thisIndex.oldName]
        thisData.id = dfData.iat[0, thisIndex.id]
        thisData.act = dfData.iat[0, thisIndex.act]
        # thisData.scale_index = int(dfData.iat[0, thisIndex.scale_index])
        thisData.scale = int(dfData.iat[0, thisIndex.scale])
        driver.get(f"{Urls_hesabro.Product.product_update}{thisData.id}")
        change_product_attr(driver=driver,thisData=thisData,act_chk=thisData.act)
        # is_True,df_invalid = _run_active_product_in_site(driver,main_url,thisData)
        # ls_invalid.append(df_invalid)
        # if len(df_invalid)!= 
        # is_act = _run_active_shop(driver,p_ul,thisData)
        time.sleep(3)
        # driver.get(main_url)
        # time.sleep(3)
        dfData = dfData.loc[dfData[ThisCols.id] != thisData.id]
        # print(os.getcwd())
        dfData.to_excel("مانده های فعال سازی در سایت.xlsx",index=False)
    print("DONE")
    print("ALL PRODUCTS SUCCESSFULLY EDITED.")

    # dfData = pd.concat(ls_invalid)
    # dfData.to_excel("محصولاتی که در کادر جستجو در فعال سازی برای سایت انتخاب نشدند.xlsx",index=False)
        # if is_True:
        #     dfData = dfData.loc[dfData[ThisCols.product_name] != thisData.product_name]
        #     dfData.to_excel(f"ثبت نشده های فرایند فعال سازی در سایت مای هانی مون {todayIs}.xlsx",index= False)
        # else:
        #     import random as r
        #     sl = r.randint(20,80)
        #     print(f"please wait for {sl} seconds ...")
        #     time.sleep(sl)
                
       
