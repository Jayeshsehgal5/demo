from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from .views import DemoView

urlpatterns = [
    path('via_postman', DemoView.as_view(), name='Demo'),
    
]
