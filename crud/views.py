from django.shortcuts import render, redirect
from .models import mytask
from .forms import task_form
from django.contrib.auth.models import User,auth
from django.contrib import messages

def regi_task(request, id=0):
    workall=mytask.objects.all()
    if request.method=="GET":
        if id==0:
            form=task_form()
        else:
            work=mytask.objects.get(pk=id)
            form=task_form(instance=work)
        return render(request, 'index.html', {'f':form,'w':workall})
    else:
        if id==0:
            form=task_form(request.POST)
        else:
            work=mytask.objects.get(pk=id)
            form=task_form(request.POST,instance=work)
        if form.is_valid():
            form.save()
            return redirect('/')
        return render(request, 'index.html',{'f':form, 'w':work} )
        
def Delete(request,id):
    dele=mytask.objects.get(pk=id)
    dele.delete()
    return redirect('/')

def register(request):
    if request.method=='POST':
        first_name=request.POST['fname']
        last_name=request.POST['lname']
        email=request.POST['email']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password1==password2:

            if User.objects.filter(username=username).exists():
                
                messages.info(request, "Username already exist!")
                return redirect("/register")

            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already exist!")
                return redirect("/register")

            else:
                user=User.objects.create_user(first_name=first_name, last_name=last_name, email= email, username=username, password=password1)
                user.save()
                messages.info(request, "Registered successfully")
                return render(request, 'login.html')
        
        else:
            messages.info(request, "Password did not match, Please check!")
            return render(request, 'register.html')
        
    else:
        return render(request, 'register.html')

def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Username/Password')
            return redirect('/login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

