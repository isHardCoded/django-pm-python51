from django.urls import path
from contacts.views import *

urlpatterns = [
    path('send/', send_message, name='send_message'),
]