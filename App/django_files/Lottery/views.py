import pandas as pd
from django.shortcuts import render
from selenium_files.settings_selenium import app_tasks as atk
from selenium_files.settings_selenium.run_app import task_selector
from python_files.settings_python.app_structures import lottery_requires
from .forms import ExcelUploadForm

# Create your views here.
def send_sms_to_invalid_response(request):
    form = ExcelUploadForm()
    result = {"result":"stoped", "form": form}
    if request.method == 'POST':
        data = request.POST
        action = data.get("act")
        sms_text = data.get("sms_text")
        if action == "run":
            form = ExcelUploadForm(request.POST, request.FILES)
            # driver = webdriver.Firefox()
            # if timeCheck():
            if form.is_valid():
            # if True:
                result = {"result":"running"}
                correct_barcodes = request.FILES['correct_barcodes']
                incorrect_barcodes = request.FILES['incorrect_barcodes']
                # for w in range(10):
                #     print(invoices_file)
                # try:
                dfCorrect_barcodes = pd.read_excel(correct_barcodes)
                dfIncorrect_barcodes = pd.read_excel(incorrect_barcodes)
                # except:
                #     df_invoices = pd.read_csv(correct_barcodes,sep=",")
                # driver = webdriver.Firefox()
                # if timeCheck():
                # df = tsksl_s(atk_s.task_name.update_birthday_call_brs, brs)
                # df_invoices = df_invoices.sort_values(by=asts_p.tjCol.history)
                # df_invoices.drop_duplicates(subset=asts_p.tjCol.mobile, inplace=True)
                args_ = {lottery_requires.correct_barcodes:dfCorrect_barcodes,
                         lottery_requires.incorrect_barcodes:dfIncorrect_barcodes,
                         lottery_requires.sms_text : sms_text
                         }#type: ignore
                # final_result = tsksl_s(atk_s.task_name.send_birthday_data_to_sheets,args_)
                



                task_selector(atk.task_name.lottery_barcodes,args_)
        # driver.get('http://aradpayamak.net')
            # driver.get("https://honeymoonatr.com")
                # for t in driver.title:
            # result = {"result":(f"عنوان سایت بارگزاری شده: {driver.title}") }
        else:
            print("stop")
            # driver.close()
        
        # return redirect(("arad/"))
    # message ={"messages":"test"}
    
    return render(request,'lottery/lottery_for_sendSms.html',result)
def lottery_page(request):
    # 
    return render(request,'lottery/lottery_page.html')