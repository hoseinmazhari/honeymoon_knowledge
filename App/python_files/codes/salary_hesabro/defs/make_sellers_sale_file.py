
import os, sys,pandas as pd

# parent = os.path.abspath('.')
# sys.path.insert(1, parent)
from python_files.settings_python.app_structures import  _make_farsi_text,getIndexTj,tjCol
from python_files.settings_python import printProgress as prgs
# from main import _make_farsi_text
# from main import * 


def make_seller_SaleFile(dfData,shiftWork): #,df_detailes,dfExclusiveBite
    tjIndex = getIndexTj(dfData)
    
    print(_make_farsi_text("برنامه در حال محاسبه فروش هر مشاور در تمام شعب می باشد"))
    print()
    # dfexclusive= pd.DataFrame()
    # dfnonExclusive= pd.DataFrame()
    dfCheckout=pd.DataFrame()
    ls_Checkout = []
    l = len(dfData)
    while len(dfData):
        
        this_iter = l-len(dfData)
        seller_id= dfData.iloc[0,tjIndex.seller_id]
        seller_name= dfData.iloc[0,tjIndex.seller_name]
        prgs.printProgressBar(this_iter, l, prefix = 'Progress:', suffix = f' - this procces is  {_make_farsi_text(seller_name)}', length = 25)
        dfseller_name = dfData.loc[dfData[tjCol.seller_id]==seller_id]
        # df_seller_nameDetailedSales=df_detailes.loc[df_detailes[frCol.seller_name]==seller_name]
        while len(dfseller_name):
            
     
            branch_id = dfseller_name.iloc[0,tjIndex.branch_id]
            branch = dfseller_name.iloc[0,tjIndex.branch]
            dfBranch= dfseller_name.loc[dfseller_name[tjCol.branch_id]==branch_id]
            
           
            Cash = int(dfBranch[tjCol.Cash].sum())
            earnest = int(dfBranch[tjCol.earnest].sum())
            tasvieBaMarjooe = int(dfBranch[tjCol.tasvieBaMarjooe].sum())
            Deposit = int(dfBranch[tjCol.Deposit].sum())
            transitional = int(dfBranch[tjCol.transitional].sum())
            to_other_person = int(dfBranch[tjCol.to_other_person].sum())
            check = int(dfBranch[tjCol.check].sum())
            Received = Cash+earnest+tasvieBaMarjooe+Deposit+transitional+check + to_other_person
            
            
            ls_Checkout.append({tjCol.branch:branch,tjCol.branch_id:branch_id,tjCol.seller_name:seller_name,tjCol.seller_id:seller_id,
                            tjCol.Received:Received,tjCol.saleTime:shiftWork
                            }) # type: ignore
                               
                
            dfseller_name = dfseller_name.loc[dfseller_name[tjCol.branch]!=branch]
        
        dfData = dfData.loc[dfData[tjCol.seller_name]!=seller_name]
    prgs.printProgressBar(l, l, prefix = 'Progress:', suffix = f'Complete', length = 25)
    dfCheckout = pd.DataFrame(ls_Checkout)
    return dfCheckout