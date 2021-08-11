from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def landing_page(request):
    return HttpResponse("Hello World! Nama saya Aliya")


def second_page(request):
    return HttpResponse("SecondPage")


def example(request):
    return render(request, 'example.html')


def newpage(request):
    return HttpResponse("new")
