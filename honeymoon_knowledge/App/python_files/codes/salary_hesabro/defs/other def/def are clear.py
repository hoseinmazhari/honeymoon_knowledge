class concatSaleWithTargetCol():
    branch = invoicesMergeCol.branch
    Registrar = invoicesMergeCol.Registrar
    Received = invoicesMergeCol.Received
    shiftWork = invoicesMergeCol.shiftWork
    exclusiveReceived = invoicesMergeCol.exclusiveReceived
    nonExclusiveReceived  = invoicesMergeCol.nonExclusiveReceived
    exclusivePercent= targetCol.exclusivePercent
    nonExclusivePercent = targetCol.nonExclusivePercent
    commissionExclusive = "پورسانت نیش انحصاری"
    commission_nonExclusive = "پورسانت نیش تجاری"
    commission = "مجموع پورسانت"
class deductionCommissionCol(targetCol):
    Received = invoicesMergeCol.Received
    exclusiveReceived = invoicesMergeCol.exclusiveReceived
    nonExclusiveReceived  = invoicesMergeCol.nonExclusiveReceived
    commissionExclusive = "پورسانت نیش انحصاری"
    commission_nonExclusive = "پورسانت نیش تجاری"
    commission = "مجموع پورسانت"
    deduction = "کسر بابت تارگت"
def getIndexDeductionCommission(df):
    dfCols = deductionCommissionCol()
    thisIndex=-1
    for col in df.columns:        
        thisIndex+=1
        if dfCols.branch == col:
            dfCols.branch = thisIndex# type: ignore
        elif dfCols.adviser == col:
            dfCols.adviser = thisIndex# type: ignore
        elif dfCols.shiftWork == col:
            dfCols.shiftWork = thisIndex# type: ignore
        elif dfCols.exclusivePercent == col:
            dfCols.exclusivePercent = thisIndex# type: ignore
        elif dfCols.nonExclusivePercent == col:
            dfCols.nonExclusivePercent = thisIndex# type: ignore
        elif dfCols.goodTarget == col:
            dfCols.goodTarget = thisIndex# type: ignore
        elif dfCols.perfectTarget == col:
            dfCols.perfectTarget = thisIndex# type: ignore
        elif dfCols.Received == col:
            dfCols.Received = thisIndex# type: ignore
        elif dfCols.exclusiveReceived == col:
            dfCols.exclusiveReceived = thisIndex# type: ignore
        elif dfCols.nonExclusiveReceived == col:
            dfCols.nonExclusiveReceived = thisIndex# type: ignore
        elif dfCols.commissionExclusive == col:
            dfCols.commissionExclusive = thisIndex# type: ignore
        elif dfCols.commission_nonExclusive == col:# type: ignore
            dfCols.commission_nonExclusive = thisIndex# type: ignore
        elif dfCols.commission == col:
            dfCols.commission = thisIndex# type: ignore
        elif dfCols.deduction == col:
            dfCols.deduction = thisIndex# type: ignore
    return dfCols
class commissionAndFinesCol():
    Registrar = concatSaleWithTargetCol.Registrar
    commisson = concatSaleWithTargetCol.commission
    exclusive_fines= returnedCommissionCol.exclusive_deductible
    nonExclusive_fines  =returnedCommissionCol.nonExclusive_deductible
    salary= "حقوق قابل پرداخت"
def getIndexcommissionAndFines(df):
    dfCols = commissionAndFinesCol()
    thisIndex=-1
    for col in df.columns:        
        thisIndex+=1
        if dfCols.Registrar == col:
            dfCols.Registrar = thisIndex# type: ignore
        elif dfCols.commisson == col:
            dfCols.commisson = thisIndex# type: ignore
        elif dfCols.nonExclusive_fines == col:
            dfCols.nonExclusive_fines = thisIndex# type: ignore
        elif dfCols.exclusive_fines == col:
            dfCols.exclusive_fines = thisIndex# type: ignore
        elif dfCols.salary == col:
            dfCols.salary = thisIndex# type: ignore
    return dfCols
# class commissionAndFinesIndex():
#     Registrar =0
#     commisson = 1
#     exclusive_fines= 2
#     nonExclusive_fines  =3
#     salary=4

class commissionIndex():
    register=0
    Received =1 
    exclusive = 2
    nonExclusive =3
    commission =2

class commissionCol():
    register=concatSaleWithTargetCol.Registrar
    TotalReceived =concatSaleWithTargetCol.Received
    exclusive = "فروش نیش انحصاری"
    nonExclusive = "فروش نیش تجاری"
    commission =concatSaleWithTargetCol.commission

class finalCommmissionCol():
    branch= deductionCommissionCol.branch
    adviser = deductionCommissionCol.adviser
    goodTarget = deductionCommissionCol.goodTarget
    saleAmount = deductionCommissionCol.Received
    commissionExclusive = deductionCommissionCol.commissionExclusive
    commission_nonExclusive = deductionCommissionCol.commission_nonExclusive
    commission = deductionCommissionCol.commission
    deductionTarget = "قابل کسر برای تارگت"
    deductionReturns = "قابل کسر برای مرجوعی"
    payableCommission = "پورسانت قابل پرداخت"

#################################################################################
#################################################################################
#################################################################################
def finalCommission(dfData,df_targets,df_commissionAndFines,deductionPercent):
    df_employe = pd.DataFrame()
    commissionAndFinesIndex = getIndexcommissionAndFines(df_commissionAndFines)
    # l= len(df_targets)

    targetIndex = getIndexTarget(df_targets)
    deductionCommissionIndex = getIndexDeductionCommission(dfData)
    while(len(df_targets)):
        adviser = df_targets.iloc[0, targetIndex.adviser]
        baseSalary = 0 
        baseSalary = df_targets.iat[0,targetIndex.baseSalary]
        thisTarget = df_targets.iloc[0,targetIndex.goodTarget]
        branch = df_targets.iloc[0,targetIndex.branch]
        dfAdviser = dfData.loc[dfData[deductionCommissionCol.adviser]==adviser]
        
        saleAmount = 0
        goodTarget =0
        commissionExclusive =0
        commission_nonExclusive = 0
        commission = 0
        deductionTarget = 0
        deductionReturn =0
        Received=0
        dfTest = df_commissionAndFines.loc[df_commissionAndFines[commissionAndFinesCol.Registrar]==adviser]
        if(len(dfTest)):
            testCommission = dfTest.iloc[0,commissionAndFinesIndex.commisson]
            deductionReturn = dfTest.iloc[0,commissionAndFinesIndex.nonExclusive_fines]+dfTest.iloc[0,commissionAndFinesIndex.exclusive_fines]
            for i in range(len(dfAdviser)):
                currentTarget = dfAdviser.iloc[i,deductionCommissionIndex.goodTarget]
                if thisTarget:
                    try:
                        if dfAdviser.iloc[i,deductionCommissionIndex.Received] != 0:
                            if thisTarget != 0:
                                if currentTarget != 0:
                                    saleAmount += (((dfAdviser.iloc[i,deductionCommissionIndex.Received]) * thisTarget)/currentTarget)
                    except:
                        pass
                else:
                    saleAmount += dfAdviser.iloc[i,deductionCommissionIndex.Received]    
                Received += dfAdviser.iloc[i,deductionCommissionIndex.Received]
                commissionExclusive+=dfAdviser.iloc[i,deductionCommissionIndex.commissionExclusive]
                commission_nonExclusive += dfAdviser.iloc[i,deductionCommissionIndex.commission_nonExclusive]
                commission += dfAdviser.iloc[i,deductionCommissionIndex.commission]
            if saleAmount< thisTarget:
                diffSale = thisTarget - saleAmount
                if deductionPercent:
                    deductionTarget = diffSale*deductionPercent/100
                else:
                    deductionTarget = 0
            payableCommission = commission-deductionTarget-deductionReturn
            df_employe = df_employe.append({finalCommmissionCol.branch:branch,finalCommmissionCol.adviser:adviser, finalCommmissionCol.goodTarget:thisTarget,"فروش واقعی":Received,finalCommmissionCol.saleAmount:saleAmount,finalCommmissionCol.commissionExclusive:commissionExclusive,finalCommmissionCol.commission_nonExclusive:commission_nonExclusive,finalCommmissionCol.commission:commission,finalCommmissionCol.deductionTarget:deductionTarget,finalCommmissionCol.deductionReturns:deductionReturn,finalCommmissionCol.payableCommission:payableCommission,targetCol.baseSalary:baseSalary,"final":payableCommission+baseSalary},ignore_index=True) # type: ignore
        df_targets = df_targets.loc[df_targets[targetCol.adviser]!= adviser]
    return df_employe
def deductionCommision(dfData,df_targets):
    df_employes=pd.DataFrame()
    targetIndex = getIndexTarget(df_targets)
    l= len(dfData)
    prtLines(3)
    invoicesMergeIndex = getIndexInvoicesMerge(dfData)
    print(_make_farsi_text("ادغام فروش با تارگت"))
    while len(dfData):
        
        branch= dfData.iloc[0,invoicesMergeIndex.branch]
        # print(branchFR)
        prgsCounter = l- len(dfData)
        prgs.printProgressBar(prgsCounter, l, prefix = 'Progress:', suffix = 'Complete', length = 25)

        df_branch = dfData.loc[dfData[invoicesMergeCol.branch]==branch]
        while len(df_branch):
            shiftWork = df_branch.iloc[0,invoicesMergeIndex.shiftWork]
            df_thisTarget = df_targets.loc[df_targets[targetCol.branch]==branch]
            df_thisTarget = df_thisTarget.loc[df_thisTarget[targetCol.shiftWork]==shiftWork]
            if len(df_thisTarget):
                exclusivePercent = df_thisTarget.iloc[0,targetIndex.exclusivePercent]
                nonExclusivePercent= df_thisTarget.iloc[0,targetIndex.nonExclusivePercent]
                goodTarget = df_thisTarget.iloc[0,targetIndex.goodTarget]
            else:
                exclusivePercent = 0
                nonExclusivePercent= 0
                goodTarget = 0
            dfShiftWork = df_branch.loc[df_branch[invoicesMergeCol.shiftWork]==shiftWork]
            while len(dfShiftWork):
                Registrar = dfShiftWork.iloc[0,invoicesMergeIndex.Registrar]
                Received = dfShiftWork.iloc[0,invoicesMergeIndex.Received]
                exclusiveReceived = dfShiftWork.iloc[0,invoicesMergeIndex.exclusiveReceived]
                nonExclusiveReceived = dfShiftWork.iloc[0,invoicesMergeIndex.nonExclusiveReceived]
                Received = dfShiftWork.iloc[0,invoicesMergeIndex.Received]
                if exclusivePercent:
                    commissionExclusive = exclusiveReceived*exclusivePercent/100
                else:
                    commissionExclusive = 0
                if nonExclusivePercent:
                    commission_nonExclusive = nonExclusiveReceived*nonExclusivePercent/100
                else:
                    commission_nonExclusive = 0
                commission = commission_nonExclusive+commissionExclusive
                df_employes = df_employes.append({deductionCommissionCol.branch:branch,deductionCommissionCol.adviser:Registrar,
                        deductionCommissionCol.Received:Received, deductionCommissionCol.shiftWork:shiftWork,
                        deductionCommissionCol.exclusiveReceived:exclusiveReceived,
                        deductionCommissionCol.nonExclusiveReceived:nonExclusiveReceived,
                        deductionCommissionCol.exclusivePercent:exclusivePercent,
                        deductionCommissionCol.nonExclusivePercent:nonExclusivePercent,
                        deductionCommissionCol.commissionExclusive:commissionExclusive,deductionCommissionCol.commission_nonExclusive:commission_nonExclusive,
                        deductionCommissionCol.commission:commission,deductionCommissionCol.goodTarget:goodTarget
                        },ignore_index = True) # type: ignore
                dfShiftWork= dfShiftWork.loc[dfShiftWork[invoicesMergeCol.Registrar]!=Registrar]
            df_branch = df_branch.loc[df_branch[invoicesMergeCol.shiftWork]!=shiftWork]
        dfData = dfData.loc[dfData[invoicesMergeCol.branch]!=branch]
    prgs.printProgressBar(l, l, prefix = 'Progress:', suffix = 'Complete', length = 25)
    return df_employes


def commissionAndFines(dfData, dfReturnM):
    CSTC=concatSaleWithTargetCol()
    CSTI= getIndexConcatSaleWithTarget(dfData) #concatSaleWithTargetIndex()
    RCC= returnedCommissionCol()
    RCI =getIndexReturnedCommission(dfReturnM)
    CAFC = commissionAndFinesCol()
    # CAFI = commissionAndFinesIndex()
    df_ans=pd.DataFrame()
    while len(dfData):
        Registrar= dfData.iloc[0,CSTI.Registrar]
        dfRegistrar = dfData.loc[dfData[CSTC.Registrar]==Registrar]
        Received = int(dfRegistrar[CSTC.commission].sum())
        dfReturn = dfReturnM.loc[dfReturnM[RCC.Registrar]==Registrar]
        if len(dfReturn):
            nonExclusive_fines= int(dfReturn[RCC.nonExclusive_deductible].sum())
            exclusive_fines= int(dfReturn[RCC.exclusive_deductible].sum())
        else:
            nonExclusive_fines=0
            exclusive_fines =0
        
        df_ans= df_ans.append({CAFC.Registrar:Registrar,CAFC.nonExclusive_fines:nonExclusive_fines,
                CAFC.exclusive_fines:exclusive_fines,CAFC.commisson:Received},ignore_index=True) # type: ignore
        dfData= dfData.loc[dfData[CSTC.Registrar]!=Registrar]


    return df_ans

def MergeTargetWithReturned(dfData,dfTargets):
    targetIndex = getIndexTarget(dfTargets)
    
    df_ans = pd.DataFrame()
    MMSOBC = mergeMissSaleOnBrCol()
    MMSOBI = getIndexMergeMissSaleOnBr(dfData)
    
    RCC=returnedCommissionCol()
    # RCI=returnedCommissionIndex()
    l = len(dfData)
    prtLines(3)
    print(_make_farsi_text("برنامه در حال ادغام مرجوعی و تارگت ها برای هر شعبه وشیفت می باشد"))
    print()
    while len(dfData):
        Registrar= dfData.iloc[0,MMSOBI.Registrar]
        
        prgsCounter = l- len(dfData)
        prgs.printProgressBar(prgsCounter, l, prefix = 'Progress:', suffix = 'Complete', length = 25)
        
        dfRegistrar = dfData.loc[dfData[MMSOBC.Registrar]==Registrar]
        
        while len(dfRegistrar):
            branch = dfRegistrar.iloc[0,MMSOBI.branch]
            dfBranch= dfRegistrar.loc[dfRegistrar[MMSOBC.branch]==branch]
            dfTargetsBranch = dfTargets.loc[dfTargets[targetCol.branch]==branch]
            if len(dfTargetsBranch):
                while len(dfBranch):
                    shiftWork = dfBranch.iloc[0,MMSOBI.shiftWork]
                    dfShiftWork = dfBranch.loc[dfBranch[MMSOBC.shiftWork]==shiftWork]
                    dfTargetShiftWork = dfTargetsBranch.loc[dfTargetsBranch[targetCol.shiftWork]==shiftWork]
                    exclusivePercent = dfTargetShiftWork.iloc[0,targetIndex.exclusivePercent]
                    exclusive_returned=int(dfShiftWork.iloc[0,MMSOBI.exclusive_returned])
                    exclusive_deductible= exclusive_returned*exclusivePercent/100
                    nonExclusivePercent = dfTargetShiftWork.iloc[0,targetIndex.nonExclusivePercent]
                    nonExclusive_returned=int(dfShiftWork.iloc[0,MMSOBI.nonExclusive_returned])
                    nonExclusive_deductible = nonExclusive_returned*nonExclusivePercent/100
                    df_ans=df_ans.append({RCC.Registrar:Registrar,RCC.branch:branch,RCC.shiftWork:shiftWork,
                                    RCC.exclusive_returned:exclusive_returned,RCC.exclusivePercent:exclusivePercent,
                                    RCC.exclusive_deductible:exclusive_deductible,
                                    RCC.nonExclusive_returned:nonExclusive_returned,RCC.nonExclusivePercent:nonExclusivePercent,
                                    RCC.nonExclusive_deductible:nonExclusive_deductible
                    },ignore_index=True) # type: ignore
                    dfBranch=dfBranch.loc[dfBranch[MMSOBC.shiftWork]!=shiftWork]
            dfRegistrar=dfRegistrar.loc[dfRegistrar[MMSOBC.branch]!=branch]
        dfData = dfData.loc[dfData[MMSOBC.Registrar]!=Registrar]
    prgs.printProgressBar(l, l, prefix = 'Progress:', suffix = 'Complete', length = 25)
    # df_ans.to_excel("test")
    return df_ans



def MergeMissSaleOnBr(dfMisSale,shiftWork,xlsxFileNum):
    
    from codes.returned import returnedSaleItemsNish as RSI
    
    EMSI= RSI.getIndexEMSI(dfMisSale)
    # EMSI =RSI.EMSI()
    # print()
    # print(EMSC.quantity)
    # print(EMSI.quantity)
    # print()
    df_ans=pd.DataFrame()
    MMSOBC = mergeMissSaleOnBrCol()
    MMSOBI = getIndexMergeMissSaleOnBr(dfMisSale)
    l = len(dfMisSale)
    prtLines(3)
    print(_make_farsi_text(f"برنامه در حال محاسبه مجموع مرجوعی های مشاوران در {shiftWork} هر شعبه می باشد"))
    print()
    dfRgs=pd.DataFrame()
    while len(dfMisSale):
        Registrar= dfMisSale.iloc[0,EMSI.saleRegistrarLbl]
        
        prgsCounter = l- len(dfMisSale)
        prgs.printProgressBar(prgsCounter, l, prefix = 'Progress:', suffix = 'Complete', length = 25)
        
        dfRegistrar = dfMisSale.loc[dfMisSale[EMSC.saleRegistrarLbl]==Registrar]
        dfRgs = dfRgs.append(dfRegistrar,ignore_index=True) # type: ignore
        
        while len(dfRegistrar):
            branch = dfRegistrar.iloc[0,EMSI.branch]
            dfBranch= dfRegistrar.loc[dfRegistrar[EMSC.branch]==branch]
            exclusive_totalOne = int(dfBranch[EMSC.exclusive_singleCollection].sum())
            exclusive_returnUsedCharge = int(dfBranch[EMSC.exclusive_returnUsedCharge].sum())
            exclusiveDiscount = int(dfBranch[EMSC.exclusiveDiscount].sum())
            exclusive_returned=exclusive_totalOne-exclusive_returnUsedCharge-exclusiveDiscount
            nonExclusive_totalOne = int(dfBranch[EMSC.nonExclusive_singleCollection].sum())
            nonExclusive_returnUsedCharge = int(dfBranch[EMSC.nonExclusive_returnUsedCharge].sum())
            nonExclusive_Discount = int(dfBranch[EMSC.nonExclusive_Discount].sum())
            nonExclusive_returned=nonExclusive_totalOne-nonExclusive_returnUsedCharge-nonExclusive_Discount
            df_ans=df_ans.append({MMSOBC.Registrar:Registrar,MMSOBC.branch:branch,MMSOBC.exclusive_totalOne:exclusive_totalOne,
                    MMSOBC.exclusive_Discount:exclusiveDiscount,MMSOBC.exclusive_returnUsedCharge:exclusive_returnUsedCharge,
                    MMSOBC.exclusive_returned:exclusive_returned,
                    MMSOBC.nonExclusive_totalOne:nonExclusive_totalOne,
                    MMSOBC.nonExclusive_Discount:nonExclusive_Discount,
                    MMSOBC.nonExclusive_returnUsedCharge:nonExclusive_returnUsedCharge,MMSOBC.nonExclusive_returned:nonExclusive_returned,
                    MMSOBC.shiftWork:shiftWork},ignore_index=True) # type: ignore
            dfRegistrar=dfRegistrar.loc[dfRegistrar[EMSC.branch]!=branch]
        dfMisSale=dfMisSale.loc[dfMisSale[EMSC.saleRegistrarLbl]!=Registrar]
    prgs.printProgressBar(100, 100, prefix = 'Progress:', suffix = 'Complete', length = 25)
    dfRgs.to_excel(f"{xlsxFileNum}- مرجوعی های {shiftWork}.xlsx",index=False)
    df_ans.to_excel(f"{xlsxFileNum}- مرجوعی های ادغام شده مشاوران در {shiftWork}.xlsx",index=False)
    return df_ans



class saleMergedWithTargetIndex():
    branch = targetCol.branch
    Registrar = tjCol.Registrar
    Received = tjCol.Received
    shiftWork = condition.shiftWork
    exclusivePercent= targetCol.exclusivePercent
    nonExclusivePercent = targetCol.nonExclusivePercent
    commission = "پورسانت"

class returnedCommissionCol():
    Registrar= mergeMissSaleOnBrCol.Registrar
    branch= mergeMissSaleOnBrCol.branch
    shiftWork = mergeMissSaleOnBrCol.shiftWork
    exclusive_returned=mergeMissSaleOnBrCol.exclusive_returned
    exclusivePercent = targetCol.exclusivePercent
    exclusive_deductible = "قابل کسر برای نیش انحصاری"
    nonExclusive_returned= mergeMissSaleOnBrCol.nonExclusive_returned
    nonExclusivePercent = targetCol.nonExclusivePercent
    nonExclusive_deductible = "قابل کسر برای نیش تجاری"

def getIndexReturnedCommission(df):
    thisIndex = -1
    thisClass = returnedCommissionCol()
    for col in df.columns:
        thisIndex += 1
        if col == thisClass.branch:
            thisClass.branch = thisIndex # type: ignore
        elif col == thisClass.exclusive_deductible:
            thisClass.exclusive_deductible = thisIndex # type: ignore
        elif col == thisClass.exclusive_returned:
            thisClass.exclusive_returned = thisIndex # type: ignore
        elif col == thisClass.exclusivePercent:
            thisClass.exclusivePercent = thisIndex # type: ignore
        elif col == thisClass.nonExclusive_deductible:
            thisClass.nonExclusive_deductible = thisIndex # type: ignore
        elif col == thisClass.nonExclusive_returned:
            thisClass.nonExclusive_returned = thisIndex # type: ignore
        elif col == thisClass.nonExclusivePercent:
            thisClass.nonExclusivePercent = thisIndex # type: ignore
        elif col == thisClass.Registrar:
            thisClass.Registrar =  thisIndex # type: ignore
        elif col == thisClass.shiftWork:
            thisClass.shiftWork = thisIndex # type: ignore
