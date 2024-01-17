from . import views
from django.urls import path

app_name = 'bankapp'

urlpatterns = [
    path('', views.demo, name='demo'),
    path('about/', views.about, name='about'),
    path('package/', views.package, name='package'),
    path('service/', views.service, name='service'),
    path('contact/', views.contact, name='contact'),
    path('booking/', views.booking, name='booking'),
    path('destination/', views.destination, name='destination'),
    path('team/', views.team, name='team'),
    path('testimonial/', views.testimonial, name='testimonial'),
]
