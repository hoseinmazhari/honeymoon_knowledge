# import requests
from ...settings import xpath_hesabro as xph
from ...settings import DateJuToJa as djtj
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from .xpath import get_xpath
from ...settings.xpath import get_xpath
import time
import pandas as pd
import os

from selenium.webdriver.common.keys import Keys
# from .merchandise import search_fieldProduct
from ...settings.browser import write_in_element
from ...settings import app_address
from .fetch_birthday import set_title
from .fetch_report_data import download_data
# from tqdm import tqdm
# from .test import dwn

def get_birthdays_data(driver,title): 
    #  1- تغییر آدرس مرورگر به صفححه ایجاد گزاشات
    # this_address = app_address.urls["birthday"]["create_rpt"]
    this_address = app_address.url_address.create_report.birthday
    driver.get(this_address)
    while driver.current_url != this_address: # جهت اطمینان از باز شدن صفحه ی درخواست شده در گزینه 1 از حلقه استفاده شده است
        driver.get(this_address)
        time.sleep(3)
    
    # 2- جهت استخراج تاریخ جاری و استفاده از آن در برنامه از این قسمت استفاده شده است
    this_date = str(djtj.todaydate()).replace("/","-")

    # 5- جهت تعیین عنوان گزارش از این قسمت استفاده شده است
    title = f"{title} {this_date}"

    this_delay = 6
    # 6-  جهت کلیک روی گزینه ایجاد گزارش از این گزینه استفاده شده است
    # نکته: از شمارنده برای اطمینان از عدم پگینیشن بودن وضعیت سایت استفاده شده است
    is_true = False
    counter = 0
    while is_true==False:
        
        try:
            element =driver.find_elements(By.XPATH,xph.create_reportcustomer.btn_createRpt)
            element[1].click()
            is_true = True
        except:
            counter += 1
            if counter>20:
                driver.get(this_address)
                counter = 0
            is_true = False
            time.sleep(this_delay)

    # 7- از این قسمت برای ذخیره آدرس مربوط به ایجاد گزارش استفاده شده است تا در صورت نیاز مجدد بارگزاری شود
    current_url = driver.current_url
    
    # 8- از این قسمت برای درج عنوان استفاده شده است
    set_title(driver, current_url, title, this_delay)
    # is_true = False
    # while is_true == False:

    is_true = False
    while is_true==False:
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xph.create_reportcustomer.save)))
            element.click()
            # write_in_element(birthdaytoday, element)
            is_true = True
        except:
            is_true = False
    time.sleep(3)
    dfData = download_data(driver, title, this_delay)
    return dfData




    # is_true = False
    # while is_true==False:
    #     try:
    #         element = WebDriverWait(driver, 10).until(
    #             EC.presence_of_element_located((By.XPATH, xph.create_reportcustomer.download)))
    #         this_file_path=element.get_attribute("href")
    #         # print(this_file_path)
    #         url = this_file_path
    #         this_file = requests.get(url, allow_redirects=True)
    #         # print(this_file)
    #         # this_file = requests.get(this_file_path)
    #         this_path = os.getcwd()
    #         # print(this_path)
    #         open(f"{this_path}/{title}.xls", "wb").write(this_file.content)
    #         #     f.write(this_file.content)
    #         #     f.close()
    #         # # write_in_element(birthdaytoday, element)
    #         is_true = True
    #     except:
    #         is_true = False
