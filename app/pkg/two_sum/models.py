from django.contrib.postgres.fields import ArrayField
from django.db import models


class TwoSum(models.Model):
    numbers_array = ArrayField(models.IntegerField())
    target = models.IntegerField()
    result = ArrayField(
        models.IntegerField(), size=2, blank=True, null=True
    )
