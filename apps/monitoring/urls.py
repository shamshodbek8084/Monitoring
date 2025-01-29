from django.contrib import admin
from django.urls import path
from .views import ProjectAPIView

urlpatterns = [
    path('project/<int:pk>', ProjectAPIView.as_view(), name = 'project'),

]