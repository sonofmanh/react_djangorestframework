from django.db import models

# Create your models here.

class  Messages(models.Model):
    firstName = models.CharField(max_length=20)
    lastNname = models.CharField(max_length=20)
    Messages = models.CharField(max_length=500)
    subjectMatter = models.CharField(max_length=20)

    def __str__(self):
        return self.subject_matter