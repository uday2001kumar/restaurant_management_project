from django.shortcuts import render
from django.conf import settings
# Create your views here.
def home(request):
    return render(request, 'home.html',{'restaurent_name':settings.RESTAURENT_NAME,'restaurent_phone':settings.RESTAURENT_PHONE})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request, 'contact.html')