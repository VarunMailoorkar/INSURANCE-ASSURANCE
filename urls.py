# urls.py

from django.urls import path
from .views import *

urlpatterns = [
    path('', welcome_view, name='welcome'),
    path('login/', user_login, name='login'),
    path('register/', user_registration, name='register'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('policy/', policy_list, name="policy_list"),  # Use name="policy_list" for consistency
    path('policynew/', policy_create, name="addpolicy"),  # Make sure to include trailing slash
    path('vehicle/', vehicle_lookup,name='vehicle_list'),
    path('vehiclenew/', vehicle_add,name='vehicle_add'),
    path('customer/',customer_list,name='customer_list'),
    path('customernew/',customer_add,name= 'customer_add'),
    path('accident/',accident_list,name='accident_list'),
    path('accidentnew/',accident_new,name='accident_new'),
    path('payment/',pay_list,name='payment_list'),
    path('paynew/',pay_record,name='pay_record'),
    
]
