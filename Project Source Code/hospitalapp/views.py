from django.shortcuts import render,redirect,get_object_or_404
from hospitalapp.models import *
from django.contrib import messages
from django.contrib.auth import logout
from userapp.models import *
from django.db.models import Count
from django.db.models import Sum
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def user_logout(request):
    logout(request)
    return redirect('hospital_login')


def hospital_dashboard(request):
    hospital_id = request.session.get('hospital_verified_id')
    hospital_name = Hospital.objects.get(pk=hospital_id)
    hospital_name = hospital_name.hospital_name
    total_medicines = Medicine.objects.count()
    total_appointments = Appointment.objects.count()
    pending_count = Appointment.objects.filter(hospital=hospital_name, status='pending').count()
    accepted_count = Appointment.objects.filter(hospital=hospital_name, status='accepted').count()
    doctors_by_specialization = DoctorAvailability.objects.filter(hospital_id=hospital_id).count()
    total_bed_availability = BedAvailability.objects.filter(hospital_id=hospital_id).aggregate(total=Sum('num_beds_available'))['total']
    context = {
        'total_medicines': total_medicines,
        'total_appointments': total_appointments,
        'total_beds_available': total_bed_availability,
        'pending_count':pending_count,
        'accepted_count':accepted_count,
        'doctors_by_specialization': doctors_by_specialization,
    }
    return render(request,"hospital/index.html",context)



from ethicareproject.BlockcahinAlgo import HashDataBlock
def medicines(request):
    hospital_id = request.session.get('hospital_verified_id')
    if request.method == 'POST':
        medicine_name = request.POST.get('medicineName')
        medicine_type = request.POST.get('medicineType')
        medicine_price = request.POST.get('medicinePrice')
        medicine_description = request.POST.get('medicineDescription')
        stock_size = request.POST.get('stockSize')
        medicine_image = request.FILES.get('medicineImage')
        
        # Convert the price to string and hash it
        hash_medicine_price = hashlib.sha256(medicine_price.encode()).hexdigest()
        
        existing_medicine = Medicine.objects.filter(hospital_id=hospital_id, medicine_name=medicine_name, medicine_type=medicine_type).first()
        if existing_medicine:
            if existing_medicine.stock_size == 0:
                existing_medicine.delete()
            else:
                messages.error(request, 'Medicine already exists for this hospital and has stock available.')
                return redirect('medicines')
        medicine = Medicine.objects.create(
            hospital_id=hospital_id,
            medicine_name=medicine_name,
            medicine_type=medicine_type,
            medicine_price=medicine_price,  
            medicine_description=medicine_description,
            stock_size=stock_size,
            medicine_image=medicine_image
        )
        hash_medicineid = hashlib.sha256(str(medicine.id).encode()).hexdigest()
        hash_medicine_type = hashlib.sha256(medicine_type.encode()).hexdigest()
        
        bk_model_instance = BkModel.objects.create(
            medicine=medicine,
            medicineid=hash_medicineid,
            medicine_price=hash_medicine_price, 
            medicine_type=hash_medicine_type
        )
        key = 'dk84dfao63o94wsghl3o14'
        messages.success(request, 'Medicine Added Successfully.')
        return redirect('medicines')
    return render(request, "hospital/add-medicines.html")




def view_medicines(request):
    hospital_id = request.session.get('hospital_verified_id')
    print(hospital_id)
    if hospital_id:
        medicines = Medicine.objects.filter(hospital_id=hospital_id)
        print("Medicines for Hospital ID:", hospital_id)
        return render(request, "hospital/view-medicines.html", {"medicines": medicines})
    else:
        print("Hospital ID not found in session.")
        messages.error(request, 'Hospital ID not found. Please log in again.')
        return redirect("view_medicines")

def all_medicines(request):
    hospital_id = request.session.get('hospital_verified_id')
    if hospital_id:
        medicines_list = Medicine.objects.filter(hospital_id=hospital_id)
        paginator = Paginator(medicines_list, 8) 
        page = request.GET.get('page')
        try:
            medicines = paginator.page(page)
        except PageNotAnInteger:
            medicines = paginator.page(1)
        except EmptyPage:
            medicines = paginator.page(paginator.num_pages)
        return render(request, "hospital/all-medicines.html", {"medicines": medicines})
    else:
        messages.error(request, 'Hospital ID not found. Please log in again.')
        return redirect("all_medicines")


def bed(request):
    if request.method == 'POST':
        hospital_id = request.session.get('hospital_verified_id')
        bed_type = request.POST.get('bedType')
        bed_price = request.POST.get('bedPrice')
        bed_description = request.POST.get('bedDescription')
        num_beds_available = request.POST.get('numBedsAvailable')
        if hospital_id:
            bed_availability = BedAvailability.objects.create(
                hospital_id=hospital_id,
                bed_type=bed_type,
                bed_price_per_day=bed_price,
                bed_description=bed_description,
                num_beds_available=num_beds_available
            )
            messages.success(request, 'Bed details added successfully.')
            return redirect('bed')
        else:
            messages.error(request, 'Hospital ID not found in session. Please log in again.')
            return redirect('bed')
    return render(request, "hospital/bed.html")


def view_bed(request):
    hospital_id = request.session.get('hospital_verified_id')
    beds = BedAvailability.objects.filter(hospital_id=hospital_id)
    paginator = Paginator(beds, 5) 
    page = request.GET.get('page')
    try:
        beds = paginator.page(page)
    except PageNotAnInteger:
        beds = paginator.page(1)
    except EmptyPage:
        beds = paginator.page(paginator.num_pages)
    return render(request, "hospital/view-bed.html", {"beds": beds})



def removeBed(request, bed_id):
    bed = BedAvailability.objects.get(pk=bed_id)
    bed.delete()
    messages.info(request,"Removed !")
    return redirect('view_bed') 


def list_doct(request):
    if request.method == 'POST':
        hospital_id = request.session.get('hospital_verified_id')
        doctor_name = request.POST.get('doctorName')
        specialization = request.POST.get('doctorSpecialization')
        available_days = ','.join(request.POST.getlist('availableDays[]'))
        timings = request.POST.get('timings')
        existing_doctor = DoctorAvailability.objects.filter(hospital_id=hospital_id, doctor_name=doctor_name, specialization=specialization).exists()
        if not existing_doctor:
            DoctorAvailability.objects.create(
                hospital_id=hospital_id,
                doctor_name=doctor_name,
                specialization=specialization,
                available_days=available_days,
                timings=timings
            )
            messages.success(request, "Doctor availability details added successfully.")
        else:
            messages.error(request, "Doctor with the same name and specialization already Added.")
        return redirect('list_doct')
    return render(request, "hospital/list-appiontments.html")




def pendingAppointments(request):
    hospital_id = request.session.get('hospital_verified_id')
    hospital = Hospital.objects.get(pk=hospital_id)
    hospital_name = hospital.hospital_name
    appointments = Appointment.objects.filter(hospital=hospital_name, status='pending')
    paginator = Paginator(appointments, 5) 
    page = request.GET.get('page')
    try:
        appointments = paginator.page(page)
    except PageNotAnInteger:
        appointments = paginator.page(1)
    except EmptyPage:
        appointments = paginator.page(paginator.num_pages)
    return render(request, "hospital/pending-appiontments.html", {'appointments': appointments})



def acceptAppointment(request, appointment_id):
    appointment = Appointment.objects.get(pk=appointment_id)
    appointment.status = 'accepted'
    appointment.save()
    messages.success(request, 'Appointment Accepted.')
    return redirect('pendingAppointments')



def viewAppointments(request):
    hospital_id = request.session.get('hospital_verified_id')
    hospital = Hospital.objects.get(pk=hospital_id)
    hospital_name = hospital.hospital_name
    appointments = Appointment.objects.filter(hospital=hospital_name, status='accepted')
    paginator = Paginator(appointments, 5)
    page = request.GET.get('page')
    try:
        appointments = paginator.page(page)
    except PageNotAnInteger:
        appointments = paginator.page(1)
    except EmptyPage:
        appointments = paginator.page(paginator.num_pages)
    return render(request, "hospital/view-appiontments.html", {'appointments': appointments})


def cancelAppointment(request, appointment_id):
    appointment = Appointment.objects.get(pk=appointment_id)
    appointment.delete()
    messages.warning(request, 'Appointment Deleted.')
    return redirect('viewAppointments')


def viewservices(request):
    hospital_id = request.session.get('hospital_verified_id')
    
    surgical_services = SurgicalService.objects.filter(hospital_id=hospital_id)
    emergency_services = EmergencyService.objects.filter(hospital_id=hospital_id)
    diagnostic_services = DiagnosticService.objects.filter(hospital_id=hospital_id)

    return render(request, "hospital/view-services.html", {
        'surgical_services': surgical_services,
        'emergency_services': emergency_services,
        'diagnostic_services': diagnostic_services,
    })



def removeService(request, service_type, service_id):
    if service_type == 'surgical':
        service = SurgicalService.objects.get(pk=service_id)
    elif service_type == 'emergency':
        service = EmergencyService.objects.get(pk=service_id)
    elif service_type == 'diagnostic':
        service = DiagnosticService.objects.get(pk=service_id)
    service.delete()
    messages.warning(request, 'Services Deleted.')
    return redirect('viewservices')


def services(request):
    hospital_id = request.session.get('hospital_verified_id')
    if request.method == 'POST':
        tab = request.POST.get('tab')
        print(tab,"active tab")
        if tab == 'surgical': 
            surgical_service = request.POST.get('surgicalService')
            price = request.POST.get('price')
            service_details = request.POST.get('surgicalServiceDetails')

            hospital = Hospital.objects.get(pk=hospital_id)
            surgical_service_obj = SurgicalService.objects.create(
                hospital=hospital,
                surgical_service=surgical_service,
                price=price,
                service_details=service_details
            )
            surgical_service_obj.save()
            messages.success(request, 'Services Added.')
        elif tab == 'emergency':  
            emergency_service = request.POST.get('emergencyService')
            price = request.POST.get('price')
            service_details = request.POST.get('surgicalServiceDetails')
            hospital = Hospital.objects.get(pk=hospital_id)
            emergency_service_obj = EmergencyService.objects.create(
                hospital=hospital,
                emergency_service=emergency_service,
                price=price,
                service_details=service_details
            )
            emergency_service_obj.save()
            messages.success(request, 'Services Added.')
        elif tab == 'diagnostic': 
            diagnostic_service = request.POST.get('diagnosticService')
            price = request.POST.get('price')
            service_details = request.POST.get('surgicalServiceDetails')
            hospital = Hospital.objects.get(pk=hospital_id)
            diagnostic_service_obj = DiagnosticService.objects.create(
                hospital=hospital,
                diagnostic_service=diagnostic_service,
                price=price,
                service_details=service_details
            )
            diagnostic_service_obj.save()
            messages.success(request, 'Services Added.')
        return redirect('services')

    return render(request, "hospital/add-services.html")




def edit_medicines(request, medicine_id):
    medicine = Medicine.objects.get(id=medicine_id)
    print(medicine)
    if request.method == 'POST':
        new_medicine_name = request.POST.get('medicineName')
        new_medicine_type = request.POST.get('medicineType')
        existing_medicine = Medicine.objects.filter(hospital=medicine.hospital, 
                                                     medicine_name=new_medicine_name,
                                                     medicine_type=new_medicine_type).exclude(id=medicine_id).exists()
        if existing_medicine:
            messages.error(request, 'A medicine with the same name and type already exists for this hospital.')
            return redirect('edit_medicines', medicine_id=medicine_id)
        medicine.medicine_name = new_medicine_name
        medicine.medicine_type = new_medicine_type
        medicine.medicine_price = request.POST.get('medicinePrice')
        medicine.medicine_description = request.POST.get('medicineDescription')
        medicine.stock_size = request.POST.get('stockSize')
        medicine_image = request.FILES.get('medicineImage')
        if medicine_image:
            medicine.medicine_image = medicine_image
        medicine.save()

        hash_medicineid = hashlib.sha256(str(medicine.id).encode()).hexdigest()
        hash_medicine_price = hashlib.sha256(medicine.medicine_price.encode()).hexdigest()  # Hashing medicine price
        hash_medicine_type = hashlib.sha256(medicine.medicine_type.encode()).hexdigest()
        
        bk_model_instance = BkModel.objects.get(medicine=medicine)
        bk_model_instance.medicineid = hash_medicineid
        bk_model_instance.medicine_price = hash_medicine_price
        bk_model_instance.medicine_type = hash_medicine_type
        bk_model_instance.save()

        messages.success(request, 'Medicine updated successfully.')
        return redirect('edit_medicines', medicine_id=medicine_id)
    return render(request, "hospital/edit-medicines.html", {'medicine': medicine})


def remove_medicine(request, medicine_id):
    medicine = Medicine.objects.get(id=medicine_id)
    medicine.delete()
    messages.success(request, "Medicine removed successfully.")
    return redirect('view_medicines')


def view_orders(request):
    hospital_id = request.session.get('hospital_verified_id')
    pending_orders = CartItem.objects.filter(medicine__hospital_id=hospital_id, status='ordered',hospital_status="pending")
    pending_orders = remove_duplicates(pending_orders, key=lambda x: x.medicine.id)
    paginator = Paginator(pending_orders, 5) 
    page = request.GET.get('page')
    try:
        pending_orders = paginator.page(page)
    except PageNotAnInteger:
        pending_orders = paginator.page(1)
    except EmptyPage:
        pending_orders = paginator.page(paginator.num_pages)
    return render(request, "hospital/view-orders.html", {'pending_orders': pending_orders})

def remove_duplicates(queryset, key):
    """
    Remove duplicates from a queryset based on a specified key.
    """
    seen = set()
    unique_items = []
    for item in queryset:
        value = key(item)
        if value not in seen:
            seen.add(value)
            unique_items.append(item)
    return unique_items


def update_order_status(request, order_id):
    order = CartItem.objects.get(pk=order_id)
    medicine_id = order.medicine_id
    related_orders = CartItem.objects.filter(medicine_id=medicine_id)
    for related_order in related_orders:
        related_order.hospital_status = 'delivered'
        related_order.save()
    return redirect('view_orders')



def all_orders(request):
    hospital_id = request.session.get('hospital_verified_id')
    delivered_orders = CartItem.objects.filter(medicine__hospital_id=hospital_id, hospital_status='delivered', status='ordered')
    paginator = Paginator(delivered_orders, 5)
    page = request.GET.get('page')
    try:
        delivered_orders = paginator.page(page)
    except PageNotAnInteger:
        delivered_orders = paginator.page(1)
    except EmptyPage:
        delivered_orders = paginator.page(paginator.num_pages)
    return render(request, "hospital/all-orders.html", {'delivered_orders': delivered_orders})