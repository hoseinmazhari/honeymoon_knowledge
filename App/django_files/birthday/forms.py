from django import forms

class ExcelUploadForm(forms.Form):
    invoices_merged = forms.FileField(label='انتخاب فایل فاکتورهای ادغام شده با همیار')
    
