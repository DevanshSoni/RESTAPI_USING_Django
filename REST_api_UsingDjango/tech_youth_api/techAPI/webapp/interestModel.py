from django.db import models
# import datetime
from .userModel import *
class interest(models.Model):
    temp_id=models.ForeignKey(to=user,max_length=40,on_delete=models.PROTECT)
    InterestArea=models.CharField(max_length=40)
    def __str__(self):
        return f"{self.InterestArea}"
