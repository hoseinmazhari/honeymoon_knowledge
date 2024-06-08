from django.db import models
from django_files.rules.models import Rules
customer_kinds = (
    ("عادی","عادی"),
    ("شرکت ها","شرکت ها"),
)
customer_genders = (
    ("مرد", "مرد"),
    ("زن", "زن")
)
customer_nationality = (
    ("ایرانی", "ایرانی"),
    ("خارجی", "خارجی"),

)
customer_address_type =(
    ("دفتر":"دفتر"),
    ("خانه","خانه"),
    ("شرکت","شرکت"),
    ("سایر","سایر"),

)
# Create your models here.
class Work(models.Model):
    title  =models.CharField(max_length=50, verbose_name= 'عنوان شغل')
class Customer(models.Model):
    kind = models.CharField(max_length=10,choices=customer_kinds, verbose_name= 'نوع')
    gender = models.CharField(max_length=10,choices=customer_genders, verbose_name= 'جنسیت')
    nationality = models.CharField(max_length=10,choices=customer_nationality, verbose_name = 'ملیت')
    name = models.CharField(max_length=100, verbose_name = 'نام')
    last_name = models.CharField(max_length=100, verbose_name = 'نام خانوادگی')
    nick_name = models.CharField(max_length=100, verbose_name = 'نام نمایشی')
    birthday = models.CharField(max_length=10, verbose_name = 'تاریخ تولد')
    email = models.EmailField(verbose_name = 'ایمیل')
    work = models.ForeignKey(Work,verbose_name='شغل')
    mobile = models.CharField(max_length=11, verbose_name = 'موبایل', primary_key=True)
    is_deleted = models.BooleanField(default=False)
    mobile_authenticate = models.IntegerField(verbose_name = 'کد احراز هویت')
    address_type = models.CharField(max_length=20,choices=customer_address_type, verbose_name = 'نوع آدرس')
    postal_code = models.CharField(max_length=11, verbose_name = 'کد پستی')
    address = models.CharField(max_length=512, verbose_name = 'آدرس')
    des = models.CharField(max_length=512, verbose_name = 'توضیحات')
    rules = models.ForeignKey(Rules)
    def __str__(self):
        return self.nick_name