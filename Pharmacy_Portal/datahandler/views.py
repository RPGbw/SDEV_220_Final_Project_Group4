from django.shortcuts import render

def pharmacyportal(request):
    return render(request, 'datahandler\\pharmacyportal', {})