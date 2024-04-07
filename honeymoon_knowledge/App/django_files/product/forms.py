from django import forms

class ExcelUploadForm(forms.Form):
    product_list = forms.FileField(label='فایل لیست کالاها را انتخاب نمایید')
    
