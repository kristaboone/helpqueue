from django.db import models
# from .utils import code_generator, create_shortcode
from django.conf import settings
from django.contrib.auth.models import User, Group


class Class(models.Model):
    className = models.CharField(max_length=50,)
    startTime = models.TimeField()
    endTime = models.TimeField()
    semesterEndDate = models.DateField()
    students = models.ManyToManyField(User)
    # instructor = models.ForeignKey(User)
