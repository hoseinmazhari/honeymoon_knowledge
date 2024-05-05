from django.urls import path,include
from . import views
app_name = "birthday_app"
urlpatterns = [
    
    path('',views.birthday_page,name="birthday_page"),
    path('update_db_to_sendSms/',views.update_db_to_sendSms,name="update_db_to_sendSms"),
    path('update_birthday_call_brs/',views.update_birthday_call_brs,name='update_birthday_call_brs')
    # path('arad/',views.arad_detail,name="arad_detail"),
]
