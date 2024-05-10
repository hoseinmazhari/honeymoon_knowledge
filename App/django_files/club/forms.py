from django import forms

class ExcelUploadForm(forms.Form):
    Data = forms.FileField(label='فایل اکسل را انتخاب نمایید')
    