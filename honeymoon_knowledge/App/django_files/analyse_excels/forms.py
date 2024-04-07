from django import forms

class ExcelUploadForm(forms.Form):
    invoices_file = forms.FileField(label='انتخاب فایل فاکتورها')
    targets_file = forms.FileField(label='انتخاب فایل تارگت ها')
