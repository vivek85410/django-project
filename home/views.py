from django.shortcuts import render,HttpResponse
from home.models import contact
#create your views here.
def index(request):
    
    return render(request,'index.html')

def services(request):
    #return HttpResponse("this is services")
    
    return render(request,'services.html')

def About(request):
   #return HttpResponse("welcome to my ice cream centre we have many types of ice creams.")
   return render(request,'About.html')
 
 
def details(request): 
     #return HttpResponse("feel free to contact on email : singhvivek49966@gmail.com")
    if request.method=="POST":
        Contact=contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        Contact.name=name
        Contact.email=email
        Contact.phone=phone
        Contact.desc=desc

        Contact.save() 
        return HttpResponse ("Thanks for your response")

      
    return render(request,'details.html')
  

