
import os, sys,pandas as pd

parent = os.path.abspath('.')
sys.path.insert(1, parent)
from python_files.settings_python.app_structures import  _make_farsi_text,getIndexTj,tjCol
from python_files.settings_python import printProgress as prgs
# from main import _make_farsi_text
# from main import * 


def makeRegistrarSaleFile(dfData,shiftWork): #,df_detailes,dfExclusiveBite
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
        Registrar_id= dfData.iloc[0,tjIndex.Registrar_id]
        Registrar= dfData.iloc[0,tjIndex.Registrar]
        prgs.printProgressBar(this_iter, l, prefix = 'Progress:', suffix = f' - this procces is  {_make_farsi_text(Registrar)}', length = 25)
        dfRegistrar = dfData.loc[dfData[tjCol.Registrar_id]==Registrar_id]
        # df_RegistrarDetailedSales=df_detailes.loc[df_detailes[frCol.Registrar]==Registrar]
        while len(dfRegistrar):
            
     
            idBranch = dfRegistrar.iloc[0,tjIndex.idBranch]
            branch = dfRegistrar.iloc[0,tjIndex.branch]
            dfBranch= dfRegistrar.loc[dfRegistrar[tjCol.idBranch]==idBranch]
            
           
            Cash = int(dfBranch[tjCol.Cash].sum())
            earnest = int(dfBranch[tjCol.earnest].sum())
            tasvieBaMarjooe = int(dfBranch[tjCol.tasvieBaMarjooe].sum())
            Deposit = int(dfBranch[tjCol.Deposit].sum())
            transitional = int(dfBranch[tjCol.transitional].sum())
            to_other_person = int(dfBranch[tjCol.to_other_person].sum())
            check = int(dfBranch[tjCol.check].sum())
            Received = Cash+earnest+tasvieBaMarjooe+Deposit+transitional+check + to_other_person
            
            
            ls_Checkout.append({tjCol.branch:branch,tjCol.idBranch:idBranch,tjCol.Registrar:Registrar,tjCol.Registrar_id:Registrar_id,
                            tjCol.Received:Received,tjCol.saleTime:shiftWork
                            }) # type: ignore
                               
                
            dfRegistrar = dfRegistrar.loc[dfRegistrar[tjCol.branch]!=branch]
        
        dfData = dfData.loc[dfData[tjCol.Registrar]!=Registrar]
    prgs.printProgressBar(l, l, prefix = 'Progress:', suffix = f'Complete', length = 25)
    dfCheckout = pd.DataFrame(ls_Checkout)
    return dfCheckout