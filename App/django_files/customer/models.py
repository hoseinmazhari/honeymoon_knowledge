from django.db import models
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
# Create your models here.
class Customer(models.Model):
    kind = models.CharField(max_length=10,choices=customer_kinds)
    gender = models.CharField(max_length=10,choices=customer_genders)
    nationality = models.CharField(max_length=10,choices=customer_nationality)
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    nick_name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name