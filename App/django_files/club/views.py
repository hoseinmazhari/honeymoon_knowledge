from django.shortcuts import render
from .forms import ExcelUploadForm
from selenium_files.settings_selenium.run_app import task_selector as tsksl_s
from selenium_files.settings_selenium import app_tasks as atk_s
import pandas as pd
# Create your views here.
def club_page(request):
    return render(request,'club/club_page.html')

def Update_hesabro_customers_from_hamyar(request):
    form = ExcelUploadForm()
    result = "stoped"
    # for i in range(10):
    #     print("start")
    # scales = [10, 15, 20, 30, 50]
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
                Data = request.FILES['Data']
                # for w in range(10):
                #     print(invoices_file)
                try:
                    df_Data = pd.read_excel(Data)
                except:
                    df_Data = pd.read_csv(Data,sep=",")
                # driver = webdriver.Firefox()
                # if timeCheck():
                # df = tsksl_s(atk_s.task_name.update_birthday_call_brs, brs)
                # df_invoices = df_invoices.sort_values(by=asts.tjCol.history)
                # df_invoices.drop_duplicates(subset=asts.tjCol.mobile, inplace=True)
                # args_ = scales#type: ignore
                final_result = tsksl_s(atk_s.task_name.Update_hesabro_customers_from_hamyar,df_Data)
                # for i in range(10):
                #     print("run", final_result)
                # df = pd.read_excel("")
            # driver.get('http://aradpayamak.net')
                # driver.get("https://honeymoonatr.com")
                    # for t in driver.title:
                # result = {"result":(f"عنوان سایت بارگزاری شده: {driver.title}") }
        else:
            result = "stoped"
            print("stop")
            for i in range(10):
                print("stped")
            # driver.close()
        
        # return redirect(("arad/"))
    # message ={"messages":"test"}
    
    return render(request, 'club/Update_hesabro_customers_from_hamyar.html',{'form': form, "result":"stoped"})

def Create_hesabro_customers_from_hamyar(request):
    form = ExcelUploadForm()
    result = "stoped"
    # for i in range(10):
    #     print("start")
    # scales = [10, 15, 20, 30, 50]
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
                Data = request.FILES['Data']
                # for w in range(10):
                #     print(invoices_file)
                try:
                    df_Data = pd.read_excel(Data)
                except:
                    df_Data = pd.read_csv(Data,sep=",")
                # driver = webdriver.Firefox()
                # if timeCheck():
                # df = tsksl_s(atk_s.task_name.update_birthday_call_brs, brs)
                # df_invoices = df_invoices.sort_values(by=asts.tjCol.history)
                # df_invoices.drop_duplicates(subset=asts.tjCol.mobile, inplace=True)
                # args_ = scales#type: ignore
                final_result = tsksl_s(atk_s.task_name.Create_hesabro_customers_from_hamyar,df_Data)
                # for i in range(10):
                #     print("run", final_result)
                # df = pd.read_excel("")
            # driver.get('http://aradpayamak.net')
                # driver.get("https://honeymoonatr.com")
                    # for t in driver.title:
                # result = {"result":(f"عنوان سایت بارگزاری شده: {driver.title}") }
        else:
            result = "stoped"
            print("stop")
            for i in range(10):
                print("stped")
            # driver.close()
        
        # return redirect(("arad/"))
    # message ={"messages":"test"}
    
    return render(request, 'club/Create_hesabro_customers_from_hamyar.html',{'form': form, "result":"stoped"})