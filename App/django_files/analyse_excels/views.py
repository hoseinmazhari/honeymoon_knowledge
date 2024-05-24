import time
from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
# from selenium import webdriver
from django.http import FileResponse
# from A.celery import app
# import os,sys
# sys.path.append("..")
# from python_files.codes.a00001_invoices import a0_1_invoices_Count
# from python_files.file_types.excel_files import tjCol
# from python_files.file_types.excel_files import getIndexTj
from selenium_files.settings_selenium.run_app import task_selector
from selenium_files.settings_selenium import app_tasks as atk
from python_files.settings_python import app_structures as asts
# from .forms import UploadFileForm
# from somewhere import handle_uploaded_file
import pandas as pd
# from selenim_files.hesabro.datpaa.user_
# from selenium.
# os.path.abspath(os.path.join(os.getcwd(), '...'))
# from .honeymoon_project.sel
# import 
# from ...selenium_files.hesabro.settings.run_app import run_hesabro
from .forms import ExcelUploadForm
def factors_count(request):
    # print("this is test")
    result = {"result":"stoped"}
    if request.method == 'POST':
        data = request.POST
        action = data.get("act")
        sms_text = data.get("sms_text")
        if action == "run":
            # driver = webdriver.Firefox()
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
    
    return render(request,'birthday/update_birthday_db.html',result)
def analyse_list(request):
    # 
    return render(request,'analyse_excels/analyse_list.html')
def merge_base_factors(request):
    result = {"result":"stoped_baseMerge"}
    print(result,1)
    if request.method == 'POST':
        print(result,"post")
        data = request.POST
        action = data.get("act")
        # sms_text = data.get("sms_text")
        if action == "run":
            result = {"result":"running"}
            print(result)
            # driver = webdriver.Firefox()
            # task_selector(atk.task_name.update_birthday,sms_text)
            print("run")
        # driver.get('http://aradpayamak.net')
            # driver.get("https://honeymoonatr.com")
                # for t in driver.title:
            # result = {"result":(f"عنوان سایت بارگزاری شده: {driver.title}") }
        else:
            print("stop")
            # driver.close()
        
        # return redirect(("arad/"))
    # message ={"messages":"test"}
    
    return render(request,"analyse_excels/merge_factors_hamyar_hesabro.html",result)
# def rsp(response):
#     return response
def download_file(request):
    # if request.method == 'POST':
    try:
        # print(answer)
        # staticIndex = answer.find('media')
        
        # answer = answer[staticIndex:]
        # print(answer)
        file = open("temp.txt","r+", encoding="utf-8") 
        #change from here
        
        answer= (file.read())
        # answer = answer.replace("?????", "/")
        # answer = answer.replace("%%%%%%", ":")
        for x in range(100):
            print(answer)
        with open(answer, 'rb') as f:
            response = HttpResponse(f.read(), content_type="application/ms-excel")
            response['Content-Disposition'] = 'attachment; filename={}_Report{}'.format("exported", ".xlsx")
            # file_path = "example.xlsx"
            return response
    except Exception as e:
        print(e)
    # return render(request, 'analyse_excels/result.html', {'answer': answer})
    # return render(request,'/@analyse_excels/result.html') 
    return render(request,'result.html')
# @app.task
# def salary_task(invoices_file,targets_file,data):
    
def salary_hesabro(request):
    form = ExcelUploadForm()
    result = {"result":"stoped"}
    # print(result,1)
    if request.method == 'POST':
        print(result,"post")
        
        data = request.POST
        # action = data.get("act")
        action = "run"
        if action == "run":
           
            result = {"result":"running"}
            print(result,"post")
            form = ExcelUploadForm(request.POST, request.FILES)
            if form.is_valid():
                print("is valid")
                invoices_file = request.FILES['invoices_file']
                targets_file = request.FILES['targets_file']
                # print(invoices_file)
                # excel_file = request.FILES.get('csv_file')
                # try:
                try:
                    df_invoices = pd.read_excel(invoices_file)
                except:
                    df_invoices = pd.read_csv(invoices_file,sep=",")
                df_targets = pd.read_excel(targets_file)
                # print(result)
                # file_invoices = data.get("file_invoices")
                # print(file_invoices)
                # form = UploadFileForm(request.POST, request.FILES)
                # if form.is_valid():
                #     handle_uploaded_file(request.FILES["file"])
                
                # df_invoices = pd.read_csv(f"{file_invoices}")
                # print(df_invoices)
                # print(df_invoices)
                # file_targets = data.get("file_targets")
                startDate = data.get("startDate")
                endDate = data.get("endDate")
                # driver = webdriver.Firefox()
                args_ = {asts.salary_requires.invoices:df_invoices, 
                        asts.salary_requires.targets: df_targets,
                        asts.salary_requires.startDate: startDate,
                        asts.salary_requires.endDate: endDate}
                answer = task_selector(atk.task_name.salary,args_)
                import shutil
                archived = shutil.make_archive("zipped file", 'zip', answer)
                # answer= (archived.read())
                # print("run")
                # file = open("temp.txt","w", encoding="utf-8")
                # file.write(answer)
                # file.close()
                # # answer = answer.replace("\\", "?????")
                # # answer = answer.replace(":", "%%%%%%")
                # return redirect('download_file/')
                    # return redirect('/@analyse_excels/salary/result/')
                    # return redirect('/@analyse_excels/result.html/?answer={}'.format(answer))
                    # return redirect('/@analyse_excels/result/{}/'.format(answer))
                    # answer = "factor.xlsx
                    # try:
                    #     print(answer)
                    #     # staticIndex = answer.find('media')
                        
                    #     # answer = answer[staticIndex:]
                    #     # print(answer)
                    #     # answer = answer.replace("\\", "/")
                    #     with open(answer, 'rb') as f:
                    #         response = HttpResponse(f.read(), content_type="application/ms-excel")
                    #         response['Content-Disposition'] = 'attachment; filename={}_Report{}'.format("exported", ".xlsx")
                    #         # file_path = "example.xlsx"
                    #         return response
                    # except Exception as e:
                    #     print(e)
                    # return render(request, 'analyse_excels/result.html', {'answer': answer})
                # driver.get('http://aradpayamak.net')
                    # driver.get("https://honeymoonatr.com")
                        # for t in driver.title:
                    # result = {"result":(f"عنوان سایت بارگزاری شده: {driver.title}") }
                # except Exception as e:
                # # در صورت وقوع خطا، آن را نمایش می‌دهیم
                #     return render(request, 'analyse_excels/error.html', {'error': str(e)})
        else:
            print("stop")
            # driver.close()
            form = ExcelUploadForm()
        # return redirect(("arad/"))
    # message ={"messages":"test"}
    
    return render(request,"analyse_excels/salary_hesabro.html", {'form': form, "result":"stoped"})
    
def merge_factors_customers(request):
    return HttpResponse("merge_factors_customers")