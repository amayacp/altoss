
from django.shortcuts import redirect, render
from django.contrib import messages
from app.models import  apply, enquery, userdata,register

# Create your views here.
def ex(request):
    return render(request, 'ex.html')

def base(request):
    return render(request, 'base.html')

def home(request):
    return render(request, 'home.html')

def training(request):
    return render(request, 'training.html')

def contact(request):
    return render(request, 'contact.html')
    
def course(request):
    return render(request, 'course.html')

def add_user(request):
    if request.method=='POST':
        uname=request.POST['Name']
        
        uemail=request.POST['Email']
        uphone=request.POST['Phone']
        umsg=request.POST['massage']


        
        user=userdata(Name=uname,massage=umsg,Email=uemail,Phone=uphone,)
       
    if userdata.objects.filter(Email=uemail).exists():
                messages.info(request, 'Email already exists!!!!!!')
                return redirect('contact') 
    else:
         messages.info(request,'You have registered successfully ')
    

    user.save()
        
       
    return redirect('contact')  


def reg(request):
    if request.method=='POST':
        uname=request.POST['Name']
        udate=request.POST['date']
        uemail=request.POST['Email']
        uphone=request.POST['Phone']
        umsg=request.POST['message']


        
        user=register(Name=uname,message=umsg,Email=uemail,Phone=uphone,date=udate)
       
    if register.objects.filter(Email=uemail).exists():
                messages.info(request, 'Email already exists!!!!!!')
                return redirect('course') 
    else:
         messages.info(request,'You have registered successfully ')
    

    user.save()
        
       
    return redirect('course') 

def enquerys(request):
    if request.method=='POST':
        uname=request.POST['Name']
        uemail=request.POST['Email']
        uphone=request.POST['Phone']
        umsg=request.POST['message']


        
        user=enquery(Name=uname,Email=uemail,Phone=uphone,message=umsg)
       
    if enquery.objects.filter(Email=uemail).exists():
                messages.info(request, 'Email already exists!!!!!!')
                return redirect('home') 
    else:
         messages.info(request,'Thank you for your inquiry....')
    

    user.save()
    return redirect('home') 

def app(request):
    if request.method=='POST':
        ucourse=request.POST['course']
        uname=request.POST['Name']
        uemail=request.POST['Email']
        uphone=request.POST['Phone']
        uplace=request.POST['place']


        
        user=apply(Name=uname,place=uplace,Email=uemail,Phone=uphone,course=ucourse)
       
    if apply.objects.filter(Email=uemail).exists():
                messages.info(request, 'Email already exists!!!!!!')
                return redirect('training') 
    else:
         messages.info(request,'APPLICATION RECIEVED....')
    

    user.save()
        
       
    return redirect('training') 