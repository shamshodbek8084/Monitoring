from django.shortcuts import render, get_object_or_404
from .serializer import PaymentSerializer, ProjectSerializer, Registration_serializer
from .models import Payment, Project, User
from rest_framework.response import Response
from rest_framework.views import APIView 
from rest_framework.permissions import AllowAny
from rest_framework.generics import (CreateAPIView,
                                        UpdateAPIView,
                                        DestroyAPIView,
                                        RetrieveAPIView,
                                        ListAPIView)


# Create your views here.


# Class APIView bo'yicha qilindi-------------------------------------
# class ProjectAPIView(APIView):
#     serializer_class = ProjectSerializer
#     permission_classes = (AllowAny, )
#     model = Project
#     def get(self, request, pk):
#         project = get_object_or_404(self.model, id=pk)
#         serializer = self.serializer_class(instance = project)
#         data = {
#             'data':serializer.data
#         }
#         return Response(data=data)
    
#     def put(self, request, pk):
#         project = get_object_or_404(self.model, id=pk)
#         serializer = self.serializer_class(instance = project)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.data)
    
        
class Create_project(CreateAPIView):
    queryset = Project.objects.filter(is_active = True)
    serializer_class = ProjectSerializer
    permission_classes = (AllowAny, )

class Read_project(RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (AllowAny, )

class List_project(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (AllowAny, )

class Update_project(UpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (AllowAny, )

class Delete_project(DestroyAPIView):
    queryset = Project.objects.filter(is_active = True)
    serializer_class = ProjectSerializer
    permission_classes = (AllowAny, )

class Register_User(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = Registration_serializer
    permission_classes = (AllowAny, )







