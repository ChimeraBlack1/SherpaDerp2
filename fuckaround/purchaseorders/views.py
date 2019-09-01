from django.shortcuts import render

def purchaseorders(request):
    return render(request, 'purchaseorders/purchaseorders.html')