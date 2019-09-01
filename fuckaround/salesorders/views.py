from django.shortcuts import render

# Create your views here.
def salesorders(request):
    return render(request, 'salesorders/salesorders.html')