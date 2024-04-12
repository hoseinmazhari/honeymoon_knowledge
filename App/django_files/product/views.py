from django.shortcuts import render,HttpResponse
import os,sys, pandas as pd
from .forms import ExcelUploadForm,ExcelProduct_list
sys.path.append("..")
from selenium_files.settings_selenium.run_app import task_selector as tsksl_s
from selenium_files.settings_selenium import app_tasks as atk_s
# from python_files.settings_python import app_structures as asts_p
def modification_barcodes(request):
    form = ExcelProduct_list()
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
            form = ExcelProduct_list(request.POST, request.FILES)
            if form.is_valid():
            # if True:
                result = "running"
                # for w in range(10):
                #     print(result)
                product_list = request.FILES['product_list']
                # for w in range(10):
                #     print(invoices_file)
                try:
                    df_product_list = pd.read_excel(product_list)
                except:
                    df_product_list = pd.read_csv(product_list,sep=",")
                # driver = webdriver.Firefox()
                # if timeCheck():
                # df = tsksl_s(atk_s.task_name.update_birthday_call_brs, brs)
                # df_invoices = df_invoices.sort_values(by=asts.tjCol.history)
                # df_invoices.drop_duplicates(subset=asts.tjCol.mobile, inplace=True)
                # args_ = scales#type: ignore
                final_result = tsksl_s(atk_s.task_name.modification_barcodes,df_product_list)
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
    
    return render(request, 'product/modification_barcodes.html',{'form': form, "result":"stoped"})
    # ret
def active_in_site(request):
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
                product_list = request.FILES['product_list']
                # for w in range(10):
                #     print(invoices_file)
                try:
                    df_product_list = pd.read_excel(product_list)
                except:
                    df_product_list = pd.read_csv(product_list,sep=",")
                # driver = webdriver.Firefox()
                # if timeCheck():
                # df = tsksl_s(atk_s.task_name.update_birthday_call_brs, brs)
                # df_invoices = df_invoices.sort_values(by=asts.tjCol.history)
                # df_invoices.drop_duplicates(subset=asts.tjCol.mobile, inplace=True)
                # args_ = scales#type: ignore
                final_result = tsksl_s(atk_s.task_name.active_in_site,df_product_list)
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
    
    return render(request, 'product/active_in_site.html',{'form': form, "result":"stoped"})
    # return render(request,'product/active_in_site.html')
def price_with_t(request):
    pass
def order_point(request):
    result = {"result":"stoped"}
    if request.method == 'POST':
        data = request.POST
        action = data.get("act")
        if action == "run":
            # driver = webdriver.Firefox()
            tsksl_s(atk_s.task_name.set_order_point)
            
        # driver.get('http://aradpayamak.net')
            # driver.get("https://honeymoonatr.com")
                # for t in driver.title:
            # result = {"result":(f"عنوان سایت بارگزاری شده: {driver.title}") }
        else:
            print("stop")
           
            # driver.close()
        
        # return redirect(("arad/"))
    # message ={"messages":"test"}
    
    return render(request,'product/update_order_point.html',result)
def product_page(request):
    return render(request,'product/product_page.html')