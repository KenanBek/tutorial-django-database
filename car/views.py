from django.shortcuts import get_object_or_404, render, redirect

from models import Car
from forms import CarForm


def index(request, template="car/index.html", context={}):
    car_list = Car.objects.all()
    context['car_list'] = car_list
    return render(request, template, context)


def car(request, car_id=None, template="car/car.html", context={}):
    car_object = None
    car_form = None

    if car_id:
        car_object = get_object_or_404(Car, pk=car_id)

    car_form = CarForm(request.POST or None, instance=car_object)

    if request.method == 'POST':
        car_object = car_form.save()
        return redirect('/car')

    context['car_id'] = car_id
    context['car_object'] = car_object
    context['car_form'] = car_form

    return render(request, template, context)
