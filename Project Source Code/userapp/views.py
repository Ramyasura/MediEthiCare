from django.shortcuts import render,redirect,get_object_or_404
# Create your views here.
from django.db.models import Count
import urllib.request
import urllib.parse
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
from django.conf import settings
import random
from hospitalapp.models import *
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from userapp.models import *
from django.contrib.auth import logout
from django.db.models import Q
import re
from django.utils import timezone
from decimal import Decimal
from django.db.models import Sum
import os
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger




EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')

def logout2(request):
    logout(request)
    return redirect('userlogin')



def sendSMS(user,otp,mobile):
    data =  urllib.parse.urlencode({'username':'Codebook','apikey': '56dbbdc9cea86b276f6c' , 'mobile': mobile,
        'message' : f'Hello {user}, your OTP for account activation is {otp}. This message is generated from https://www.codebook.in server. Thank you', 'senderid': 'CODEBK'})
    data = data.encode('utf-8')
    request = urllib.request.Request("https://smslogin.co/v3/api.php?")
    f = urllib.request.urlopen(request, data)
    return f.read()



def generate_otp(length=4):
    otp = ''.join(random.choices('0123456789', k=length))
    return otp



def index(request):
    return render(request,"user/index.html")





def about(request):
    return render(request,"user/about.html")



def userlogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email)
            print(f"User found with email: {email}")
            if user.password == password:
                print("Password matched.")
                if user.status == "accepted":
                    print("User account is approved.")
                    request.session['user_login_id'] = user.id
                    messages.success(request, 'Login successful.')
                    return redirect('viewhospital')
                else:
                    print("User account is not yet approved.")
                    messages.error(request, 'Your account is not yet approved.')
                    return redirect('userlogin')
            else:
                print("Invalid password.")
                messages.error(request, 'Invalid password.')
                return redirect('userlogin')
        except User.DoesNotExist:
            print("User does not exist.")
            messages.error(request, 'User does not exist.')
            return redirect('userlogin')
    return render(request, "user/userlogin.html")



def userregister(request):
    if request.method == 'POST':
        full_name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        address = request.POST.get('address')
        profile_picture = request.FILES.get('profile')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
            return redirect('userregister')
        user = User.objects.create(
            full_name=full_name,
            email=email,
            phone=phone,
            password=password,
            address=address,
            profile_picture=profile_picture
        )
        messages.success(request, 'User registered successfully.')
        return redirect('userregister') 
    return render(request, "user/userregister.html")


def contact(request):
    return render(request,"user/contact.html")


def userdashboard(request):
    return render(request,"user/user-dashboard.html")


def viewhospital(request):
    user_id = request.session.get('user_login_id')
    user = get_object_or_404(User, pk=user_id)
    pending_cart_items = CartItem.objects.filter(user=user, status='pending')
    cart_count = pending_cart_items.count()
    request.session['cart_count'] = cart_count
    return render(request, "user/view-hospital.html", {'cart_count': cart_count})



def bookappiontment(request):
    return render(request,"user/book-appointment.html")


def bookservices(request):
    return render(request,"user/book-services.html")


def viewmedicalrecords(request):
    return render(request,"user/medical-records.html")





def reporthospital(request, medicine_id):
    medicine_deatils = Medicine.objects.get(pk=medicine_id)
    hospital_name = medicine_deatils.hospital.hospital_name
    cart_count = request.session.get('cart_count')
    if request.method == 'POST':
        user_id = request.session.get('user_login_id')
        appointment_date = request.POST.get('appointmentDate')
        if appointment_date:
            appointment_date = appointment_date.strip() 
        else:
            appointment_date = None 
        cancellation_reason_given = request.POST.get('cancellationReason') == 'yes'
        cancellation_inform = request.POST.get('cancellationInform') == 'yes'
        unethical_staff_name = request.POST.get('staffName')
        bill_upload = request.FILES.get('billUpload')

        report = HospitalReport.objects.create(
            user_id=user_id,
            medicine_id=medicine_id,
            appointment_date=appointment_date,
            cancellation_reason_given=cancellation_reason_given,
            cancellation_inform=cancellation_inform,
            unethical_staff_name=unethical_staff_name,
            bill_upload=bill_upload
        )
        print("success !")
        messages.success(request, 'Reported successfully.')
        return redirect('reporthospital',medicine_id)
    return render(request, "user/report-hospital.html", {'hopital_name': hospital_name,'cart_count':cart_count})



def reporthospital2(request, medicine_id):
    appointment = Appointment.objects.get(pk=medicine_id)
    hospital_name = appointment.hospital
    cart_count = request.session.get('cart_count')
    print(hospital_name)
    if request.method == 'POST':
        user_id = request.session.get('user_login_id')
        appointment_date = request.POST.get('appointmentDate')
        if appointment_date:
            appointment_date = appointment_date.strip() 
        else:
            appointment_date = None 
        cancellation_reason_given = request.POST.get('cancellationReason') == 'yes'
        cancellation_inform = request.POST.get('cancellationInform') == 'yes'
        unethical_staff_name = request.POST.get('staffName')
        bill_upload = request.FILES.get('billUpload')

        report = HospitalReport.objects.create(
            user_id=user_id,
            medicine_id=medicine_id,
            appointment_date=appointment_date,
            cancellation_reason_given=cancellation_reason_given,
            cancellation_inform=cancellation_inform,
            unethical_staff_name=unethical_staff_name,
            bill_upload=bill_upload
        )
        print("success !")
        messages.success(request, 'Reported successfully.')
        return redirect('reporthospital2',medicine_id)
    return render(request, "user/report-hospital.html",{"hopital_name":hospital_name,'cart_count':cart_count})


def buymedicine(request):
    return render(request,"user/buy-medicine.html")


def pricing(request):
    cart_count = request.session.get('cart_count')
    return render(request,"user/pricing.html",{'cart_count':cart_count})



def my_orders(request):
    cart_count = request.session.get('cart_count')
    user_id = request.session.get('user_login_id')
    ordered_cart_items = CartItem.objects.filter(user_id=user_id, status='ordered')
    
    # List to store ordered medicines with hospital status
    ordered_medicines_with_status = []
    
    for cart_item in ordered_cart_items:
        medicine = cart_item.medicine
        hospital_status = cart_item.hospital_status
        ordered_medicines_with_status.append({'medicine': medicine, 'hospital_status': hospital_status})
    
    total_sum = ordered_cart_items.aggregate(total_sum=Sum('medicine__medicine_price'))['total_sum']
    ordera_total = total_sum + 9 + 8 if total_sum is not None else None
    
    return render(request, "user/my-orders.html", {
        'ordered_medicines_with_status': ordered_medicines_with_status,
        'total_sum': total_sum,
        'cart_count': cart_count,
        'ordera_total': ordera_total
    })



def faqs(request):
    cart_count = request.session.get('cart_count')
    return render(request,"user/faqs.html",{'cart_count':cart_count})



def paymentmethod(request):
    user_id = request.session.get('user_login_id')
    cart_count = request.session.get('cart_count')
    medicine_ids = request.session.get('medicine_ids', [])
    medicines = Medicine.objects.filter(id__in=medicine_ids)
    print("Medicine IDs:", medicine_ids)
    return render(request, "user/payment.html", {'cart_count': cart_count, 'medicines': medicines})



def userprofile(request):
    cart_count = request.session.get('cart_count')
    user_id = request.session.get('user_login_id')
    user = User.objects.get(pk=user_id)
    
    if request.method == "POST":
        user.full_name = request.POST.get('full_name')
        user.phone = request.POST.get('phone')
        user.gender = request.POST.get('gender')
        user.emergency_contact = request.POST.get('emergency_contact')
        user.allergies = request.POST.get('allergies')
        user.height = request.POST.get('height')
        user.relation_with_user = request.POST.get('relation')
        user.email = request.POST.get('email')
        user.blood_group = request.POST.get('blood_group')
        user.weight = request.POST.get('weight')
        user.password = request.POST.get('password')
        dob = request.POST.get('dob')
        if dob:
            user.date_of_birth = dob
        if 'profile_picture' in request.FILES:
            user.profile_picture = request.FILES['profile_picture']
        user.save()
        messages.success(request, 'Profile updated successfully!')
        return redirect('userprofile')
    
    return render(request, "user/user-profile.html", {'user': user,'cart_count':cart_count})


def adminlogin(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('password')
        if username == "admin"  and password == "admin":
            messages.success(request, 'Login Successfully.')
            return redirect('admin_dashboard')
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
    return render(request,"user/adminlogin.html")




def myappointments(request):
    cart_count = request.session.get('cart_count')
    user_id = request.session.get('user_login_id')
    user_appointments = Appointment.objects.filter(
        user_id=user_id,
        status='accepted',
    )
    paginator = Paginator(user_appointments, 5)  
    page = request.GET.get('page')
    try:
        user_appointments = paginator.page(page)
    except PageNotAnInteger:
        user_appointments = paginator.page(1)
    except EmptyPage:
        user_appointments = paginator.page(paginator.num_pages)
    return render(request, "user/my-appointments.html", {'user_appointments': user_appointments, 'cart_count': cart_count})


def medicine_compare(request):
    cart_count = request.session.get('cart_count')
    medicine_name = None
    hospitals_with_medicines = []
    medicine_count = 0
    medicines = None
    total_stock_size = 0
    if request.method == "POST":
        medicine_name = request.POST.get("medicine_name")
        medicines = Medicine.objects.filter(Q(medicine_name__iexact=medicine_name) | Q(medicine_name__icontains=f' {medicine_name} '))
        medicine_count = medicines.count()
        if medicine_count == 0:
            medicines = Medicine.objects.none()
        else:
            for medicine in medicines:
                stock_size = medicine.stock_size
                total_stock_size += stock_size
                hospitals_with_medicines.append({
                    'medicine_id':medicine.pk,
                    'medicine_name': medicine.medicine_name,
                    'medicine_type': medicine.medicine_type,
                    'medicine_price': medicine.medicine_price,
                    'medicine_description': medicine.medicine_description,
                    'stock_size': medicine.stock_size,
                    'medicine_image': medicine.medicine_image.url if medicine.medicine_image else None,
                    'hospital_name': medicine.hospital.hospital_name,
                    'hospital_type': medicine.hospital.hospital_type,
                    'hospital_address': medicine.hospital.address,
                })

    context = {
        'medicine_name': medicine_name,
        'medicine_count': medicine_count,
        'hospitals_with_medicines': hospitals_with_medicines,
        'total_stock_size': total_stock_size,
        'medicines': medicines,  
        'cart_count':cart_count,
    }
    print(medicines)
    
    return render(request, "user/medicine-compare.html", context)





def diagnosticservices(request):
    cart_count = request.session.get('cart_count')
    diagnostic_services = DiagnosticService.objects.all()
    paginator = Paginator(diagnostic_services, 5) 
    page = request.GET.get('page')
    try:
        diagnostic_services = paginator.page(page)
    except PageNotAnInteger:
        diagnostic_services = paginator.page(1)
    except EmptyPage:
        diagnostic_services = paginator.page(paginator.num_pages)
    return render(request, "user/diagnostic-services.html", {'diagnostic_services': diagnostic_services, 'cart_count': cart_count})


def surgicalservices(request):
    cart_count = request.session.get('cart_count')
    surgical_services = SurgicalService.objects.all()
    paginator = Paginator(surgical_services, 5)
    page = request.GET.get('page')
    try:
        surgical_services = paginator.page(page)
    except PageNotAnInteger:
        surgical_services = paginator.page(1)
    except EmptyPage:
        surgical_services = paginator.page(paginator.num_pages)
    return render(request, "user/surgical-services.html", {'surgical_services': surgical_services, 'cart_count': cart_count})


def emergencyservices(request):
    cart_count = request.session.get('cart_count')
    emergency_services = EmergencyService.objects.all()
    paginator = Paginator(emergency_services, 5) 
    page = request.GET.get('page')
    try:
        emergency_services = paginator.page(page)
    except PageNotAnInteger:
        emergency_services = paginator.page(1)
    except EmptyPage:
        emergency_services = paginator.page(paginator.num_pages)
    return render(request, "user/emergency-services.html", {'emergency_services': emergency_services, 'cart_count': cart_count})


def hospital_register(request):
    if request.method == 'POST':
        hospital_name = request.POST.get('hospitalName')
        email = request.POST.get('email')
        contact_number = request.POST.get('contact')
        hospital_type = request.POST.get('hospitalType')
        password = request.POST.get('password')
        hospital_image = request.FILES.get('hospitalImage')
        docimage = request.FILES.get('docimage')
        address = request.POST.get('address')
        if Hospital.objects.filter(email=email).exists():
            messages.error(request, 'Email is already registered.')
            return redirect('hospital_register') 
        otp = generate_otp()
        new_hospital = Hospital.objects.create(
            hospital_name=hospital_name,
            email=email,
            contact_number=contact_number,
            hospital_type=hospital_type,
            password=password,
            hospital_image=hospital_image,
            hospital_doc=docimage,
            address=address,
            otp=otp,
        )
        try:
            resp = sendSMS(new_hospital.hospital_name, otp, new_hospital.contact_number)
            subject = 'OTP Verification for your Hospital Account'
            message = f'Hello {new_hospital.hospital_name},\n\nYou are attempting for an otp to your account. Your OTP for login verification is: {otp}\n\nIf you did not request this OTP, please ignore this email.'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [new_hospital.email]
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        except Exception as e:
            messages.error(request, 'Error occurred while sending OTP or email. Try Again after sometime.')
            new_hospital.delete()
            return redirect('hospital_register')
        # messages.success(request, 'Hospital registered successfully.')
        print("Hospital registered successfully")
        request.session['hospital_id'] = new_hospital.id
        return redirect('otp')  
    return render(request, "user/hospital-register.html")




def hospital_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print("Entered email:", email)
        print("Entered password:", password)
        try:
            hospital = Hospital.objects.get(email=email)
        except Hospital.DoesNotExist:
            messages.error(request, 'Invalid email or password.')
            print("Hospital with email {} does not exist.".format(email))
            return redirect('hospital_login')
        if password == hospital.password:
            if hospital.otp_status == "verified":
                if hospital.admin_status == "accepted":
                    print("Hospital login successful. Redirecting to hospital dashboard.")
                    request.session['hospital_verified_id'] = hospital.id
                    messages.success(request, 'Login Successful !')
                    return redirect('hospital_dashboard')
                else:
                    messages.info(request, 'Your hospital account is pending approval from the admin.')
                    return redirect('hospital_login')
            else:
                otp = generate_otp()
                hospital.otp = otp
                hospital.save()
                subject = 'OTP Verification for Hospital Login'
                message = f'Your OTP for login verification is: {otp}'
                from_email = settings.EMAIL_HOST_USER
                recipient_list = [hospital.email]
                send_mail(subject, message, from_email, recipient_list, fail_silently=False)
                sendSMS(hospital.hospital_name, otp, hospital.contact_number)
                messages.info(request, 'OTP sent to your email and phone. Please enter the OTP to login.')
                print("OTP sent to email and phone:", otp)
                return redirect('otp')
        else:
            messages.error(request, 'Invalid email or password.')
            print("Password entered for {} is incorrect.".format(email))
            return redirect('hospital_login')
    return render(request, "user/hospital-login.html")




def otp(request):
    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        hospital_id = request.session.get('hospital_id')
        print("Entered OTP:", entered_otp)
        print("Hospital ID from session:", hospital_id)
        if hospital_id:
            hospital = Hospital.objects.get(id=hospital_id)
            if entered_otp:
                if entered_otp == hospital.otp:
                    hospital.otp_status = "verified"
                    hospital.save()
                    messages.success(request, 'OTP validated successfully.')
                    hospital_id = hospital.id
                    request.session['hospital_verified_id'] = hospital_id
                    print("Hospital ID after verification:", hospital_id)
                    return redirect('hospital_login')
                else:
                    messages.error(request, 'Invalid OTP. Please try again.')
                    return redirect('otp')
            else:
                messages.error(request, 'Please enter the OTP.')
                return redirect('otp')
        else:
            messages.error(request, 'Hospital information not found. Please register again.')
            return redirect('hospital_register')
    return render(request, "user/otp.html")




def bed_availity(request):
    cart_count = request.session.get('cart_count')
    beds = BedAvailability.objects.all()
    paginator = Paginator(beds, 5)
    page = request.GET.get('page')
    try:
        beds = paginator.page(page)
    except PageNotAnInteger:
        beds = paginator.page(1)
    except EmptyPage:
        beds = paginator.page(paginator.num_pages)
    return render(request, "user/bed-avaliblity.html", {"beds": beds, 'cart_count': cart_count})



def appointment(request):
    cart_count = request.session.get('cart_count')
    doctor_availability = DoctorAvailability.objects.all()
    hospitals = Hospital.objects.all()
    if request.method == 'POST':
        appointment_for = request.POST.get('appointmentFor')
        service_required = request.POST.get('serviceRequired')
        appointment_type = request.POST.get('appointmentType')
        emergency_contact = request.POST.get('emergencyContact')
        date = request.POST.get('date')
        name = request.POST.get('name')
        time = request.POST.get('time')
        hospital = request.POST.get('hospital')
        user_id = request.session.get('user_login_id')
        user = User.objects.get(pk=user_id)
        appointment = Appointment.objects.create(
            user=user,
            appointment_for=appointment_for,
            service_required=service_required,
            appointment_type=appointment_type,
            emergency_contact=emergency_contact,
            date=date,
            time=time,
            name=name,
            hospital=hospital
        )
        appointment.save()
        messages.success(request,"Appointment Request Successful")
        return redirect('appointment')
    return render(request, "user/appointment.html", {'doctor_availability': doctor_availability, 'hospitals': hospitals,'cart_count':cart_count})





def request_appointment(request, doctor_availability_id):
    user_id = request.session.get('user_login_id')
    user = get_object_or_404(User, pk=user_id)
    doctor_availability = get_object_or_404(DoctorAvailability, pk=doctor_availability_id)
    hospital = doctor_availability.hospital 
    appointment = Appointment.objects.create(
        user=user,
        appointment_for="self", 
        service_required='Regular', 
        name=user.full_name, 
        appointment_type='Regular', 
        emergency_contact=user.phone, 
        date=datetime.date.today(), 
        time=datetime.datetime.now().time(), 
        hospital=hospital,  
        status='pending' 
    )
    subject = f'Appointment Request from {user.full_name}'
    message = f'Hello,\n\nA new appointment request has been made by {user.full_name}.\n\nAppointment Details:\nDate: {appointment.date}\nTime: {appointment.time}\nService Required: Regular\n\nPlease take necessary action.\n\nBest regards,\nYour Hospital Team'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [hospital.email]  
    send_mail(subject, message, from_email, recipient_list, fail_silently=False)
    messages.success(request, "Appointment Request Successful")
    return redirect('appointment')


def add_to_cart(request, medicine_id):
    medicine = Medicine.objects.get(pk=medicine_id)
    user_id = request.session.get('user_login_id')
    user = User.objects.get(pk=user_id)
    if medicine.stock_size > 0:
        cart_item = CartItem.objects.create(user=user, medicine=medicine, quantity=1)
        medicine.stock_size -= 1
        medicine.save()
        messages.success(request, "Added successfully!")
    else:
        messages.error(request, "Sorry, this medicine is out of stock.")
    return redirect('cart')



def cart(request):
    user_id = request.session.get('user_login_id')
    user = get_object_or_404(User, pk=user_id)
    pending_cart_items = CartItem.objects.filter(user=user, status='pending')
    pending_medicine_ids = list(set(pending_cart_items.values_list('medicine_id', flat=True)))
    medicines = Medicine.objects.filter(pk__in=pending_medicine_ids)
    total_amount = pending_cart_items.aggregate(total_amount=Sum('medicine__medicine_price'))['total_amount'] or Decimal('0')
    medicines_count = pending_cart_items.count()
    return render(request, "user/cart.html", {'medicines': medicines, 'medicines_count': medicines_count, "total_amount": total_amount})






def checkout(request):
    if request.method == 'POST':
        user_id = request.session.get('user_login_id')
        if user_id:
            user = User.objects.get(pk=user_id)
            cart_items = CartItem.objects.filter(user=user, status='pending')
            for cart_item in cart_items:
                cart_item.mark_as_ordered()
            return redirect('payment')
        return redirect('cart')


def blockchain(request, medicine_id):
    cart_count = request.session.get('cart_count')
    medicine = get_object_or_404(Medicine, id=medicine_id)
    bk_model_instance = get_object_or_404(BkModel, medicine=medicine)
    hash_medicineid = hashlib.sha256(str(medicine.id).encode()).hexdigest()
    hash_medicine_price = hashlib.sha256(medicine.medicine_price.encode()).hexdigest() 
    hash_medicine_type = hashlib.sha256(medicine.medicine_type.encode()).hexdigest()

    tampering_details = []  
    if bk_model_instance.medicineid != hash_medicineid:
        tampering_details.append('Medicine ID')
    if bk_model_instance.medicine_price != hash_medicine_price:
        tampering_details.append('Medicine Price')
    if bk_model_instance.medicine_type != hash_medicine_type:
        tampering_details.append('Medicine Type')

    if tampering_details:
        tampering_status = f"Data Tampered - {' and '.join(tampering_details)} tampered"
        messages.info(request, "Medicine Data Has Been Changed")
    else:
        tampering_status = "Data Not Tampered"

    context = {
        'medicine': medicine,
        'bk_model_instance': bk_model_instance,
        'tampering_status': tampering_status,
        'cart_count':cart_count,
    }
    return render(request, 'user/block-chain.html', context)


# Find Alternatives Testing
from django.shortcuts import render

def find_alternatives(request):
    message = ""
    alternatives = None
    
    if request.method == 'POST':
        medicine_name = request.POST.get('medicine_name', '').lower()
        if medicine_name == "acnesol 15gm":
            alternatives = [
                {'Drug_Name': 'Isotroin 30mg Capsule 10\'S', 'Reason': 'Acne', 'Description': 'combined with anti-acne actives of both natural and synthetic origin'},
                {'Drug_Name': 'Isotroin 20mg Capsule', 'Reason': 'Acne', 'Description': 'combined with anti-acne actives of both natural and synthetic origin'},
                {'Drug_Name': 'Vedasol 20% Gel 30gm', 'Reason': 'Acne', 'Description': 'combined with anti-acne actives of both natural and synthetic origin'},
                {'Drug_Name': 'Vedasol 30% Gel 60gm', 'Reason': 'Acne', 'Description': 'combined with anti-acne actives of both natural and synthetic origin'},
                {'Drug_Name': 'Clinopak 300Mg Tablet 10\'s', 'Reason': 'Acne', 'Description': 'combined with anti-acne actives of both natural and synthetic origin'},
                {'Drug_Name': 'Clinopak Gel 20gm', 'Reason': 'Acne', 'Description': 'combined with anti-acne actives of both natural and synthetic origin'},
                {'Drug_Name': 'Ticin Cream 20gm', 'Reason': 'Acne', 'Description': 'combined with anti-acne actives of both natural and synthetic origin'},
                {'Drug_Name': 'Addnok Tablet 20\'S', 'Reason': 'Adhd', 'Description': 'combined with anti-acne actives of both natural and synthetic origin'},
            ]
            print(alternatives)
        elif medicine_name == "paracetamol":
            alternatives = [
                {'Drug_Name': 'Tramadol', 'Reason': 'Pain relief', 'Description': 'both general and nerve-related pain.'},
                {'Drug_Name': 'Gabapentin', 'Reason': 'Pain relief', 'Description': 'both general and nerve-related pain.'},
                {'Drug_Name': 'Ibuprofen', 'Reason': 'Pain relief', 'Description': 'both general and nerve-related pain.'},
                {'Drug_Name': 'Tylenol', 'Reason': 'Pain relief', 'Description': 'both general and nerve-related pain.'},
            ]
            print(alternatives)
        elif medicine_name == "shelcal 90":
            message = "No similar medicine available."
        else:
            message = "Please enter a valid medicine name."
    else:
        message = "Please enter a medicine name."

    return render(request, 'find_alternatives.html', {'message': message, 'alternatives': alternatives})
