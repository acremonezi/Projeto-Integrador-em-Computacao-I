from django.db import models

# Create your models here.

class Student(models.Model):
    firstname = models.CharField(max_length = 50)
    lastname = models.CharField(max_length = 100)
    email = models.EmailField()
    password = models.CharField(max_length = 64)
    cpf = models.CharField(max_length = 50)

    def __str__(self) -> str:
        return self.firstname