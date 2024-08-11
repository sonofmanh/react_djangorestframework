from django.db import models

# Create your models here.


class Contact(models.Model):
    firstName=models.CharField(max_length=50)
    lastName=models.CharField(max_length=50)
    subjectMatter = models.CharField( max_length=50)
    message = models.TextField(max_length=500)