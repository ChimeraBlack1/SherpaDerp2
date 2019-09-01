from django.shortcuts import render

# Create your views here.
def payables(request):
    return render(request, 'payables/payables.html')