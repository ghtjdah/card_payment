from django.shortcuts import render

# Create your views here.

def pay(request):
    return render(request, 'pay.html')

def completepay(request):
    return render(request, 'completepayment.html')