from django.db import models
from apps.base.models import BaseModel
from django.contrib.auth.models import User

# Create your models here.

class Project(BaseModel):
    name = models.CharField(max_length=256)
    price = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_projects',null=True,blank=True)
   
    def __str__(self):
        return self.name
    
class Payment(BaseModel):
    comment = models.CharField(max_length=256)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_payments', null=True,blank=True)
    price = models.IntegerField(default=0)
    date = models.DateTimeField()
    
    def __str__(self):
        return self.comment

