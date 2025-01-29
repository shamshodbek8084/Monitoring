from django.shortcuts import render, get_object_or_404
from .serializer import PaymentSerializer, ProjectSerializer
from .models import Payment, Project
from rest_framework.response import Response
from rest_framework.views import APIView 
from rest_framework.permissions import AllowAny


# Create your views here.

class ProjectAPIView(APIView):
    serializer_class = ProjectSerializer
    permission_classes = (AllowAny, )
    model = Project
    def get(self, request, pk):
        project = get_object_or_404(self.model, id=pk)
        serializer = self.serializer_class(instance = project)
        data = {
            'data':serializer.data
        }
        return Response(data=data)
    
    def put(self, request, pk):
        project = get_object_or_404(self.model, id=pk)
        serializer = self.serializer_class(instance = project)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.data)
        


