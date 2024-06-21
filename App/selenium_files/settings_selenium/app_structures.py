
class report_output_cols():
    row = "ردیف"
    mobile = "موبایل"
    name = "نام و نام خانوادگی"
    birthday = "تاریخ تولد"
    gender = "جنسیت"
    email = "ایمیل"
    trusted = "تایید شده"
    passport_id = "کدملی-پاسپورت"
    id = "آیدی"
    
def get_index_report_output_cols(df):
    thisClass = report_output_cols()
    thisItter = -1
    for col in df.columns:
        thisItter += 1
        if col== thisClass.birthday:
            thisClass.birthday = thisItter
        elif col == thisClass.row:
            thisClass.row = thisItter
        elif col == thisClass.mobile:
            thisClass.mobile = thisItter
        elif col == thisClass.name:
            thisClass.name = thisItter
        elif col == thisClass.gender:
            thisClass.gender = thisItter
        elif col == thisClass.email:
            thisClass.email = thisItter
        elif col == thisClass.trusted:
            thisClass.trusted = thisItter
        elif col == thisClass.passport_id:
            thisClass.passport_id = thisItter
        elif col == thisClass.id:
            thisClass.id = thisItter
    return thisClass
