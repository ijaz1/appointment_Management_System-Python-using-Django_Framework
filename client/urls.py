from django.urls import path
from . import views

urlpatterns = [
    path('', views.fnIndex, name='index'),
    path('signUp/', views.fnSignUp, name='signUp'),
    path('logIn/', views.fnLogIn, name='logIn'),
    path('client_Home/', views.fnClient_Home, name='client_Home'),
    path('booking_Web/', views.fnBooking_Web, name='booking_Web'),
    path('booking_App/', views.fnBooking_App, name='booking_App'),
    path('admin_Home/', views.fnAdmin_Home, name='admin_Home'),
    path('schedule_web/', views.fnschedule_web, name='schedule_web'),
    path('schedule_app/', views.fnschedule_app, name='schedule_app'),
    path('saveScheduledTimeSlot/', views.fnsaveScheduledTimeSlot, name='saveScheduledTimeSlot'),
    path('CheckWeb/', views.fnCheckWeb, name='CheckWeb'),
    path('CheckApp/', views.fnCheckApp, name='CheckApp'),
    path('saveScheduledTimeSlotApp/', views.fnsaveScheduledTimeSlotApp, name='saveScheduledTimeSlotApp'),
    path('logoutAdmin/', views.fnadminLogOut, name='logoutAdmin'),
    path('LogoutClient/', views.fnclientLogOut, name='LogoutClient'),
    path('WebBookingSlot/<slotId>', views.fnWebBookingSlot, name='WebBookingSlot'),
    path('viewWebBookingClient/', views.fnviewWebBookingClient, name='viewWebBookingClient'),
    path('canselWebBooking/<slot>', views.fncanselWebBooking, name='canselWebBooking'), 
    path('AppBookingSlot/<AppSlotId>', views.fnAppBookingSlot, name='AppBookingSlot'), 
    path('viewAppBookingClient/', views.fnviewAppBookingClient, name='viewAppBookingClient'), 
    path('canselAppBooking/<Appslot>', views.fncanselAppBooking, name='canselAppBooking'), 
    path('ViewWebAdmin/', views.fnViewWebAdmin, name='ViewWebAdmin'), 
    path('ViewAppAdmin/', views.fnViewAppAdmin, name='ViewAppAdmin'), 

]
