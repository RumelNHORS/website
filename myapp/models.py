from django.db import models

# Create your models here.

class Contract(models.Model):
	name = models.CharField(max_length=30)
	email = models.EmailField()
	desc = models.TextField(max_length=500)

