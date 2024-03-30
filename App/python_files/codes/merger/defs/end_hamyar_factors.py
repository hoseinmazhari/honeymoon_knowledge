import os, sys

parent = os.path.abspath('.')
sys.path.insert(1, parent)

from main import _make_farsi_text
from main import *
def dump_cumulativeSales_on_date(df_cumulativeSales,df_branch_equaller):
  equIndex = get_index_branch_equaller(df_branch_equaller)
  dfTest = []
  for i in range(len(df_branch_equaller)):
    branch_id = df_branch_equaller.iat[i,equIndex.branch_id_hamyar]
    df_branch = df_cumulativeSales.loc[df_cumulativeSales[tjCol.idBranch]==branch_id]

    history = df_branch_equaller.iat[i,equIndex.history]    
    # dfTest.append(df_branch.loc[df_branch[tjCol.history]>=history])
    
    df_branch = df_branch.loc[df_branch[tjCol.history]<history]
    dfTest.append(df_branch)

    df_cumulativeSales = df_cumulativeSales.loc[df_cumulativeSales[tjCol.idBranch]!=branch_id]
  # ls_data=[]
  # ls_data.append(df_cumulativeSales)
  dfTest.append(df_cumulativeSales)
  df_cumulativeSales = pd.concat(dfTest)
  # dfTest = pd.concat(dfTest)
  # dfTest.to_excel("test.xlsx",index = False)
  return df_cumulativeSales


def dump_detailSale_on_date(df_detailedSales,df_branch_equaller):
  equIndex = get_index_branch_equaller(df_branch_equaller)
  l = len(df_branch_equaller)
  dfTest = []
  for i in range(len(df_branch_equaller)):
    prgsCounter = i+1 #l- len(dfData)
    prgs.printProgressBar(prgsCounter, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
    branch_id = df_branch_equaller.iat[i,equIndex.branch_id_hamyar]
    df_branch = df_detailedSales.loc[df_detailedSales[tjCol.idBranch]==branch_id]

    history = df_branch_equaller.iat[i,equIndex.history]    
    df_branch = df_branch.loc[df_branch[frCol.history]<history]
    dfTest.append(df_branch)
    df_detailedSales = df_detailedSales.loc[df_detailedSales[tjCol.idBranch]!=branch_id]

  ls_data = []
  ls_data.append(df_detailedSales)
  ls_data.append(pd.concat(dfTest))
  df_detailedSales = pd.concat(ls_data)

  return df_detailedSales