import time, pandas as pd
from django.conf import settings
from selenium_files.settings_selenium.app_address import File_locations
from selenium_files.settings_selenium import app_tasks as atsk
from python_files.settings_python.app_structures import report_output_cols,\
    get_index_report_output_cols
from python_files.settings_python import DateJuToJa as djtj
from .sms_sender import send_sms_from_df
def run_send_daily_birthday_message():
    print("send birthday daily started...")
    birthday_location = File_locations.Data_base.Club.Customers.Birthdays.file_address
    sms_text = """
@نام_و_نام_خانوادگی عزیز
💗تولدت مبارک💗
20% تخفیف خرید، فقط برای شما، در تمامی شعب هانی مون
مهلت: 10 روز
09910359002
"""
    title = atsk.task_name.send_daily_birthday_message
    thisCols = report_output_cols()
    today = djtj.todaydate()
    print("today is: ",today)
    today = str(today[-6:])
    print("today birthday filter is: ",today)
    # time.sleep(5)   
    # now = datetime.now() 
    # current_time = now.strftime("%H:%M:%S")
    # print(current_time)
    db_address = File_locations.Data_base.Club.Customers.Specifications.db_address
    this_file = f"{settings.BASE_DIR}/{db_address}"
    print("this_file is loading please wait...", this_file)
    while True:
        try:
            df_customers_specifications = pd.read_excel(this_file)
            break
        except:
            time.sleep(20)
    print("file is load complete please wait until done")
    

    # new_file = f"{settings.BASE_DIR}/{hesabro_db_address}/new_customers_list.xlsx"
    # df_customers_specifications.to_excel(new_file,index=False)
    # print(new_file)
    print("create copy from df")
    dfData = df_customers_specifications.copy()
    print("fillna with 0 ")
    dfData.fillna(0, inplace = True)
    print("remove null birthday from df")
    dfData =dfData.loc[dfData[thisCols.birthday]!=0]
    print("filter birthday from df")
    dfData = dfData[dfData[thisCols.birthday].str.contains(str(today))]
    print("create birthday file name please wait...")
    today = today.replace("/","-")[1:]
    new_file = f"{settings.BASE_DIR}/{birthday_location}/{today}.xlsx"
    # dfData.fillna({thisCols.birthday:"0000"}, inplace = True)
    # dfData = dfData.loc[dfData[thisCols.birthday]!=""]
    # dfData = dfData[dfData[thisCols.birthday].str.contains(str(today))]
    # new_file = f"{settings.BASE_DIR}/{hesabro_db_address}/new_current_birth.xlsx"
    dfData.to_excel(new_file,index=False)
    send_sms_from_df(dfData,title,sms_text)
    print("test sms to 09162078094 is started")
    ls_mobiles = [9162078094, 9132995389]
    # ls_mobiles = [9162078094]
    birthday_count = len(dfData)
    sms_text = f"تعداد {birthday_count} تولدی ارسال شد"
    for mobile in ls_mobiles:
        dfData = df_customers_specifications.loc[df_customers_specifications[thisCols.mobile]==mobile]
        new_file = f"{settings.BASE_DIR}/{birthday_location}/{mobile}.xlsx"
        dfData.to_excel(new_file, index=False)
        send_sms_from_df(dfData,title,sms_text)
    
    # dfData.to_excel("data.xlsx",index=False)
    
    print("send  birthday daily now is complete.")