from django.db import models
from django.utils import timezone
import datetime
from hospitalapp.models import *
from hospitalapp.models import Medicine

# Create your models here.
class User(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    status = models.CharField(max_length=10,default='accepted')
    medicines = models.ManyToManyField(Medicine, related_name='users', blank=True)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')],null=True)
    emergency_contact = models.CharField(max_length=100,null=True)
    allergies = models.TextField(blank=True)  # Allows multiple allergies separated by commas
    height = models.CharField(max_length=20,null=True)
    relation_with_user = models.CharField(max_length=100,null=True)
    blood_group = models.CharField(max_length=10, blank=True)
    date_of_birth = models.DateField(null=True)
    weight = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.full_name
    

class Appointment(models.Model):
    APPOINTMENT_TYPES = [
        ('Regular', 'Regular'),
        ('Emergency', 'Emergency'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    appointment_for = models.CharField(max_length=10)
    service_required = models.CharField(max_length=100)
    name = models.CharField(max_length=100, default= "user")
    appointment_type = models.CharField(max_length=20, choices=APPOINTMENT_TYPES)
    emergency_contact = models.CharField(max_length=15)
    date = models.DateField()
    time = models.TimeField()
    hospital = models.CharField(max_length=100) 
    status = models.CharField(max_length=10,default='pending')

    def __str__(self):
        return f"{self.user.full_name}'s Appointment"
    

class HospitalReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    appointment_date = models.DateField(blank=True, null=True)
    cancellation_reason_given = models.BooleanField()
    cancellation_inform = models.BooleanField()
    unethical_staff_name = models.CharField(max_length=100,default='user')
    bill_upload = models.FileField(upload_to='hospital_reports/', blank=True, null=True)



class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1) 
    added_at = models.DateTimeField(auto_now_add=True) 
    status = models.CharField(max_length=10, default='pending')
    hospital_status = models.CharField(max_length=10, default='pending')


    def __str__(self):
        return f"{self.quantity} x {self.medicine.medicine_name} ({self.user.full_name})"

    def mark_as_ordered(self):
        self.status = 'ordered'
        self.save()
    




class PendingMedicine(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    medicine_ids = models.TextField() 

    def __str__(self):
        return f"Pending Medicine for {self.user.full_name}"