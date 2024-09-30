from django.db import models

class Interview(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    question = models.TextField()

    def __str__(self):
        return self.name
