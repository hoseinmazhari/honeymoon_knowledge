import os, sys

parent = os.path.abspath('.')
sys.path.insert(1, parent)

from main import _make_farsi_text
from main import *
from codes.merger.defs import end_hamyar_factors as ehf
from codes.merger.defs import equaller as eqa
def detailedSales(folderName,df_branch_equaller,df_seller_equaller,df_products_equaller):
    thisPath = os.getcwd()
    print(_make_farsi_text("فایل های حسابرو را انتخاب نمایید"))
    fileTypes = myDataType_names.hesabro
    df_detailedSales_hesabro = loadData(fileTypes,folderName)
    # os.chdir(thisPath)
    df_detailedSales_hesabro[frCol.buyer]= df_detailedSales_hesabro[sale_hesabro.first_name] + " " + df_detailedSales_hesabro[sale_hesabro.last_name]
    df_detailedSales_hesabro = df_detailedSales_hesabro[[sale_hesabro.id,sale_hesabro.factor_date,sale_hesabro.branch,sale_hesabro.branch_id,
                                                         sale_hesabro.seller_name,sale_hesabro.seller_id,sale_hesabro.merchandise,sale_hesabro.count,
                                                         sale_hesabro.unit_price,sale_hesabro.sum_price,sale_hesabro.product_id,sale_hesabro.buyer,sale_hesabro.mobile
                                                        ]]
    # tjCol.earnest,,tjCol.saler
    
    
    df_detailedSales_hesabro=df_detailedSales_hesabro.rename(columns={sale_hesabro.id:frCol.saleId,sale_hesabro.factor_date:frCol.history,
                                                                      sale_hesabro.branch:frCol.branch,sale_hesabro.branch_id:tjCol.idBranch,
                                                         sale_hesabro.seller_name:frCol.Registrar,sale_hesabro.seller_id:tjCol.Registrar_id,
                                                         sale_hesabro.merchandise:frCol.merchandise,sale_hesabro.count:frCol.quantity, sale_hesabro.unit_price:frCol.AmountOne,
                                                         sale_hesabro.sum_price:frCol.TotalOne,sale_hesabro.product_id:frCol.idCode,sale_hesabro.mobile:frCol.mobile
                                                                      })
    prtLines(3)
    # df_detailedSales_hesabro.to_excel("hesabro.xlsx",index=False,encoding="utf-8") # type: ignore
    os.chdir(thisPath)
    # df_detailedSales_hesabro.to_csv(" فروش حسابرو بعد از تغییر نام ستون ها.xlsx",index=False)
    print(_make_farsi_text("فایل های همیار سیستم را انتخاب نمایید"))
    fileTypes= myDataType_names.detailedSales
    df_detailedSales = loadData(fileTypes,folderName)
    os.chdir(thisPath)
    # df_detailedSales.to_excel("1-fist hamyar.xlsx",index=False,encoding="utf-8") # type: ignore # type: ignor
    df_detailedSales = ehf.dump_detailSale_on_date(df_detailedSales,df_branch_equaller)
    # df_detailedSales.to_excel("2- on date filter.xlsx",index=False)
    # df_detailedSales.to_csv("فروش های همیار سیستم.xlsx",index=False)
    
    os.chdir(thisPath)
    ls = []
    ls.append(df_detailedSales)
    ls.append(df_detailedSales_hesabro)
    dfData = pd.concat(ls)
    dfData =eqa.branch_eqaller(df_branch_equaller,dfData)
    dfData = eqa.seller_eqaller(df_seller_equaller,dfData)
    dfData = eqa.product_equaller(df_products_equaller,dfData)
    steps = len(dfData)//2
    df1 = dfData[:steps]
    os.chdir(thisPath)
    dfData.to_excel(" فروش ادغام شده ی نهایی.xlsx",index=False)
    # dfData.to_csv(" فروش ادغام شده ی نهایی.xlsx",index=False)
    # correctFiles(dataTypeAddresses.detailedSales,myDataType_names.detailedSales)