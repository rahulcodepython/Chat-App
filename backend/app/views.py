from django.shortcuts import render

# Create your views here.

def chatHomeView(request):
    return render(request, 'index.html')