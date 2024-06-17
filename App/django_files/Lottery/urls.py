from django.urls import path
from . import views
app_name = "lottery_app"

urlpatterns = [
    
    path('',views.lottery_page,name="lottery_page"),
    path('send_sms_to_invalid_response/',views.send_sms_to_invalid_response,name="send_sms_to_invalid_response"),
   
]