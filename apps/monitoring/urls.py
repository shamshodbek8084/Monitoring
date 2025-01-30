from django.contrib import admin
from django.urls import path
# from .views import ProjectAPIView
from .views import (Create_project,
                    Read_project,
                    List_project,
                    Update_project,
                    Delete_project,
                    Register_User,
                    Create_payment,
                    Read_payment,
                    List_payment,
                    Update_payment,
                    Delete_payment)

urlpatterns = [
    # path('project/<int:pk>', ProjectAPIView.as_view(), name = 'project'),
# ---------------------------------------------Project-------------------------------------------------

    path('create_project/', Create_project.as_view(), name='create_project'),
    path('read_project/<int:pk>', Read_project.as_view(), name='read_project'),
    path('list_project/', List_project.as_view(), name='list_project'),
    path('update_project/<int:pk>', Update_project.as_view(), name='update_project'),
    path('delete_project/<int:pk>', Delete_project.as_view(), name='delete_project'),

# ---------------------------------------------Register-------------------------------------------------

    path('register/', Register_User.as_view(), name='register'),

# ---------------------------------------------Payment-------------------------------------------------

    path('create_payment/', Create_payment.as_view(), name='create_payment'),
    path('read_payment/<int:pk>', Read_payment.as_view(), name='read_payment'),
    path('list_payment/', List_payment.as_view(), name='list_payment'),
    path('update_payment/<int:pk>', Update_payment.as_view(), name='update_payment'),
    path('delete_payment/<int:pk>', Delete_payment.as_view(), name='delete_payment'),

]