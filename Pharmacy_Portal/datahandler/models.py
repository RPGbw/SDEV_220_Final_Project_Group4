from django.conf import settings
from django.db import models



class Medicine(models.Model):
    med_name = models.CharField(max_length=128)
    

    def __str__(self):
        return(f"ID:{self.id}: Name {self.med_name}")