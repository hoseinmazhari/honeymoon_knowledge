import os, sys

# parent = os.path.abspath('.')
# sys.path.insert(1, parent)
from python_files.settings_python.app_structures import _make_farsi_text, tjCol, hesabroTjCol
# from main import _make_farsi_text
# from main import * 

class targetCol():
    branch = tjCol.branch
    adviser = "نام مشاور"
    shiftWork = "شیفت کاری"
    commission_percent = "درصد پورسانت"
    commission = "پورسانت"
    goodTarget = "تارگت خوب"
    perfectTarget = "تارگت ایده ال"
    baseSalary = "حقوق پایه"
    branch_id = hesabroTjCol.branch_id
    seller_id = hesabroTjCol.seller_id


def getIndexTarget(df):
    thisClass = targetCol()
    thisIndex=-1
    for col in df.columns:        
        thisIndex+=1
        if thisClass.branch == col:
            thisClass.branch = thisIndex # type: ignore
        elif thisClass.adviser == col:
            thisClass.adviser = thisIndex# type: ignore
        elif thisClass.shiftWork == col:
            thisClass.shiftWork = thisIndex# type: ignore
        elif thisClass.commission_percent == col:
            thisClass.commission_percent = thisIndex# type: ignore
        elif thisClass.commission == col:
            thisClass.commission = thisIndex# type: ignore
        elif thisClass.goodTarget == col:
            thisClass.goodTarget = thisIndex# type: ignore
        elif thisClass.perfectTarget == col:
            thisClass.perfectTarget = thisIndex# type: ignore
        elif thisClass.baseSalary == col:
            thisClass.baseSalary = thisIndex # type: ignore
        elif thisClass.branch_id == col:
            thisClass.branch_id = thisIndex # type: ignore
        elif thisClass.seller_id == col:
            thisClass.seller_id = thisIndex # type: ignore
    return thisClass
