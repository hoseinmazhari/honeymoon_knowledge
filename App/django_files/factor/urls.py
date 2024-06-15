from django.urls import path
from . import views
app_name = "factor_app"
urlpatterns = [
    
    path('',views.product_page,name="factors_page"),
    path('get_sales/',views.fetch_sales,name="fetch_sales"),
    
]
