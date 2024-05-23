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
    Received = tjCol.Received
    saleTime = tjCol.saleTime
    commission_percent = targetCol.commission_percent
    commission = targetCol.commission
    baseSalary = targetCol.baseSalary
    salary = "حقوق"
    # goodTarget = targetCol.goodTarget
    # perfectTarget = targetCol.perfectTarget
def get_index_finalTarget(df):
    thisClass = finalTargetCol()
    thisItter = -1
    for col in df.columns:
        thisItter += 1
        if thisClass.branch == col:
            thisClass.branch = thisItter #type: ignore
        elif thisClass.branch_id == col:
            thisClass.branch_id = thisItter  #type: ignore
        elif thisClass.seller_name == col:
            thisClass.seller_name = thisItter  #type: ignore
        elif thisClass.seller_id == col:
            thisClass.seller_id = thisItter #type: ignore
        elif thisClass.Received == col:
            thisClass.Received = thisItter #type: ignore
        elif thisClass.saleTime == col:
            thisClass.saleTime = thisItter #type: ignore
        elif thisClass.commission_percent == col:
            thisClass.commission_percent = thisItter #type: ignore
        elif thisClass.commission == col:
            thisClass.commission = thisItter #type: ignore
    return thisClass



                      
def commission(dfData,dfTarget):
    thisIndex = get_index_finalTarget(dfData)
    targetIndex = target.getIndexTarget(dfTarget)
    df_ans = pd.DataFrame()
    ls_ans = []
    while len(dfData):
        seller_name = dfData.iat[0,thisIndex.seller_name]
        seller_id = dfData.iat[0,thisIndex.seller_id]
        dfseller_name = dfData.loc[dfData[finalTargetCol.seller_id]==seller_id]
        Received = int(dfseller_name[finalTargetCol.Received].sum())
        commission = int(dfseller_name[finalTargetCol.commission].sum())
        dfBaseSalary = dfTarget.loc[dfTarget[targetCol.adviser]==seller_name]
        if len(dfBaseSalary):
            baseSalary = dfBaseSalary.iat[0,targetIndex.baseSalary]
            goodTarget = dfBaseSalary.iat[0,targetIndex.goodTarget]
            branch = dfBaseSalary.iat[0,targetIndex.branch]
            perfectTarget = dfBaseSalary.iat[0,targetIndex.perfectTarget]
            salary = baseSalary+commission
            ls_ans.append({finalTargetCol.branch:branch,finalTargetCol.seller_name:seller_name,targetCol.goodTarget:goodTarget,
                                    targetCol.perfectTarget:perfectTarget,finalTargetCol.Received:Received,
                                    finalTargetCol.commission:commission,targetCol.baseSalary:baseSalary,
                                    finalTargetCol.salary:salary}) # type: ignore
        else:
            baseSalary = 0
            goodTarget = 0
            branch = "honeymoon"
            perfectTarget = 0
            salary = 0
            commission = 0
            ls_ans.append({finalTargetCol.branch:branch,finalTargetCol.seller_name:seller_name,targetCol.goodTarget:goodTarget,
                                    targetCol.perfectTarget:perfectTarget,finalTargetCol.Received:Received,
                                    finalTargetCol.commission:commission,targetCol.baseSalary:baseSalary,
                                    finalTargetCol.salary:salary}) # type: ignore
        
        dfData = dfData.loc[dfData[finalTargetCol.seller_id]!= seller_id]
    df_ans = pd.DataFrame(ls_ans)
    return df_ans

  