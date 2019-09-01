from django.shortcuts import render

# Create your views here.
def itemreceipts(request):
    return render(request, 'itemreceipts/itemreceipts.html')
