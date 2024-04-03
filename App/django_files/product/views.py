from django.shortcuts import render,HttpResponse
import os,sys, pandas as pd
sys.path.append("..")
from selenium_files.settings.run_app import task_selector
from selenium_files.settings import app_tasks as atk
from .forms import ExcelUploadForm
# Create your views here.
from selenium_files.settings.run_app import task_selector
from selenium_files.settings import app_tasks as atk
from python_files.settings import app_structures as asts
def active_in_site(request):
    form = ExcelUploadForm()
    result = "stoped"
    scales = [10, 15, 20, 30, 50]
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
                    df_invoices = pd.read_csv(product_list,sep=",")
                # driver = webdriver.Firefox()
                # if timeCheck():
                # df = task_selector(atk.task_name.update_birthday_call_brs, brs)
                # df_invoices = df_invoices.sort_values(by=asts.tjCol.history)
                # df_invoices.drop_duplicates(subset=asts.tjCol.mobile, inplace=True)
                args_ = scales#type: ignore
                final_result = task_selector(atk.task_name.active_in_site,args_)
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
            task_selector(atk.task_name.set_order_point)
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