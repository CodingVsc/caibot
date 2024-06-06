from django.urls import path
from .views import check_account_number, send_message

urlpatterns = [
    path('acc/<str:account_number>/', check_account_number, name='check_account_number'),
    path('message/', send_message, name='send_message'),
]