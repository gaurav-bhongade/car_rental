from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from datetime import datetime
from .models import Booking
from apps.cars.models import Car

def book_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        pickup_date = request.POST.get('pickup_date')
        return_date = request.POST.get('return_date')
        
        # Calculate total price
        pickup = datetime.strptime(pickup_date, '%Y-%m-%d').date()
        return_d = datetime.strptime(return_date, '%Y-%m-%d').date()
        days = (return_d - pickup).days
        total_price = car.price_per_day * days
        
        Booking.objects.create(
            car=car,
            customer_name=customer_name,
            email=email,
            phone=phone,
            pickup_date=pickup,
            return_date=return_d,
            total_price=total_price
        )
        messages.success(request, 'Booking submitted successfully!')
        return redirect('car_detail', pk=car.id)
    return render(request, 'bookings/book_car.html', {'car': car})
