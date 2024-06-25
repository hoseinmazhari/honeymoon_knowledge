import os, sys, pandas as pd

# parent = os.path.abspath('.')
# sys.path.insert(1, parent)
from python_files.settings_python.app_structures import _make_farsi_text, prtLines,getIndexTj,tjCol
from python_files.settings_python import printProgress as prgs
# from main import _make_farsi_text
# from main import * 

from . import target as gitt
from .target import targetCol
def concatWithTargets(dfData,df_targets):
    # df_employes=pd.DataFrame()
    ls_employes = []
    targetIndex = gitt.getIndexTarget(df_targets)
    l= len(dfData)
    prtLines(3)
    tjIndex = getIndexTj(dfData)
    print(_make_farsi_text("ادغام فروش با تارگت"))
    while len(dfData):
        
        branch= dfData.iat[0,tjIndex.branch]
        branch_id =  dfData.iat[0,tjIndex.branch_id]
        # print(tjIndex.branch)
        # print(branch)
        prgsCounter = l- len(dfData)
        prgs.printProgressBar(prgsCounter, l, prefix = 'Progress:', suffix = 'Complete', length = 25)
     

        df_branch = dfData.loc[dfData[tjCol.branch_id]==branch_id]
        while len(df_branch):
            saleTime = df_branch.iat[0,tjIndex.saleTime]
            df_thisTarget = df_targets.loc[df_targets[targetCol.branch]==branch]
            df_thisTarget = df_thisTarget.loc[df_thisTarget[targetCol.shiftWork]==saleTime]
            if len(df_thisTarget):
                commission_percent = df_thisTarget.iat[0,targetIndex.commission_percent]
                
            else:
                commission_percent = 0
                
            dfsaleTime = df_branch.loc[df_branch[tjCol.saleTime]==saleTime]
            while len(dfsaleTime):
                seller_name = dfsaleTime.iat[0,tjIndex.seller_name]
                seller_id = dfsaleTime.iat[0,tjIndex.seller_id]
                received_with_checkout = dfsaleTime.iat[0,tjIndex.received_with_checkout]
                received_without_checkout = dfsaleTime.iat[0, tjIndex.received_without_checkout]
                
                # Received = dfsaleTime.iat[0,tjIndex.Received]
                if commission_percent:
                    commission_with_checkout = received_with_checkout * commission_percent / 100
                    commission_without_checkout = received_without_checkout * commission_percent / 100
                else:
                    commission_with_checkout = 0
                    commission_without_checkout = 0
                
               
                ls_employes.append({tjCol.branch:branch,tjCol.branch_id:branch_id,
                                    tjCol.saleTime: saleTime,
                                    tjCol.seller_name:seller_name,tjCol.seller_id:seller_id,
                                    targetCol.commission_percent:commission_percent,
                                    tjCol.received_with_checkout: received_with_checkout,
                                    targetCol.commission_with_checkout: commission_with_checkout,
                                    tjCol.received_without_checkout: received_without_checkout,
                                    targetCol.commission_without_checkout:commission_without_checkout,                       
                        }) # type: ignore
                dfsaleTime= dfsaleTime.loc[dfsaleTime[tjCol.seller_id]!=seller_id]
            df_branch = df_branch.loc[df_branch[tjCol.saleTime]!=saleTime]
        dfData = dfData.loc[dfData[tjCol.branch_id]!=branch_id]
    prgs.printProgressBar(l, l, prefix = 'Progress:', suffix = 'Complete', length = 25)
    df_employes = pd.DataFrame(ls_employes)
    return df_employes
