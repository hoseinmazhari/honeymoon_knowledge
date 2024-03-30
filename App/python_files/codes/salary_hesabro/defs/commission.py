import os, sys, pandas as pd

parent = os.path.abspath('.')
sys.path.insert(1, parent)
from . import target
# from codes.salary.defs import target 
from .target import targetCol
from ....settings.app_structures import _make_farsi_text,tjCol
# from main import _make_farsi_text
# from main import * 
class finalTargetCol():
    branch=tjCol.branch
    branch_id= tjCol.idBranch
    Registrar = tjCol.Registrar
    Registrar_id = tjCol.Registrar_id
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
        elif thisClass.Registrar == col:
            thisClass.Registrar = thisItter  #type: ignore
        elif thisClass.Registrar_id == col:
            thisClass.Registrar_id = thisItter #type: ignore
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
        Registrar = dfData.iat[0,thisIndex.Registrar]
        Registrar_id = dfData.iat[0,thisIndex.Registrar_id]
        dfRegistrar = dfData.loc[dfData[finalTargetCol.Registrar_id]==Registrar_id]
        Received = int(dfRegistrar[finalTargetCol.Received].sum())
        commission = int(dfRegistrar[finalTargetCol.commission].sum())
        dfBaseSalary = dfTarget.loc[dfTarget[targetCol.adviser]==Registrar]
        if len(dfBaseSalary):
            baseSalary = dfBaseSalary.iat[0,targetIndex.baseSalary]
            goodTarget = dfBaseSalary.iat[0,targetIndex.goodTarget]
            branch = dfBaseSalary.iat[0,targetIndex.branch]
            perfectTarget = dfBaseSalary.iat[0,targetIndex.perfectTarget]
            salary = baseSalary+commission
            ls_ans.append({finalTargetCol.branch:branch,finalTargetCol.Registrar:Registrar,targetCol.goodTarget:goodTarget,
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
            ls_ans.append({finalTargetCol.branch:branch,finalTargetCol.Registrar:Registrar,targetCol.goodTarget:goodTarget,
                                    targetCol.perfectTarget:perfectTarget,finalTargetCol.Received:Received,
                                    finalTargetCol.commission:commission,targetCol.baseSalary:baseSalary,
                                    finalTargetCol.salary:salary}) # type: ignore
        
        dfData = dfData.loc[dfData[finalTargetCol.Registrar_id]!= Registrar_id]
    df_ans = pd.DataFrame(ls_ans)
    return df_ans

  