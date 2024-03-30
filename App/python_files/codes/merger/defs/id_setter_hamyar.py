import os, sys

parent = os.path.abspath('.')
sys.path.insert(1, parent)

from main import _make_farsi_text
from main import *
def seller_id_setter(df_cumulative_sale,df_detail_sale):
    tjIndex = getIndexTj(df_cumulative_sale)
    while len(df_cumulative_sale):
        seller = df_cumulative_sale.iat[0,tjIndex.Registrar]
        Registrar_id = df_cumulative_sale.iat[0,tjIndex.Registrar_id]
        
        condition = (df_detail_sale[frCol.Registrar] == seller)
        df_detail_sale.loc[condition, tjCol.Registrar_id] = Registrar_id

        # df_detail_sale[tjCol.Registrar_id].mask(df_detail_sale[frCol.Registrar] == seller, Registrar_id, inplace=True)
        df_cumulative_sale = df_cumulative_sale.loc[df_cumulative_sale[tjCol.Registrar]!=seller]
    return df_detail_sale
def branch_id_setter(df_cumulative_sale,df_detail_sale):
    tjIndex = getIndexTj(df_cumulative_sale)
    while len(df_cumulative_sale):
        branch = df_cumulative_sale.iat[0,tjIndex.branch]
        id_branch = df_cumulative_sale.iat[0,tjIndex.idBranch]

        condition = (df_detail_sale[frCol.branch] == branch)
        df_detail_sale.loc[condition, tjCol.idBranch] = id_branch

        # df_detail_sale[tjCol.idBranch].mask(df_detail_sale[frCol.branch] == branch, id_branch, inplace=True)
        df_cumulative_sale = df_cumulative_sale.loc[df_cumulative_sale[tjCol.branch]!=branch]
    return df_detail_sale
