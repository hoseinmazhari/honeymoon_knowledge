import os, sys, pandas as pd

# parent = os.path.abspath('.')
# sys.path.insert(1, parent)
from . import target
# from codes.salary.defs import target 
from .target import targetCol
from python_files.settings_python.app_structures import _make_farsi_text,tjCol
# from main import _make_farsi_text
# from main import * 
class finalTargetCol():
    branch=tjCol.branch
    branch_id= tjCol.branch_id
    seller_name = tjCol.seller_name
    seller_id = tjCol.seller_id
    received_with_checkout = tjCol.received_with_checkout
    received_without_checkout = tjCol.received_without_checkout
    saleTime = tjCol.saleTime
    commission_percent = targetCol.commission_percent
    commission_with_checkout = targetCol.commission_with_checkout
    commission_without_checkout = targetCol.commission_without_checkout
    baseSalary = targetCol.baseSalary
    salary_with_checkout = "حقوق با تسویه مرجوعی"
    salary_without_checkout = "حقوق بدون تسویه با مرجوعی"
    goodTarget = targetCol.goodTarget
    perfectTarget = targetCol.perfectTarget
def get_index_finalTarget(df):
    thisCols = finalTargetCol()
    thisItter = -1
    for col in df.columns:
        thisItter += 1
        if thisCols.branch == col:
            thisCols.branch = thisItter #type: ignore
        elif thisCols.branch_id == col:
            thisCols.branch_id = thisItter  #type: ignore
        elif thisCols.seller_name == col:
            thisCols.seller_name = thisItter  #type: ignore
        elif thisCols.seller_id == col:
            thisCols.seller_id = thisItter #type: ignore
        elif thisCols.received_without_checkout == col:
            thisCols.received_without_checkout = thisItter #type: ignore
        elif col == thisCols.received_with_checkout:
            thisCols.received_with_checkout = thisItter #type: ignore
        elif thisCols.saleTime == col:
            thisCols.saleTime = thisItter #type: ignore
        elif thisCols.commission_percent == col:
            thisCols.commission_percent = thisItter #type: ignore
        elif thisCols.commission_with_checkout == col:
            thisCols.commission_with_checkout = thisItter #type: ignore
        elif thisCols.commission_without_checkout == col:
            thisCols.commission_without_checkout = thisItter #type: ignore
        elif thisCols.salary_with_checkout == col:
            thisCols.salary_with_checkout = thisItter #type: ignore
        elif col == thisCols.salary_without_checkout:
            thisCols.salary_without_checkout = thisItter #type: ignore
        elif col == thisCols.perfectTarget:
            thisCols.perfectTarget = thisItter #type: ignore
        elif col == thisCols.goodTarget:
            thisCols.goodTarget = thisItter
    return thisCols



                      
def commission_calculator(dfData,dfTarget):
    thisIndex = get_index_finalTarget(dfData)
    targetIndex = target.getIndexTarget(dfTarget)
    df_ans = pd.DataFrame()
    ls_ans = []
    while len(dfData):
        seller_name = dfData.iat[0,thisIndex.seller_name]
        seller_id = dfData.iat[0,thisIndex.seller_id]
        dfseller_name = dfData.loc[dfData[finalTargetCol.seller_id]==seller_id]
        received_with_checkout = int(dfseller_name[finalTargetCol.received_with_checkout].sum())
        received_without_checkout = int(dfseller_name[finalTargetCol.received_without_checkout].sum())
        commission_with_checkout = int(dfseller_name[finalTargetCol.commission_with_checkout].sum())
        commission_without_checkout = int(dfseller_name[finalTargetCol.commission_without_checkout].sum())
        dfBaseSalary = dfTarget.loc[dfTarget[targetCol.adviser_id]==seller_id]
        if len(dfBaseSalary):
            baseSalary = dfBaseSalary.iat[0,targetIndex.baseSalary]
            goodTarget = dfBaseSalary.iat[0,targetIndex.goodTarget]
            branch = dfBaseSalary.iat[0,targetIndex.branch]
            branch_id = dfBaseSalary.iat[0, targetIndex.branch_id]
            perfectTarget = dfBaseSalary.iat[0,targetIndex.perfectTarget]
            salary_with_checkout = baseSalary+commission_with_checkout
            salary_without_checkout = baseSalary + commission_without_checkout
            ls_ans.append({finalTargetCol.branch_id: branch_id,finalTargetCol.branch:branch,
                           finalTargetCol.seller_name:seller_name,targetCol.goodTarget:goodTarget,
                            targetCol.perfectTarget:perfectTarget,
                            finalTargetCol.received_with_checkout:received_with_checkout,
                            finalTargetCol.commission_with_checkout:commission_with_checkout,
                            finalTargetCol.received_without_checkout: received_without_checkout,
                            finalTargetCol.commission_without_checkout: commission_without_checkout,
                            targetCol.baseSalary:baseSalary,
                            finalTargetCol.salary_with_checkout:salary_with_checkout,
                            finalTargetCol.salary_without_checkout: salary_without_checkout
                            }) # type: ignore
        else:
            baseSalary = 0
            goodTarget = 0
            branch = ""
            branch_id = ""
            perfectTarget = 0
            salary_with_checkout = 0
            salary_without_checkout = 0
            commission_with_checkout = 0
            commission_without_checkout = 0
            ls_ans.append({finalTargetCol.branch_id: branch_id,finalTargetCol.branch:branch,
                           finalTargetCol.seller_name:seller_name,targetCol.goodTarget:goodTarget,
                            targetCol.perfectTarget:perfectTarget,
                            finalTargetCol.received_with_checkout:received_with_checkout,
                            finalTargetCol.commission_with_checkout:commission_with_checkout,
                            finalTargetCol.received_without_checkout: received_without_checkout,
                            finalTargetCol.commission_without_checkout: commission_without_checkout,
                            targetCol.baseSalary:baseSalary,
                            finalTargetCol.salary_with_checkout:salary_with_checkout,
                            finalTargetCol.salary_without_checkout: salary_without_checkout
                            }) # ty
            # ls_ans.append({finalTargetCol.branch:branch,finalTargetCol.seller_name:seller_name,targetCol.goodTarget:goodTarget,
            #                         targetCol.perfectTarget:perfectTarget,finalTargetCol.Received:Received,
            #                         finalTargetCol.commission:commission,targetCol.baseSalary:baseSalary,
            #                         finalTargetCol.salary:salary}) # type: ignore
        
        dfData = dfData.loc[dfData[finalTargetCol.seller_id]!= seller_id]
    df_ans = pd.DataFrame(ls_ans)
    return df_ans

  