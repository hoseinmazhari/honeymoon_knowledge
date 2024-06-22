from django.urls import path
from . import views
app_name = "product_app"
urlpatterns = [
    
    path('',views.product_page,name="product_page"),
    path('order_point/',views.order_point,name="order_point"),
    path('active_in_site/',views.active_in_site,name="active_in_site"),
    path('correct_zero_prices_barcodes/',views.correct_zero_prices_barcodes,name="correct_zero_prices_barcodes"),
    path('obsolete/',views.obsolete,name="obsolete"),
    path('update/', views.update_variaty_of_products,name='update_variaty')
    
    
    
]
