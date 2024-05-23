from django.urls import path
from . import views
app_name = "club_app"
urlpatterns = [
    
    path('',views.club_page,name="club_page"),
    path('Update_hesabro_customers_from_hamyar/',views.Update_hesabro_customers_from_hamyar,name="Update_hesabro_customers_from_hamyar"),
    path('Create_hesabro_customers_from_hamyar/',views.Create_hesabro_customers_from_hamyar,name="Create_hesabro_customers_from_hamyar"),
    
    
]
