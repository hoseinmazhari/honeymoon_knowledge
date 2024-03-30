import os, sys, pandas as pd

parent = os.path.abspath('.')
sys.path.insert(1, parent)
from . import target 
from .target import targetCol
from ....settings.app_structures import _make_farsi_text,tjCol
# from main import * 

class thisCols():
    branch = tjCol.branch
    idBranch = tjCol.idBranch
    Registrar = tjCol.Registrar
    Registrar_id = tjCol.Registrar_id
    Received = tjCol.Received
    shiftWork = tjCol.saleTime

def getIndexThisCols(df):
    thisClass = thisCols()
    thisItter = -1
    for col in df.columns:
        thisItter += 1
        if thisClass.branch == col:
            thisClass.branch = thisItter  # type: ignore
        elif thisClass.idBranch == col:
            thisClass.idBranch = thisItter # type: ignore
        elif thisClass.Registrar == col:
            thisClass.Registrar = thisItter # type: ignore
        elif thisClass.Registrar_id == col:
            thisClass.Registrar_id = thisItter # type: ignore
        elif thisClass.Received == col:
            thisClass.Received = thisItter # type: ignore
        elif thisClass.shiftWork == col:
            thisClass.shiftWork = thisItter # type: ignore
    return thisClass

                     

def sale_employes(dfData):
    this_index = getIndexThisCols(dfData)  
    ls_data = []
    while len(dfData):
        Registrar_id = dfData.iat[0,this_index.Registrar_id]
        dfRegistrar = dfData.loc[dfData[thisCols.Registrar_id]== Registrar_id]
        dfData = dfData.loc[dfData[thisCols.Registrar_id] != Registrar_id]
        Received = int(dfRegistrar[thisCols.Received].sum())
        Registrar = dfRegistrar.iat[0, this_index.Registrar]
        ls_data.append({thisCols.Registrar_id:Registrar_id, 
                        thisCols.Registrar : Registrar, thisCols.Received:Received
                        })
    df_ans = pd.DataFrame(ls_data)
    return df_ans

  