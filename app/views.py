
from django.shortcuts import redirect, render
from django.contrib import messages
from app.models import  apply, enquery, userdata,register
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth

# Create your views here.
def ex(request):
    return render(request, 'ex.html')

def base(request):
    return render(request, 'base.html')

def base2(request):
    return render(request, 'base2.html')
    
def home(request):
    return render(request, 'home.html')

def training(request):
    return render(request, 'training.html')

def contact(request):
    return render(request, 'contact.html')
    
def course(request):
    return render(request, 'course.html')

def signin(request):
    return render(request, 'signin.html')



def user_login (request):
    if request.method=='POST':
        username=request.POST['uname']
        password=request.POST['psw']
        user=auth.authenticate(username=username,password=password)
        request.session["uid"]=user.id
        
        if user is not None:
            if user.is_staff:
                login(request,user)
                return redirect('admin')
            else:
                login(request,user)
                auth.login(request,user)
                Name=user.first_name +" "+ user.last_name
                messages.info(request, f'Welcome {Name}')
                return redirect('tutor_home')

        else:
            messages.info(request, 'Invalid Username or Password. Try Again.')
            return redirect('login_page')
    else:
        return redirect('login_page')

@login_required(login_url='user_login')
def admin(request):
    if not request.user.is_staff:
        return redirect('login_page')
    return render(request,'admin.html')

def logout(request):
    request.session["uid"] = ""
    auth.logout(request)
    return redirect('signin')

def add_user(request):
    if request.method=='POST':
        uname=request.POST['Name']
        
        uemail=request.POST['Email']
        uphone=request.POST['Phone']
        umsg=request.POST['massage']

        u=userdata(Name=uname,massage=umsg,Email=uemail,Phone=uphone)
       
    if userdata.objects.filter(Email=uemail).exists():
                messages.error(request, 'Email already exists!!!!!!')
                return redirect('contact') 
    else:
        messages.success(request,'Thank you for contacting us.We will try to reach you as soona as possible... ')

    

    u.save()
        
       
    return redirect('contact')

@login_required(login_url='user_login')
def msg(request):
    msg=userdata.objects.all()
    
    return render(request,'msg.html',{'u':msg})

def msg_approve(request,pk):
    leave = userdata.objects.get(id=pk)
    leave.status = 1
    leave.save()
    return redirect('msg')

def msg_reject(request, pk):
    leave =  userdata.objects.get(id=pk)
    leave.status = 2
    leave.save()
    return redirect('msg')

    

@login_required(login_url='user_login')
def edit_user(request,pk):
    if request.method=="POST":
        msg=userdata.objects.get(id=pk)
        msg.Name=request.POST['Name']
        msg.Email=request.POST['Email']
        msg.Phone=request.POST['Phone']
        msg.massage=request.POST['massage']
        msg.save()
        return redirect('msg')
 
#@login_required(login_url='user_login')
#def delete_user(request,pk):
 #   msg=userdata.objects.get(id=pk)
 #   msg.delete()
 #   return redirect('msg')
@login_required(login_url='user_login')
def delete_user(request,pk):
    u=userdata.objects.get(id=pk)
    u.delete()
    return redirect('msg')  


    
def reg(request):
    if request.method=='POST':
        uname=request.POST['Name']
        udate=request.POST['date']
        uemail=request.POST['Email']
        uphone=request.POST['Phone']
        umsg=request.POST['message']


        
        user=register(Name=uname,message=umsg,Email=uemail,Phone=uphone,date=udate)
       
    if register.objects.filter(Email=uemail).exists():
                messages.error(request, 'Email already exists!!!!!!')
                return redirect('course') 
    else:
         messages.success(request,'You have registered successfully ')
    

    user.save()
        
       
    return redirect('course') 

@login_required(login_url='user_login')
def regist(request):
    msg=register.objects.all()
    return render(request,'regist.html',{'user':msg})

def regist_approve(request,pk):
    leave = register.objects.get(id=pk)
    leave.status = 1
    leave.save()
    return redirect('regist')

def regist_reject(request, pk):
    leave =  register.objects.get(id=pk)
    leave.status = 2
    leave.save()
    return redirect('regist')


@login_required(login_url='user_login')
def delete_reg(request,pk):
    user=register.objects.get(id=pk)
    user.delete()
    return redirect('regist')  


def enquerys(request):
    if request.method=='POST':
        uname=request.POST['Name']
        uemail=request.POST['Email']
        uphone=request.POST['Phone']
        uproject=request.POST['project']
        umsg=request.POST['message']


        
        user=enquery(Name=uname,Email=uemail,Phone=uphone,message=umsg,project=uproject,)
       
    if enquery.objects.filter(Email=uemail).exists():
                messages.error(request, 'Email already exists!!!!!!')
                return redirect('home') 
    else:
         messages.success(request,'Thank you for your enquiry....')
    

    user.save()
    return redirect('home') 

@login_required(login_url='user_login')
def enquir(request):
    msg=enquery.objects.all()
    return render(request,'enquir.html',{'user':msg})

def enquir_approve(request,pk):
    leave = enquery.objects.get(id=pk)
    leave.status = 1
    leave.save()
    return redirect('enquir')

def enquir_reject(request, pk):
    leave =  enquery.objects.get(id=pk)
    leave.status = 2
    leave.save()
    return redirect('enquir')


@login_required(login_url='user_login')
def delete_enq(request,pk):
    user=enquery.objects.get(id=pk)
    user.delete()
    return redirect('enquir')  


def app(request):
    if request.method=='POST':
        ucourse=request.POST['course']
        uname=request.POST['Name']
        uemail=request.POST['Email']
        uphone=request.POST['Phone']
        uplace=request.POST['place']


        
        user=apply(Name=uname,place=uplace,Email=uemail,Phone=uphone,course=ucourse)
       
    if apply.objects.filter(Email=uemail).exists():
                messages.error(request, 'Email already exists!!!!!!')
                return redirect('training') 
    else:
         messages.success(request,'APPLICATION RECIEVED....')
    

    user.save()
        
       
    return redirect('training') 

@login_required(login_url='user_login')
def appl(request):
    msg=apply.objects.all()
    return render(request,'appl.html',{'user':msg})

def appl_approve(request,pk):
    leave = apply.objects.get(id=pk)
    leave.status = 1
    leave.save()
    return redirect('appl')

def appl_reject(request, pk):
    leave =  apply.objects.get(id=pk)
    leave.status = 2
    leave.save()
    return redirect('appl')


@login_required(login_url='user_login')
def delete_apply(request,pk):
    user=apply.objects.get(id=pk)
    user.delete()
    return redirect('appl')  