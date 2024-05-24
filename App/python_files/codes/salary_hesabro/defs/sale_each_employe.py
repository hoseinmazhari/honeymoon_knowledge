import os, sys, pandas as pd

# parent = os.path.abspath('.')
# sys.path.insert(1, parent)
from . import target 
from .target import targetCol
from python_files.settings_python.app_structures import _make_farsi_text,tjCol
# from main import * 

class thisCols():
    branch = tjCol.branch
    branch_id = tjCol.branch_id
    seller_name = tjCol.seller_name
    seller_id = tjCol.seller_id
    Received = tjCol.Received
    shiftWork = tjCol.saleTime

def getIndexThisCols(df):
    thisClass = thisCols()
    thisItter = -1
    for col in df.columns:
        thisItter += 1
        if thisClass.branch == col:
            thisClass.branch = thisItter  # type: ignore
        elif thisClass.branch_id == col:
            thisClass.branch_id = thisItter # type: ignore
        elif thisClass.seller_name == col:
            thisClass.seller_name = thisItter # type: ignore
        elif thisClass.seller_id == col:
            thisClass.seller_id = thisItter # type: ignore
        elif thisClass.Received == col:
            thisClass.Received = thisItter # type: ignore
        elif thisClass.shiftWork == col:
            thisClass.shiftWork = thisItter # type: ignore
    return thisClass

                     
def sale_sellers_in_each_branch(dfData):
    this_index = getIndexThisCols(dfData)  
    ls_data = []
    while len(dfData):
        seller_id = dfData.iat[0,this_index.seller_id]
        seller_name = dfData.iat[0, this_index.seller_name]
        df_seller= dfData.loc[dfData[thisCols.seller_id]== seller_id]
        dfData = dfData.loc[dfData[thisCols.seller_id] != seller_id]
        while len(df_seller):
            branch = df_seller.iat[0, this_index.branch]
            dfBranch = df_seller.loc[df_seller[thisCols.branch] == branch]
            df_seller = df_seller.loc[df_seller[thisCols.branch] != branch]
            Received = int(dfBranch[thisCols.Received].sum())
            
            ls_data.append({thisCols.branch:branch,
                            thisCols.seller_id:seller_id, 
                            thisCols.seller_name : seller_name,
                            thisCols.Received:Received
                            })
    df_ans = pd.DataFrame(ls_data)
    return df_ans

# def sale_employes(dfData):
#     this_index = getIndexThisCols(dfData)  
#     ls_data = []
#     while len(dfData):
#         seller_id = dfData.iat[0,this_index.seller_id]
#         dfseller_name = dfData.loc[dfData[thisCols.seller_id]== seller_id]
#         dfData = dfData.loc[dfData[thisCols.seller_id] != seller_id]
#         Received = int(dfseller_name[thisCols.Received].sum())
#         seller_name = dfseller_name.iat[0, this_index.seller_name]
#         ls_data.append({thisCols.seller_id:seller_id, 
#                         thisCols.seller_name : seller_name, thisCols.Received:Received
#                         })
#     df_ans = pd.DataFrame(ls_data)
#     return df_ans

  