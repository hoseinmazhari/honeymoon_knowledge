


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
from selenium_files.hesabro.club.coin import coin_setter
import os, pandas as pd						
class Update_hesabro_customers_from_hamyar_cols():
    mobile = "موبایل"
    customer = "نام ونام خانوادگی"
    charge = "مانده شارژ"
    coin = "شارژ معادل برای حسابرو"
    birthday = 'تاریخ تولد'
    address = 'آدرس'
    postalCode = 'کدپستی'
    work = 'شغل'
    phone = 'تلفن'
    codeMelli = 'کدملی'
    gender = 'جنسیت'
    education = 'تحصیلات'
def get_index_Update_hesabro_customers_from_hamyar_cols(df):
    thisClass = Update_hesabro_customers_from_hamyar_cols()
    thisItter = -1
    for col in df.columns:
        thisItter += 1
        if col == thisClass.mobile:
            thisClass.mobile = thisItter #type: ignore
        elif col == thisClass.customer:
            thisClass.customer = thisItter #type: ignore
        elif col == thisClass.charge:
            thisClass.charge = thisItter #type: ignore
        elif col == thisClass.coin:
            thisClass.coin = thisItter #type: ignore
        elif col == thisClass.birthday:
            thisClass.birthday = thisItter #type: ignore
        elif col == thisClass.address:
            thisClass.address = thisItter #type: ignore
        elif col == thisClass.postalCode:
            thisClass.postalCode = thisItter #type: ignore
        elif col == thisClass.work:
            thisClass.work = thisItter #type: ignore
        elif col == thisClass.phone:
            thisClass.phone = thisItter #type: ignore
        elif col == thisClass.codeMelli:
            thisClass.codeMelli = thisItter #type: ignore
        elif col == thisClass.gender:
            thisClass.gender = thisItter #type: ignore
        elif col == thisClass.education:
            thisClass.education = thisItter #type: ignore
    return thisClass

def act():
    pass
def run_Update_hesabro_customers_from_hamyar(driver, main_url, dfData):
    thisIndex = get_index_Update_hesabro_customers_from_hamyar_cols(dfData)
    thisCols = Update_hesabro_customers_from_hamyar_cols()
    _ls_deactive_users = []
    _ls_active_users = []
    thisTime = time.ctime()
    l = len(dfData)
    save_counter = 0
    while len(dfData):
        # prgsCounter = l- len(dfData)
        # prgs.printProgressBar(prgsCounter, l, prefix = 'Progress:', suffix = 'Complete', length = 25)    
        customer = dfData.iat[0, thisIndex.customer]
        charge = dfData.iat[0, thisIndex.charge]
        coin = dfData.iat[0, thisIndex.coin]
        birthday = dfData.iat[0, thisIndex.birthday]
        address = dfData.iat[0, thisIndex.address]
        postalCode = dfData.iat[0, thisIndex.postalCode]
        work = dfData.iat[0, thisIndex.work]
        phone = dfData.iat[0, thisIndex.phone]
        codeMelli = dfData.iat[0, thisIndex.codeMelli]
        gender = dfData.iat[0, thisIndex.gender]
        education = dfData.iat[0, thisIndex.education]
        mobile = dfData.iat[0, thisIndex.mobile]
        
        # dic_customer = {thisCols.mobile:mobile,}
        dfData = dfData.loc[dfData[thisCols.mobile] != mobile]
        
        # print(f'numer of mobiles is {l}')

        
        # while len(dfData):
        save_counter += 1
        # driver.get(main_url)
        time.sleep(2.5)
        # mobile = dfData.iat[0,0]
        # user = dfData.iat[0,1]
        # this_mobile = f"0{int(mobile)}"
        # coin = str(dfData.iat[0,2])
        
        # print(f"charge {mobile} is doing! please wait...")
        hamyar_condition = True
        # if prgsCounter > 10:
        #     hamyar_condition =False
        
        action_True = coin_setter(mobile, driver, main_url, coin, hamyar_condition)
        
        # dfData = dfData.loc[dfData["mobile"]!=mobile]
        if action_True == False:
            # file.writelines(this_mobile)
            _ls_deactive_users.append({thisCols.mobile:mobile,thisCols.customer:customer,thisCols.charge:charge,
                                   thisCols.coin: coin, thisCols.birthday:birthday, thisCols.address:address,
                                   thisCols.postalCode:postalCode, thisCols.work:work, thisCols.phone:phone,
                                   thisCols.codeMelli: codeMelli, thisCols.gender: gender, thisCols.education : education,
                                   })
            df = pd.DataFrame(_ls_deactive_users)
            thisPath = os.getcwd()
            
            df.to_excel(f"{thisPath}/media/deative_users {thisTime}.xlsx")
            # false_count += 1
        else:
            
            _ls_active_users.append({thisCols.mobile:mobile,thisCols.customer:customer,thisCols.charge:charge,
                                   thisCols.coin: coin, thisCols.birthday:birthday, thisCols.address:address,
                                   thisCols.postalCode:postalCode, thisCols.work:work, thisCols.phone:phone,
                                   thisCols.codeMelli: codeMelli, thisCols.gender: gender, thisCols.education : education,
                                   })
            df = pd.DataFrame(_ls_active_users)
            thisPath = os.getcwd()
            
            df.to_excel(f"{thisPath}/media/Active_users {thisTime}.xlsx")

        # item = random.randint(1,len(urls['random']))
        # rnd_page = get_rnd_page(item)
        # driver.get(rnd_page)
        time.sleep(1)
        # while driver.current_url != rnd_page:
        #     driver.get(rnd_page)
        #     time.sleep(3)
        if save_counter>10:
            save_counter = 0
            dfData.to_excel(f"{thisPath}/media/newCharge.xlsx",index=False)
        # time.sleep(random.randint(3,6))
        
        # thisPath = os.getcwd()
        # acdcu = "active and deactive users"
        # try:
        #     os.mkdir(acdcu)
        # except:
        #     pass
        # os.chdir(acdcu)
        # if len(_ls_active_users):
        #     df_active_users = pd.DataFrame(_ls_active_users)
        #     # try:
        #     #     df_active_users.to_excel(f"active users{thisTime}.xlsx",index=False)
        #     # except:
        #     #     pass
        # if len(_ls_deactive_users):
        #     df_deactive_users = pd.DataFrame(_ls_deactive_users)
        #     # try:
            #     df_deactive_users.to_excel(f'deactive users{thisTime}.xlsx',index=False)
            # except:
            #     pass
        # os.chdir(thisPath)
        # if len(_ls_active_users):
        #     df_active_users = pd.DataFrame(_ls_active_users)
        #     try:
        #         df_active_users.to_excel(f"active users.xlsx",index=False)
        #     except:
        #         pass
        # if len(_ls_deactive_users):
        #     df_deactive_users = pd.DataFrame(_ls_deactive_users)
        #     try:
        #         df_deactive_users.to_excel('deactive users.xlsx',index=False)
        #     except:
    #         pass