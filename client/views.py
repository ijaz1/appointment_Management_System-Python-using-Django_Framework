import email
from http import client
from django.contrib import messages
from django.shortcuts import redirect, render
from client.models import Client, WebTimeSlot, AppTimeSlot, BookedWebTimeSlots, BookedAppTimeSlots
from django.core.mail import send_mail

# Create your views here.


def fnIndex(request):
    return render(request, 'index.html')


def fnClient_Home(request):
    return render(request, 'client_Home.html')


def fnBooking_Web(request):
    return render(request, 'booking_Web.html')


def fnBooking_App(request):
    return render(request, 'booking_App.html')


def fnAdmin_Home(request):
    return render(request, 'admin_Home.html')


def fnschedule_web(request):
    return render(request, 'schedule_web_booking.html')


def fnschedule_app(request):
    return render(request, 'schedule_app_booking.html')


def fnSignUp(request):
    if request.method == 'POST':
        email = request.POST['email']
        obj = Client.objects.filter(email=email).exists()
        if obj == False:
            firstname = request.POST['firstname']
            print(firstname)
            lastname = request.POST['lastname']
            print(lastname)
            phonenumber = request.POST['phonenumber']
            print(phonenumber)
            email = request.POST['email']
            print(email)
            password = request.POST['password']
            print(password)
            obj1 = Client(first_Name=firstname, last_Name=lastname,
                          phone_Number=phonenumber, email=email, password=password)
            obj1.save()
            messages.success(request, 'Account Created Successfully')
            return redirect('client_Home')
        messages.error('Email already exist')
        return redirect('index')
    return redirect('index')


def fnLogIn(request):
    email = request.POST['email']
    password = request.POST['password']
    obj = Client.objects.filter(email=email).exists()
    if email == 'admin@it.in' and password == '12345678':
        request.session['admin'] = '111'
        return redirect('admin_Home')
    elif obj == True:
        try:
            ob = Client.objects.get(email=email, password=password)
            request.session['client'] = ob.id
            return redirect('client_Home')
        except:
            messages.error(request, 'password is wrong')
            return redirect('index')
    else:
        messages.error(request, 'email is error')
        return redirect('index')


def fnsaveScheduledTimeSlot(request):
    if request.method == 'POST':
        scheduled_date = request.POST['scheduled_date']
        firstSlot = request.POST['firstSlot']
        firstSelect = request.POST['firstSelect']
        SecondSlot = request.POST['SecondSlot']
        SecondSelect = request.POST['SecondSelect']
        ThirdSlot = request.POST['ThirdSlot']
        ThirdSelect = request.POST['ThirdSelect']
        fourthSlot = request.POST['fourthSlot']
        fourthSelect = request.POST['fourthSelect']
        fifthSlot = request.POST['fifthSlot']
        fifthSelect = request.POST['fifthSelect']
        sixthSlot = request.POST['sixthSlot']
        sixthSelect = request.POST['sixthSelect']
        seventhSlot = request.POST['seventhSlot']
        seventhSelect = request.POST['seventhSelect']
        WebTimeSlot(scheduled_Date=scheduled_date,scheduled_Time=firstSlot, status=firstSelect).save()
        WebTimeSlot(scheduled_Date=scheduled_date,scheduled_Time=SecondSlot, status=SecondSelect).save()
        WebTimeSlot(scheduled_Date=scheduled_date,scheduled_Time=ThirdSlot, status=ThirdSelect).save()
        WebTimeSlot(scheduled_Date=scheduled_date,scheduled_Time=fourthSlot, status=fourthSelect).save()
        WebTimeSlot(scheduled_Date=scheduled_date,scheduled_Time=fifthSlot, status=fifthSelect).save()
        WebTimeSlot(scheduled_Date=scheduled_date,scheduled_Time=sixthSlot, status=sixthSelect).save()
        WebTimeSlot(scheduled_Date=scheduled_date,scheduled_Time=seventhSlot, status=seventhSelect).save()
        messages.success(request, 'Time Slot Added Succesfully')
        return redirect('admin_Home')
    messages.error(request, 'something went error try again')
    return redirect('admin_Home')


def fnsaveScheduledTimeSlotApp(request):
    if request.method == 'POST':
        scheduled_date = request.POST['scheduled_date']
        firstSlot = request.POST['firstSlot']
        firstSelect = request.POST['firstSelect']
        SecondSlot = request.POST['SecondSlot']
        SecondSelect = request.POST['SecondSelect']
        ThirdSlot = request.POST['ThirdSlot']
        ThirdSelect = request.POST['ThirdSelect']
        fourthSlot = request.POST['fourthSlot']
        fourthSelect = request.POST['fourthSelect']
        fifthSlot = request.POST['fifthSlot']
        fifthSelect = request.POST['fifthSelect']
        sixthSlot = request.POST['sixthSlot']
        sixthSelect = request.POST['sixthSelect']
        seventhSlot = request.POST['seventhSlot']
        seventhSelect = request.POST['seventhSelect']
        AppTimeSlot(scheduled_Date=scheduled_date,scheduled_Time=firstSlot, status=firstSelect).save()
        AppTimeSlot(scheduled_Date=scheduled_date,scheduled_Time=SecondSlot, status=SecondSelect).save()
        AppTimeSlot(scheduled_Date=scheduled_date,scheduled_Time=ThirdSlot, status=ThirdSelect).save()
        AppTimeSlot(scheduled_Date=scheduled_date,scheduled_Time=fourthSlot, status=fourthSelect).save()
        AppTimeSlot(scheduled_Date=scheduled_date,scheduled_Time=fifthSlot, status=fifthSelect).save()
        AppTimeSlot(scheduled_Date=scheduled_date,scheduled_Time=sixthSlot, status=sixthSelect).save()
        AppTimeSlot(scheduled_Date=scheduled_date,scheduled_Time=seventhSlot, status=seventhSelect).save()
        messages.success(request, 'Time Slot Added Succesfully')
        return redirect('admin_Home')
    messages.error(request, 'something went error try again')
    return redirect('admin_Home')


def fnCheckWeb(request):
    checkDate = request.POST['checkDate']
    obj = WebTimeSlot.objects.filter(
        scheduled_Date=checkDate, status='available')
    context = {'availableSlot': obj}
    return render(request, 'booking_Web.html', context)


def fnCheckApp(request):
    checkDate = request.POST['checkDate']
    obj = AppTimeSlot.objects.filter(
        scheduled_Date=checkDate, status='available')
    context = {'availableSlotApp': obj}
    return render(request, 'booking_App.html', context)


def fnadminLogOut(request):
    del request.session['admin']
    return redirect('index')


def fnclientLogOut(request):
    del request.session['client']
    return redirect('index')


def fnWebBookingSlot(request, slotId):
    try:
        WebTimeSlot.objects.filter(id=slotId).update(status='booked')
        ob = request.session['client']
        obemail = Client.objects.get(id=ob)
        email = obemail.email
        send_mail(
            'Your Request is Accepted',
            'we will contact you',
            'muhammedijazkari168@gmail.com',
            [email],
            fail_silently=False,
        )
        obslot = WebTimeSlot.objects.get(id=slotId)
        BookedWebTimeSlots(client_id=ob, slot_id=slotId, scheduled_Date=obslot.scheduled_Date,
                           scheduled_Time=obslot.scheduled_Time, status=obslot.status, client_Name=obemail.first_Name, client_email=email, client_phone=obemail.phone_Number).save()
        messages.success(
            request, 'You have booked succesfully you get confirmation mail')
        return redirect('client_Home')
    except:
        messages.error(request, 'something went wrong try again')
        return redirect('client_Home')


def fnviewWebBookingClient(request):
    clientId = request.session['client']
    obslot = BookedWebTimeSlots.objects.filter(
        client_id=clientId, status='booked')
    context = {'slot': obslot}
    return render(request, 'viewWebDevelopmentBookingClient.html', context)


def fncanselWebBooking(request, slot):
    try:
        BookedWebTimeSlots.objects.filter(id=slot).update(status='cancelled')
        obslot_id = BookedWebTimeSlots.objects.get(id=slot)
        webSlotId = obslot_id.slot_id
        WebTimeSlot.objects.filter(id=webSlotId).update(status='available')
        messages.success(request, 'Your Appointment Cancelled Succesfully')
        return redirect('viewWebBookingClient')
    except:
        return redirect('client_Home')


def fnAppBookingSlot(request, AppSlotId):
    try:
        AppTimeSlot.objects.filter(id=AppSlotId).update(status='booked')
        ob = request.session['client']
        obemail = Client.objects.get(id=ob)
        email = obemail.email
        send_mail(
            'Your Request is Accepted',
            'we will contact you',
            'muhammedijazkari168@gmail.com',
            [email],
            fail_silently=False,
        )
        obslot = AppTimeSlot.objects.get(id=AppSlotId)
        BookedAppTimeSlots(client_id=ob, slot_id=AppSlotId, scheduled_Date=obslot.scheduled_Date,
                           scheduled_Time=obslot.scheduled_Time, status=obslot.status, client_Name=obemail.first_Name, client_email=email, client_phone=obemail.phone_Number).save()
        messages.success(
            request, 'You have booked succesfully you get confirmation mail')
        return redirect('client_Home')
    except:
        messages.error(request, 'something went wrong try again')
        return redirect('client_Home')


def fnviewAppBookingClient(request):
    clientId = request.session['client']
    obslot = BookedAppTimeSlots.objects.filter(
        client_id=clientId, status='booked')
    context = {'slot': obslot}
    return render(request, 'viewAppDevelopmentBookingClient.html', context)


def fncanselAppBooking(request, Appslot):
    try:
        BookedAppTimeSlots.objects.filter(
            id=Appslot).update(status='cancelled')
        obslot_id = BookedAppTimeSlots.objects.get(id=Appslot)
        AppSlotId = obslot_id.slot_id
        AppTimeSlot.objects.filter(id=AppSlotId).update(status='available')
        messages.success(request, 'Your Appointment Cancelled Succesfully')
        return redirect('viewAppBookingClient')
    except:
        return redirect('client_Home')

def fnViewWebAdmin(request):
    obj=BookedWebTimeSlots.objects.filter(status='booked')
    context={'web':obj}
    return render(request,'viewWebBookingsAdmin.html',context)

def fnViewAppAdmin(request):
    obj=BookedAppTimeSlots.objects.filter(status='booked')
    context={'app':obj}
    return render(request,'viewAppBookingsAdmin.html',context)
