import os,time,pandas as pd

from selenium_files.settings_selenium import xpath_hesabro as xph

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium_files.settings_selenium.app_address import Urls_hesabro,File_locations
from selenium_files.settings_selenium.app_structures \
    import get_index_report_output_cols,report_output_cols
def download_page(driver): 
    # this_address = driver.current_url
    try:
        # is_true = False
        # name = []
        # mobile = []
        # birthday = []
            lsData = []
        
        # repeat_count = 1
        # while is_true==False:
            # thisReport = driver.current_url
        
            element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xph.create_reportcustomer.dataReport.tbody)))
            # element.click()
            
            # element =driver.find_element(By.XPATH,xph.create_reportcustomer.dataReport.tbody)
            # element[1].click()
            trs = element.find_elements(By.TAG_NAME, "tr")
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            for tr_index in trs:
                tds = tr_index.find_elements(By.TAG_NAME, "td")
                row = (tds[0].text)
                id = (tds[1].text)
                name = (tds[2].text).replace("(موقت)", "")
                gender = (tds[3].text)
                birthday = (tds[4].text)
                passport_id = (tds[5].text)
                email = (tds[6].text)
                mobile = (tds[7].text)
                trusted = (tds[8].text)
                lsData.append({report_output_cols.row : row,
                    report_output_cols.id : id,  report_output_cols.name : name,
                    report_output_cols.gender : gender, report_output_cols.birthday : birthday,
                    report_output_cols.passport_id : passport_id, report_output_cols.email : email,
                    report_output_cols.mobile : mobile, report_output_cols.trusted : trusted
                                })
                
                # for more pretty act]ions in ui , ux this code writed to next_p
                
                # time.sleep(0.6)
            element =driver.find_element(By.XPATH,xph.create_reportcustomer.dataReport.next_p)
            time.sleep(2.5)
            # element = WebDriverWait(driver, 10).until(
            #     EC.presence_of_element_located((By.XPATH, xph.create_reportcustomer.download)))
    except Exception as e:
        print(e)
        # is_true = False

    return pd.DataFrame(lsData),  driver
def update_customers_specifications(driver): 
    #  1- تغییر آدرس مرورگر به صفححه ایجاد گزاشات
    # this_address = app_address.urls["birthday"]["create_rpt"]
    # this_address = app_address.url_address.create_report.birthday
    # this_address = "https://hesabro.ir/@hm/report-customer/view?id=100&page=469&per-page=50"
    this_address = Urls_hesabro.Club.Customers.Specifications.link
    db_address = File_locations.Data_base.Club.Customers.Specifications.db_address
    this_path = os.getcwd()
    df_customers_specifications = pd.read_excel(f"{this_path}/{db_address}")
    dfData = df_customers_specifications.copy()
    driver.get(this_address)
    this_delay = 3
    while driver.current_url != this_address: # جهت اطمینان از باز شدن صفحه ی درخواست شده در گزینه 1 از حلقه استفاده شده است
        driver.get(this_address)
        time.sleep(this_delay)
        this_delay += 1
    
    # this_delay 
        
    # thisPage = driver.current_url
    # pageIndexStart = thisPage.find("&page=")+1
    # pageIndexEnd = thisPage.find("&per-page")
    # print(thisPage[pageIndexStart:pageIndexEnd])
    

    this_delay = 2
    ls_data = []
    df_pageData, driver = (download_page(driver))
    
    is_finish = False
    thisItter = 0
    while  is_finish == False:
        thisItter += 1
        print(thisItter)
        while len(df_pageData):
            thisIndex = get_index_report_output_cols(df_pageData)
            thisCols = report_output_cols()
            mobile = df_pageData.iat[0, thisIndex.mobile]
            row = df_pageData.iat[0, thisIndex.row]
            id = df_pageData.iat[0, thisIndex.id]
            birthday = df_pageData.iat[0, thisIndex.birthday]
            email = df_pageData.iat[0, thisIndex.email]
            gender = df_pageData.iat[0, thisIndex.gender]
            name = df_pageData.iat[0, thisIndex.name]
            passport_id = df_pageData.iat[0, thisIndex.passport_id]
            trusted = df_pageData.iat[0, thisIndex.trusted]
            df_pageData = df_pageData.loc[df_pageData[thisCols.mobile]!=mobile]
            if len(dfData.loc[dfData[thisCols.mobile] == mobile]):
                is_finish = True
            else:
                ls_data.append({thisCols.row:row, thisCols.id: id,
                                thisCols.mobile:mobile,thisCols.name: name,
                                thisCols.gender: gender, thisCols.birthday:\
                                birthday,
                                thisCols.email: email,
                                thisCols.passport_id: passport_id, thisCols.trusted:\
                                trusted
                                })
        df_pageData, driver = (download_page(driver))

        # ls_data.append(data)
        # if is_continu==False:
        #     break
    dfData = pd.DataFrame(ls_data)
    dfData = pd.concat(dfData, df_customers_specifications)

    dfData.to_excel(File_locations.Data_base.Club.Customers.Specifications.db_address,index=False)
    # return dfData

# def append_data(df_pageData):
    
# def f():
#                 thisPage = driver.current_url
#                 pageIndexStart = thisPage.find("&page=")+1
#                 pageIndexEnd = thisPage.find("&per-page")
#                 print(thisPage[pageIndexStart:pageIndexEnd])
#                 print(time.ctime())
#                 print(counter_page)
#                 print("-------------------------")
                
#                 # if counter_page % 1 == 0 :
#                 if True:

#                     # counter_page = 1
#                     thisData = pd.DataFrame(lsData)
#                     # thisData.to_excel(f"{title}bk_p50.xlsx",index=False)
                
#                 element =driver.find_element(By.XPATH,xph.create_reportcustomer.dataReport.next_p)
#                 counter_page += 1
                
               
#                 if element.is_displayed():
#                         element.click()
                        
#                         # time.sleep(1)
#                 else:
#                     is_true = True
#                     # driver.close()
#                 # time.sleep(6)
                
               
#             except Exception as e:
#                 # print(e)
#                 repeat_count += 1
#                 if repeat_count>20:
#                     break
#                 try:
#                     data = pd.read_excel(f"{title}bk_p50.xlsx")
#                     row = data['row'].max()
#                     page_index = row//50
#                 except:
#                     page_index =1
#                 pageIndexStart = thisPage.find("&page=")+6
#                 pageIndexEnd = thisPage.find("&per-page")
#                 # print(thisPage[pageIndexStart:pageIndexEnd])
#                 step1 = thisReport[:pageIndexStart]
#                 step2 = thisReport[pageIndexEnd:]
#                 this_address = f"{step1}{page_index}{step2}"
#                 driver.close()
                
#                 # driver, is_logged_in = run_hesabro()
                
#                 # driver.get(this_address)
#                 # this_delay = 3
#                 # while driver.current_url != this_address: # جهت اطمینان از باز شدن صفحه ی درخواست شده در گزینه 1 از حلقه استفاده شده است
#                 #     driver.get(this_address)
#                 #     time.sleep(this_delay)
#                 #     this_delay += 1
#                 # data = pd.DataFrame(lsData)
#                 # data.to_excel(f"{title}.xlsx",index=False)
#                 # is_true = True
                
                
                
#             #     time.sleep(5)
#             #     is_true = False
#         data = pd.DataFrame(lsData)
#         data.to_excel(f"{title}.xlsx",index=False)
