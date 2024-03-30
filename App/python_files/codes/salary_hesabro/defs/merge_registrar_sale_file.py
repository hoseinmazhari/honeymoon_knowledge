
# import os, sys

# parent = os.path.abspath('.')
# sys.path.insert(1, parent)

# from main import _make_farsi_text
# from main import * 

# def mergeInvoices(dfData):
    
#     df_ans = pd.DataFrame()
#     tjIndex = getIndexTj(dfData)
#     while len(dfData):
#         Registrar_id = dfData.iloc[0,tjIndex.Registrar_id]
#         Registrar = dfData.iloc[0,tjIndex.Registrar]
#         dfRegistrar = dfData.loc[dfData[tjCol.Registrar_id]==Registrar_id]
#         while len(dfRegistrar):
#             saleTime = dfRegistrar.iloc[0,tjIndex.saleTime]
#             dfsaleTime = dfRegistrar.loc[dfRegistrar[tjCol.saleTime]==saleTime]
#             while len(dfsaleTime):
#                 branch= dfsaleTime.iloc[0,tjIndex.branch]
#                 idBranch= dfsaleTime.iloc[0,tjIndex.idBranch]
#                 dfBranch = dfsaleTime.loc[dfsaleTime[tjCol.idBranch]==idBranch]
#                 # while len(dfBranch):
#                 Received = dfBranch[tjCol.Received].sum()
                
#                 df_ans=df_ans.append({tjCol.branch:branch,tjCol.idBranch:idBranch,tjCol.Registrar_id:Registrar_id,tjCol.Registrar:Registrar,tjCol.Received:Received,
#                         tjCol.saleTime:saleTime},ignore_index= True) # type: ignore
#                 # print(df_ans)
#                 dfsaleTime = dfsaleTime.loc[dfsaleTime[tjCol.branch]!=branch]
            
#             dfRegistrar = dfRegistrar.loc[dfRegistrar[tjCol.saleTime]!=saleTime]
#         dfData = dfData.loc[dfData[tjCol.Registrar]!=Registrar]
#     return df_ans