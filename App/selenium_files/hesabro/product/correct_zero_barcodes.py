
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
from selenium_files.settings_selenium.app_address import urls_hesabro
# from .merchandise import 
# from selenium_files.settings_selenium.main_defs import    
from selenium_files.settings_selenium.main_defs import write_in_element,search_fieldProduct_navbar,clear_txt, select_product_inSearchFeild
# from ...settings_selenium.browser import write_in_element
from python_files.settings_python import DateJuToJa as djtj
class correct_barcodes():
    # merchandise = "عنوان کالا"
    id = 'آیدی'
    merchandise = 'نام کامل'
    # id = "کد کالا"    
    
		# عنوان کالا	کد کالا	جمع واحد	مقدار	تعداد روز فعال شعبه	مجموع تعداد فروش	ماه	
		

def get_index_correct_barcodes_file(df):
    thisItter = -1
    thisClass = correct_barcodes()
    for col in df.columns:
        thisItter += 1
        if col == thisClass.id:
            thisClass.id = thisItter # type: ignore
        
        elif col == thisClass.merchandise:
            thisClass.merchandise = thisItter # type: ignore
        
    return thisClass

def update_product_correct_prices_barcodes(driver,main_url,id,correct_barcodes): 
    # if act== "exit_product":
        is_true = True
        # is_search_fieldProduct = search_fieldProduct_navbar(driver)
        # while search_fieldProduct(driver)
        # _product_input = driver.switch_to.active_element
        
        # select_product_inSearchFeild(driver, main_url, id, _product_input)
        this_product = f'{urls_hesabro.product.product_view_detail}{id}'
        driver.get(this_product)
        time.sleep(2.4)
        # write_in_element(id,_product_input)
        # _product_input.send_keys(Keys.ENTER)
        # time.sleep(3.5)
        
        # _product_input.send_keys(Keys.ENTER)
        # time.sleep(3.5)
        driver.implicitly_wait(2)
        # while driver.current_url!=main_url:
        if driver.current_url != main_url:
            element = driver.find_element(By.XPATH, xpath_hesabro.product_view.tabs.details.lbl_price_store)
            store_price = str((element.text).replace(',',''))
            
            # try:
            if int(store_price)>10:
                print("store price is: ", store_price)
                try:
                    element = WebDriverWait(driver, 10).until(
                        
                    EC.presence_of_element_located((By.XPATH, f"{xpath_hesabro.product_view.tabs.uniq_Barcode.link}")))
                    element.click()
                    time.sleep(2)
                except:
                    is_true = False
                # is_true = False
                # name = []
                # mobile = []
                # birthday = []
                lsData = []
                counter_page = 1
                repeat_count = 1
                # while is_true==False:
                while True:
                    # thisReport = driver.current_url
                        try:
                            element = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.XPATH, xpath_hesabro.product_view.tabs.uniq_Barcode.tbl)))
                            element.click()

                            
                            element =element.find_element(By.XPATH,xpath_hesabro.product_view.tabs.uniq_Barcode.tbody)
                        except:
                            # break         
                            pass

                        try:
                            # element[1].click()
                            trs = element.find_elements(By.TAG_NAME, "tr")
                            # driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                            this_row = 1
                            # for xxxxx in range(10):
                            #     print("trs len :", len(trs))
                            # test_tr= 0
                            # for tr_test in trs:
                            #     test_tr += 1
                            # print("test count tr is : ", test_tr)
                        except:
                            pass
                        # if True :
                        for tr_index in trs:
                            this_row += 2
                            # print("this_row = ", this_row)
                            have_row = True
                            try:
                                tds = tr_index.find_elements(By.TAG_NAME, "td")
                                price = (f"{(tds[7].text)}") # 7 is sale price
                                print("price is: ", price)
                                # price = int(price)
                                
                                is_exit = f"{(tds[12].text)}"  # 12 is date exit
                                # for yyy in range(10):
                                print(is_exit, "len date exit is: " ,len(is_exit))
                            except: 
                                have_row = False
                            if have_row:
                                if len(price)<3 and len(is_exit) == 0:
                                # if True:
                                    # try:
                                        act_btn = f'//*[@id="w{this_row}-button"]'
                                        element = driver.find_element(By.XPATH,act_btn)
                                        element.click()
                                        time.sleep(2.3)
                                        update_btn = f'//*[@id="w{this_row+1}"]/a[5]'
                                        element = driver.find_element(By.XPATH,update_btn)
                                        element.click()
                                        time.sleep(2.3)

                                        element = driver.find_element(By.XPATH,xpath_hesabro.product_view.tabs.uniq_Barcode.update_form.price)
                                        element.click()
                                        time.sleep(2.3)
                                        
                                        clear_txt(element)
                                        time.sleep(2)
                                        write_in_element(store_price, element)
                                        time.sleep(2)
                                        element = driver.find_element(By.XPATH,xpath_hesabro.product_view.tabs.uniq_Barcode.update_form.submit_btn)
                                        element.click()
                                        time.sleep(2.3)
                                        is_closed = False
                                        while is_closed ==False:
                                            try:
                                                element = driver.find_element(By.XPATH, xpath_hesabro.product_view.tabs.uniq_Barcode.update_form.close_form)
                                                element.click()
                                                time.sleep(2.3)
                                                is_closed = True
                                            except:
                                                is_closed = False
                                        
                                    # except:
                                    #     pass    
                            # for i in range(len(tds)) :
                            #      print(f"{i}: { (tds[i].text)}")                       # for more pretty actions in ui , ux this code writed to next_p
                        
                        # time.sleep(0.6)
                        # thisPage = driver.current_url
                        # pageIndexStart = thisPage.find("&page=")+1
                        # pageIndexEnd = thisPage.find("&per-page")
                        # print(thisPage[pageIndexStart:pageIndexEnd])
                        # print(time.ctime())
                        # print(counter_page)
                        # print("-------------------------")
                        
                        
                        
                        
                        
                        try:
                            this_url = driver.current_ulr
                            element =driver.find_element(By.XPATH,xpath_hesabro.product_view.tabs.uniq_Barcode.next_p)
                            counter_page += 1
                            element.click()
                            time.sleep(4)
                            new_page = driver.current_url
                            if new_page == this_url:
                                time.sleep(1)
                                break
                        except:
                            break
                    
                        # if element.is_displayed():
                                
                                
                                # time.sleep(1)
                        # else:
                        #     is_true = True
                            # driver.close()
                #         # time.sleep(6)
                #         if counter_page%1==0:
                #             # counter_page = 1
                #             thisData = pd.DataFrame(lsData)
                #             # thisData.to_excel(f"{title}bk_p50.xlsx",index=False)
                #     except Exception as e:
                #         # print(e)
                #         repeat_count += 1
                #         if repeat_count>20:
                #             break
                #         try:
                #             # data = pd.read_excel(f"{title}bk_p50.xlsx")
                #             row = data['row'].max()
                #             page_index = row//50
                #         except:
                #             page_index =1
                #         pageIndexStart = thisPage.find("&page=")+6
                #         pageIndexEnd = thisPage.find("&per-page")
                #         # print(thisPage[pageIndexStart:pageIndexEnd])
                #         step1 = thisReport[:pageIndexStart]
                #         step2 = thisReport[pageIndexEnd:]
                #         this_address = f"{step1}{page_index}{step2}"
                #         driver.close()
                #         from ...settings.run_app import run_hesabro
                #         driver, is_logged_in = run_hesabro()
                        
                #         driver.get(this_address)
                #         this_delay = 3
                #         while driver.current_url != this_address: # جهت اطمینان از باز شدن صفحه ی درخواست شده در گزینه 1 از حلقه استفاده شده است
                #             driver.get(this_address)
                #             time.sleep(this_delay)
                #             this_delay += 1
                #         # data = pd.DataFrame(lsData)
                #         # data.to_excel(f"{title}.xlsx",index=False)
                #         # is_true = True
                        
                        
                        
                #     #     time.sleep(5)
                #     #     is_true = False
                # data = pd.DataFrame(lsData)
                # data.to_excel(f"{title}.xlsx",index=False)
                # return data
                    # element = WebDriverWait(driver, 10).until(
                    #     EC.presence_of_element_located((By.XPATH, xph.create_reportcustomer.download)))
            # except Exception as e:
            #     print(e)
            #     is_true = False

def run_correctPrices_to_barcodes(driver,main_url, dfData):
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
    #     # thisIndex = get_index_correct_barcodes_file(dfData)
    #     # print("start export file")
    #     # branch = dfData.iat[0,thisIndex.branch]
    #     # dfData.to_excel(f" {branch} -{todayIs}.xlsx",index= False)
    #     # print("export complete")
    #     # testers_avalible = True
    # dfData = pd.concat(lsData)
    # dfData.to_excel("order point all brs.xlsx")
    # return False
    counter = 0
    # dfData = pd.read_excel("..//dist/order point/products.xlsx")
    thisIndex = get_index_correct_barcodes_file(dfData)
    # ls_true = []
    # ls_false = []
    ls_ans = []
    while len(dfData):
        driver.get(main_url)
        time.sleep(3)
        counter += 1
        merchandise = dfData.iat[0,thisIndex.merchandise]
        
        
        id = f"{int(dfData.iat[0,thisIndex.id])}"
        
        # print(counter)
        is_True = update_product_correct_prices_barcodes(driver,main_url,id,correct_barcodes)
        # is_True = update_product_correct_prices_barcodes(driver,main_url,id,correct_barcodes)
        
        dfData = dfData.loc[dfData[correct_barcodes.id]!= int(id)]
        if is_True:
            ls_ans.append({"id":id, "product":merchandise,"is_True":True})
            # dfData.to_excel("correct-mod.xlsx",index= False)
        else:
            ls_ans.append({"id":id, "product":merchandise,"is_True":False})
            # import random as r
            # sl = r.randint(2,6)
            # print(f"please wait for {sl} seconds ...")
            # time.sleep(sl)
        df_ans = pd.DataFrame(ls_ans)
        dfData.to_excel("ZeroBarcodes.xlsx", index=False)
        df_ans.to_excel("ans correctBarcodes.xlsx",index=False)
        # if is_True:
        #     ls_true.append({testers.id:id,testers.tester:tester,testers.buy_price:buy_price,testers.sale_price:salePrice})
        #     df = pd.DataFrame(ls_true)
        #     df.to_excel("ok_orders.xlsx",index=False)
        # else:
        #     # try:
        #     ls_false.append({testers.id:id,testers.tester:tester,testers.buy_price:buy_price,testers.sale_price:salePrice})
        #     df = pd.DataFrame(ls_false)
        #     df.to_excel("false_]orders.xlsx",index=False)
        #     # except:
        #     #     pass
