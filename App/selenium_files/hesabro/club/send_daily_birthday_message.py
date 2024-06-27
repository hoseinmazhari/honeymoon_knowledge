import pandas as pd
from django.conf import settings
from selenium_files.settings_selenium.app_address import File_locations,hesabro_db_address
from python_files.settings_python.app_structures import report_output_cols,get_index_report_output_cols
from python_files.settings_python import DateJuToJa as djtj

def run_send_daily_birthday_message():
    print("send birthday daily started...")
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
    new_file = f"{settings.BASE_DIR}/{hesabro_db_address}/new_customers_list.xlsx"
    df_customers_specifications.to_excel(new_file,index=False)
    print(new_file)
    dfData = df_customers_specifications.copy()
    dfData.fillna({thisCols.birthday:"0000"}, inplace = True)
    dfData = dfData.loc[dfData[thisCols.birthday]!=""]
    dfData = dfData[dfData[thisCols.birthday].str.contains(str(today))]
    new_file = f"{settings.BASE_DIR}/{hesabro_db_address}/new_current_birth.xlsx"
    dfData.to_excel(new_file,index=False)

    print("send  birthday daily now is complete.")