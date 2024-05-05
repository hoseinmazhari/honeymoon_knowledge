import os, sys

parent = os.path.abspath('.')
sys.path.insert(1, parent)

from main import _make_farsi_text
from main import *
from codes.merger.defs import cols_selector as csr
from codes.merger.defs import equaller as eqa
from codes.merger.defs import end_hamyar_factors as ehf


def cumulativeSales(folderName,df_branch_equaller,df_seller_equaller):
    thisPath = os.getcwd()
    xlsxItter = 1
    print(_make_farsi_text("در این مرحله فایل های حسابرو را انتخاب نمایید"))
    fileTypes = myDataType_names.hesabro
    df_cumulativeSales_hesabro = loadData(fileTypes,folderName)
    df_cumulativeSales_hesabro = csr.cumulative_hesabro_cols(df_cumulativeSales_hesabro)
    
    file_name = f"تجمیعی فروش حسابرو"
    xlsxItter = df_to_xlsx_and_return_itter(df_cumulativeSales_hesabro,file_name,xlsxItter)
    
    prtLines(3)
    os.chdir(thisPath)
    print(_make_farsi_text("در این مرحله فایل های همیار سیستم را انتخاب نمایید"))
    fileTypes= myDataType_names.cumulativeSales
    df_cumulativeSales = loadData(fileTypes,folderName)
    df_cumulativeSales= csr.cumulative_cols(df_cumulativeSales)
    
    file_name = f"تجمیعی فروش همیار"
    xlsxItter = df_to_xlsx_and_return_itter(df_cumulativeSales,file_name,xlsxItter)
    
    
    df_cumulativeSales = ehf.dump_cumulativeSales_on_date(df_cumulativeSales,df_branch_equaller)
    
    file_name = f"تجمیعی فروش همیار پس از حذف از تاریخ شروع حسابرو"
    xlsxItter = df_to_xlsx_and_return_itter(df_cumulativeSales,file_name,xlsxItter)
    

    ls = []
    ls.append(df_cumulativeSales)
    ls.append(df_cumulativeSales_hesabro)
    df = pd.concat(ls)
    
    file_name = f"تجمیعی فروش ادغام شده ی حسابرو و همیار"
    xlsxItter = df_to_xlsx_and_return_itter(df, file_name, xlsxItter)
    
    dfData =eqa.branch_eqaller(df_branch_equaller,df)
    dfData = eqa.seller_eqaller(df_seller_equaller,dfData)
    
    file_name = f"تجمیعی فروش ادغام شده و یکسان شده ی نهایی"
    xlsxItter = df_to_xlsx_and_return_itter(dfData, file_name, xlsxItter)
    