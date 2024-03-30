import os, sys

parent = os.path.abspath('.')
sys.path.insert(1, parent)

from main import _make_farsi_text
from main import *


from codes.merger.defs import cumulative_sale as cse
from codes.merger.defs import detail_sale as dse
from codes.merger.defs import cumulative_and_detail_for_col as cadfc
from codes.merger.defs import item_selector as isr
from codes.merger.defs import cumulative_sale_with_customers as cswc
def this_def(df_branch_equaller,df_seller_equaller,df_products_equaller):
  print()
  thisPath=os.getcwd()
  thisLoop = True
  this_folderName = "ادغام فایل ها"
  thisCase = [
      "0- خروج از برنامه",
      "1- تجمیعی فروش همیار و حسابرو",
      "2- فروش حسابرو و همیار",
      "3- ایجاد ستون های کد ثبت کننده و کدشرکت برای فایل فروش از فایل تجمیعی و فروش",
      "4- ادغام تجمیعی و فایل مشخصات افراد در حسابرو"
  ]
  
  while thisLoop:
        
        print(_make_farsi_text(this_folderName))
        selected = isr.item_selector(thisPath,thisCase)
        
        folderName = f"{thisCase[int(selected)]} -{this_folderName} {getDateTimeForFileName()}"

        if selected == "0":
            thisLoop =False  
        elif selected == "1":
            cse.cumulativeSales(folderName,df_branch_equaller,df_seller_equaller)
        elif selected == "2":
            dse.detailedSales(folderName,df_branch_equaller,df_seller_equaller,df_products_equaller)
        elif selected == "3":
            cadfc.col_for_detail(folderName)    
        elif selected == "4":
            cswc.merge_cumulative_sale_with_customers(folderName)     
        else:
            print(_make_farsi_text("گزینه صحیحی انتخاب نگردید و برنامه بسته می شود"))
        
        thisLoop = False
        continueLoop = input(_make_farsi_text(" آیا می خواهید ادامه دهید؟ (y/n): "))
        if continueLoop.lower()=="y" or continueLoop=="1":
            thisLoop = True
df_branch_equaller = read_branch_equaller_file()
df_seller_equaller = read_seller_equaller_file()
df_products_equaller = read_products_equaller_file()
this_def(df_branch_equaller,df_seller_equaller,df_products_equaller) # type: ignore