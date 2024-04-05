from django.shortcuts import render,redirect,get_object_or_404
from hospitalapp.models import *
from userapp.models import *
from django.contrib.auth import logout
from django.contrib import messages
from hospitalapp.models import *
from userapp.models import *
from django.core.paginator import Paginator
# Create your views here.
def admin_logout(request):
    logout(request)
    return redirect('adminlogin')

def admin_dashboard(request):
    total_hospitals = Hospital.objects.all().count()
    total_users = User.objects.all().count()
    total_reports = HospitalReport.objects.all().count()
    context = {
        'total_hospitals':total_hospitals,
        'total_users':total_users,
        'total_reports':total_reports,

    }
    return render(request,"admin/index.html",context)


def view_Reports(request):
    hospital_reports = HospitalReport.objects.all()
    
    paginator = Paginator(hospital_reports, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, "admin/view-reports.html", {'hospital_reports': page_obj})


def all_medicines(request):
    all_medicines = Medicine.objects.all()
    paginator = Paginator(all_medicines, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "admin/view-medicines.html", {'all_medicines': page_obj})
    

def appointments_details(request):
    accepted_appointments = Appointment.objects.filter(status='accepted')
    paginator = Paginator(accepted_appointments, 5) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, "admin/appointments-details.html", {'accepted_appointments': page_obj})


def all_hospitals(request):
    all_hospitals = Hospital.objects.filter(otp_status='Verified', admin_status='accepted')
    paginator = Paginator(all_hospitals, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "admin/all-hospitals.html", {'all_hospitals': page_obj})



def pendinghospital(request):
    pending_hospitals = Hospital.objects.filter(otp_status='Verified', admin_status='pending')
    paginator = Paginator(pending_hospitals, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "admin/pending-hospitals.html", {'pending_hospitals': page_obj})


def accept_hospital(request, hospital_id):
    hospital = get_object_or_404(Hospital, pk=hospital_id)
    hospital.admin_status = 'accepted'
    hospital.save()
    messages.info(request,"Approved !")
    return redirect('pendinghospital')


def remove_hospital(request, hospital_id):
    hospital = get_object_or_404(Hospital, pk=hospital_id)
    hospital.delete()
    return redirect('all_hospitals')


def delete_medicine(request, medicine_id):
    medicine = Medicine.objects.get(id=medicine_id)
    medicine.delete()
    messages.success(request, "Medicine removed successfully.")
    return redirect('admin_all_medicines')
    


def delete_report(request, report_id):
    report = get_object_or_404(HospitalReport, id=report_id)
    report.delete()
    return redirect('view_Reports')