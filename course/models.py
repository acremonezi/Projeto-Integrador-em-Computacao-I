from django.db import models

# Create your models here.

class Course(models.Model):
    nome = models.CharField(max_length = 100)
    descricao = models.TextField()
    thumb = models.ImageField(upload_to = "courses_images")
    url = models.URLField()

    def __str__(self) -> str:
        return self.nome