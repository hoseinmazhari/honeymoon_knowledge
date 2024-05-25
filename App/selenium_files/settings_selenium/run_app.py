

import os, sys, time, random, pandas as pd
from .browser import Browser

from .main_defs import write_in_element
from selenium.webdriver.common.keys import Keys

# from .xpath import get_xpath
from . import xpath_hesabro
# import app_address
# from .app_address import hesabro_domain,get_rnd_page,urls,arad_payamek_domain,honeymoonatr_domain
from .app_address import hesabro_domain,honeymoonatr_domain

from selenium_files.hesabro.product import obsolete
from selenium_files.hesabro.club import update_hesabro_customers_from_hamyar as uhcfh
from .user_pass import get_index_user_pass
# from . import xpath
from . import app_address
from ..hesabro.product.order_points import set_order_point
# from ..hesabro.product.order_points_allBrs import set_order_point_allBrs
from . import app_tasks as tsk
from selenium_files.hesabro.product import active_in_site 
from selenium_files.hesabro.product import correct_zero_barcodes
from ..hesabro.club import fetch_birthdays_data as fbsd
from ..hesabro.club import fetch_birthday as upb
from ..hesabro.club import fetch_report_data as frd
from ..hesabro.club import fetch_coin_report_data as fcrd
from ..hesabro.club.sms_sender import send_group_sms
from ..honeymoonatr import update_products as upsh
# from ...python_files.codes.salary_hesabro import salary
from  python_files.codes.salary_hesabro.salary import salary
from python_files.settings_python import app_structures as asts
from python_files.settings_python.app_structures import _make_farsi_text
from python_files.settings_python import printProgress as prgs
from python_files.settings_python import DateJuToJa as djtj
def get_user_pass(this_domain):
    df_user_pass = pd.read_excel("..//selenium_files/data/user_pass/user_pass.xlsx")
    df_user_pass.to_excel("test.xlsx", index=False)
    df_data = df_user_pass.loc[df_user_pass['domain']==this_domain]
    # if len(df_hesabro)
    this_index = get_index_user_pass(df_data)
    # for i in range(1000):
    #     print(this_index.have_username)
    have_username = df_data.iat[0,this_index.have_username]
    if have_username == "True" or have_username == True:
        username = df_data.iat[0,this_index.username]
    else:
        username = ""
    have_password = df_data.iat[0, this_index.have_password]
    if have_password == "True" or have_password== True:
        password = df_data.iat[0,this_index.password]
    else:
        password = ""
    return username,password

# def run_arad_payamek(driver):
#     driver.get(arad_payamek_domain)
#     username,password = get_user_pass(arad_payamek_domain)
#     print(username)
#     time.sleep(5)
#     element = driver.find_element(by="xpath",value=xpath.aradpayamak.login_page.username)
#     element.click()
#     write_in_element(username,element)
#     element = driver.find_element(by="xpath",value=xpath.aradpayamak.login_page.password)
#     element.click()
#     write_in_element(password,element)
#     element = driver.find_element(by="xpath",value=xpath.aradpayamak.login_page.btn_login)
#     element.click()
#     # element.send_keys(Keys.ENTER)
#     driver.get(app_address.urls_arad.simple_send_sms.send_page)

#     time.sleep(5)
#     return driver
# def arad_send_simple_sms(driver,sms_text,number):
#     element = driver.find_element(by = "xpath", value=xpath.aradpayamak.simple_send_sms.input_sms )
#     element.click()
#     element.clear()
#     write_in_element(sms_text,element)
#     driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
#     element = driver.find_element(by = "xpath", value=xpath.aradpayamak.simple_send_sms.input_number)
#     element.click()
#     element.clear()
#     write_in_element(number,element)
#     driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
#     element = driver.find_element(by = "xpath", value=xpath.aradpayamak.simple_send_sms.btn_send )
#     element.click()
#     time.sleep(3)
#     return driver
def run_hesabro():
    # sys.path.append("..")
    # for i in range(1000):
        # print(os.getcwd())
        # print(app_tasks.tasks.update_birthday)
    
    main_url= f"{hesabro_domain}/site/index"
    username,password = get_user_pass(hesabro_domain)
    thisTime = djtj.getDateTimeForFileName()

    is_logged_in = False
    mybrowser = Browser()
    mybrowser.change_url(main_url)
    driver = mybrowser.driver
    # number = driver.find_element(by="id",value='loginform-number')
    files = os.listdir()
    file_exist = False
    cookies_file_name = f'cookies_hesabro_{username}'
    for f in files:
        # print(f)
        if f'{cookies_file_name}.pkl'== f:
            file_exist = True
            break
    # logged_in = True
    if file_exist:
        mybrowser.rem_cookies()
        mybrowser.load_cookies(f'{cookies_file_name}')
        time.sleep(4)
        if mybrowser.driver.current_url == main_url:
            is_logged_in = True
        else:
            driver.get(main_url)
            os.remove(f'{cookies_file_name}.pkl') 
            time.sleep(5)
                
    if is_logged_in == False:
        # login_hesabro(driver)
        driver.get(main_url)
        # _number = driver.find_element(by="xpath",value=f"{get_xpath('login','number')}")
        _number = driver.find_element(by="xpath",value=f"{xpath_hesabro.login_form.number}")
        
        write_in_element(username,_number)
        _number.send_keys(Keys.ENTER)

        _password = driver.find_element(by="xpath",value=f"{xpath_hesabro.login_form.password}")
        # _password = driver.find_element(by="xpath",value=f"{get_xpath('login','password')}")
        write_in_element(password,_password)
        
        # _authenticator = driver.find_element(by="xpath",value=get_xpath('login','authenticator'))
        _authenticator = driver.find_element(by="xpath",value=xpath_hesabro.login_form.authenticator)
        
        _authenticator.click()
        time.sleep(15)
        _authenticator.send_keys(Keys.ENTER)
        time.sleep(7)
        try:
            # _test = _coin = driver.find_element(by="xpath",value=get_xpath('user_detail','coin'))
            print('this message show for wait to logged in after login continue')
            waiter = input("press any key and enter: ")
            Browser.save_cookies(mybrowser,cookies_file_name)
            is_logged_in = True
        
        except:
            is_logged_in = False
    return driver , is_logged_in

def run_honeymoonatr():
    print("now set data to variables")
    print_delay = .4
    time.sleep(print_delay)
    main_url= f"{honeymoonatr_domain}" 
    cookie_fileName = "honeymoonatr_cookies"
    time.sleep(print_delay)
    cookies_path = app_address.file_locations.cookies
    print("set data to variables is complete!")
    time.sleep(print_delay)
    print("start run mozilla bot")
    time.sleep(print_delay)
    mybrowser = Browser()
    driver = mybrowser.driver
    print(f"start load site {honeymoonatr_domain}")
    time.sleep(print_delay)
    driver.get(main_url)
    print(f"site {honeymoonatr_domain} is now loaded!")
    time.sleep(print_delay)
    print(f"now we start check existing saved cookies")
    time.sleep(print_delay)
    thisPath = os.getcwd()
    os.chdir(f"{thisPath}/{cookies_path}")
    print("change url to cookies path")
    time.sleep(print_delay)
    ls_files = os.listdir()
    print("change app url is performed")
    time.sleep(print_delay)
    print(f"check cookie file for {honeymoonatr_domain} ")
    time.sleep(print_delay)
    print("file list is:")
    time.sleep(print_delay)
    is_logged_in = False
    for f in ls_files:
        # print(f)
        # time.sleep(print_delay)
        if f == f"{cookie_fileName}.pkl":
            print(f"cookie for {honeymoonatr_domain} is now avalible!")
            time.sleep(print_delay)
            
            print("first remove cookeis in browser")
            time.sleep(print_delay)
            mybrowser.rem_cookies()
            print("remove cookeis on browser is completed")
            time.sleep(print_delay)
            print("now start loading cookie to your browser")
            time.sleep(print_delay)
            for i in range(10, -1):
                print(i, end="\r")
                time.sleep(print_delay)
            
            mybrowser.load_cookies(f'{cookie_fileName}')
            
            print(f"cookie file for {honeymoonatr_domain} is successfully loaded!")
            time.sleep(print_delay)
            print("now exit check cookies files")
            time.sleep(print_delay)
            wp_admin = "https://honeymoonatr.com/wp-admin/"
            driver.get(wp_admin)
            time.sleep(4)
            is_logged_in = True
            if  driver.current_url != wp_admin:
                is_logged_in = False
                driver.get(main_url)
                os.remove(f'{cookie_fileName}.pkl') 
                time.sleep(5)
            
            break
    if is_logged_in == False:
        for i in range(30):
            print(i, end="\r")
            time.sleep(1)
    # print("load main_url is complete0")
        
        waiter = input("press any key and enter: ")
        is_true = False
        while is_true ==False:
            try:
                Browser.save_cookies(mybrowser,"honeymoonatr_cookies")
                time.sleep(3)
                is_true =True
            except:
                pass
        print("cookies is saved please wait...")
        for i in range(30):
                print(i, end="\r")
                time.sleep(1)
        driver.get("https://honeymoonatr.com/wp-admin/edit.php?post_type=product")
        
        
        
    os.chdir(thisPath)
    return driver, is_logged_in 
    # time.sleep(20)
    
    
    # for i in range(1, 6):
    #     print(i, end="\r")
    #     time.sleep(1)
    
        
    #/di-admin"
    # username,password = get_user_pass(honeymoonatr_domain)
    # thisTime = djtj.getDateTimeForFileName()

    # is_logged_in = False
    
    # mybrowser.change_url(main_url)
    
    # print("load main_url")
    # driver.get(main_url)
    return False
    for i in range(30):
            print(i, end="\r")
            time.sleep(1)
    # print("load main_url is complete0")
    
    waiter = input("press any key and enter: ")
    is_true = False
    while is_true ==False:
        try:
            Browser.save_cookies(mybrowser,"honeymoonatr_cookies")
            time.sleep(3)
            is_true =True
        except:
            pass
    print("cookies is saved please wait...")
    for i in range(30):
            print(i, end="\r")
            time.sleep(1)
    driver.get("https://honeymoonatr.com/wp-admin/edit.php?post_type=product")
    
    
    
    
    return True
    # number = driver.find_element(by="id",value='loginform-number')
    # thisPath = os.getcwd()
    # os.chdir(f"{thisPath}/cookies")
    # files = os.listdir()
    # print(files)
    # print(os.getcwd())
    # # file_exist = False
    # cookies_file_name = f'cookies'
    # cookie = {"name": "PHPSESSID", 
    #            "value":"e20a5d206e0f148c0e8936fa5665898b"}
    # driver.add_cookie(cookie)
    # for f in files:
    #     # print(f)
    #     if f'{cookies_file_name}.pkl'== f:
    #         file_exist = True
    #         break
    # # logged_in = True
    # if file_exist:
    # if True:
        # mybrowser.rem_cookies()
        # print("start load cookies")
        # mybrowser.load_cookies(f'{cookies_file_name}')
        
        # # time.sleep(120)
        # if mybrowser.driver.current_url == main_url:
        #     is_logged_in = True
        # else:
            # driver.get(main_url)
            # os.remove(f'{cookies_file_name}.pkl') 
            # time.sleep(5)
    return False        
    if is_logged_in == False:
        # login_hesabro(driver)
        driver.get(main_url)
        _number = driver.find_element(by="xpath",value=f"{get_xpath('login','number')}")
        
        write_in_element(username,_number)
        _number.send_keys(Keys.ENTER)

        _password = driver.find_element(by="xpath",value=f"{get_xpath('login','password')}")
        write_in_element(password,_password)
        
        _authenticator = driver.find_element(by="xpath",value=get_xpath('login','authenticator'))
        _authenticator.click()
        time.sleep(15)
        _authenticator.send_keys(Keys.ENTER)
        time.sleep(7)
        try:
            # _test = _coin = driver.find_element(by="xpath",value=get_xpath('user_detail','coin'))
            print('this message show for wait to logged in after login continue')
            waiter = input("press any key and enter: ")
            Browser.save_cookies(mybrowser,cookies_file_name)
            is_logged_in = True
        except:
            is_logged_in = False
    return driver , is_logged_in


def task_selector(selected,args_= "",**kwargs):
        answer = ""
        # print("type:")
        # print("1 : for charge setter!")
        # print(f"2 : matrook nemoodan list kala ")
        # print("3: de matrook list kala")
        # print("4: update sale and buy price for testers")
        # print("5: set noghte sefaresh")
        # selected = input("please type and then enter num of your choice: ")
        # selected = "5"
        main_url = f"{hesabro_domain}/site/index"
        print()
        print(_make_farsi_text(selected))
        print()
        if selected == tsk.task_name.Update_hesabro_customers_from_hamyar:
            driver, is_logged_in = run_hesabro()
            if is_logged_in:
                title = tsk.task_name.Update_hesabro_customers_from_hamyar
                dfData = args_
                answer = uhcfh.run_Update_hesabro_customers_from_hamyar(driver, main_url, dfData)
                # dfData.to_excel(f"{title}.xlsx", index= False)
                print(answer)
        if selected == tsk.task_name.obsolete:
            driver, is_logged_in = run_hesabro()
            if is_logged_in:
                title = tsk.task_name.obsolete
                dfData = args_
                answer = obsolete.run_obsolete_products(dfData, driver)
                # dfData.to_excel(f"{title}.xlsx", index= False)
                print(answer)
        if selected == tsk.task_name.correct_zero_prices_barcodes:
            driver, is_logged_in = run_hesabro()
            if is_logged_in:
                title = tsk.task_name.correct_zero_prices_barcodes
                dfData = args_
                answer = correct_zero_barcodes.run_correctPrices_to_barcodes(driver,main_url,dfData)
                # dfData.to_excel(f"{title}.xlsx", index= False)
                print(answer)
        if selected == tsk.task_name.active_in_site:
            driver, is_logged_in = run_hesabro()
            if is_logged_in:
                title = tsk.task_name.active_in_site
                dfData = args_
                answer = active_in_site.run_active_products_inSite(driver,main_url,dfData)
                # dfData.to_excel(f"{title}.xlsx", index= False)
                print(answer)
            # answer = update_birthday_for_call_brs(args_)
        if selected == tsk.task_name.send_birthday_data_to_sheets:
            df_invoices = args_[asts.send_birthday_toSheets_require.invoices]
            monthNum = "01"
            df_invoices = df_invoices[df_invoices[asts.tjCol.birthday].str.contains(f'/{monthNum}/', na=False)]
            # branchs_sheets = args_[asts.send_birthday_toSheets_require.branchs]
            # brs = branchs_sheets.keys()
            tjIndex = asts.getIndexTj(df_invoices)
            thisPath = os.getcwd()
            os.chdir(f"{thisPath}/media/exported")
            try:
                os.mkdir(tsk.task_name.send_birthday_data_to_sheets)
            except:
                pass
            thisPath = os.getcwd()
            os.chdir(f"{thisPath}/{tsk.task_name.send_birthday_data_to_sheets}")
            df_invoices = df_invoices[[asts.tjCol.branch,asts.tjCol.mobile,asts.tjCol.birthday]]#asts.tjCol.buyer,
            # df_invoices.to_excel("alll.xlsx",index=False)
            
            
            temp_birthday="temp_birthday"
            tjIndex = asts.getIndexTj(df_invoices)
            shape = df_invoices.shape
            columnCount = shape[1]
            df_invoices.insert(columnCount,temp_birthday,"")
            
            for i in range(len(df_invoices)):
                try:
                    df_invoices.iat[i,columnCount]= df_invoices.iat[i,tjIndex.birthday][5:]
                except:
                    df_invoices.iat[i,columnCount]= "0000/00/00"
            df_invoices = df_invoices.sort_values(by=temp_birthday)
            # # end sort on day
            # # کد مرتب سازی تا اینجاست


            # # حذف و اضافه نمودن ستون های دلخواه
            # # df_invoices = df_invoices[[frCol.mobile,frCol.buyer,frCol.branch,frCol.birthday]]
            df_invoices.insert(4,"تماس گیرنده","")
            df_invoices.insert(5,"تاریخ پیگیری اول","")
            df_invoices.insert(6,"تاریخ پیگیری دوم","")
            df_invoices.insert(7,"تاریخ پیگیری سوم","")
            df_invoices.insert(8,"تاریخ پیگیری چهارم","")
            df_invoices.insert(9,"نتیجه","")
            df_invoices.insert(10,"توضیحات","")

            df_invoices.drop(temp_birthday, axis=1 , inplace=True) 

            while len(df_invoices):
                branch = df_invoices.iat[0, tjIndex.branch]
                dfbranchs = df_invoices.loc[df_invoices[asts.tjCol.branch]==branch]
                df_invoices = df_invoices.loc[df_invoices[asts.tjCol.branch]!=branch]
                dfbranchs.to_excel(f"{branch}.xlsx",index =False)
                
                # mybrowser = Browser()
                # this_address = branchs_sheets[branch]
                
                # # mybrowser.change_url(main_url)
                # driver = mybrowser.driver
                # driver.get(this_address)
                
        if selected == tsk.task_name.update_birthday_call_brs:
            driver, is_logged_in = run_hesabro()
            if is_logged_in:
                title = tsk.task_name.update_birthday_call_brs
                dfData = fbsd.get_birthdays_data(driver,title)
                dfData.to_excel(f"{title}.xlsx", index= False)
            # answer = update_birthday_for_call_brs(args_)
        if selected == tsk.task_name.salary:
            # pass
            df_invoices = args_[asts.salary_requires.invoices]
            df_targets = args_[asts.salary_requires.targets]
            startDate = args_[asts.salary_requires.startDate]
            endDate = args_[asts.salary_requires.endDate]
            filesPath,fileName = salary(df_invoices, df_targets, startDate, endDate)
            answer = [filesPath, fileName]
            # df = pd.read_csv(args_,sep=",")
            
            # df.to_excel("this Is test.xlsx")
        if selected == tsk.task_name.run_honeymoonatr:
            # print("seledted is ok")
            driver, is_logged_in =run_honeymoonatr()
            if is_logged_in:
                
                upsh.start_update(driver)
                
        elif selected == tsk.task_name.update_birthday:
            driver, is_logged_in = run_hesabro()
            if is_logged_in:
                dfData = upb.get_birthday_data(driver,main_url,tsk.task_name.update_birthday)
                
                for i in range(len(dfData)):
                    
                send_group_sms(dfData,tsk.task_name.update_birthday,args_)
                try:
                    birthPath = os.getcwd()
                    reports = "reports"
                    os.mkdir(reports)
                except:
                    pass
                # os.chdir(f"{birthPath}/{reports}")

                # birthPath = os.getcwd()
                birthPath = f"{birthPath}/{reports}"
                birthdayDir = f"{birthPath}/birthday"
                try:
                    # birthdayDir = "birthday"
                    os.mkdir(birthdayDir)
                except:
                    pass
                # os.chdir(f"{birthPath}/{birthdayDir}")
                # dfData.to_excel(f"{birthdayDir}/birthday in {djtj.getDateTimeForFileName()}.xlsx",index=False)
            # mybrowser = Browser()
            # # mybrowser.change_url(main_url)
            # driver = mybrowser.driver
            # driver = run_arad_payamek(driver)
            # sms_text = "تست ارسال پیامک\nلغو 11"
            # number = '09162078094'

            
            # msg = "#نام و نام خانوادگی عزیز سلام\nتولدت مبارک\n20% تخفیف نقدی تا 10 روز برای شما در تمامی شعب هانی مون"
            # _msg = args_
            # args_ = "test\n لغو 11"
            mobile = "موبایل"
            name = "نام و نام خانوادگی"
            birthday = "تاریخ تولد"
            ls = []
            # this_dict = {
            #     mobile:"09136199868",
            #     name: "علی خراسانی",
            #     birthday:"1380/01/01"}
            # ls.append(this_dict)
            # this_dict = 
            ls.append({mobile:"09139960164", name: "حسین مظهری", birthday:"1365/06/29"})
            dfData = pd.DataFrame(ls)
            # dfData.to_excel("data.xlsx",index=False)
            send_group_sms(dfData,tsk.task_name.update_birthday,args_)
            # time.sleep(60)
            # driver.close()
        elif selected == tsk.task_name.get_report_from_hesabro_link:
            driver, is_logged_in = run_hesabro()
            print("this select")
            if is_logged_in:
                dfData = frd.get_report_data(driver,tsk.task_name.get_report_from_hesabro_link,args_)
            dfData.to_excel("report_data.xlsx",index=False)
        elif selected == tsk.task_name.get_coin_report_from_hesabro_link:
            driver, is_logged_in = run_hesabro()
            print("hesabro is running")
            if is_logged_in:
                print("run download")
                dfData = fcrd.get_coin_report_data(driver,tsk.task_name.get_coin_report_from_hesabro_link,args_)
            # dfData.to_excel("report_data.xlsx",index=False)
        elif selected == tsk.task_name.set_order_point:
            driver, is_logged_in = run_hesabro()
            if is_logged_in:
                title = tsk.task_name.obsolete
                dfData = args_
                answer = set_order_point(driver, dfData)
                # dfData.to_excel(f"{title}.xlsx", index= False)
                print(answer)

        elif selected == "1":
            pass
        elif selected == "2"        :
            dfData = pd.read_excel("product.xlsx")
            print('product file now upload successfully')
            _ls_deactive_users = []
            _ls_active_users = []
            l = len(dfData)
            print(f'numer of product is {l}')
            
            save_counter = 0
            while len(dfData):
                save_counter += 1
                driver.get(main_url)
                time.sleep(2.5)
                product = dfData.iat[0,0]
                # user = dfData.iat[0,1]
                # this_mobile = f"0{int(mobile)}"
                # coin = str(dfData.iat[0,2])
                prgsCounter = l- len(dfData)
                prgs.printProgressBar(prgsCounter, l, prefix = 'Progress:', suffix = 'Complete', length = 25)    
                # print(f"charge {mobile} is doing! please wait...")
                # hamyar_condition = True
                # if prgsCounter > 10:
                #     hamyar_condition =False
                # from product import update_product
                act = "exit_product"
                # action_True = update_product(act,product,driver,main_url)
                
                dfData = dfData.loc[dfData["product"]!=product]
                
        elif selected == "3":
            print("please wait until see 'done'...")
            matrook = True
            counter = 0
            while matrook:
                counter += 1
                print(counter)
                # matrook = check_matrook(driver,main_url)

            print("done")
        elif selected == "4":
            # testersPrice(driver,main_url)

            print("done")
        elif selected == "5":
            set_order_point(driver,main_url)
        elif selected == "6":
            pass
            # create_product_address = urls["product"]["create_product"]
            # create_product(driver,main_url,create_product_address)
        elif selected == "7":
            # deactive_product(driver,main_url)
            pass
        elif selected == "8":
            # price_changer(driver,main_url)
            pass
        elif selected == "9":
            pass
            # create_product_address = urls["product"]["create_product"]
            # create_testers(driver,main_url,create_product_address)
            # dfData = pd.read_excel("product.xlsx")
            # print('product file now upload successfully')
            # _ls_deactive_users = []
            # _ls_active_users = []
            # l = len(dfData)
            # print(f'numer of product is {l}')
            
            # save_counter = 0
            # while len(dfData):
            #     save_counter += 1
            #     driver.get(main_url)
            #     time.sleep(2.5)
            #     product = dfData.iat[0,0]
            #     # user = dfData.iat[0,1]
            #     # this_mobile = f"0{int(mobile)}"
            #     # coin = str(dfData.iat[0,2])
            #     prgsCounter = l- len(dfData)
            #     prgs.printProgressBar(prgsCounter, l, prefix = 'Progress:', suffix = 'Complete', length = 25)    
            #     # print(f"charge {mobile} is doing! please wait...")
            #     # hamyar_condition = True
            #     # if prgsCounter > 10:
            #     #     hamyar_condition =False
            #     # from product import update_product
            #     act = "exit_product"
            #     action_True = update_product(act,product,driver,main_url)
                
            #     dfData = dfData.loc[dfData["product"]!=product]
        
        return answer    