from django.db import models
from django.core.validators import MinLengthValidator
from contributors.models import Contributor

class Book(models.Model):
    title = models.CharField(max_length=200, validators=[MinLengthValidator(5)])
    language = models.CharField(max_length=200, validators=[MinLengthValidator(5)])
    contributor = models.ForeignKey(Contributor, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title
