from django import forms

class ExcelUploadForm(forms.Form):
    correct_barcodes = forms.FileField(label='فایل بارکدهای صحیح را انتخاب فرمایید')
    incorrect_barcodes = forms.FileField(label='فایل بارکد های اشتباه را انتخاب نمایید')

