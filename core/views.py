from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')


def harekrishna(request):
    return render(request, 'harekrishna.html')


def customer_page(request):
    return render(request, 'harekrishna.html')


def courier_page(request):
    return render(request, 'harekrishna.html')
