# جهت اجرای این کد ابتدا باید فایل های تجمیعی همیار و حسابرو ادغام شوند سپس
# به فایل ادغام شده ستون 
# thisRow
# اضافه شود و شماره گزاری شود
# سپس این فایل با لیست کل مشتریان که از حسابرو استخراج شده طی فرایند انتخاب و ادغام می شود
import os, sys

parent = os.path.abspath('.')
sys.path.insert(1, parent)

from main import _make_farsi_text
from main import *
from codes.merger.defs import cols_selector as csr
from codes.merger.defs import equaller as eqa
from codes.merger.defs import end_hamyar_factors as ehf
class merged_cumulative():
  saleTime = tjCol.saleTime
  transitional = tjCol.transitional
  check = tjCol.check
  Discount = tjCol.Discount
  tasvieBaMarjooe = tjCol.tasvieBaMarjooe
  earnest = tjCol.earnest
  Cash = tjCol.Cash
  Deposit = tjCol.Deposit
  buyer = tjCol.buyer
  chargeUse = tjCol.chargeUse
  TotalOne = tjCol.TotalOne
  mobile = tjCol.mobile
  Registrar_id = tjCol.Registrar_id
  Registrar = tjCol.Registrar 
  idBranch = tjCol.idBranch
  branch = tjCol.branch
  history = tjCol.history
  saleId = tjCol.saleId
class customerCols():
  id = "آیدی"
  customer_id = "آیدی خریدار"
  cusomer = "نام و نام خانوادگی"
  gender = "جنسیت"
  birthday = "تاریخ تولد"
  passport_id = "کدملی-پاسپورت"
  email = "ایمیل"
  mobile = "موبایل"
def get_index_customers(df):
  thisItter = -1
  thisClass = customerCols()
  for col in df.columns:
    thisItter += 1
    if col == thisClass.id:
      thisClass.id = thisItter # type: ignore
    elif col == thisClass.cusomer:
      thisClass.cusomer = thisItter # type: ignore
    elif col == thisClass.gender:
      thisClass.gender = thisItter # type: ignore
    elif col == thisClass.birthday:
      thisClass.birthday = thisItter # type: ignore
    elif col == thisClass.passport_id:
      thisClass.passport_id = thisItter # type: ignore
    elif col == thisClass.email:
      thisClass.email = thisItter # type: ignore
    elif col == thisClass.mobile:
      thisClass.mobile == thisItter # type: ignore
  return thisClass
def merge_cumulative_sale_with_customers(folderName):
  thisPath = os.getcwd()
  xlsxItter = 1
  print(_make_farsi_text("در این مرحله فایل های حسابرو را انتخاب نمایید"))
  fileTypes = myDataType_names.hesabro
  df_customers_hesabro = loadData(fileTypes,folderName)
  # df_customers_hesabro = csr.cumulative_hesabro_cols(df_customers_hesabro)
  
  # file_name = f"فایل مشخصات افراد در حسابرو"
  # xlsxItter = df_to_xlsx_and_return_itter(df_customers_hesabro,file_name,xlsxItter)
  
  prtLines(3)
  os.chdir(thisPath)
  print(_make_farsi_text("در این مرحله فایل های همیار سیستم را انتخاب نمایید"))
  fileTypes= myDataType_names.cumulativeSales
  df_cumulativeSales = loadData(fileTypes,folderName)
  # df_cumulativeSales= csr.cumulative_cols(df_cumulativeSales)
  
  # file_name = f"تجمیعی فروش همیار"
  # xlsxItter = df_to_xlsx_and_return_itter(df_cumulativeSales,file_name,xlsxItter)
  
  ls_ans = []
  tjIndex = getIndexTj(df_cumulativeSales)
  customer_index = get_index_customers(df_customers_hesabro)
  
  l = len(df_cumulativeSales)
  # جهت اجرای این کد ابتدا باید فایل های تجمیعی همیار و حسابرو ادغام شوند سپس
  # به فایل ادغام شده ستون 
  # thisRow
  # اضافه شود و شماره گزاری شود
  # سپس این فایل با لیست کل مشتریان که از حسابرو استخراج شده طی فرایند انتخاب و ادغام می شود
  print(f"count is: {l}")
  print()
  while len(df_cumulativeSales):
    thisRow = df_cumulativeSales.iat[0,1]
    df_test = df_cumulativeSales.loc[df_cumulativeSales["thisRow"]== thisRow]
    saleTime = df_test.iat[0, tjIndex.saleTime]
    transitional = df_test.iat[0, tjIndex.transitional]
    check = df_test.iat[0, tjIndex.check]
    Discount = df_test.iat[0, tjIndex.Discount]
    tasvieBaMarjooe = df_test.iat[0, tjIndex.tasvieBaMarjooe]
    earnest = df_test.iat[0, tjIndex.earnest]
    Cash = df_test.iat[0, tjIndex.Cash]
    Deposit = df_test.iat[0, tjIndex.Deposit]
    buyer = df_test.iat[0, tjIndex.buyer]
    chargeUse =df_test.iat[0, tjIndex.chargeUse]
    TotalOne = df_test.iat[0, tjIndex.TotalOne]
    Registrar_id = df_test.iat[0, tjIndex.Registrar_id]
    Registrar = df_test.iat[0, tjIndex.Registrar]
    idBranch = df_test.iat[0, tjIndex.idBranch]
    branch = df_test.iat[0, tjIndex.branch]
    history = df_test.iat[0, tjIndex.history]
    saleId = df_test.iat[0, tjIndex.saleId]
    mobile = df_test.iat[0, tjIndex.mobile]
    df_mobile = df_customers_hesabro.loc[df_customers_hesabro[customerCols.mobile]== mobile]
    
    if len(df_mobile):
      gender = df_mobile.iat[0, customer_index.gender]
      birthday = df_mobile.iat[0, customer_index.birthday]
      email = df_mobile.iat[0, customer_index.email]
      if email == "0" or email == 0:
        email = "-"
      passport_id = df_mobile.iat[0, customer_index.passport_id]
      customer_id = df_mobile.iat[0, customer_index.id]
      ls_ans.append({merged_cumulative.saleId : saleId, merged_cumulative.history : history,
        merged_cumulative.branch : branch, merged_cumulative.idBranch : idBranch,
        merged_cumulative.Registrar : Registrar, merged_cumulative.Registrar_id : Registrar_id,
        merged_cumulative.TotalOne : TotalOne, merged_cumulative.chargeUse : chargeUse,
        customerCols.customer_id: customer_id,
        merged_cumulative.buyer : buyer, merged_cumulative.mobile : mobile,
        customerCols.email: email, customerCols.passport_id : passport_id,
        customerCols.gender : gender, customerCols.birthday : birthday,
        merged_cumulative.Deposit : Deposit,
        merged_cumulative.Cash : Cash, merged_cumulative.earnest : earnest,
        merged_cumulative.tasvieBaMarjooe : tasvieBaMarjooe, merged_cumulative.Discount : Discount,
        merged_cumulative.check : check, merged_cumulative.transitional : transitional,
        merged_cumulative.saleTime : saleTime 
                     
                     })
    else:
      ls_ans.append({merged_cumulative.saleId : saleId, merged_cumulative.history : history,
        merged_cumulative.branch : branch, merged_cumulative.idBranch : idBranch,
        merged_cumulative.Registrar : Registrar, merged_cumulative.Registrar_id : Registrar_id,
        merged_cumulative.TotalOne : TotalOne, merged_cumulative.chargeUse : chargeUse,
        customerCols.customer_id: 0,
        merged_cumulative.buyer : buyer, merged_cumulative.mobile : mobile,
        customerCols.email: "-", customerCols.passport_id : 0,
        customerCols.gender : "تعیین نشده", customerCols.birthday : "0000/00/00",
        merged_cumulative.Deposit : Deposit,
        merged_cumulative.Cash : Cash, merged_cumulative.earnest : earnest,
        merged_cumulative.tasvieBaMarjooe : tasvieBaMarjooe, merged_cumulative.Discount : Discount,
        merged_cumulative.check : check, merged_cumulative.transitional : transitional,
        merged_cumulative.saleTime : saleTime })
      
    df_cumulativeSales = df_cumulativeSales.loc[df_cumulativeSales["thisRow"]!= thisRow]
    prgsCounter = l- len(df_cumulativeSales)
    prgs.printProgressBar(prgsCounter, l, prefix = 'Progress:', suffix = 'Complete', length = 25)
    
  dfData = pd.DataFrame(ls_ans)
  # prgs.printProgressBar(l, l, prefix = 'Progress:', suffix = 'Complete', length = 25)
  file_name = f"تجمیعی فروش ادغام شده با مشخصات افراد در حسابرو نهایی"
  xlsxItter = df_to_xlsx_and_return_itter(dfData, file_name, xlsxItter)
