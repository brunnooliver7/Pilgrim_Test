from django.db import models
from django.core.validators import MinLengthValidator

class Contributor(models.Model):
    name = models.CharField(max_length=200, validators=[MinLengthValidator(5)])
    author = models.CharField(max_length=200)
    editor = models.CharField(max_length=200)
    reviewer = models.CharField(max_length=200)
    email = models.EmailField()
    country = models.CharField(max_length=200, validators=[MinLengthValidator(5)])

    def __str__(self):
        return self.name
