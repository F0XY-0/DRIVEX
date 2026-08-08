from django.db.models import Min , Max , Count 
from django.shortcuts import render
from random import choice
from .models import Car
from django.shortcuts import render , get_object_or_404


# Create your views here.
def home(request) : 
    cars = Car.objects.all()
    return render(request , "Main.html" , {"cars" : cars})

def contact(request) : 
    return render (request , "contact.html")

def main(request) :
    cars = Car.objects.all()

    price_min = request.GET.get('price_min')
    price_max = request.GET.get('price_max')
    hp_min = request.GET.get('hp_min')
    hp_max = request.GET.get('hp_max')
    color = request.GET.get('color')

    # conds 

    if price_min:
        cars = cars.filter(price__gte=price_min)
    if price_max:
        cars = cars.filter(price__lte=price_max)
    if hp_min:
        cars = cars.filter(horsepower__gte=hp_min)
    if hp_max:
        cars = cars.filter(horsepower__lte=hp_max)
    if color:
        cars = cars.filter(color__iexact=color)  

    colors = Car.objects.values_list('color', flat=True).distinct().order_by('color')

    stats = Car.objects.aggregate(
        total=Count('id'),
        min_price=Min('price'),
        max_price=Max('price'),
    )

    context = {
        'cars': cars,
        'colors': colors,
        'stats': stats,
        'filters': {
            'price_min': price_min or '',
            'price_max': price_max or '',
            'hp_min': hp_min or '',
            'hp_max': hp_max or '',
            'color': color or '',
        }
    }
    return render(request, 'Main.html', context)  

def Home(request) :
    cars = Car.objects.order_by("?")[:5]

    hero_car = choice(cars) if cars else None

    return render (request , "home.html" ,{
        "hero_car" : hero_car , 
        "cars" : cars ,
    })

def compare(request) : 
    ids = request.GET.get('ids' , '') 
    id_list = [i for i in ids.split(',') if i.isdigit()]
    cars = Car.objects.filter(id__in = id_list)

    max_values = {
        'price' : max((c.price for c in cars) , default=None) , 
        'year': max((c.year for c in cars), default=None) ,
        'horsepower': max((c.horsepower for c in cars), default=None) ,
        'mileage': max((c.mileage for c in cars), default=None) ,
    }

    return render(request , 'compare.html' , {'cars' : cars , 'max_values': max_values})

def car_detail(request , pk):
    car = get_object_or_404(Car , pk = pk ) 
    return render (request , 'car_detail.html' , {'car' : car})

