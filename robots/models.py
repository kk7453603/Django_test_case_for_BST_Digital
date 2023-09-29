from django.db import models
from django.core.exceptions import ValidationError
import re


def valid_models(value1,value2):
    pattern = r'^[A-Z0-9]{2}$'
    if not re.match(pattern, value1) or not re.match(pattern,value2):
        raise ValidationError("Invalid pattern value")



class Robot(models.Model):
    serial = models.CharField(max_length=5, blank=False, null=False)
    model = models.CharField(max_length=2, blank=False, null=False)
    version = models.CharField(max_length=2, blank=False, null=False)
    created = models.DateTimeField(blank=False, null=False)

    def clean(self):
        valid_models(self.model,self.version)

    @property
    def __str__(self):
        return self.model
