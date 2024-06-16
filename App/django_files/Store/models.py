from django.db import models

# Create your models here.
class Branchs(models.Model):
    title = models.CharField(max_length=255,null=False)
class Storeroom(models.Model):
    title = models.CharField(max_length=255, null=False)
    branch = models.ForeignKey(Branchs,on_delete=models.CASCADE)
class Factor_type(models.Model):
    title = models.CharField(max_length=255)
class Mobiles(models.Model):
    mobile = models.CharField(max_length=255)
    mobile_is_authenticated = models.BooleanField(default=False)
# class Address_type(models.Model):
    
#     title = models.CharField(max_length=255)
class Address(models.Model):
    
    CUSTOMER_ADDRESS_TYPES = [
        ("O":"دفتر"),
        ("H","خانه"),
        ("C","شرکت"),
        ("S","سایر"),
    ]
        

    
    address_type = models.CharField(max_length=1,choices=CUSTOMER_ADDRESS_TYPES, verbose_name= 'نوع آدرس')
    address = models.TextField(verbose_name = 'آدرس')
    postal_code = models.CharField(max_length=11, verbose_name = 'کد پستی')
    city = models.CharField(max_length=255, null=True)
    ostan = models.CharField(max_length=255,null=True)
    country = models.CharField(max_length=2555, null=True)

class Work(models.Model):
    title  =models.CharField(max_length=50, verbose_name= 'عنوان شغل')
# class Mobile(models.Model):
#     mobile = models.CharField(max_length=11, unique=True)
#     mobile_is_authenticated = models.BooleanField(default=False)
# class Address(models.Model):
#     address = models.TextField()

class Customer(models.Model):
    # first_name = models.CharField(max_length=255)
    # last_name = models.CharField(max_length=255)
    # nick_name = models.CharField(max_length=255)
    # mobile = models.ForeignKey(Mobiles,on_delete=models.CASCADE)
    # address = models.ForeignKey(Address, on_delete=models.PROTECT)
    customer_kinds = [
    ("N","عادی"),
    ("C","شرکت ها")
    ]
    customer_genders = [
        ("M", "مرد"),
        ("F", "زن")
    ]
    customer_nationality = [
        ("I", "ایرانی"),
        ("N", "خارجی")
    ]
    
    kind = models.CharField(max_length=1,choices=customer_kinds, verbose_name= 'نوع')
    gender = models.CharField(max_length=1,choices=customer_genders, verbose_name= 'جنسیت')
    nationality = models.CharField(max_length=1,choices=customer_nationality, verbose_name = 'ملیت')
    name = models.CharField(max_length=255, verbose_name = 'نام')
    last_name = models.CharField(max_length=255, verbose_name = 'نام خانوادگی')
    nick_name = models.CharField(max_length=255, verbose_name = 'نام نمایشی')
    birthday = models.CharField(max_length=10, verbose_name = 'تاریخ تولد')
    email = models.EmailField(verbose_name = 'ایمیل', unique=True)
    work = models.ForeignKey(Work,verbose_name='شغل')
    # mobile = models.CharField(max_length=11, verbose_name = 'موبایل', primary_key=True)
    mobile = models.ForeignKey(Mobiles,on_delete=models.PROTECT, verbose_name='موبایل')
    is_deleted = models.BooleanField(default=False)
    # mobile_authenticate = models.IntegerField(verbose_name = 'کد احراز هویت')
    # address_type = models.CharField(max_length=1,choices=customer_address_type, verbose_name = 'نوع آدرس')
    
    address = models.TextField( verbose_name = 'آدرس')
    des = models.TextField( verbose_name = 'توضیحات')
    rules = models.ForeignKey(Rules)
    def __str__(self):
        return self.nick_name



class Factors(models.Model):
    code = models.CharField(max_length=255 , null=False)
    storeroom = models.ForeignKey(Storeroom,on_delete=models.CASCADE)
    created = models.CharField(max_length=255)
    update = models.CharField(max_length=255)
    this_created = models.CharField(max_length=255)
    this_update = models.CharField(max_length=255)
    factor_type = models.ForeignKey(Factor_type,on_delete=models.PROTECT)

