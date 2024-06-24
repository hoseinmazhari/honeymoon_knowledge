import os, sys, pandas as pd

# parent = os.path.abspath('.')
# sys.path.insert(1, parent)
from python_files.settings_python.app_structures import _make_farsi_text, prtLines,getIndexTj,tjCol
from python_files.settings_python import printProgress as prgs
# from main import _make_farsi_text
# from main import * 

from . import target as gitt
from .target import targetCol
class Compare_sellers_with_targetsCols():
    branch = tjCol.branch
    branch_id = tjCol.branch_id
    seller_name = tjCol.seller_name
    seller_id = tjCol.seller_id
    # Received = tjCol.Received
    received_with_checkout = tjCol.received_with_checkout
    received_without_checkout = tjCol.received_without_checkout
    goodTarget = targetCol.goodTarget
    progress_with_checkout =  'نسبت دریافتی با تسویه با مرجوعی به تارگت خوب' # "پیشرفت"
    progress_without_checkout = 'نسبت دریافتی بدون تسویه با مرجوعی به تارگت خوب' # "پیشرفت"
def get_index_Compare_sellers_with_targetsCols(df):
    thisClass = Compare_sellers_with_targetsCols()
    thisItter = -1
    for col in df.columns:
        thisItter += 1
        if col == thisClass.branch:
            thisClass.branch = thisItter #type: ignore
        elif col == thisClass.branch_id:
            thisClass.branch_id = thisItter # type: ignore
        elif col == thisClass.seller_name:
            thisClass.seller_name = thisItter# type: ignore
        elif col == thisClass.seller_id:
            thisClass.seller_id = thisItter# type: ignore
        elif col == thisClass.received_with_checkout:
            thisClass.received_with_checkout = thisItter# type: ignore
        elif col == thisClass.received_without_checkout:
            thisClass.received_without_checkout = thisItter #type: ignore
        elif col == thisClass.goodTarget:
            thisClass.goodTarget = thisItter# type: ignore
        elif col == thisClass.progress_with_checkout:
            thisClass.progress_with_checkout = thisItter #type: ignore
        elif col == thisClass.progress_without_checkout:
            thisClass.progress_without_checkout = thisItter #type: ignore
    return thisClass
def compare_salers_with_targets(dfData,df_targets):
    # df_employes=pd.DataFrame()
    ls_employes = []
    targetIndex = gitt.getIndexTarget(df_targets)
    l= len(dfData)
    prtLines(3)
    tjIndex = getIndexTj(dfData)
    print(_make_farsi_text("فروشندگان برتر هانی مون"))
    while len(dfData):
        
        branch= dfData.iat[0,tjIndex.branch]
        branch_id =  dfData.iat[0,tjIndex.branch_id]
        # print(tjIndex.branch)
        # print(branch)
        prgsCounter = l- len(dfData)
        prgs.printProgressBar(prgsCounter, l, prefix = 'Progress:', suffix = 'Complete', length = 25)
        # print(_make_farsi_text(branch))

        df_branch = dfData.loc[dfData[tjCol.branch_id]==branch_id]
        while len(df_branch):
            saleTime = df_branch.iat[0,tjIndex.saleTime]
            # print(_make_farsi_text(saleTime))
            df_thisTarget = df_targets.loc[df_targets[targetCol.branch_id]==branch_id]
            df_thisTarget = df_thisTarget.loc[df_thisTarget[targetCol.shiftWork]==saleTime]
            if len(df_thisTarget):
                this_goodTarget = df_thisTarget.iat[0,targetIndex.goodTarget]
                
            else:
                this_goodTarget = 0
            
            dfsaleTime = df_branch.loc[df_branch[tjCol.saleTime]==saleTime]
            while len(dfsaleTime):
                seller_name = dfsaleTime.iat[0,tjIndex.seller_name]
                # print(_make_farsi_text(seller_name))
                seller_id = dfsaleTime.iat[0,tjIndex.seller_id]
                df_seller_goodTarget = df_targets.loc[df_targets[targetCol.seller_id]==seller_id]
                df_seller_goodTarget = df_seller_goodTarget.loc[df_seller_goodTarget[targetCol.goodTarget]!=0]
                if len(df_seller_goodTarget):
                    seller_branch = df_seller_goodTarget.iat[0, targetIndex.branch]
                    seller_branch_id = df_seller_goodTarget.iat[0, targetIndex.branch_id]
                    seller_goodTarget = df_seller_goodTarget.iat[0, targetIndex.goodTarget]
                        
                    this_received_with_checkout = dfsaleTime.iat[0,tjIndex.received_with_checkout]
                    this_received_without_checkout = dfsaleTime.iat[0, tjIndex.received_without_ckeckout]
                    try:
                        percent_with_checkout = this_received_with_checkout * 100 / seller_goodTarget -100
                    except:
                        percent_with_checkout = 0

                    try:
                        percent_without_checkout = this_received_without_checkout * 100 / seller_goodTarget -100
                    except:
                        percent_without_checkout = 0

                    received_with_checkout = this_received_with_checkout + this_received_with_checkout * percent_with_checkout/100
                    received_without_checkout = this_received_without_checkout + \
                                this_received_without_checkout* percent_without_checkout/100
                    # Received = this_Received + this_Received * percent/100

                    
                    thisClass = Compare_sellers_with_targetsCols()
                    ls_employes.append({thisClass.branch:seller_branch,thisClass.branch_id:seller_branch_id,thisClass.seller_name:seller_name,
                                        thisClass.seller_id:seller_id,
                                        thisClass.received_without_checkout:received_without_checkout,
                                        thisClass.received_with_checkout: received_with_checkout,
                                        thisClass.goodTarget: seller_goodTarget,
                                        thisClass.progress_without_checkout: 0,
                                        thisClass.progress_with_checkout: 0
                            }) # type: ignore
                dfsaleTime= dfsaleTime.loc[dfsaleTime[tjCol.seller_id]!=seller_id]
            df_branch = df_branch.loc[df_branch[tjCol.saleTime]!=saleTime]
        dfData = dfData.loc[dfData[tjCol.branch_id]!=branch_id]
    prgs.printProgressBar(l, l, prefix = 'Progress:', suffix = 'Complete', length = 25)
    df_employes = pd.DataFrame(ls_employes)
    # df_employes.to_excel("test.xlsx",index=False)
    thisIndex = get_index_Compare_sellers_with_targetsCols(df_employes)
    thisClass = Compare_sellers_with_targetsCols()
    ls_data = []
    while len(df_employes):
        seller_name = df_employes.iat[0, thisIndex.seller_name]
        seller_id = df_employes.iat[0, thisIndex.seller_id]
        branch = df_employes.iat[0, thisIndex.branch]
        branch_id = df_employes.iat[0, thisIndex.branch_id]
        goodTarget = df_employes.iat[0, thisIndex.goodTarget]
        df_seller = df_employes.loc[df_employes[thisClass.seller_id] == seller_id]
        received_with_checkout  = int(df_seller[thisClass.received_with_checkout].sum())
        received_without_checkout = int(df_seller[thisClass.received_without_checkout].sum())
        progress_with_checkout = received_with_checkout * 100 / goodTarget -100
        progress_without_checkout = received_without_checkout * 100 /goodTarget - 100
        ls_data.append({thisClass.branch:branch,thisClass.branch_id:branch_id,
                                thisClass.seller_name:seller_name,
                                thisClass.seller_id:seller_id,
                                thisClass.goodTarget: goodTarget,
                                thisClass.received_with_checkout:received_with_checkout,
                                thisClass.progress_with_checkout: progress_with_checkout,
                                
                                thisClass.received_without_checkout:received_without_checkout,
                                thisClass.progress_without_checkout:progress_without_checkout
                            }) # type: ignore
        df_employes = df_employes.loc[df_employes[thisClass.seller_id] != seller_id]
    dfData = pd.DataFrame(ls_data)
    return dfData









































# df_employes=pd.DataFrame()
#     ls_employes = []
#     targetIndex = gitt.getIndexTarget(df_targets)
#     l= len(dfData)
#     prtLines(3)
#     df_all_targets = df_targets.copy()
#     df_targets = df_targets.loc[df_targets[targetCol.goodTarget]!=0]
#     tjIndex = getIndexTj(dfData)
#     print(_make_farsi_text("فروشندگان برتر هانی مون"))
#     while len(df_targets):
        
#         branch= df_targets.iat[0,targetIndex.branch]
#         branch_id =  df_targets.iat[0,targetIndex.branch_id]
#         # print(tjIndex.branch)
#         # print(branch)
#         prgsCounter = l- len(dfData)
#         prgs.printProgressBar(prgsCounter, l, prefix = 'Progress:', suffix = 'Complete', length = 25)
     

#         df_branch = df_targets.loc[df_targets[targetCol.branch_id]==branch_id]
#         while len(df_branch):
#             seller_id = df_branch.iat[0,targetIndex.seller_id]
#             goodTarget = df_branch.iat[0, targetIndex.goodTarget]
#             df_this_branch = dfData.loc[df_branch[tjCol.branch]==branch]

#             if len(df_this_branch):   
#                 df_seller = df_this_branch.loc[df_this_branch[tjCol.seller_id]== seller_id]
#                 if len(df_seller):
#                     seller_name = df_seller.iat[0, tjIndex.seller_name]
#                     Recieved = int(df_seller[tjCol.Received].sum())
#                     try:
#                         percent = Recieved*100/goodTarget
#                     except:
#                         percent = 0

#                     ls_employes.append({tjCol.branch:branch,tjCol.branch_id:branch_id,tjCol.seller_name:seller_name,tjCol.seller_id:seller_id,
#                             tjCol.Received:Received, tjCol.saleTime:saleTime,
                            
#                             targetCol.commission_percent:commission_percent,
#                             targetCol.commission:commission
                            
#                         }) # type: ignore
#                 dfsaleTime= dfsaleTime.loc[dfsaleTime[tjCol.seller_name]!=seller_name]
#             df_branch = df_branch.loc[df_branch[tjCol.saleTime]!=saleTime]
#         dfData = dfData.loc[dfData[tjCol.branch]!=branch]
#     prgs.printProgressBar(l, l, prefix = 'Progress:', suffix = 'Complete', length = 25)
#     df_employes = pd.DataFrame(ls_employes)
#     return df_employes
