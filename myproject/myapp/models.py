from django.db import models

# Create your models here.
class Person(models.Model):
    name=models.CharField(max_length=255,blank=False,null=True)
    email=models.EmailField()
    phone=models.CharField(max_length=15,null=True,blank=True)
    address=models.TextField(null=True,blank=True)
    age=models.PositiveIntegerField(default=5)
    def __str__(self):
        return f"{self.name} - {self.email}"
