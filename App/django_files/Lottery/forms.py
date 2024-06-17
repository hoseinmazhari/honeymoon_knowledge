from django import forms

class ExcelUploadForm(forms.Form):
    correct_barcodes = forms.FileField(label='فایل پاسخ های صحیح (بارکد صحیح) را اینجا انتخاب فرمایید')
    incorrect_barcodes = forms.FileField(label='فایل پاسخ های (بارکد های) اشتباه را اینجا انتخاب نمایید')

