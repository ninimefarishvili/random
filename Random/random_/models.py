from django.db import models


class ragaca(models.model):
    name = models.CharField(max_length=18 , null=False, blank=False)
    last_name = models.CharField(max_length=18 , null=False, blank=False)
