import os, sys

parent = os.path.abspath('.')
sys.path.insert(1, parent)

from main import _make_farsi_text
from main import *
from codes.merger.defs import id_setter_hamyar as ish
def col_for_detail(folderName):
  
    thisPath = os.getcwd()
    print(_make_farsi_text("در قدم اول فایل های تجمیعی فروش همیار سیستم را انتخاب نمایید"))
    fileTypes= myDataType_names.cumulativeSales
    df_cumulativeSales = loadData(fileTypes,folderName)
    
    df_cumulativeSales= df_cumulativeSales[[tjCol.saleId,tjCol.history,tjCol.branch,tjCol.idBranch,tjCol.Registrar,tjCol.Registrar_id,tjCol.mobile,
                                        tjCol.buyer,
                                        tjCol.earnest,tjCol.Deposit,tjCol.Cash,tjCol.tasvieBaMarjooe,
                                        tjCol.transitional,tjCol.saleTime]]
    # df_cumulativeSales.to_excel("تجمیعی فروش های همیار سیستم.xlsx",index=False)
    prtLines(3)
    os.chdir(thisPath)
    print(_make_farsi_text("در این مرحله فایل های فروش همیار سیستم را انتخاب نمایید"))
    fileTypes = myDataType_names.detailedSales
    df_detailedSales = loadData(fileTypes,folderName)
    # payCol = sale_hesabro_payment()
    df_detailedSales = df_detailedSales[[frCol.saleId,frCol.history,frCol.branch,frCol.Registrar,frCol.mobile,frCol.buyer,
                                    frCol.merchandise,frCol.idCode,frCol.AmountOne,frCol.quantity,frCol.TotalOne
                                    ]]
    # tjCol.earnest,,tjCol.saler
    df_detailedSales[tjCol.Registrar_id]=0
    df_detailedSales[tjCol.idBranch]=0
    
    
      
    df_detailedSales = ish.seller_id_setter(df_cumulativeSales,df_detailedSales)
    df_detailedSales = ish.branch_id_setter(df_cumulativeSales,df_detailedSales)
    df_detailedSales.to_excel(" فروش بعد از اضافه تمودن نام ستون ها.xlsx",index=False)