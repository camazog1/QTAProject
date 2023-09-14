from django.shortcuts import render
from django.http import HttpResponse
from .models import Ticket

# Create your views here.
def home(request):
    return render(request, 'home.html')
 
def mainscreen(request):
    tickets = Ticket.objects.all()
    return render(request, 'mainscreen.html',{'tickets':tickets})