# Create your models here.
from django.db import models


class Course(models.Model):
    course_text = models.CharField(max_length=200)
    course_name = models.CharField(max_length=255, default='training')
    course_info = models.TextField(default="This is the information!")
    course_teacher = models.CharField(max_length=255, default='hank')
    course_price = models.IntegerField(default=5000)
    pub_date = models.DateTimeField('date published')

