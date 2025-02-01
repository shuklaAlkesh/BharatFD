from django.urls import path
from .views import faq_list_create

urlpatterns = [
    path('', faq_list_create, name='faq-list'),
]
