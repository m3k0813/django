from django.db import models


class Mail(models.Model):
    title = models.CharField(max_length=20)
    contents = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.contents[:100]


# Create your models here.
