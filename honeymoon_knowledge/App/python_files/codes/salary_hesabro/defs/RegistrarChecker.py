
import os, sys

parent = os.path.abspath('.')
sys.path.insert(1, parent)
from ....settings.app_structures import _make_farsi_text
# from main import _make_farsi_text
# from main import * 

def RegistrarEditter(df_detials,dfInvoices):
   
        
    # print(df_detials)
    # df_detials.to_excel("dfDetails.xlsx",index= False)
    # dfInvoices.to_excel("dfINvoices.xlsx", index =False)
    ls_accouters= ["ياسمن رستمي","مرضيه شريفي","حسين مظهري","آزاده  جمشيدي جم",
            "ياسمن رستمي","مهدي پوراميني","آزاده  جمشيدي جم","حسين مظهري","فرهاد باقري زاده","مهدي پوراميني"]
    dfDataInvoices = dfInvoices.copy()
    ls_invoices=[]
    # ls_details=[]
    tjIndex = getIndexTj(dfDataInvoices)
    frIndex = getIndexFr(df_detials)
    while len(dfDataInvoices):

        branch= dfDataInvoices.iloc[0,tjIndex.branch]
        dfBranchInvoices= dfDataInvoices.loc[dfDataInvoices[tjCol.branch]==branch]
        dfBranchDetails= df_detials.loc[df_detials[frCol.branch]==branch]
        l= len(dfBranchInvoices)
        prtLines(2)
        print(_make_farsi_text(branch))
        for RowNum in range(len(dfBranchInvoices)):
            
            prgsCounter = RowNum#l- len(dfData)
            prgs.printProgressBar(prgsCounter, l, prefix = 'Progress:', suffix = 'Complete', length = 25)
    
            Registrar = dfBranchInvoices.iloc[RowNum,tjIndex.Registrar]
            if Registrar  in ls_accouters:
                # print("*******************")
                # print(Registrar)
                saleId= dfBranchInvoices.iloc[RowNum,tjIndex.saleId]
                
                dfRegistrar = dfBranchDetails.loc[dfBranchDetails[frCol.saleId]==saleId]
                try:
                    trueRegistrar= dfRegistrar.iloc[0, frIndex.Registrar]# برای اینکه اگر ثبت کننده اتومات پیدا نشد دستی اصلاح شود
                except:
                    trueRegistrar= "نا مشخص"# برای اینکه اگر ثبت کننده اتومات پیدا نشد دستی اصلاح شود
                for i in range(len(dfRegistrar)):
                    # for j in range(len(ls_accouters)):
                        if dfRegistrar.iloc[i, frIndex.Registrar]!=Registrar:
                            trueRegistrar = dfRegistrar.iloc[i,frIndex.Registrar]

                            break

                dfBranchInvoices.iat[RowNum,tjIndex.Registrar]=trueRegistrar
        prgs.printProgressBar(l, l, prefix = 'Progress:', suffix = 'Complete', length = 25)
                # print(trueRegistrar)
                # print(dfBranchInvoices.iat[RowNum,tjIndex.Registrar])
        # prgs.printProgressBar(l, l, prefix = 'Progress:', suffix = 'Complete', length = 100)
        # dfBranchInvoices.to_excel(f"{branch}.xlsx",index=False)
        ls_invoices.append(dfBranchInvoices)
        dfDataInvoices=dfDataInvoices.loc[dfDataInvoices[tjCol.branch]!=branch]
    prtLines(2)
    df_ans = pd.DataFrame()
    df_ans = pd.concat(ls_invoices) # type: ignore
    # df_ans.to_excel("newExcel.xlsx",index=False)
    return df_ans




# os.chdir("data")
    
# df_detials = pd.read_excel("df_detials.xlsx")
# dfInvoices=pd.read_excel("dfInvoices.xlsx")
# RegistrarEditter(df_detials,dfInvoices)
# pureDeposit=0
#                 perfumeDeposit=0
#                 perfume_earnest=0# پیش دریفات عطر
#                 pure_earnest=0 # پیش دریافت پیور
#                 perfumeCach=0 # نقدی عطر
#                 pureCach=0# نقدی پیور
#                 perfume_tasvieBaMarjooe=0 # تسویه با مرجوعی عطر
#                 pure_tasvieBaMarjooe=0# تسویه با مرجوعی پیور
#                 perfume_transitional=0
#                 pure_transitional=0
#                 perfume_chargeUse=0
#                 pure_chargeUse=0
#                 perfume_remaining=0
#                 pure_remaining=0
def test(dfData):
    df_ans = pd.DataFrame()
    tjIndex=getIndexTj(dfData)
    while len(dfData):
        Registrar = dfData.iloc[0,tjIndex.Registrar]
        dfRegistrar = dfData.loc[dfData[tjCol.Registrar]==Registrar]
        Cash = int(dfRegistrar[tjCol.Cash].sum())
        earnest = int(dfRegistrar[tjCol.earnest].sum())
        Deposit = int(dfRegistrar[tjCol.Deposit].sum())
        tasvieBaMarjooe = int(dfRegistrar[tjCol.tasvieBaMarjooe].sum())
        transitional = int(dfRegistrar[tjCol.transitional].sum())

        sumOfAll = Cash+earnest+tasvieBaMarjooe+Deposit+transitional
        df_ans= df_ans.append({"مجموع دریافتی ها":sumOfAll,tjCol.Registrar:Registrar,tjCol.Cash:Cash,tjCol.earnest:earnest,tjCol.tasvieBaMarjooe:tasvieBaMarjooe,tjCol.Deposit:Deposit,tjCol.transitional:transitional},ignore_index = True) # type: ignore
        dfData = dfData.loc[dfData[tjCol.Registrar]!=Registrar]
    
    return df_ans