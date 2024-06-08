from django.db import models

# Create your models here.
class Rules(models.Model):
    title = models.CharField(max_length=100, verbose_name= 'عنوان')
    des = models.CharField(max_length=512,verbose_name='توضیحات')