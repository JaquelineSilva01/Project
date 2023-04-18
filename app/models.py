from django.db import models

class Post(models.Model):

    autor = models.CharField(max_length=50)
    titulo = models.CharField(max_length=50)
    comentario = models.CharField(max_length=100)
    data = models.CharField(max_length=10)
    def __str__(self):
        return self.autor
