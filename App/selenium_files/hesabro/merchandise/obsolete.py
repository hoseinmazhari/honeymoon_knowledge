# from ...settings.xpath import get_xpath
# from ...settings_selenium.app_address import get_address
from selenium_files.settings_selenium import xpath_hesabro 
from selenium_files.settings_selenium.browser import Browser
from selenium_files.settings_selenium.main_defs import write_in_element, change_chk
# ,write_in_element

from selenium.webdriver.common.keys import Keys
import time
from selenium_files.settings_selenium.app_address import urls_hesabro
from selenium_files.settings_selenium.xpath_hesabro import product_view
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class obsolete_products_cols():
    product_name = "عنوان کالا"
    id = "کد کالا"    
    act = "نوع اقدام"

def get_index_obsolete_products_cols(df):
    thisItter = -1
    thisClass = obsolete_products_cols()
    for col in df.columns:
        thisItter += 1
        if col == thisClass.product_name:
            thisClass.product_name = thisItter # type: ignore
        elif col == thisClass.id:
            thisClass.id = thisItter# type: ignore
        elif col == thisClass.act:
            thisClass.act = thisItter #type: ignore
        
    return thisClass


def run_obsolete_products(dfData,driver):
    thisIndex = get_index_obsolete_products_cols(dfData)
    thisCols = obsolete_products_cols()
    while len(dfData):
        act = dfData.iat[0, thisIndex.act]
        id = dfData.iat[0, thisIndex.id]
        dfData = dfData.loc[dfData[thisCols.id] != id]
        driver.get(f"{urls_hesabro.product.product_update}{id}")
        time.sleep(3)
        # try:
        if True:
            # time.sleep(2)
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f"{product_view.tabs.details.update_page.check_exit}")))
            change_chk(element, act)
            # for xxx in range(100):
            #     print(element.is_selected())
            # element.send_keys(Keys.SPACE)
            time.sleep(2)
        # except Exception as e:
        #     print(e)
        # try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f"{product_view.tabs.details.update_page.btn_submit}")))
            element.click()
            # while driver.current_url!= main_url:
            #     driver.get(main_url)
            #     time.sleep(2)
            time.sleep(3)
        # except:
        #     pass
    