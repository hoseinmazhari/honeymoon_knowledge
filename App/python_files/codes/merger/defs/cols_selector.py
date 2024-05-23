import os, sys

# parent = os.path.abspath('.')
# sys.path.insert(1, parent)
from python_files.settings_python.app_structures import _make_farsi_text,tjCol,sale_hesabro_payment,frCol
# from main import _make_farsi_text
# from main import *
def cumulative_cols(df_cumulativeSales):
  df_cumulativeSales[tjCol.check]=0
  this_ls = []
  for i in range(len(df_cumulativeSales)):
    this_ls.append(0)
  df_cumulativeSales.loc[:, tjCol.check] =this_ls
  df_cumulativeSales.loc[:, tjCol.to_other_person]= this_ls
  df_cumulativeSales = df_cumulativeSales[[tjCol.saleId,tjCol.factor_date,tjCol.branch,tjCol.branch_id,tjCol.seller_name,
                                          tjCol.seller_id,tjCol.mobile,tjCol.TotalOne,tjCol.chargeUse,
                                          tjCol.buyer,
                                          tjCol.Deposit,
                                          tjCol.Cash,
                                          tjCol.earnest,tjCol.tasvieBaMarjooe,
                                          tjCol.Discount,
                                          tjCol.to_other_person,
                                          tjCol.check,
                                          tjCol.transitional,tjCol.saleTime]]
  return df_cumulativeSales
  
def cumulative_hesabro_cols(df_cumulativeSales_hesabro):
    payCol = sale_hesabro_payment()
    df_cumulativeSales_hesabro[tjCol.buyer]=df_cumulativeSales_hesabro[payCol.first_name] + " " + df_cumulativeSales_hesabro[payCol.last_name]
    df_cumulativeSales_hesabro = df_cumulativeSales_hesabro[[payCol.id,payCol.factor_date,payCol.branch,
                                                             payCol.branch_id,payCol.seller_name,payCol.seller_id,
                                                             payCol.mobile, tjCol.buyer,
                                                             payCol.factor_amount,payCol.coin,
                                                             payCol.cart,
                                                             payCol.cash,payCol.check_out,payCol.bank_transfer,
                                                             payCol.discount_code,
                                                             
                                                             payCol.check,
                                                             payCol.to_other_person,
                                                             payCol.saleTime]]
    df_cumulativeSales_hesabro[tjCol.earnest]=0
            
    df_cumulativeSales_hesabro=df_cumulativeSales_hesabro.rename(columns={payCol.id:tjCol.saleId ,
                                                payCol.factor_date:tjCol.factor_date,payCol.branch:tjCol.branch,payCol.branch_id:tjCol.branch_id,payCol.seller_name:tjCol.seller_name,
                                               payCol.seller_id:tjCol.seller_id,payCol.mobile:tjCol.mobile,
                                               payCol.factor_amount:tjCol.TotalOne,payCol.coin:tjCol.chargeUse,

                                            payCol.cart:tjCol.Deposit,
                                            payCol.cash:tjCol.Cash,payCol.check_out:tjCol.tasvieBaMarjooe,payCol.bank_transfer:tjCol.transitional,
                                            payCol.discount_code: tjCol.Discount,
                                            payCol.to_other_person:tjCol.to_other_person,
                                            payCol.check: tjCol.check,
                                            payCol.saleTime:tjCol.saleTime})
            # df_cumulativeSales_hesabro.to_excel("تجمیعی فروش حسابرو بعد از تغییر نام ستون ها.xlsx",index=False)
    return df_cumulativeSales_hesabro

def detail_sale_col(df_detailedSales):
    df_detailedSales = df_detailedSales[[frCol.factor_date,frCol.saleId,frCol.branch,tjCol.branch_id,frCol.seller_name,
                                         tjCol.seller_id,frCol.merchandise,frCol.AmountOne,frCol.quantity,frCol.summation,
                                         frCol.idCode]]
