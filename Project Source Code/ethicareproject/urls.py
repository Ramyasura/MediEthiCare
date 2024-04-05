"""
URL configuration for ethicareproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from userapp import views as userviews
from hospitalapp import views as hosviews
from adminapp import views as adminviews


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',userviews.index,name="index"),
    path('about/',userviews.about,name="about"),
    path('user/login/',userviews.userlogin,name="userlogin"),
    path('user/register/',userviews.userregister,name="userregister"),
    path('user/admin-login/',userviews.adminlogin,name="adminlogin"),
    path('user/hospital-register/',userviews.hospital_register,name="hospital_register"),
    path('user/hospital-login/',userviews.hospital_login,name="hospital_login"),
    path('contact/',userviews.contact,name="contact"),
    path('hospital-otp/',userviews.otp,name="otp"),



    path('user/dashboard/',userviews.userdashboard,name="userdashboard"),
    path('user/view-hospital/',userviews.viewhospital,name="viewhospital"),
    path('user/book-appiontment/',userviews.bookappiontment,name="bookappiontment"),
    path('user/book-services/',userviews.bookservices,name="bookservices"),
    path('user/medical-services/',userviews.viewmedicalrecords,name="medicalservices"),
    path('user/report-hospital/<int:medicine_id>/',userviews.reporthospital,name="reporthospital"),
    path('user/appointment-report/<int:medicine_id>/',userviews.reporthospital2,name="reporthospital2"),
    path('user/buy-medicine/',userviews.buymedicine,name="buymedicine"),
    path('user/pricing/',userviews.pricing,name="pricing"),
    path('user/faqs/',userviews.faqs,name="faqs"),
    path('user/profile/',userviews.userprofile,name="userprofile"),
    path('user/bed-availability/',userviews.bed_availity,name="bed_availity"),
    path('user/appointments/',userviews.appointment,name="appointment"),
    path('user/logout/', userviews.logout2, name='logout'),
    path('user/emergency-services/', userviews.emergencyservices, name='emergencyservices'),
    path('user/surgical-services/', userviews.surgicalservices, name='surgicalservices'),
    path('user/diagnostic-services/', userviews.diagnosticservices, name='diagnosticservices'),
    path('user/request-appointment/<int:doctor_availability_id>/', userviews.request_appointment, name='request_appointment'),
    path('user/medicine-compare/', userviews.medicine_compare, name='medicine_compare'),
    path('user/cart-page/', userviews.cart, name='cart'),
    path('user/add-to-cart-page/<int:medicine_id>/', userviews.add_to_cart, name='add_to_cart'),
    path('checkout/', userviews.checkout, name='checkout'),
    path('user/my-appointments/', userviews.myappointments, name='myappointments'),
    path('user/my-orders/', userviews.my_orders, name='my_orders'),
    path('user/medicine/<int:medicine_id>/blockchain/', userviews.blockchain, name='blockchain'),
    path('user/payment/online/', userviews.paymentmethod, name='payment'),
    path('find-alternative-medicines/', userviews.find_alternatives, name='medicine_recommendation'),













    path('hospital/dashboard/',hosviews.hospital_dashboard,name="hospital_dashboard"),
    path('hospital/add-medicines/',hosviews.medicines,name="medicines"),
    path('hospital/add-services/',hosviews.services,name="services"),
    path('hospital/view-services/',hosviews.viewservices,name="viewservices"),
    path('hospital/view-medicines/',hosviews.view_medicines,name="view_medicines"),
    path('hospital/all-medicines/',hosviews.all_medicines,name="all_medicines"),
    path('hospital/edit-medicines/<int:medicine_id>/', hosviews.edit_medicines, name="edit_medicines"),
    path('hospital/beds/',hosviews.bed,name="bed"),
    path('hospital/view-beds/',hosviews.view_bed,name="view_bed"),
    path('hospital/list-doctors/',hosviews.list_doct,name="list_doct"),
    path('hospital/pending-appiontments/',hosviews.pendingAppointments,name="pendingAppointments"),
    path('hospital/accept-appointment/<int:appointment_id>/',hosviews.acceptAppointment, name='accept-appointment'),
    path('cancel-appointment/<int:appointment_id>/',hosviews.cancelAppointment, name='cancel-appointment'),
    path('hospital/All-appiontments/',hosviews.viewAppointments,name="viewAppointments"),
    path('hospital/logout/', hosviews.user_logout, name='user_logout'),
    path('hospital/remove-medicine/<int:medicine_id>/', hosviews.remove_medicine, name='remove_medicine'),
    path('remove-service/<str:service_type>/<int:service_id>/', hosviews.removeService, name='remove-service'),
    path('remove-bed/<int:bed_id>/', hosviews.removeBed, name='remove-bed'),
    path('hospital/view-orders/', hosviews.view_orders, name='view_orders'),
    path('update-order-status/<int:order_id>/', hosviews.update_order_status, name='update_order_status'),
    path('hospital/all-orders/', hosviews.all_orders, name='all_orders'),









    path('admin-dashboard/', adminviews.admin_dashboard, name='admin_dashboard'),
    path('admin-pendninghospitals/', adminviews.pendinghospital, name='pendinghospital'),
    path('admin-all-hospitals/', adminviews.all_hospitals, name='all_hospitals'),
    path('admin-all-medicines/', adminviews.all_medicines, name='admin_all_medicines'),
    path('admin-view-reports/', adminviews.view_Reports, name='view_Reports'),
    path('admin-appointment-details/', adminviews.appointments_details, name='appointments_details'),
    path('accept_hospital/<int:hospital_id>/', adminviews.accept_hospital, name='accept_hospital'),
    path('remove_hospital/<int:hospital_id>/', adminviews.remove_hospital, name='remove_hospital'),
    path('delete-hospital-medicine/<int:medicine_id>/', adminviews.delete_medicine, name='delete_medicine'),
    path('delete_report/<int:report_id>/', adminviews.delete_report, name='delete_report'),
    path('admin-logout/', adminviews.admin_logout, name='admin_logout'),















]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)