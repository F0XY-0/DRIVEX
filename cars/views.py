from django.db.models import Min , Max , Count
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from random import choice
from .models import Car

class ContactView(TemplateView):
    template_name = "contact.html"

class HomeView(ListView):
    model = Car
    template_name = "home.html"
    context_object_name = "cars"

    def get_queryset(self):
        return Car.objects.order_by("?")[:5]   

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cars = context["cars"]
        context["hero_car"] = choice(cars) if cars else None
        context["colors"] = Car.objects.values_list('color', flat=True).distinct().order_by('color')
        return context

    


class CarListView(ListView):
    model = Car
    template_name = "Main.html"
    context_object_name = "cars"

    def get_queryset(self):
        queryset = Car.objects.all()

        self.price_min = self.request.GET.get('price_min')
        self.price_max = self.request.GET.get('price_max')
        self.hp_min = self.request.GET.get('hp_min')
        self.hp_max = self.request.GET.get('hp_max')
        self.color = self.request.GET.get('color')

        if self.price_min:
            queryset = queryset.filter(price__gte=self.price_min)
        if self.price_max:
            queryset = queryset.filter(price__lte=self.price_max)
        if self.hp_min:
            queryset = queryset.filter(horsepower__gte=self.hp_min)
        if self.hp_max:
            queryset = queryset.filter(horsepower__lte=self.hp_max)
        if self.color:
            queryset = queryset.filter(color__iexact=self.color)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["colors"] = Car.objects.values_list(
            'color', flat=True
        ).distinct().order_by('color')

        context["stats"] = Car.objects.aggregate(
            total=Count('id'),
            min_price=Min('price'),
            max_price=Max('price'),
        )

        context["filters"] = {
            'price_min': self.price_min or '',
            'price_max': self.price_max or '',
            'hp_min': self.hp_min or '',
            'hp_max': self.hp_max or '',
            'color': self.color or '',
        }

        return context


class CarDetailView(DetailView):
    model = Car
    template_name = "car_detail.html"
    context_object_name = "car"
    pk_url_kwarg = "pk"


class CompareView(TemplateView):
    template_name = "compare.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        ids = self.request.GET.get('ids', '')
        id_list = [i for i in ids.split(',') if i.isdigit()]
        cars = Car.objects.filter(id__in=id_list)

        context["cars"] = cars
        context["max_values"] = {
            'price': max((c.price for c in cars), default=None),
            'year': max((c.year for c in cars), default=None),
            'horsepower': max((c.horsepower for c in cars), default=None),
            'mileage': max((c.mileage for c in cars), default=None),
        }

        return context