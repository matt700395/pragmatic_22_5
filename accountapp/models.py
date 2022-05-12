from django.db import models

# Create your models here.

class HelloWorld(models.Model):
    text_test_0001init = models.CharField(max_length=255, null=False)
    text_2 = models.CharField(max_length=100, null=True)

