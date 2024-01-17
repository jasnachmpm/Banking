from django.http import HttpResponse
from django.shortcuts import render
#from .models import Place


# Create your views here.
def demo(request):
    #obj = Place.objects.all()
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def package(request):
    #obj = Place.objects.all()
    return render(request, 'package.html')


def service(request):
    return render(request, 'service.html')


def contact(request):
    return render(request, 'contact.html')

def booking(request):
    return render(request, 'booking.html')

def destination(request):
    return render(request, 'destination.html')

#def team(request):
#    return render(request, 'team.html')

#def testimonial(request):
#    return render(request, 'testimonial.html')
