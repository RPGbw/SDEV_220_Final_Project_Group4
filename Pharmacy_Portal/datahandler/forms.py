from django import forms
from .models import Prescription

class PrescriptionForms(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ['patient_name', 'doctor_name', 'medication', 'dosage', 'quantity']