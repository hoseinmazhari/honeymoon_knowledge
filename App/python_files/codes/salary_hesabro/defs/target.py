import os, sys

# parent = os.path.abspath('.')
# sys.path.insert(1, parent)
from python_files.settings_python.app_structures import _make_farsi_text, tjCol, hesabroTjCol
# from main import _make_farsi_text
# from main import * 

class targetCol():
    branch = tjCol.branch
    adviser = "نام مشاور"
    adviser_id = "آیدی مشاور"
    shiftWork = "شیفت کاری"
    commission_percent = "درصد پورسانت"
    commission_with_checkout = "پورسانت با تسویه مرجوعی"
    commission_without_checkout = "پورسانت بدون تسویه با مرجوعی"
    goodTarget = "تارگت خوب"
    perfectTarget = "تارگت ایده ال"
    baseSalary = "حقوق پایه"
    branch_id = hesabroTjCol.branch_id
    # seller_id = hesabroTjCol.seller_id


def getIndexTarget(df):
    thisCols = targetCol()
    thisIndex=-1
    for col in df.columns:        
        thisIndex+=1
        if thisCols.branch == col:
            thisCols.branch = thisIndex # type: ignore
        elif thisCols.adviser == col:
            thisCols.adviser = thisIndex# type: ignore
        elif col == thisCols.adviser_id:
            thisCols.adviser_id = thisIndex #type: ignore
        elif thisCols.shiftWork == col:
            thisCols.shiftWork = thisIndex# type: ignore
        elif thisCols.commission_percent == col:
            thisCols.commission_percent = thisIndex# type: ignore
        elif thisCols.commission_with_checkout == col:
            thisCols.commission_with_checkout = thisIndex# type: ignore
        elif thisCols.commission_without_checkout == col:
            thisCols.commission_without_checkout = thisIndex
        elif thisCols.goodTarget == col:
            thisCols.goodTarget = thisIndex# type: ignore
        elif thisCols.perfectTarget == col:
            thisCols.perfectTarget = thisIndex# type: ignore
        elif thisCols.baseSalary == col:
            thisCols.baseSalary = thisIndex # type: ignore
        elif thisCols.branch_id == col:
            thisCols.branch_id = thisIndex # type: ignore
        # elif thisCols.seller_id == col:
        #     thisCols.seller_id = thisIndex # type: ignore
    return thisCols
