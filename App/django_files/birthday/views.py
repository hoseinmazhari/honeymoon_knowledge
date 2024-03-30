from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from selenium import webdriver
# some_file.py
# import sys
# # caution: path[0] is reserved for script path (or '' in REPL)
# sys.path.insert(1, r'C:/honeymoon_project/selenium/hesabro/settings')
import os,sys, time, pandas as pd
from .forms import ExcelUploadForm
sys.path.append("..")
from selenium_files.settings.run_app import run_hesabro
from selenium_files.settings.run_app import task_selector
from selenium_files.settings import app_tasks as atk

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
                df = task_selector(atk.task_name.update_birthday_call_brs, brs)
                
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
            if timeCheck():
                task_selector(atk.task_name.update_birthday,sms_text)
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
    
    for i in range(20):
        print(i)
    driver = webdriver.Firefox()
    # driver.get('http://aradpayamak.net')
    driver.get("https://honeymoonatr.com")
        # for t in driver.title:
    result = (f"عنوان سایت بارگزاری شده: {driver.title}")  
    
    return render(request,"birthday/arad/arad_detail.html")