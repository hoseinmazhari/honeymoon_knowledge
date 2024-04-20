
import os, sys, pandas as pd, datetime,time

parent = os.path.abspath('.')
sys.path.insert(1, parent)

from .defs import sale_each_employe, concat_sale_with_target as cswt,commission
# from codes.salary_new.defs import concat_sale_with_target as cswt
# from codes.salary_new.defs import commission 
from python_files.settings_python.app_structures import export_path, mediaName, _make_farsi_text, prtLines, getDateTimeForFileName, getIndexTj,myDataType_names, tjCol, condition, loadData, yearDetail, monthCol, monthsSelector
# from main import * 
from ..merger.defs import cols_selector as csr
# import merger.defs.cols_selector  as csr
# from .defs import RegistrarChecker as RgsChk
from .defs import make_registrar_sale_file as mrsf
# from python_files.settings_python import DateJuToJa
class chechOutCol():
    branch = tjCol.branch
    saleId = tjCol.saleId
    Registrar = tjCol.Registrar
    Received = tjCol.Received
    shiftWork = condition.shiftWork
    exclusiveReceived = "دریافتی نیش انحصاری"
    nonExclusiveReceived = "دریافتی نیش تجاری"
class chechOutIndex():
    branch = 0
    saleId = 1
    Registrar = 2
    Received = 3
    shiftWork = 4
    exclusiveReceived = 5
    nonExclusiveReceived = 6

class saleMergedWithTargetCol():
    branch = 0
    Registrar = 1
    Received = 2
    shiftWork = 3
    exclusivePercent= 4
    nonExclusivePercent = 5
    commission = 6


class invoicesMergeCol():
    branch=chechOutCol.branch
    # saleid= tjCol.saleId
    Registrar = chechOutCol.Registrar
    shiftWork = chechOutCol.shiftWork
    Received = chechOutCol.Received
    exclusiveReceived = chechOutCol.exclusiveReceived
    nonExclusiveReceived  = chechOutCol.nonExclusiveReceived
    
def getIndexInvoicesMerge(df):
    thisClass = invoicesMergeCol()
    thisIndex = -1
    for col in df.columns:
        thisIndex += 1
        if col == thisClass.branch:
            thisClass.branch = thisIndex # type: ignore
        elif col == thisClass.exclusiveReceived:
            thisClass.exclusiveReceived = thisIndex # type: ignore
        elif col == thisClass.nonExclusiveReceived:
            thisClass.nonExclusiveReceived = thisIndex # type: ignore
        elif col == thisClass.Received:
            thisClass.Received = thisIndex # type: ignore
        elif col == thisClass.Registrar:
            thisClass.Registrar = thisIndex # type: ignore
        elif col == thisClass.shiftWork:
            thisClass.shiftWork = thisIndex # type: ignore
    return thisClass

# def getIndexConcatSaleWithTarget(df):
#     thisIndex= -1
#     thisClass = concatSaleWithTargetCol()
#     for col in df.columns:
#         thisIndex += 1
#         if col == thisClass.branch:
#             thisClass.branch = thisIndex # type: ignore
#         elif col == thisClass.commission:
#             thisClass.commission = thisIndex # type: ignore
#         elif col == thisClass.commissionExclusive:
#             thisClass.commissionExclusive = thisIndex # type: ignore
#         elif col == thisClass.commission_nonExclusive:
#             thisClass.commission_nonExclusive = thisIndex # type: ignore
#         elif col == thisClass.exclusivePercent:
#             thisClass.exclusivePercent = thisIndex # type: ignore
#         elif col == thisClass.exclusiveReceived:
#             thisClass.exclusiveReceived = thisIndex # type: ignore
#         elif col == thisClass.nonExclusivePercent:
#             thisClass.nonExclusivePercent = thisIndex # type: ignore
#         elif col == thisClass.nonExclusiveReceived:
#             thisClass.nonExclusiveReceived = thisIndex # type: ignore
#         elif col == thisClass.Received:
#             thisClass.Received = thisIndex # type: ignore
#         elif col == thisClass.Registrar:
#             thisClass.Registrar = thisIndex # type: ignore
#         elif col == thisClass.shiftWork:
#             thisClass.shiftWork = thisIndex # type: ignore
#     return thisClass



def calculateSaleEachSaler(dfData):
    tjIndex = getIndexTj(dfData)
    lsDatas =[]
    while len(dfData):
        Registrar_id = dfData.iat[0,tjIndex.Registrar_id]
        dfRegistrar = dfData.loc[dfData[tjCol.Registrar_id]==Registrar_id]
        Registrar = dfRegistrar.iat[0,tjIndex.Registrar]
        Cash = int(dfRegistrar[tjCol.Cash].sum())
        earnest = int(dfRegistrar[tjCol.earnest].sum())
        tasvieBaMarjooe = int(dfRegistrar[tjCol.tasvieBaMarjooe].sum())
        Deposit = int(dfRegistrar[tjCol.Deposit].sum())
        transitional = int(dfRegistrar[tjCol.transitional].sum())
        check = int(dfRegistrar[tjCol.check].sum())
        to_other_person = int(dfRegistrar[tjCol.to_other_person].sum())
        Received = Cash+earnest+tasvieBaMarjooe+Deposit+transitional+check+to_other_person
        
        
        lsDatas.append({tjCol.Registrar:Registrar,tjCol.Registrar_id:Registrar_id,
                        tjCol.Received:Received
                        })
                    
        dfData = dfData.loc[dfData[tjCol.Registrar_id]!=Registrar_id]
    dfData = pd.DataFrame(lsDatas)
    return dfData
    # dfData.to_excel("فروش تمامی مشاوران.xlsx",index=False)
def make_file(df,thisFileName,xlsxFileNum):
    xlsxFileNum += 1
    # thisFileName = f'جمع فروش هر مشاور.xlsx'
    thisFileName = f"{xlsxFileNum}- {thisFileName}"
    df.to_excel(thisFileName,index = False)
    prtLines(2)
    print(_make_farsi_text(f"{thisFileName} استخراج و ذخیره شد"))
    prtLines(2)
    return xlsxFileNum
def salary(df_cumulativeSales, df_targets, startDate, endDate):
        xlsxFileNum = 0
        appPath = os.getcwd()
        selectedOption="0"
        while len(selectedOption)<5:
            selectedOption = "0" + selectedOption

        # start coding
        #
        folderName = f"{selectedOption}- حقوق مشاوران {getDateTimeForFileName()}"
        prtLines(2)
        print(_make_farsi_text("انتخاب شما: "))
        print(_make_farsi_text(folderName))
        thisPath = os.getcwd()
        thisPath = f"{thisPath}/{mediaName}"
        os.chdir(thisPath)
        prtLines(2)
        print(_make_farsi_text(": انتقال مسیر خروجی فایل های به"))
        print(thisPath)
        try:
            os.mkdir(export_path)
        except:
            pass
        thisPath = f"{thisPath}/{export_path}"
        os.chdir(thisPath)
        prtLines(2)
        print(_make_farsi_text(": انتقال مسیر خروجی فایل های به"))
        print(thisPath)
        try:
            os.mkdir(folderName)
        except:
            pass
        thisPath = f"{thisPath}/{folderName}"
        os.chdir(thisPath)
        prtLines(2)
        print(_make_farsi_text(": انتقال مسیر خروجی فایل های به"))
        print(thisPath)
        
        fileTypes= myDataType_names.hesabro
        # fileTypes= myDataType_names.cumulativeSales
        # df_cumulativeSales = loadData(fileTypes,folderName)
        # df_cumulativeSales= df_cumulativeSales[[tjCol.history,tjCol.branch,tjCol.Registrar,tjCol.Cash,tjCol.mobile,
        
        #                                         tjCol.earnest,tjCol.Deposit,tjCol.tasvieBaMarjooe,
        #                                         tjCol.transitional,tjCol.saleId,tjCol.saleTime,tjCol.idBranch]]
        df_cumulativeSales = csr.cumulative_hesabro_cols(df_cumulativeSales)
        xlsxFileNum += 1
        thisFileName = f"فاکتورهای {fileTypes} پس از اصلاح نام ستون ها.xlsx"
        thisFileName = f"{xlsxFileNum}- {thisFileName}"
        df_cumulativeSales.to_excel(thisFileName,index = False)
        
        # dfInvoices.to_excel("dfInvoices.xlsx",index=False)
        # prtLines(1)
        prtLines(2)
        print(_make_farsi_text(f"{thisFileName} استخراج و ذخیره شد"))
        prtLines(2)
        # print(thisPath)
        # برگشت به پوشه مبدا
        # os.chdir(thisPath)
        
        # بارگزاری فایل های مرجوعی 
        # print(_make_farsi_text("لطفا فایل ها یا پوشه مربوط به مرجوعی مورد نظر خود را انتخاب فرمایید"))
        # fileType= myDataType_names.returnedMerchandise
        
        # dfReturns=loadData(fileType,folderName)
        # dfReturns.to_excel("مرجوعی ها.xlsx",index=False)
        

        # انتخاب ماه برای محاسبه حقوق
        # print(_make_farsi_text("جهت ادامه باید یکی از ماه های زیر را انتخاب فرمایید"))
         # "01":{monthCol.month:"فروردین", monthCol.Deposit:0, monthCol.Cash:0, monthCol.earnest:0, monthCol.Received:0},
        # for months in yearDetail.month:
        #     print(f"{months}: {_make_farsi_text(yearDetail.month[months][monthCol.month])}")
        
        # monthNum = input(_make_farsi_text(" :  لطفا عدد کنار ماه درخواستی را کامل وارد نمایید مثل 01 برای انتخاب فروردین"))
        # # df_detailedSales.to_excel("all.xlsx",index=False)
        # prtLines(2)
        # year ="1403"
        # startDate = f'{year}{monthsSelector.month[monthNum]["start"]}'
        # endDate = f'{year}{monthsSelector.month[monthNum]["end"]}'
        # endDate = "1402/12/26"
        # endDate = "1401/12/28"
        # فیلتر فایل تجمیعی فروش در تاریخ انتخابی
        dfInvoices =df_cumulativeSales.loc[df_cumulativeSales[tjCol.history]>=startDate]
        dfInvoices = dfInvoices.loc[dfInvoices[tjCol.history]<=endDate]
        xlsxFileNum += 1
        thisFileName = f'فاکتورهای {startDate.replace("/","-")} تا {endDate.replace("/", "-")}.xlsx'
        thisFileName = f"{xlsxFileNum}- {thisFileName}"
        dfInvoices.to_excel(thisFileName,index = False)
        time.sleep(1)
        dfInvoices = pd.read_excel(thisFileName)
        prtLines(2)
        print(_make_farsi_text(f"{thisFileName} استخراج و ذخیره شد"))
        prtLines(2)
        # برگشت به پوشه مبدا
        # os.chdir(this_export_path)
        df_SaleEachSaler = calculateSaleEachSaler(dfInvoices)
        xlsxFileNum += 1
        thisFileName = f'جمع فروش هر مشاور.xlsx'
        thisFileName = f"{xlsxFileNum}- {thisFileName}"
        df_SaleEachSaler.to_excel(thisFileName,index = False)
        prtLines(2)
        print(_make_farsi_text(f"{thisFileName} استخراج و ذخیره شد"))
        prtLines(2)
            
        # fileTypes = myDataType_names.nish
        # dfExclusiveBite = loadData(fileTypes,folderName)
        # dfExclusiveBite.to_excel("انحصاری ها.xlsx",index=False)
        # prtLines(2)
        # # برگشت به پوشه مبدا
        # os.chdir(thisPath)

        # انتخاب فایل تارگت ماه منتخب
        # print(_make_farsi_text("لطفا فایل تارگت مربوط به درصد ها را انتخاب نمایید"))
        
        # fileTypes = myDataType_names.targets
        # df_targets= loadData(fileTypes,folderName)
        # df_targets.to_excel("تارگت ها.xlsx",index=False)
        # exportPath = os.getcwd()

        # deductionPercent = int(input(_make_farsi_text(": لطفا در صد قابل کسر بابت عدم دستیابی به تارگت را وارد نمایید -")))

        # tjIndex = getIndexTj(df_detailedSales)
        # اندیس گزاری برای ستون های فایل فروش
        # frIndex = getIndexFr(df_detailedSales)
        # year = df_detailedSales.iloc[0,tjIndex.history][:4]
        # انتخاب سال از اولین ردیف دیتای فروش
        # year = df_detailedSales.iloc[0,frIndex.history][:4] # type: ignore
        # year = input(_make_farsi_text("- لطفا سال مربوط به حقوق را وارد نمایید : "))
        # انتخاب ماه
        # monthName = f'{year}{monthsSelector.month[monthNum]["name"]}'
        # تاریخ جاری برای ایجاد پوشه
        # todayDate = DateJuToJa.todaydate()
        # # جایگزینی / با - برای امکان استفاده از تاریخ
        # todayDate = todayDate.replace("/","-")


        # thisTime = str(datetime.datetime.now())
        # thisTime = thisTime[10:]
        # thisTime = thisTime[:9]
        # thisTime = thisTime.replace(":","-")

        # # تعین مسیر خروجی
        # exportPath=DateJuToJa.getDateTimeForFileName()
        #{monthNum}-{monthName}
        # try:
        #     # ساخت پوشه تولید خروجی و تغییر مسیر به آن
        #     os.mkdir(exportPath)
        #     os.chdir(exportPath)
        # except:
        #     # در صورتی که پوشه خروجی وجود دارد تغییر مسیر به آن
        #     os.chdir(exportPath)
        # prtLines(4)
        # print(_make_farsi_text("برنامه در حال اصلاح ثبت کننده های فاکتور ها می باشد لطفا منتظر بمانید"))
        # # اصلاح ثبت کننده های کالا ها در فایل فروش با استفاده از ثبت کننده فایل تجمیعی 
        # dfInvoices = RgsChk.RegistrarEditter(df_detials=df_detailedSales,dfInvoices=df_cumulativeSales)
        # df = RgsChk.test(df_cumulativeSales)
        # df.to_excel("test tj.xlsx",index=False)
        # ساخت فایل ریز دریافتی ها از فایل های انتخاب شده بدون در نظر گرفتن ماه انتخاب شده
        # df = RgsChk.test(dfInvoices)
        # df.to_excel("کل ریز دریافتی ها از ابتدای سال تا تاریخ نهایی فایل.xlsx",index=False)
        
        # بدست آوردن اولین و آخرین روز از ماه انتخاب شده
        # df = RgsChk.test(dfInvoices)
        # df.to_excel(f"ریز دریافتی های هر مشاور در {monthName}ماه.xlsx",index=False)
        # فیلتر فایل فروش در بازه ماه انتخابی
        # df_detailedSales= df_detailedSales.loc[df_detailedSales[frCol.history]>=startDate]
        # df_detailedSales= df_detailedSales.loc[df_detailedSales[frCol.history]<=endDate]

        # فیلتر فایل مرجوعی در بازه ماه انتخابی
        # dfReturns = dfReturns.loc[dfReturns[tjCol.history]>=startDate]
        # dfReturns = dfReturns.loc[dfReturns[tjCol.history]<=endDate]

        # prtLines(3)
        # os.chdir(thisPath)
        
        # nonExclusiveData = pd.read_excel(mainPath+"/base Datas/012-nonExclusives for filter salers.xlsx")
        # prtLines(3)
        # myItems= []
        # Mylist = []
        # print(_make_farsi_text("برنامه در حال استخراج لیست پیور پرفیوم ها و پک ها  و جدا سازی از عطرها میباشد منتظر بمانید"))
        # Counter = 0
        

        # جدا سازی رکورد های مربوط به شیفت صبح از فایل تجمیعی فروش
        dfAmInvoices = dfInvoices.loc[dfInvoices[tjCol.saleTime]<=condition.saleTime]
        # dfAmDetailedSales = df_detailedSales.loc[df_detailedSales[frCol.saleTime]<=condition.saleTime]
        
        # جدا سازی رکورد های مربوط به شیفت عصر از فایل تجمیعی فروش
        dfPmInvoices = dfInvoices.loc[dfInvoices[tjCol.saleTime]>condition.saleTime]
        # dfPmDetailedSales = df_detailedSales.loc[df_detailedSales[frCol.saleTime]>condition.saleTime]
        
        dfCheckoutAm=mrsf.makeRegistrarSaleFile(dfAmInvoices,condition.saleAm)#,df_detailedSales,dfExclusiveBite
        dfCheckoutPm=mrsf.makeRegistrarSaleFile(dfPmInvoices,condition.salePm)#,df_detailedSales,dfExclusiveBite
        thisFileName = "فروش شیفت عصر.xlsx"
        xlsxFileNum = make_file(dfCheckoutPm,thisFileName,xlsxFileNum)
        # dfCheckoutPm.to_excel(,index=False)
        thisFileName = "فروش شیفت صبح.xlsx"
        xlsxFileNum = make_file(dfCheckoutAm,thisFileName,xlsxFileNum)
        # dfCheckoutAm.to_excel(,index=False)
        lsCheckOut = []
        lsCheckOut.append(dfCheckoutAm)
        lsCheckOut.append(dfCheckoutPm)
        # df_ans = makeRegistrarSaleFile(df_exclusive,df_nonExclusive,df_targets,dfInvoices)
        
        dfCheckout = pd.concat(lsCheckOut)
        
        # xlsxFileNum += 1
        thisFileName = f"فروش هر مشاور در هر شعبه و شیفت.xlsx"
        xlsxFileNum = make_file(dfCheckout, thisFileName, xlsxFileNum)
        # thisFileName = f"{xlsxFileNum}- {thisFileName}"
        # dfCheckout.to_excel(thisFileName,index = False)
        
        # از این قسمت فقط برای تولید فایل فروش هر مشاور استفاده می شود
        
        df_emp_sale = sale_each_employe.sale_employes(dfCheckout)
        thisFileName = "فروش هر مشاور در هر شعبه.xlsx"
        xlsxFileNum = make_file(df_emp_sale, thisFileName, xlsxFileNum)
        # df_emp_sale.to_excel(,index=False)

        
        
        
        # prtLines(4)
        # print(_make_farsi_text("ادغام فروش مشاوران در هر شعبه و شیفت با تارگت همان شعبه و شیفت"))
        
        df_ConcatWithTargets= cswt.concatWithTargets(dfCheckout,df_targets)
        # xlsxFileNum += 1
        thisFileName = f"ادغام فروش با تارگت {folderName}.xlsx"
        xlsxFileNum = make_file(df_ConcatWithTargets, thisFileName, xlsxFileNum)
        # thisFileName = f"{xlsxFileNum}- {thisFileName}"
        # df_ConcatWithTargets.to_excel(thisFileName,index = False)
        

        # xlsxFileNum += 1
        
        df_final = commission.commission(df_ConcatWithTargets,df_targets)
        thisFileName = f"فایل نهایی برای مشاوران اصلی در {startDate.replace('/','-')} تا {endDate.replace('/', '-')} ماه.xlsx"
        xlsxFileNum = make_file(df_final, thisFileName, xlsxFileNum)
        # thisFileName = f"{xlsxFileNum}- {thisFileName}"
        # df_final.to_excel(thisFileName,index = False
        prtLines()
        print(_make_farsi_text("عملیات محاسبه حقوق تکمیل شد"))
        thisPath = os.getcwd()
        os.chdir(appPath)
        # xlsxFileNum -= 1
        return f"{thisPath}/{xlsxFileNum}- {thisFileName}"

# salary()

