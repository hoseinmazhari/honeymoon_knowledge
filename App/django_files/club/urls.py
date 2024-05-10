from django.urls import path
from . import views
app_name = "club_app"
urlpatterns = [
    
    path('',views.club_page,name="club_page"),
    path('compare_customers_hesabro_hamyar/',views.compare_customers_hesabro_hamyar,name="compare_customers_hesabro_hamyar"),
    
    
    
]
