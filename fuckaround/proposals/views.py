from django.shortcuts import render

# Create your views here.
def proposals(request):
    return render(request, 'proposals/proposals.html')