from django.shortcuts import render,redirect,HttpResponse
from datetime import datetime,timedelta
from .helpers import *
from .models import *
from django.contrib.messages import success,error

def index(request):
    context = {}
    bookings = Booking.objects.all()
    min_date = datetime.now()+timedelta(hours=3)
    max_date = datetime.now()+timedelta(days=3)
    context['bookings'] = bookings
    context['min_date'] = format_min_max(min_date)
    context['max_date'] = format_min_max(max_date)
    for i in bookings:
        
        print(datetime(i.f_date.year,i.f_date.month,i.f_date.day,i.f_date.hour,i.f_date.minute))

    return render(request,'core/index.html',context)

def book_hall(request):

    if request.POST:
        user = request.user
        reason = request.POST.get('reason',"")
        f_date = request.POST.get("f_date")
        e_date = request.POST.get("e_date")
        
        from_date = format_date(f_date)
        end_date = format_date(e_date)

        bookings = Booking.objects.all()
        eligible = True
        for i in bookings:
            
            if from_date>datetime(i.f_date.year,i.f_date.month,i.f_date.day,i.f_date.hour,i.f_date.minute) and from_date<datetime(i.e_date.year,i.e_date.month,i.e_date.day,i.e_date.hour,i.e_date.minute):
                eligible=False
        if eligible:
            book = Booking.objects.create(
                user=user,reason=reason,f_date=f_date,e_date=e_date
            )
            book.save()
            success(request,"Newton is Hall Booked!!")
        else:
            error(request,"Newton Hall is Busy at the Time!!")
    else:
        return HttpResponse("Invalid Request")
    return redirect('index')
