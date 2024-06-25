import os, sys, pandas as pd

# parent = os.path.abspath('.')
# sys.path.insert(1, parent)
from . import target 
from .target import targetCol
from python_files.settings_python.app_structures import _make_farsi_text,tjCol,getIndexTj
# from main import * 

# class Sale_sellers_in_each_branch_cols():
#     branch = tjCol.branch
#     branch_id = tjCol.branch_id
#     seller_name = tjCol.seller_name
#     seller_id = tjCol.seller_id
#     received_with_checkout = tjCol.received_with_checkout
#     received_without_checkout = tjCol.received_without_checkout
#     shiftWork = tjCol.saleTime

# def getIndexThisCols(df):
#     thisCols = Sale_sellers_in_each_branch_cols()
#     thisItter = -1
#     for col in df.columns:
#         thisItter += 1
#         if thisCols.branch == col:
#             thisCols.branch = thisItter  # type: ignore
#         elif thisCols.branch_id == col:
#             thisCols.branch_id = thisItter # type: ignore
#         elif thisCols.seller_name == col:
#             thisCols.seller_name = thisItter # type: ignore
#         elif thisCols.seller_id == col:
#             thisCols.seller_id = thisItter # type: ignore
#         elif thisCols.received_without_checkout == col:
#             thisCols.received_without_checkout = thisItter # type: ignore
#         elif thisCols.received_with_checkout:
#             thisCols.received_with_checkout = thisItter
#         elif thisCols.shiftWork == col:
#             thisCols.shiftWork = thisItter # type: ignore
#     return thisCols

                     
def sale_sellers_in_each_branch(dfData):
    this_index = getIndexTj(dfData)  
    thisCols = tjCol()
    ls_data = []
    while len(dfData):
        seller_id = dfData.iat[0,this_index.seller_id]
        seller_name = dfData.iat[0, this_index.seller_name]
        df_seller= dfData.loc[dfData[thisCols.seller_id]== seller_id]
        dfData = dfData.loc[dfData[thisCols.seller_id] != seller_id]
        while len(df_seller):
            branch = df_seller.iat[0, this_index.branch]
            branch_id = df_seller.iat[0, this_index.branch_id]
            dfBranch = df_seller.loc[df_seller[thisCols.branch_id] == branch_id]
            df_seller = df_seller.loc[df_seller[thisCols.branch_id] != branch_id]
            receive_with_checkout = int(dfBranch[thisCols.received_with_checkout].sum())
            receive_without_checkout = int(dfBranch[thisCols.received_without_checkout].sum())
            
            ls_data.append({thisCols.branch:branch,
                            thisCols.branch_id: branch_id,
                            thisCols.seller_id:seller_id, 
                            thisCols.seller_name : seller_name,
                            thisCols.received_with_checkout: receive_with_checkout,
                            thisCols.received_without_checkout:receive_without_checkout
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

  