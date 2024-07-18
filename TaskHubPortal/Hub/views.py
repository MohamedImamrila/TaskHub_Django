from django.shortcuts import render,redirect
from .models import CustomUser,AddTask
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout


def index(request):
    return render(request,'index.html')

def signup(request):
    if request.method == 'POST':
        Name = request.POST.get('Name')
        email = request.POST.get('email')
        Phonenumber = request.POST.get('Phonenumber')
        password = request.POST.get('password')
        Address = request.POST.get('Address')

        # Create a new CustomUser instance
        user = CustomUser.objects.create(username = email, email=email)
        user.Name = Name
        user.set_password(password)
        user.Phonenumber = Phonenumber
        user.Address = Address
        user.save()
        messages.success(request, 'Account created successfully')
        return redirect('/')
    else:
        messages.error(request, 'Invalid form submission')
        return redirect('/')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=email,password=password)
        if user is not None:
            login(request,user)
            messages.success(request, 'Login successfully')
            return redirect('/dashboard')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('/')
    else:
        messages.error(request, 'Please sign-Up Here')
        return redirect('signup')


def addtask(request):
    if request.method == "POST":
        TaskName = request.POST.get('TaskName')
        AssignedBy = request.POST.get('AssignedBy')
        Status = request.POST.get('Status')
        email = request.user.email
        getid = CustomUser.objects.get(username = email,)
        task = AddTask(assigned_to_id = getid.id,TaskName=TaskName,AssignedBy=AssignedBy,Status=Status)
        if task:
            task.save()
            messages.success(request, 'Task Assigned successfully')
            return redirect('dashboard')
        else:
            messages.error(request, 'Failed to assign')
            return redirect('dashboard')
    else:
        return redirect('login')
    
def dashboard(request):
    user = request.user.Name
    getid = request.user.id
    tasks_assigned_to_user = AddTask.objects.filter(assigned_to_id=getid)
    return render(request,'dashboard.html',{'tasks': tasks_assigned_to_user,'name':user})

def logout_user(request):
    logout(request)
    return redirect('home')