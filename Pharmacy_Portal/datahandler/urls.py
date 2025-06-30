from django.urls import path
from . import views
urlpatterns = [
    path('pharmacyapp/', views.pharmacyportal, name='pharmacyportal')
]