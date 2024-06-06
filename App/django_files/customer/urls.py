from django.urls import path,include
from . import views
app_name = "customers_app"
urlpatterns = [
    
    path('',views.birthday_page,name="customer_page"),
    path('import_from_excel/',views.import_from_excel,name="import_from_excel"),
    path('create/',views.create,name='create')
    # path('arad/',views.arad_detail,name="arad_detail"),
]
