from django.contrib import admin
from django.urls import path
# from .views import ProjectAPIView
from .views import (Create_project,
                    Read_project,
                    List_project,
                    Update_project,
                    Delete_project)

urlpatterns = [
    # path('project/<int:pk>', ProjectAPIView.as_view(), name = 'project'),
    path('create_project/<int:pk>', Create_project.as_view(), name='create_project'),
    path('read_project/<int:pk>', Read_project.as_view(), name='read_project'),
    path('list_project/<int:pk>', List_project.as_view(), name='list_project'),
    path('update_project/<int:pk>', Update_project.as_view(), name='update_project'),
    path('delete_project/<int:pk>', Delete_project.as_view(), name='delete_project'),

]