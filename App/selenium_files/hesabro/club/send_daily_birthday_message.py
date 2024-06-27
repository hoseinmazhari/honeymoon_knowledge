import pandas as pd
from django.conf import settings
from selenium_files.settings_selenium.app_address import File_locations,hesabro_db_address
from selenium_files.settings_selenium import app_tasks as atsk
from python_files.settings_python.app_structures import report_output_cols,get_index_report_output_cols
from python_files.settings_python import DateJuToJa as djtj
from .sms_sender import send_sms_from_df
def run_send_daily_birthday_message():
    print("send birthday daily started...")
    sms_text = """
@نام_و_نام_خانوادگی عزیز
💗تولدت مبارک💗
20% تخفیف خرید، فقط برای شما، در تمامی شعب هانی مون
مهلت: 10 روز
09910359002
"""
    title = atsk.task_name.update_birthday
    thisCols = report_output_cols()
    today = djtj.todaydate()
    today = str(today[-6:])
    print(today)
    # time.sleep(5)   
    # now = datetime.now() 
    # current_time = now.strftime("%H:%M:%S")
    # print(current_time)
    db_address = File_locations.Data_base.Club.Customers.Specifications.db_address
    this_file = f"{settings.BASE_DIR}/{db_address}"
    print(this_file)
    df_customers_specifications = pd.read_excel(this_file)
    # new_file = f"{settings.BASE_DIR}/{hesabro_db_address}/new_customers_list.xlsx"
    # df_customers_specifications.to_excel(new_file,index=False)
    # print(new_file)
    dfData = df_customers_specifications.copy()
    dfData.fillna(0, inplace = True)
    dfData =dfData.loc[dfData[thisCols.birthday]!=0]
    dfData = dfData[dfData[thisCols.birthday].str.contains(str(today))]
    today = today.replace("/","-")[1:]
    # today = today
    new_file = f"{settings.BASE_DIR}/{hesabro_db_address}/{today}.xlsx"
    dfData.fillna({thisCols.birthday:"0000"}, inplace = True)
    dfData = dfData.loc[dfData[thisCols.birthday]!=""]
    dfData = dfData[dfData[thisCols.birthday].str.contains(str(today))]
    new_file = f"{settings.BASE_DIR}/{hesabro_db_address}/new_current_birth.xlsx"
    dfData.to_excel(new_file,index=False)
    send_sms_from_df(dfData,title,sms_text)
    dfData = df_customers_specifications.loc[df_customers_specifications[thisCols.mobile]==9162078094]
    new_file = f"{settings.BASE_DIR}/{hesabro_db_address}/09162078094.xlsx"
    dfData.to_excel(new_file, index=False)
    
    
    # dfData.to_excel("data.xlsx",index=False)
    send_sms_from_df(dfData,title,sms_text)
    print("send  birthday daily now is complete.")