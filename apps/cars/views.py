from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Car

def cars_list(request):
    cars = Car.objects.filter(availability=True)
    
    # Filters
    brand = request.GET.get('brand')
    fuel_type = request.GET.get('fuel_type')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    
    if brand:
        cars = cars.filter(brand__icontains=brand)
    if fuel_type:
        cars = cars.filter(fuel_type=fuel_type)
    if min_price:
        cars = cars.filter(price_per_day__gte=min_price)
    if max_price:
        cars = cars.filter(price_per_day__lte=max_price)
    
    # Pagination
    paginator = Paginator(cars, 9)  # 9 per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'cars/cars_list.html', {'page_obj': page_obj})

def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    return render(request, 'cars/car_detail.html', {'car': car})
