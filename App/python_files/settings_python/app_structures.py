import arabic_reshaper
from bidi.algorithm import get_display
from . import DateJuToJa as djtj
import os,sys,pandas as pd

export_path = 'exported'
staticName = 'static'
mediaName = 'media'
def prtLines(count=3):
    for i in range(count):
        print()
############################################################################################
def getDateTimeForFileName():
   
    todayIs = djtj.todaydate()
    todayIs = todayIs.replace("/","-")
    import time
    timeIs = int(time.monotonic())
    return f"{todayIs} {timeIs}"
############################################################################################
def _make_farsi_text(x):
  reshaped_text = arabic_reshaper.reshape(x)
  farsi_text = get_display(reshaped_text)
  return farsi_text
############################################################################################
class tjCol():
    name = "نام"  
    count = "تعداد"
    average = "میانگین"  
    Received = "دریافتی"
    saleTime = "زمان فروش"  
    branch="عنوان شرکت"
    branch_id = "کد شرکت"
    gender="جنسیت"
    mobile="موبایل"
    transitional= "انتقالی"
    Deposit = "واریزی"
    tasvieBaMarjooe="تسویه با مرجوعي"
    earnest="پیش دریافت"
    Cash = "نقدی"
    chargeUse = "مصرف شارژ"
    saleAgentCharge = "شارژ عامل"
    charge = "مبلغ شارژ"
    saler = "فروشنده"
    saleAget = "عامل فروش"
    seller_name="ثبت کننده"
    seller_id = "کدثبت کننده"
    buyer="خريدار"
    PurchaseAmount = "ارزیابی"
    PurchaseAmountLbl = "مبلغ خرید"
    Remaining= "مانده پرداختي"
    mablagh= "جمع کل"
    Discount = "تخفيف"
    TotalOne = "جمع واحد"
    quantity = "مقدار"
    factor_date = "تاريخ"
    saleId = "شماره"
    work = "شغل"
    education = "تحصیلات"
    to_other_person = "پرداخت به شخص"
    check = "چک"
    discount_code = "کد تخفیف"
    birthday = "تاریخ تولد"

def getIndexTj(df):
    tjIndex = tjCol()
    thisIndex=-1
    for col in df.columns:        
        thisIndex+=1
        if tjIndex.name == col:
            tjIndex.name = thisIndex # type: ignore 
        elif tjIndex.count == col:
            tjIndex.count = thisIndex # type: ignore 
        elif tjIndex.average == col:
            tjIndex.average = thisIndex # type: ignore 
        elif tjIndex.branch == col:
            tjIndex.branch = thisIndex # type: ignore 
        elif tjIndex.branch_id == col:
            tjIndex.branch_id = thisIndex # type: ignore 
        elif tjIndex.gender == col:
            tjIndex.gender = thisIndex # type: ignore 
        elif tjIndex.mobile == col:
            tjIndex.mobile = thisIndex # type: ignore 
        elif tjIndex.transitional==col:
            tjIndex.transitional = thisIndex # type: ignore 
        elif tjIndex.Deposit==col:
            tjIndex.Deposit = thisIndex # type: ignore 
        elif tjIndex.tasvieBaMarjooe==col:
            tjIndex.tasvieBaMarjooe = thisIndex # type: ignore 
        elif tjIndex.earnest==col:
            tjIndex.earnest = thisIndex # type: ignore 
        elif tjIndex.Cash==col:
            tjIndex.Cash = thisIndex # type: ignore 
        elif tjIndex.chargeUse==col:
            tjIndex.chargeUse = thisIndex # type: ignore 
        elif tjIndex.saleAgentCharge==col:
            tjIndex.saleAgentCharge = thisIndex # type: ignore 
        elif tjIndex.charge==col:
            tjIndex.charge = thisIndex # type: ignore 
        elif tjIndex.saler==col:
            tjIndex.saler = thisIndex # type: ignore 
        elif tjIndex.saleAget==col:
            tjIndex.saleAget = thisIndex # type: ignore 
        elif tjIndex.seller_name==col:
            tjIndex.seller_name = thisIndex # type: ignore 
        elif tjIndex.seller_id == col: # type: ignore
            tjIndex.seller_id = thisIndex # type: ignore
        elif tjIndex.buyer==col:
            tjIndex.buyer = thisIndex # type: ignore 
        elif tjIndex.PurchaseAmount==col:
            tjIndex.PurchaseAmount = thisIndex # type: ignore 
        elif tjIndex.PurchaseAmountLbl==col:
            tjIndex.PurchaseAmountLbl = thisIndex # type: ignore 
        elif tjIndex.Remaining==col:
            tjIndex.Remaining = thisIndex # type: ignore 
        elif tjIndex.mablagh==col:
            tjIndex.mablagh = thisIndex # type: ignore 
        elif tjIndex.Discount==col:
            tjIndex.Discount = thisIndex # type: ignore  # type: ignore 
        elif tjIndex.TotalOne==col:
            tjIndex.TotalOne = thisIndex # type: ignore 
        elif tjIndex.quantity==col:
            tjIndex.quantity = thisIndex # type: ignore 
        elif tjIndex.factor_date==col:
            tjIndex.factor_date = thisIndex # type: ignore 
        elif tjIndex.saleId==col:
            tjIndex.saleId = thisIndex # type: ignore 
        elif tjIndex.saleTime == col:
            tjIndex.saleTime = thisIndex # type: ignore 
        elif tjIndex.Received == col:
            tjIndex.Received = thisIndex# type: ignore 
        elif tjIndex.work == col:
            tjIndex.work = thisIndex #type: ignore
        elif tjIndex.education == col:
            tjIndex.education = thisIndex # type: ignore
        elif tjIndex.check == col:
            tjIndex.check = thisIndex # type: ignore
        elif tjIndex.birthday == col:
            tjIndex.birthday = thisIndex # type: ignore
    return tjIndex
############################################################################################
class myDataType_names():
    cumulativeSales = "تجمیعی فروش"
    detailedSales = "فروش"
    correctData = "دیتای صحیح"
    birthdays = "تولدی های شعب"
    Festival = "جشنواره های هانی مون"
    timeWork = "مدت زمان فعالیت به دقیقه"
    contacts = "ساخت فایل مخاطب"
    compareBase = "تعیین عطرهای مشخص برای مقایسه"
    compareWith = "فایل هایی که بررسی میزان فروش آنها مقایسه میشود"
    returnedproduct_name = "مرجوعی های کالا"
    targets = "تارگت ها"
    orders = "تهیه کالا"
    buys = "خریدها"
    Costs = "هزینه ها"
    nish = "نیش پرفیوم ها"
    user_details = "تفصیلی"
    hesabro = "حسابرو"

class dataTypeAddresses():
    cumulativeSales = "/فایلهای خام/تجمیعی فروش/"
    hesabro = "/فایلهای خام/حسابرو/"
    Costs = "/فایلهای خام/هزینه ها/"
    detailedSales = "/فایلهای خام/فروش/"
    correctData = "/source/correctData/"
    # birthdays = "/source/birthdays/sent"
    birthdays = "/فایلهای خام/تولدی ها/"
    Festival = "/source/Festival"
    timeWork = "/فایلهای خام/کارکرد کارکنان/"
    user_details = "/فایلهای خام/تفصیلی/"
    contacts = "/source/Contacts/"
    compareBase = "/source/merchandize selector/base"
    compareWith = "/source/merchandize selector/with"
    returnedproduct_name = "/فایلهای خام/مرجوعی/"
    targets = "/فایلهای خام/تارگت ها/"
    orders = "/فایلهای خام/تهیه کالا/"
    buys = "/فایلهای خام/خریدها/"
    nish =  "/فایلهای خام/نیش های انحصاری/"
############################################################################################
class condition():
    saleTime = "15:29:59"
    shiftWork = "شیفت کاری"
    saleAm = "شیفت صبح"
    salePm = "شیفت عصر"
    alhchol = "فيکساتور پرفيومري"
    missData = "MisstakeData"

############################################################################################
class frCol():#version 1401.1 b ghabl chon az 1401.2 soton ha jabja shodeand dar hamyar
    saleId = "شماره"
    product_id= "کد کالا"
    factor_date = "تاريخ"
    branch = "عنوان شرکت"
    category = "عنوان طبقه"
    group = "عنوان گروه"
    groupType = "نوع گروه"
    quantity = "مقدار"
    product_name = "عنوان کالا"
    AmountOne = "مبلغ واحد"
    Discount = "تخفيف"
    TotalOne = "جمع واحد"
    summation = "جمع کل"
    PurchaseAmount="ارزیابی"
    PurchaseAmountLbl="مبلغ خرید"
    buyer = "خريدار"
    seller_name = "ثبت کننده"
    seller_id = tjCol.seller_id
    saler = "فروشنده"
    idBuyer = "کد خریدار"
    gender = "جنسیت"
    birthday = "تاریخ تولد"
    mobile = "موبایل"
    saleTime= "زمان فروش"
    branch_id = tjCol.branch_id



def getIndexFr(df):
    frIndex = frCol()
    thisIndex=-1
    for col in df.columns:        
        thisIndex+=1
        if frIndex.saleId == col:
            frIndex.saleId = thisIndex # type: ignore 
        if frIndex.branch_id == col:
            frIndex.branch_id = thisIndex #type: ignore
        if frIndex.seller_id == col:
            frIndex.seller_id = thisIndex # type: ignore
        elif frIndex.product_id == col:
            frIndex.product_id = thisIndex # type: ignore 
        elif frIndex.factor_date == col:
            frIndex.factor_date = thisIndex # type: ignore 
        elif frIndex.branch == col:
            frIndex.branch = thisIndex # type: ignore 
        elif frIndex.category == col:
            frIndex.category = thisIndex # type: ignore 
        elif frIndex.group == col:
            frIndex.group = thisIndex # type: ignore 
        elif frIndex.groupType == col:
            frIndex.groupType = thisIndex # type: ignore 
        elif frIndex.quantity == col:
            frIndex.quantity = thisIndex # type: ignore 
        elif frIndex.product_name == col:
            frIndex.product_name = thisIndex # type: ignore 
        elif frIndex.AmountOne == col:
            frIndex.AmountOne = thisIndex # type: ignore 
        elif frIndex.Discount == col:
            frIndex.Discount = thisIndex # type: ignore 
        elif frIndex.TotalOne == col:
            frIndex.TotalOne = thisIndex # type: ignore 
        elif frIndex.summation == col:
            frIndex.summation = thisIndex # type: ignore 
        elif frIndex.PurchaseAmount == col:
            frIndex.PurchaseAmount = thisIndex # type: ignore 
            frIndex.PurchaseAmountLbl = thisIndex # type: ignore 
        elif frIndex.buyer == col:
            frIndex.buyer = thisIndex # type: ignore 
        elif frIndex.seller_name == col:
            frIndex.seller_name = thisIndex # type: ignore 
        elif frIndex.saler == col:
            frIndex.saler = thisIndex # type: ignore 
        elif frIndex.idBuyer == col:
            frIndex.idBuyer = thisIndex # type: ignore 
        elif frIndex.gender == col:
            frIndex.gender = thisIndex # type: ignore 
        elif frIndex.birthday == col:
            frIndex.birthday = thisIndex # type: ignore 
        elif frIndex.mobile == col:
            frIndex.mobile = thisIndex # type: ignore 
        elif frIndex.saleTime == col:
            frIndex.saleTime = thisIndex # type: ignore 
    return frIndex

############################################################################################

class monthCol():
    month = "ماه"
    Deposit = tjCol.Deposit
    Cash = tjCol.Cash
    earnest = tjCol.earnest
    transitional= tjCol.transitional
    Received = tjCol.Received
    start = "شروع"
    end = "پایان"
    name = month
class yearDetail():
    month = {
                "01":{monthCol.month:"فروردین", monthCol.Deposit:0, monthCol.Cash:0, monthCol.earnest : 0 , monthCol.transitional : 0 , monthCol.Received : 0 , monthCol.start  :  "" , monthCol.end : ""},
                "02":{monthCol.month:"اردیبهشت", monthCol.Deposit:0, monthCol.Cash:0, monthCol.earnest : 0 , monthCol.transitional : 0 , monthCol.Received : 0 , monthCol.start  :  "" , monthCol.end : ""},
                "03":{monthCol.month:"خرداد", monthCol.Deposit:0, monthCol.Cash:0, monthCol.earnest : 0 , monthCol.transitional : 0 , monthCol.Received : 0 , monthCol.start  :  "" , monthCol.end : ""},
                "04":{monthCol.month:"تیر", monthCol.Deposit:0, monthCol.Cash:0, monthCol.earnest : 0 , monthCol.transitional : 0 , monthCol.Received : 0 , monthCol.start  :  "" , monthCol.end : ""},
                "05":{monthCol.month:"مرداد", monthCol.Deposit:0, monthCol.Cash:0, monthCol.earnest : 0 , monthCol.transitional : 0 , monthCol.Received : 0 , monthCol.start  :  "" , monthCol.end : ""},
                "06":{monthCol.month:"شهریور", monthCol.Deposit:0, monthCol.Cash:0, monthCol.earnest : 0 , monthCol.transitional : 0 , monthCol.Received : 0 , monthCol.start  :  "" , monthCol.end : ""},
                "07":{monthCol.month:"مهر", monthCol.Deposit:0, monthCol.Cash:0, monthCol.earnest : 0 , monthCol.transitional : 0 , monthCol.Received : 0 , monthCol.start  :  "" , monthCol.end : ""},
                "08":{monthCol.month:"آبان", monthCol.Deposit:0, monthCol.Cash:0, monthCol.earnest : 0 , monthCol.transitional : 0 , monthCol.Received : 0 , monthCol.start  :  "" , monthCol.end : ""},
                "09":{monthCol.month:"آذر", monthCol.Deposit:0, monthCol.Cash:0, monthCol.earnest : 0 , monthCol.transitional : 0 , monthCol.Received : 0 , monthCol.start  :  "" , monthCol.end : ""},
                "10":{monthCol.month:"دی", monthCol.Deposit:0, monthCol.Cash:0, monthCol.earnest : 0 , monthCol.transitional : 0 , monthCol.Received : 0 , monthCol.start  :  "" , monthCol.end : ""},
                "11":{monthCol.month:"بهمن", monthCol.Deposit:0, monthCol.Cash:0, monthCol.earnest : 0 , monthCol.transitional : 0 , monthCol.Received : 0 , monthCol.start  :  "" , monthCol.end : ""},
                "12":{monthCol.month:"اسفند", monthCol.Deposit:0, monthCol.Cash:0, monthCol.earnest : 0 , monthCol.transitional : 0 , monthCol.Received : 0 , monthCol.start  :  "" , monthCol.end : ""}
            }
############################################################################################
def fillNullZero(df_all):
    # try:
        
        print(_make_farsi_text("برنامه در حال اصلاح دیتاهای ثبت نشده میباشد"))
       

        df_all=df_all.fillna(0, inplace = True)
        # print("tolid file avalieh khorooji")
        # df_all.to_excel("all data-1398-1400.xlsx" , index = False)
        print("miss Data sabt shodand")

def loadFiles(currentPath):
    df_all = pd.DataFrame()
    dfs=[]
    lsF =[]
    
    indexFile = 0
    os.chdir(currentPath)
    lsF.append(os.listdir())
    # print(lsF[br])
    
    print(_make_farsi_text(": لیست سال ها و فایل های قابل بررسی "))

    # lsF[0]=[i for i in lsF[0] if os.path.isfile(i)]

    for fileName in lsF[0]:
        indexFile += 1
        print(f"{indexFile}==> {_make_farsi_text(fileName)}")
    print(" ")
    print(_make_farsi_text("انتخاب همه<== 1-"))
    print(" ")
    filesIndex = int(input(_make_farsi_text(" : لطفا عدد متناظر با انتخاب تان را وارد نمایید ")))
 
    if filesIndex == -1 :
        lsF[0]=[i for i in lsF[0] if os.path.isfile(i)]
        for fileNames in lsF[0]:             
            if os.path.isfile(fileNames) and (fileNames[-5:].lower() == ".xlsx" or fileNames[-4:].lower() == ".xls"):
                if fileNames[:2]!="~$":
                    print(f"loading {_make_farsi_text(fileNames)} please wait...")
                    
                    dfs.append(pd.read_excel(fileNames))
                else:
                    print(_make_farsi_text(f"{fileNames[2:]} در حال حاضر باز و امکان دارد ذخیره نشده باشد. با آخرین ذخیره سازی فایل دریافت می شود"))
        df_all = pd.concat(dfs)
    elif os.path.isfile(lsF[0][filesIndex-1]):
        fileNames=lsF[0][filesIndex-1]
        if os.path.isfile(fileNames) and (fileNames[-5:].lower() == ".xlsx" or fileNames[-4:].lower() == ".xls"):
            if fileNames[:2]!="~$":
                print(f"loading {_make_farsi_text(fileNames)} please wait...")
                df_all=(pd.read_excel(fileNames))
                print("load is completed...")
                print("Please wait..")
                # print(df_all)
            else:
                print(_make_farsi_text(f"{fileNames[2:]} در حال حاضر باز و امکان دارد ذخیره نشده باشد. با آخرین ذخیره سازی فایل دریافت می شود"))
    else:
        currentPath += f"/{lsF[0][filesIndex-1]}/"
        os.chdir(currentPath)
        lsF = []
        lsF.append(os.listdir())
        lsF[0]=[i for i in lsF[0] if os.path.isfile(i)]
        for fileNames in lsF[0]:             
            if os.path.isfile(fileNames) and (fileNames[-5:].lower() == ".xlsx" or fileNames[-4:].lower() == ".xls"):
                if fileNames[:2]!="~$":
                    print(f"loading {_make_farsi_text(fileNames)} please wait...")
                    dfs.append(pd.read_excel(fileNames))
                else:
                    print(_make_farsi_text(f"{fileNames[2:]} در حال حاضر باز و امکان دارد ذخیره نشده باشد. با آخرین ذخیره سازی فایل دریافت می شود"))
        print(_make_farsi_text("بررسی اولیه روی فایل ها و ادغام آنها جهت بارگزاری"))
        df_all = pd.concat(dfs)
        # print("Loading is completed.\nplease wait for a minute or more")


    print(_make_farsi_text("فایل/ها بارگزاری شدند"))
    return df_all

def loadData(filesType,destination):
    
    mainPath=os.getcwd()
    if filesType == myDataType_names.cumulativeSales:
        currentPath = mainPath + dataTypeAddresses.cumulativeSales
    elif filesType == myDataType_names.hesabro:
        currentPath = mainPath + dataTypeAddresses.hesabro
    elif filesType == myDataType_names.returnedproduct_name:
        currentPath = mainPath + dataTypeAddresses.returnedproduct_name
    elif filesType == myDataType_names.user_details:
        currentPath = mainPath + dataTypeAddresses.user_details
    elif filesType == myDataType_names.detailedSales:
        currentPath = mainPath + dataTypeAddresses.detailedSales
    elif filesType == myDataType_names.correctData:
        currentPath = mainPath + dataTypeAddresses.correctData 
    elif filesType == myDataType_names.birthdays:
        currentPath = mainPath + dataTypeAddresses.birthdays 
    elif filesType == myDataType_names.Festival:
        currentPath = mainPath + dataTypeAddresses.Festival 
    elif filesType == myDataType_names.timeWork:
        currentPath = mainPath + dataTypeAddresses.timeWork
    elif filesType == myDataType_names.contacts:
        currentPath = mainPath + dataTypeAddresses.contacts
    elif filesType == myDataType_names.compareBase:
        currentPath = mainPath + dataTypeAddresses.compareBase
    elif filesType == myDataType_names.compareWith:
        currentPath = mainPath + dataTypeAddresses.compareWith
    elif filesType== myDataType_names.targets:
        currentPath= mainPath+dataTypeAddresses.targets
    elif filesType == myDataType_names.buys:
        currentPath = mainPath+dataTypeAddresses.buys
    elif filesType == myDataType_names.orders:
        currentPath = mainPath+ dataTypeAddresses.orders
    elif filesType == myDataType_names.nish:
        currentPath = mainPath+ dataTypeAddresses.nish
   
    folderName = destination
    df_all = loadFiles(currentPath)
    
    # if filesType == myDataType_names.cumulativeSales  :
    #     # print(len(df_all))
    #     fillNullTj(df_all)
    #     # print(len(df_all))
    # elif filesType == myDataType_names.detailedSales :
    #     fillNullFr(df_all)
    # elif filesType == myDataType_names.correctData:
    #     fillNullMiss(df_all)
    # elif filesType == myDataType_names.timeWork:
    #     fillNullTimes(df_all)
    # else:
    fillNullZero(df_all)

    if filesType==myDataType_names.detailedSales:
        df_all= df_all.loc[df_all[frCol.quantity]>0]
        df_all = df_all.loc[df_all[frCol.saleId] !=0]
        df_all = df_all.loc[df_all[frCol.factor_date] !=0]
        df_all = df_all.loc[df_all[frCol.product_name] !=0]
        # setIndexFr(df_all)
        
    elif filesType == myDataType_names.cumulativeSales:
        # df_all=df_all.loc[df_all[tjCol.quantity]>0]
        df_all = df_all.loc[df_all[tjCol.saleId] !=0]
        df_all = df_all.loc[df_all[tjCol.factor_date] !=0]
        # tjIndex = (df_all)



    currentPath = mainPath
    os.chdir(currentPath)

    currentPath += "/export/"
    try:
        os.makedirs("export")
        os.chdir(currentPath)
    except:
        os.chdir(currentPath)
    
    currentPath += folderName
    try:
        os.makedirs(folderName)
        os.chdir(currentPath)
    except:
        os.chdir(currentPath)
    # df_all.to_excel("t.xlsx",index=False)
    return df_all
############################################################################################

class monthsSelector():
    month={
            "01":{"start":"/01/01","end":"/01/31","name":"فروردین"},
            "02":{"start":"/02/01","end":"/02/31","name":"اردیبهشت"},
            "03":{"start":"/03/01","end":"/03/31","name":"خرداد"},
            "04":{"start":"/04/01","end":"/04/31","name":"تیر"},
            "05":{"start":"/05/01","end":"/05/31","name":"مرداد"},
            "06":{"start":"/06/01","end":"/06/31","name":"شهریور"},
            "07":{"start":"/07/01","end":"/07/30","name":"مهر"},
            "08":{"start":"/08/01","end":"/08/30","name":"آبان"},
            "09":{"start":"/09/01","end":"/09/30","name":"آذر"},
            "10":{"start":"/10/01","end":"/10/30","name":"دی"},
            "11":{"start":"/11/01","end":"/11/30","name":"بهمن"},
            "12":{"start":"/12/01","end":"/12/30","name":"اسفند"}
        }

############################################################################################

class hesabroTjCol():
    id = "id"
    factor_date = "factor_date"
    factor_amount = "factor_amount"
    seller_id = "seller_id"
    saler_name = "name"
    branch_id = "branch_id"
    b_name_1 = "b_name_1"
    mobile = "username"
    first_name = "first_name"
    last_name = "last_name"
    customer_id = "customer_id"
    
   
    
    
def getIndexHesabroTj(df):
    thisClass = hesabroTjCol()
    thisItter = -1
    for col in df.columns:
        thisItter += 1
        if col == thisClass.id:
            thisClass.id = thisItter # type: ignore
        elif col == thisClass.branch_id:
            thisClass.branch_id = thisItter# type: ignore
        elif col == thisClass.customer_id:
            thisClass.customer_id = thisItter# type: ignore
        elif col == thisClass.factor_amount:
            thisClass.factor_amount = thisItter# type: ignore
        elif col == thisClass.b_name_1:
            thisClass.b_name_1 = thisItter# type: ignore
        elif col == thisClass.factor_date:
            thisClass.factor_date = thisItter# type: ignore
        elif col == thisClass.first_name:
            thisClass.first_name = thisItter# type: ignore
        elif col == thisClass.mobile:
            thisClass.mobile = thisItter# type: ignore
        elif col == thisClass.last_name:
            thisClass.last_name = thisItter# type: ignore
        elif col == thisClass.saler_name:
            thisClass.saler_name = thisItter# type: ignore
        elif col == thisClass.seller_id:
            thisClass.seller_id = thisItter# type: ignore
    return thisClass
############################################################################################
class salary_requires():
    invoices = "فاکتور ها"
    targets = "تارگت ها"
    startDate = "تاریخ شروع"
    endDate = "تاریخ پایان"

############################################################################################
class sale_hesabro_payment():
    id = "id"	
    factor_date = "factor_date"
    seller_id = "seller_id"
    seller_name = "name"
    branch_id = "branch_id"
    branch = "b_name_1"
    mobile = "username"
    last_name = "last_name"
    first_name = "first_name"
    factor_amount = "factor_amount"
    payment = "payment"
    cart = "cart"
    cash = "cash"
    bank_transfer = "bank_transfer"
    coin = "coin"
    check_out = "check_out" # تسویه بستانکاری
    discount_code = "discount_code"
    to_other_person = "to_other_person"
    check = "check"
    saleTime = "factor_Time"
def get_sale_hesabro_payment_index(df):
    thisIndex = -1
    thisClass = sale_hesabro_payment()
    for col in df.columns:
        thisIndex += 1
        if col == thisClass.id:
            thisClass.id = thisIndex # type: ignore  
        elif col == thisClass.factor_amount:
            thisClass.factor_amount = thisIndex # type: ignore    
        elif col == thisClass.cart:
            thisClass.cart= thisIndex # type: ignore    
        elif col == thisClass.cash:
            thisClass.cash = thisIndex # type: ignore    
        elif col == thisClass.bank_transfer:
            thisClass.bank_transfer = thisIndex # type: ignore    
        elif col == thisClass.coin:
            thisClass.coin = thisIndex # type: ignore    
        elif col == thisClass.check_out:
            thisClass.check_out = thisIndex # type: ignore    
        elif col == thisClass.factor_date:
            thisClass.factor_date = thisIndex # type: ignore    
        elif col == thisClass.seller_id:
            thisClass.seller_id = thisIndex # type: ignore    
        elif col == thisClass.seller_name:
            thisClass.seller_name = thisIndex # type: ignore    
        elif col == thisClass.branch_id:
            thisClass.branch_id = thisIndex # type: ignore    
        elif col == thisClass.branch:
            thisClass.branch = thisIndex  # type: ignore    
        elif col == thisClass.mobile:
            thisClass.mobile =thisIndex  # type: ignore   
        elif col == thisClass.last_name:
            thisClass.last_name = thisIndex  # type: ignore    
        elif col == thisClass.first_name:
            thisClass.first_name = thisIndex # type: ignore    
        elif col == thisClass.payment:
            thisClass.payment = thisIndex # type: ignore    
        elif col == thisClass.discount_code:
            thisClass.discount_code = thisIndex # type: ignore    
        elif col == thisClass.to_other_person:
            thisClass.to_other_person = thisIndex # type: ignore    
        elif col == thisClass.check:
            thisClass.check = thisIndex # type: ignore    
        elif col == thisClass.saleTime:
            thisClass.saleTime = thisIndex # type: ignore   
    return thisClass
############################################################################################
class birthday_output_cols():
    mobile = "موبایل"
    name = "نام و نام خانوادگی"
    birthday = "تاریخ تولد"
def get_index_birthday_output_cols(df):
    thisItter = -1
    thisClass = birthday_output_cols()
    for col in df.columns:
        thisItter += 1
        if col == thisClass.mobile:
            thisClass.mobile = thisItter
        elif col == thisClass.name:
            thisClass.name = thisItter
        elif col == thisClass.birthday:
            thisClass.birthday = thisItter
    return thisClass



############################################################################################
############################################################################################
############################################################################################
############################################################################################
############################################################################################