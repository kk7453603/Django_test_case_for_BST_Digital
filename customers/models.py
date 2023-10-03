from django.db import models
from robots.models import Robot


class Customer(models.Model):
    email = models.CharField(max_length=255, blank=False, null=False)
    robot = models.ForeignKey(Robot, on_delete=models.CASCADE)
    available = models.BooleanField(default=False)

