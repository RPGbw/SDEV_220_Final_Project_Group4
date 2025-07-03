from django.conf import settings
from django.db import models
# If we are wanting to use Authentication: 'from django.contrib.auth.models import User'



class Prescription(models.Model):
    # prescription fields
    patient_name = models.CharField(max_length=100)
    medication = models.CharField(max_length=100)
    doctor_name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=50)
    quantity = models.PositiveBigIntegerField()
    fulfillment = models.BooleanField(default=False) # tracking if prescription is fulfilled
    date_prescribed = models.DateField(auto_now_add=True) # sets the date to current date when added

    '''
    Link Prescriptions to doctors
    prescribed_by = models.ForiegnKey(User)
    '''

    def __str__(self):
        return f"{self.patient_name} - {self.medication} ({self.date_prescribed})"



class Medicine(models.Model):
    med_name = models.CharField(max_length=128)
    

    def __str__(self):
        return(f"ID:{self.id}: Name {self.med_name}")