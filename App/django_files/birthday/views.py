from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
# from selenium import webdriver
# some_file.py
# import sys
# # caution: path[0] is reserved for script path (or '' in REPL)
# sys.path.insert(1, r'C:/honeymoon_project/selenium/hesabro/settings')
import os,sys, time, pandas as pd
from .forms import ExcelUploadForm
sys.path.append("..")
from selenium_files.settings_selenium.run_app import task_selector as tsksl_s
from selenium_files.settings_selenium import app_tasks as atk_s
from python_files.settings_python import app_structures as asts_p
# from selenium_files.settings_selenium.run_app import run_hesabro
# from selenium_files.settings_selenium.run_app import task_selector
# from selenium_files.settings_selenium import app_tasks as atk
# from python_files.settings_python import app_structures as asts
def timeCheck()->bool:
    import time
    thisTime = time.ctime()
    # print (thisTime)
    firstColon = thisTime.find(":")
    # print(firstColon)
    thisTime = thisTime[firstColon-2:firstColon+6]
    # print(thisTime)
    if thisTime>"10:00:00" and thisTime< "11:00:00":
        
        return True
    else:
        return False
# from selenim_files.hesabro.datpaa.user_
# from selenium.
# os.path.abspath(os.path.join(os.getcwd(), '...'))
# from .honeymoon_project.sel
# import 
# from ...selenium_files.hesabro.settings.run_app import run_hesabro
def update_birthday_call_brs(request):
    form = ExcelUploadForm()
    result = "stoped"
    brs = {
        "شعبه بم": "https://docs.google.com/spreadsheets/d/14d3k5-tZBmvQXzz9NshGGkR46qjh3FfcpFlFvTQOgI4/edit#gid=228242866",
        "شعبه رفسنجان":"https://docs.google.com/spreadsheets/d/1wIvLkPjrfgaEfA0diYIQT84D4oG3UT7CwoRp2U0nG2I/edit#gid=206132103",
        
        
    }
    if request.method == 'POST':
        data = request.POST
        action = data.get("act")
        
        if action == "run":
            # for w in range(10):
            #         print(result)
            form = ExcelUploadForm(request.POST, request.FILES)
            if form.is_valid():
            # if True:
                result = "running"
                # for w in range(10):
                #     print(result)
                invoices_file = request.FILES['invoices_merged']
                # for w in range(10):
                #     print(invoices_file)
                try:
                    df_invoices = pd.read_excel(invoices_file)
                except:
                    df_invoices = pd.read_csv(invoices_file,sep=",")
                # driver = webdriver.Firefox()
                # if timeCheck():
                # df = tsksl_s(atk_s.task_name.update_birthday_call_brs, brs)
                df_invoices = df_invoices.sort_values(by=asts_p.tjCol.history)
                df_invoices.drop_duplicates(subset=asts_p.tjCol.mobile, inplace=True)
                args_ = {asts_p.send_birthday_toSheets_require.invoices:df_invoices, 
                        asts_p.send_birthday_toSheets_require.branchs: brs}#type: ignore
                final_result = tsksl_s(atk_s.task_name.send_birthday_data_to_sheets,args_)
                # df = pd.read_excel("")
            # driver.get('http://aradpayamak.net')
                # driver.get("https://honeymoonatr.com")
                    # for t in driver.title:
                # result = {"result":(f"عنوان سایت بارگزاری شده: {driver.title}") }
        else:
            result = "stoped"
            print("stop")
            # driver.close()
        
        # return redirect(("arad/"))
    # message ={"messages":"test"}
    
    return render(request, 'birthday/update_birthday_call_brs.html',{'form': form, "result":"stoped"})
def update_db_to_sendSms(request):
    # print("this is test")
    result = {"result":"stoped"}
    if request.method == 'POST':
        data = request.POST
        action = data.get("act")
        sms_text = data.get("sms_text")
        if action == "run":
            # driver = webdriver.Firefox()
            # if timeCheck():
            if True:
                tsksl_s(atk_s.task_name.update_birthday,sms_text)
        # driver.get('http://aradpayamak.net')
            # driver.get("https://honeymoonatr.com")
                # for t in driver.title:
            # result = {"result":(f"عنوان سایت بارگزاری شده: {driver.title}") }
        else:
            print("stop")
            # driver.close()
        
        # return redirect(("arad/"))
    # message ={"messages":"test"}
    
    return render(request,'birthday/update_birthday_db_to_sendSms.html',result)
def birthday_page(request):
    # 
    return render(request,'birthday/birthday_page.html')
def arad_detail(request):
    pass
    # for i in range(20):
    #     print(i)
    # driver = webdriver.Firefox()
    # # driver.get('http://aradpayamak.net')
    # driver.get("https://honeymoonatr.com")
    #     # for t in driver.title:
    # result = (f"عنوان سایت بارگزاری شده: {driver.title}")  
    
    # return render(request,"birthday/arad/arad_detail.html")