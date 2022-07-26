from django.conf import settings
from django.db import models


class Test(models.Model):
    "Generated Model"
    test = models.BigIntegerField()
    againtest = models.BigIntegerField(
        null=True,
        blank=True,
    )


class TEst123(models.Model):
    "Generated Model"
    test456 = models.BigIntegerField()
    t13654 = models.BigIntegerField(
        null=True,
        blank=True,
    )
