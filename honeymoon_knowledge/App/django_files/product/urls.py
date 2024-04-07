from django.urls import path
from . import views
app_name = "product_app"
urlpatterns = [
    
    path('',views.product_page,name="product_page"),
    path('order_point/',views.order_point,name="order_point"),
    path('active_in_site/',views.active_in_site,name="active_in_site"),
    
]
