import os, sys

parent = os.path.abspath('.')
sys.path.insert(1, parent)

from main import _make_farsi_text
from main import *
class Products_equaller_class():
    id_hesabro = "id_hesabro"
    product_hesabro = "product_hesabro"	
    thisHajm = "thisHajm"	
    thisType = "thisType"
    id_hamyar = "id_hamyar"
    product_hamyar = "product_hamyar"
def getIndex_products(df):
    thisItter = -1
    thisClass = Products_equaller_class()
    for col in df.columns:
        thisItter += 1
        if col == thisClass.id_hesabro:
            thisClass.id_hesabro = thisItter #type: ignore
        elif col == thisClass.id_hamyar:
            thisClass.id_hamyar = thisItter #type: ignore
        elif col == thisClass.product_hamyar:
            thisClass.product_hamyar = thisItter #type: ignore
        elif col == thisClass.product_hesabro:
            thisClass.product_hesabro = thisItter #type: ignore
        elif col == thisClass.thisHajm:
            thisClass.thisHajm = thisItter #type: ignore
        elif col == thisClass.thisType:
            thisClass.thisType = thisItter #type: ignore
    return thisClass
df_seller_equaller_step2 = read_seller_equaller_step2_file()
def product_equaller(df_products_equaller,dfData):
    thisPath = os.getcwd()
    os.chdir(f"{thisPath}/base Datas/equaller hamyar hesabro")
    df_product_list = pd.read_excel("product list.xlsx")
    os.chdir(thisPath)
    fr_index = getIndexFr(dfData)
    thisIndex = getIndex_products(df_products_equaller)
    ls_data = []
    pec = Products_equaller_class()
    print()
    l = len(df_products_equaller)
    while len(df_products_equaller):
        prgsCounter = l- len(df_products_equaller)
        prgs.printProgressBar(prgsCounter, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
        id_hamyar = df_products_equaller.iat[0, thisIndex.id_hamyar]
        id_hesabro = df_products_equaller.iat[0, thisIndex.id_hesabro]
        product_hamyar = df_products_equaller.iat[0,thisIndex.product_hamyar]
        # product_hesabro = df_products_equaller.iat[0, thisIndex.product_hesabro]
        df_products_hesabro = df_product_list.loc[df_product_list["id"]==id_hesabro]
        product_hesabro = df_products_hesabro.iat[0, 1]
        
        dfProducts = dfData.loc[dfData[frCol.idCode]== id_hamyar]
        dfData = dfData.loc[dfData[frCol.idCode] != id_hamyar]
        
        # dfProducts.replace({frCol.idCode:id_hamyar},{frCol.idCode:id_hesabro},inplace=True, regex=True)
        # dfProducts.replace({frCol.merchandise:product_hamyar},{frCol.merchandise:product_hesabro},inplace=True, regex=True)
        # ls_name = []
        # ls_id = []
        for i in range(len(dfProducts)):
            dfProducts.iat[i,fr_index.merchandise]= product_hesabro
            dfProducts.iat[i,fr_index.idCode]= id_hesabro
        #     ls_name.append(product_hesabro)
        #     ls_id.append(id_hesabro)
        # dfProducts[frCol.idCode] = ls_id
        # dfProducts[frCol.merchandise]= ls_name
        ls_data.append(dfProducts)
        df_products_equaller = df_products_equaller.loc[df_products_equaller[pec.product_hamyar] != product_hamyar]
    prgs.printProgressBar(l, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
    ls_ans = []
    ls_ans.append(pd.concat(ls_data))
    ls_ans.append(dfData)
    df_ans = pd.concat(ls_ans)
    return df_ans
def branch_eqaller(df_branch_equaller,dfData):
    brIndex = get_index_branch_equaller(df_branch_equaller)
    l = len(df_branch_equaller)
    prtLines(2)
    print("branch equaller")
    for i in range(len(df_branch_equaller)):
        prgsCounter = i+1# l- len(dfData)
        prgs.printProgressBar(prgsCounter, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
        branch_id = df_branch_equaller.iat[i,brIndex.branch_id_hamyar]
        hesabro_branch_id = df_branch_equaller.iat[i,brIndex.branch_id_hesabro]
        dfData.replace({tjCol.idBranch:branch_id},{tjCol.idBranch:hesabro_branch_id},inplace=True)
        
        branch_hesabro = df_branch_equaller.iat[i,brIndex.branch_hesabro]
        
        condition = (dfData[tjCol.idBranch] == hesabro_branch_id)

        dfData.loc[condition, tjCol.branch] = branch_hesabro

        # dfData[tjCol.branch].mask(dfData[tjCol.idBranch] == hesabro_branch_id, branch_hesabro, inplace=True)
        # dfData.loc[dfData[tjCol.idBranch] == hesabro_branch_id, tjCol.branch] = branch_hesabro

        
    # dfData.to_excel("branch.xlsx",index=False)
    return dfData 
def seller_equaller_step2(dfData):
    
    this_index = get_index_seller_equaller_step2(df_seller_equaller_step2)
    l = len(df_seller_equaller_step2)
    prtLines(2)
    print("seller equaller step2")
    for i in range(len(df_seller_equaller_step2)):
        prgsCounter = i+1# l- len(dfData)
        prgs.printProgressBar(prgsCounter, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
        seller_id = df_seller_equaller_step2.iat[i,this_index.seller_id_hamyar]
        hesabro_seller_id = df_seller_equaller_step2.iat[i,this_index.seller_id_hesabro]
        seller_hesabro = df_seller_equaller_step2.iat[i,this_index.seller_hesabro]
        
        # print(this_index.seller_hesabro)
        if seller_id:
            
            dfData.replace({tjCol.Registrar_id:seller_id},{tjCol.Registrar_id:hesabro_seller_id},inplace=True)
            
            condition = (dfData[tjCol.Registrar_id] == hesabro_seller_id)

            dfData.loc[condition, tjCol.Registrar] = seller_hesabro
        else:
            seller_hamyar = df_seller_equaller_step2.iat[i,this_index.seller_hamyar]
            dfData.replace({tjCol.Registrar:seller_hamyar},{tjCol.Registrar:seller_hesabro},inplace=True)
            
            condition = (dfData[tjCol.Registrar] == seller_hesabro)

            dfData.loc[condition, tjCol.Registrar_id] = hesabro_seller_id
    return dfData
def seller_eqaller(df_seller_equaller,dfData):
    slIndex = get_index_seller_equaller(df_seller_equaller)
    l = len(df_seller_equaller)
    prtLines(2)
    print("seller equaller")
    for i in range(len(df_seller_equaller)):
        prgsCounter = i+1# l- len(dfData)
        prgs.printProgressBar(prgsCounter, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
        seller_id = df_seller_equaller.iat[i,slIndex.seller_id_hamyar]
        # print(slIndex.seller_hesabro)
        hesabro_seller_id = df_seller_equaller.iat[i,slIndex.seller_id_hesabro]
        dfData.replace({tjCol.Registrar_id:seller_id},{tjCol.Registrar_id:hesabro_seller_id},inplace=True)
        
        seller_hesabro = df_seller_equaller.iat[i,slIndex.seller_hesabro]
        condition = (dfData[tjCol.Registrar_id] == hesabro_seller_id)

        dfData.loc[condition, tjCol.Registrar] = seller_hesabro

        # dfData[tjCol.Registrar].mask(dfData[tjCol.Registrar_id] == hesabro_seller_id, seller_hesabro, inplace=True)
        # dfData.loc[dfData[tjCol.Registrar_id] == hesabro_seller_id, tjCol.Registrar] = seller_hesabro
    dfData = seller_equaller_step2(dfData)
    
    return dfData 