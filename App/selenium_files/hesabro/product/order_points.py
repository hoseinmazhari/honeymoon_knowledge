# from ...settings.xpath import get_xpath
# from ...settings_selenium.app_address import get_address
from selenium_files.settings_selenium import xpath_hesabro 
from selenium_files.settings_selenium.browser import Browser
from selenium_files.settings_selenium.main_defs import write_in_element, clear_txt
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

class Order_point_cols():
    product_name = "عنوان کالا"
    # order_point= "حد سفارش"
    order_point = 'کف سفارش'
    # buy_price = "old sale price"
    product_id = "کد کالا"    
    branch = "عنوان شرکت"
		# عنوان کالا	کد کالا	جمع واحد	مقدار	تعداد روز فعال شعبه	مجموع تعداد فروش	ماه	
		

def get_index_order_point_cols(df):
    thisItter = -1
    thisClass = Order_point_cols()
    for col in df.columns:
        thisItter += 1
        if col == thisClass.product_id:
            thisClass.product_id = thisItter # type: ignore
        # elif col == thisClass.branch:
        #     thisClass.branch = thisItter

        # elif col == thisClass.buy_price:
        #     thisClass.buy_price = thisItter # type: ignore
        elif col == thisClass.product_name:
            thisClass.product_name = thisItter # type: ignore
        elif col == thisClass.order_point:
            thisClass.order_point = thisItter # type: ignore
        # elif col == thisClass.buy_price:
        #     thisClass.buy_price = thisItter # type: ignore
    return thisClass


def set_order_point(dfData,driver):
    thisIndex = get_index_order_point_cols(dfData)
    thisCols = Order_point_cols()
    while len(dfData):
        order_point = dfData.iat[0, thisIndex.order_point]
        product_id = dfData.iat[0, thisIndex.product_id]
        dfData = dfData.loc[dfData[thisCols.product_id] != product_id]
        driver.get(f"{urls_hesabro.product.product_update}{product_id}")
        time.sleep(3)
        # try:
        if True:
            # time.sleep(2)
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f"{product_view.tabs.details.update_page.order_point}")))
            element.click()
            clear_txt(element)
            time.sleep(1)
            write_in_element(order_point,element)
            # change_chk(element, act)
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
    for i in range(100):
        print("Enjoy! operation is complete.")