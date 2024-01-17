from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import UserProfile


# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        # first_name = request.POST['first_name']
        # last_name = request.POST['last_name']
        #  email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('credentials:register')
            # elif User.objects.filter(email=email).exists():
            #     messages.info(request, "Email Already Exists")
            #     return redirect('credentials:register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                messages.info(request, "Registration Successful")
                return redirect('credentials:login')  # Redirect to the login page upon successful registration

        else:
            messages.info(request, "Password not matching")
            return redirect('credentials:register')

    return render(request, 'register.html')



def login(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            #return redirect('/')
            return render(request,'personal.html')

        else:
            messages.info(request,'Invalid Credentials')
            return  redirect('login')
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def personal(request):
    if request.method == 'POST':
        name = request.POST['name']
        dob = request.POST['dob']
        age = request.POST['age']
        gender = request.POST['gender']
        phone = request.POST['phone']
        mail = request.POST['mail']
        address = request.POST['address']
        district = request.POST['district']
        branch = request.POST['branch']
        acctype = request.POST['acctype']
        material = request.POST['material']

        # Create and save the user profile
        user_profile = UserProfile.objects.create(
            name=name, dob=dob, age=age, gender=gender,
            phone=phone, mail=mail, address=address,
            district=district, branch=branch, acctype=acctype,
            material=material
        )

        messages.info(request, "Application Accepted")
        return redirect('/')  # Redirect to the login page upon successful registration

    return render(request, 'personal.html')