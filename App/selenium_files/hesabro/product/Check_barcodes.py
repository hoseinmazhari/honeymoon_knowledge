import time, pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
# from .xpath import get_xpath
# from ...settings.xpath import get_xpath
from selenium_files.settings_selenium import xpath_hesabro 


# from selenium_files.settings_selenium.xpath_hesabro import navbar
from selenium_files.settings_selenium.app_address import hesabro_domain
from selenium_files.settings_selenium.main_defs import write_in_element,search_fieldProduct_navbar,clear_txt, select_product_inSearchFeild

class Barcode_cols():
    mobile = "شماره موبایل"
    barcode = "پاسخ"
    send_at = "زمان ارسال"
    lottery_id = "ردیف شانس"

def get_index_Barcode_cols(df):
    thisCols = Barcode_cols()
    thisItter = -1
    for col in df.columns:
        thisItter += 1
        if col == thisCols.mobile:
            thisCols.mobile = thisItter
        elif col == thisCols.barcode:
            thisCols.barcode = thisItter
        elif col == thisCols.send_at:
            thisCols.send_at = thisItter
        elif col == thisCols.lottery_id:
            thisCols.lottery_id = thisItter
    return thisCols

def run_check(driver, dfData):
    thisCols = Barcode_cols()
    thisIndex = get_index_Barcode_cols(dfData)
    # check_barcode_address = "https://hesabro.ir/@hm/"
    # serial_txt = "check_barcode_address"
    thisItter = 1
    ls_data = []
    while len(dfData):
        thisItter += 1
        barcode = dfData.iat[0 , thisIndex.barcode]
        mobile = dfData.iat[0, thisIndex.mobile]
        send_at = dfData.iat[0, thisIndex.send_at]
        lottery_id = dfData.iat[0, thisIndex.lottery_id]
        dfData = dfData.loc[dfData[thisCols.barcode]!= barcode]
        while driver.current_url != hesabro_domain:
            driver.get(hesabro_domain)
            time.sleep(1.1)
        element = driver.find_element(By.XPATH,xpath_hesabro.navbar.searchbar.serial_input)
        element.click()
        write_in_element(barcode,element)
        # time.sleep(2)
        element.send_keys(Keys.ENTER)
        time.sleep(3)
        try:
            element = driver.find_element(By.XPATH, xpath_hesabro.Check_barcodes.exit_item)
            element.click()
            ls_data.append({thisCols.barcode:barcode,thisCols.mobile:mobile,
                            thisCols.send_at:send_at, thisCols.lottery_id:lottery_id})
            
        except:
            pass
    dfData = pd.DataFrame(ls_data)
    dfData.to_excel("test_barcodes.xlsx", index=False)