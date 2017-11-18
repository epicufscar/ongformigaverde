from django.shortcuts import render


def home(request):
    return render(request, 'ong/home/home.html')

