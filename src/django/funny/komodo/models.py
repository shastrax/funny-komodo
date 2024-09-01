from django.db import models

class Fortune(models.Model):
    id = models.BigAutoField(primary_key = True)
    eval_flag = models.BooleanField(default=False)
    reject_flag = models.BooleanField(default=False)
    mask = models.IntegerField(default=0)
    uuid = models.CharField(max_length=48)
    message = models.CharField(max_length=4096)
