import time
from datetime import datetime
import pandas as pd
from celery import shared_task
from selenium_files.hesabro.club.update_customers_specifications import update_customers_specifications
from selenium_files.hesabro.club.send_daily_birthday_message import run_send_daily_birthday_message
from selenium_files.settings_selenium.run_app import run_hesabro
from selenium_files.hesabro.club.sms_sender import  send_sms_from_df
from selenium_files.settings_selenium import app_tasks as tsk
@shared_task
def run_update_customers_specifications():
    print("process 'update_customers_specifications' is running")
    driver, is_logged_in = run_hesabro()
    # print("this select")
    if is_logged_in:
        update_customers_specifications(driver)
    # driver.save_cookies()
    driver.close()
    # driver.quite()
    print("process 'update_customers_specifications' is complete")
# @shared_task
# def run_send_daily_birthday_message():
#     print("send birthday daily started...")
#     time.sleep(5)   
#     now = datetime.now() 
#     current_time = now.strftime("%H:%M:%S")
#     print(current_time)
#     print("send  birthday daily now is complete.")

@shared_task
def send_daily_sms_birthday_customers():
    print("check time to birthday")
    mobile = "موبایل"
    name = "نام و نام خانوادگی"
    birthday = "تاریخ تولد"
    ls = []
    # this_dict = {
    #     mobile:"09136199868",
    #     name: "علی خراسانی",
    #     birthday:"1380/01/01"}
    # ls.append(this_dict)
    # this_dict = 
    ls.append({mobile:"09139960164", name: "حسین مظهری", birthday:"1365/06/29"})
    ls.append({mobile:"09162078094", name: "حسین", birthday:"1365/06/29"})
    dfData = pd.DataFrame(ls)
    # sms_text = "حسین مظهری عزیز تولدت مبارک"
    sms_text = """
@نام_و_نام_خانوادگی عزیز
💗تولدت مبارک💗
20% تخفیف خرید، فقط برای شما، در تمامی شعب هانی مون
مهلت: 10 روز
09910359002
"""
    title = tsk.task_name.update_birthday
    # dfData.to_excel("data.xlsx",index=False)
    # send_sms_from_df(dfData,title,sms_text)
    run_send_daily_birthday_message()
            