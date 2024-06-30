
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
class Sale_factor_list_cols():
    id = "آیدی"
    branch = "شعبه"
    factor_date = "تاریخ فاکتور"
    mod = "مانده"
    factor_price = "مبلغ فاکتور"
    factor_type = "نوع فاکتور"
    factor_group = "گروه"
    customer = "مشتری"
    moaref = "معرف"
    registrar = "عامل"
    created_in = "ایحاد شده"
    payment_type = "نوع پرداخت"
    is_ok = "تایید"
def get_index_Sale_factor_list_cols(df):
    thisCols = Sale_factor_list_cols()
    thisItter = -1
    for col in df.columns():
        thisItter+= 1
        if col == thisCols.id:
            thisCols.id = thisItter
        elif col == thisCols.branch:
            thisCols.branch = thisItter
        elif col == thisCols.factor_date:
            thisCols.factor_date = thisItter
        elif col == thisCols.mod:
            thisCols.mod = thisItter
        elif col == thisCols.factor_price:
            thisCols.factor_price = thisItter
        elif col == thisCols.factor_type:
            thisCols.factor_type = thisItter
        elif col == thisCols.factor_group:
            thisCols.factor_group = thisItter
        elif col == thisCols.customer:
            thisCols.customer = thisItter
        elif col == thisCols.moaref:
            thisCols.moaref = thisItter
        elif col == thisCols.registrar:
            thisCols.registrar = thisItter
        elif col == thisCols.created_in:
            thisCols.created_in = thisItter
        elif col == thisCols.payment_type:
            thisCols.payment_type = thisItter
        elif col == thisCols.is_ok:
            thisCols.is_ok = thisItter
    return thisCols

def sale_factors(driver):
    thisCols = Sale_factor_list_cols()
    ls_data = []
    title = "لیست فاکتور های خروج"
    page_number = 1
    is_true = True
    driver.get(Urls_hesabro.Factor.sale)
    while is_true == True:
        
        element = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, f"{xpath_hesabro.Sale_factors.tbl}")))
        element = WebDriverWait(element, 10).until(
                        EC.presence_of_element_located((By.XPATH, f"{xpath_hesabro.Sale_factors.tbody}")))
        trs = element.find_elements(By.TAG_NAME, "tr")
        for tr_index in trs:
            tds = tr_index.find_elements(By.TAG_NAME, "td")
            id = tds[2].text
            branch = tds[4].text
            factor_date = tds[5].text
            mod = tds[6].text
            factor_price = tds[7].text
            factor_type = tds[8].text
            factor_group = tds[9].text
            customer = tds[10].text
            customer = customer.replace("(موقت)", "")
            moaref = tds[11].text
            registrar = tds[12].text
            created_in = tds[13].text
            payment_type = tds[14].text
            is_ok = tds[15].text
            
            ls_data.append({
                thisCols.id:id, thisCols.branch:branch, thisCols.
                factor_date:factor_date,
                thisCols.mod:mod, thisCols.factor_price:factor_price, 
                thisCols.factor_type:factor_type,
                thisCols.factor_group:factor_group, thisCols.customer:customer,
                thisCols.moaref:moaref, thisCols.registrar:registrar, 
                thisCols.created_in:created_in,thisCols.payment_type:payment_type,
                thisCols.is_ok:is_ok
            })
            
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(1.2)
        page_number += 1
        page_address_p1 = "https://hesabro.ir/@hm/factor/index?get_total=true&page="
        page_address_p2 = "&per-page=30"
        next_page = f"{page_address_p1}{page_number}{page_address_p2}"
        this_delay = 3
        dfData = pd.DataFrame(ls_data)
        dfData.to_excel(f"{title}.xlsx",index=False)
        while driver.current_url != next_page:
            driver.get(next_page)
            time.sleep(this_delay)
            if this_delay<60:
                this_delay+=1
            else:
                # dfData = pd.DataFrame(ls_data)
                # dfData.to_excel(f"{title}.xlsx",index=False)
                is_true = False
                driver.close()
                # this_delay = 3
                break
    return dfData
        # if page_number % 50 == 0:
        #     dfData = pd.DataFrame(ls_data)
        #     dfData.to_excel(f"{title}.xlsx",index=False)
        # page_address = 
        # if page_number == 1:
        #     element =driver.find_element(By.XPATH,xpath_hesabro.Sale_factors.show_counter)
        #     element.click()
        #     time.sleep(2)
        #     driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        #     time.sleep(1.2)
        # element =driver.find_element(By.XPATH,xpath_hesabro.Sale_factors.next_p)
        # if element.is_displayed():
        # element.click()
        # time.sleep(3)
    # else:
        # is_true = False
        