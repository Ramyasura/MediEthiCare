from django.db import models
from django.utils import timezone
import hashlib
# Create your models here.
class Hospital(models.Model):
    hospital_name = models.CharField(max_length=100)
    email = models.EmailField()
    contact_number = models.CharField(max_length=15)
    hospital_type = models.CharField(max_length=50, choices=[('General Hospital', 'General Hospital'),
                                                            ('Specialty Hospital', 'Specialty Hospital'),
                                                            ('Community Hospital', 'Community Hospital'),
                                                            ('Corporate Hospital', 'Corporate Hospital')])
    password = models.CharField(max_length=50) 
    hospital_image = models.ImageField(upload_to='hospital_images/')
    hospital_doc = models.ImageField(upload_to='hospital_document_images/',null=True)
    address = models.TextField()
    otp = models.CharField(max_length=6,default=0) 
    otp_status = models.CharField(max_length=15, default='Not Verified')
    admin_status = models.CharField(max_length=15, default='pending')


class Medicine(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    medicine_name = models.CharField(max_length=100)
    medicine_type = models.CharField(max_length=50, choices=[('Tablet', 'Tablet'),
                                                            ('Capsule', 'Capsule'),
                                                            ('Liquid', 'Liquid'),
                                                            ('Injection', 'Injection'),
                                                            ('Ointment', 'Ointment')])
    medicine_price = models.CharField(max_length=100)
    medicine_description = models.TextField()
    stock_size = models.IntegerField()
    medicine_image = models.ImageField(upload_to='medicine_images/')
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.medicine_name} - {self.hospital.hospital_name}"



class BedAvailability(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    bed_type = models.CharField(max_length=50, choices=[('General Bed', 'General Bed'),
                                                        ('ICU Bed', 'ICU Bed'),
                                                        ('Pediatric Bed', 'Pediatric Bed'),
                                                        ('Specialized Bed', 'Specialized Bed')])
    bed_price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    bed_description = models.TextField()
    num_beds_available = models.IntegerField()

    def __str__(self):
        return f"{self.hospital.hospital_name} - {self.bed_type}"
    

class DoctorAvailability(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    doctor_name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=50, choices=[
        ('General Physician', 'General Physician'),
        ('Cardiologist', 'Cardiologist'),
        ('Surgeon', 'Surgeon'),
        ('Dermatologist', 'Dermatologist'),
        ('Ophthalmologist', 'Ophthalmologist'),
        ('Pediatrician', 'Pediatrician')
    ])
    available_days = models.CharField(max_length=100)  # Comma-separated list of available days
    timings = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.doctor_name} - {self.hospital.hospital_name}"
    


class SurgicalService(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    surgical_service = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    service_details = models.TextField()

    def __str__(self):
        return f"{self.hospital.hospital_name} - Surgical Service: {self.surgical_service}"



class EmergencyService(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    emergency_service = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    service_details = models.TextField()

    def __str__(self):
        return f"{self.hospital.hospital_name} - Emergency Service: {self.emergency_service}"



class DiagnosticService(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    diagnostic_service = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    service_details = models.TextField()

    def __str__(self):
        return f"{self.hospital.hospital_name} - Diagnostic Service: {self.diagnostic_service}"
    




class BkModel(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.SET_NULL, null=True)
    medicineid = models.CharField(max_length=100)
    medicine_price = models.CharField(max_length=100)
    medicine_type = models.CharField(max_length=100)


    class Meta:
        db_table = 'blockchainmodel'