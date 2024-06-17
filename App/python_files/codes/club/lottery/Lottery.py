
import os, sys, pandas as pd, datetime,time

# parent = os.path.abspath('.')
# sys.path.insert(1, parent)

from python_files.settings_python.app_structures import export_path, mediaName,\
    _make_farsi_text, prtLines, getDateTimeForFileName, getIndexTj,myDataType_names, \
    tjCol, condition, loadData, yearDetail, monthCol, monthsSelector,Lottery_Cols,get_index_Lottery_Cols

def make_file(df,thisFileName,xlsxFileNum,thisPath):
    xlsxFileNum += 1
    # thisFileName = f'جمع فروش هر مشاور.xlsx'
    thisFileName = f"{xlsxFileNum}- {thisFileName}"
    # file_name = 'MarksData.xlsx'
 
    # creating an ExcelWriter object
    # file_name = 'MarksData.xlsx'
 
    # creating an ExcelWriter object
    with pd.ExcelWriter(f"{thisPath}/{thisFileName}") as writer:
        # writing to the 'Employee' sheet
        df.to_excel(writer, sheet_name='Sales', index=False)
    # df.to_excel(thisFileName,index = False)
    prtLines(2)
    print(_make_farsi_text(f"{thisFileName} استخراج و ذخیره شد"))
    prtLines(2)
    return xlsxFileNum
def incorrect_remover_from_corrects(df_correct_barcode, df_incorrect_barcode):
        xlsxFileNum = 0
        appPath = os.getcwd()
        selectedOption="0"
        while len(selectedOption)<5:
            selectedOption = "0" + selectedOption

        # start coding
        #
        folderName = f"{selectedOption}- لیست مشتریان برای پیام اصلاح بارکدها {getDateTimeForFileName()}"
        prtLines(2)
        print(_make_farsi_text("انتخاب شما: "))
        print(_make_farsi_text(folderName))
        thisPath = os.getcwd()
        thisPath = f"{thisPath}/{mediaName}"
        # os.chdir(thisPath)
        prtLines(2)
        print(_make_farsi_text(": انتقال مسیر خروجی فایل های به"))
        print(thisPath)
        try:
            os.mkdir(f"{thisPath}/{export_path}")
        except:
            pass
        thisPath = f"{thisPath}/{export_path}"
        # os.chdir(thisPath)
        prtLines(2)
        print(_make_farsi_text(": انتقال مسیر خروجی فایل های به"))
        print(thisPath)
        try:
            os.mkdir(f"{thisPath}/{folderName}")
        except:
            pass
        thisPath = f"{thisPath}/{folderName}"
        # os.chdir(thisPath)
        prtLines(2)
        print(_make_farsi_text(": انتقال مسیر خروجی فایل های به"))
        print(thisPath)
        thisIndex = get_index_Lottery_Cols(df_correct_barcode)
        thisCols = Lottery_Cols()
        while len(df_correct_barcode):
             mobile = df_correct_barcode.iat[0, thisIndex.mobile]
             if len(df_incorrect_barcode.loc[df_incorrect_barcode[thisCols.mobile]==mobile]):
                  df_incorrect_barcode = df_incorrect_barcode.loc[df_incorrect_barcode[thisCols.mobile] != mobile]
        if len(df_incorrect_barcode):
            xlsxFileNum += 1
            thisFileName = "مشتریانی که بارکد صحیح را هیچ وقت صحیح ارسال نکرده اند.xlsx"
            xlsxFileNum = make_file(df_incorrect_barcode,thisFileName,xlsxFileNum,thisPath)
            # dfCheckoutPm.to_excel(,index=False)
            return df_incorrect_barcode,thisPath,folderName

# salary()

