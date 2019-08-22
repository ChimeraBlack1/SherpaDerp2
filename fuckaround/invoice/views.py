from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def invoice(request):
    return render(request, 'invoice/invoice.html')