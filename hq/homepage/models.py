from django.db import models
# from .utils import code_generator, create_shortcode
from django.conf import settings
from django.contrib.auth.models import User, Group
import uuid


class Table(models.Model):
    number = models.DecimalField(decimal_places=0, max_digits = 2 )
    students = models.ManyToManyField(User,)
    maxStudents = models.DecimalField(decimal_places = 0, max_digits = 2)

    def __str__(self):
        return str(self.number)

class Classe(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    className = models.CharField(max_length=50,)
    startTime = models.TimeField()
    endTime = models.TimeField()
    semesterEndDate = models.DateField()
    students = models.ManyToManyField(User)
    instructor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name = '+') #idk what models.cascade does
    teachingAssistant = models.ForeignKey(User, on_delete = models.SET_NULL, null= True, related_name = '+')
    table = models.ManyToManyField(Table,)

class Question(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    questionTime = models.TimeField(auto_now=True)
    student = models.ForeignKey(User, on_delete = models.CASCADE,  related_name = '+')
    qclass = models.ForeignKey(Classe, on_delete= models.CASCADE, related_name = '+')
    qtable = models.ForeignKey(Table, on_delete = models.SET_NULL, null=True, related_name = '+')
