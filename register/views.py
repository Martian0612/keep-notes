# for using built-in register form from django which have basic username, password1, passwor2 fields with proper validation.

# from django.shortcuts import render
# from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm

# # Create your views here.
# def register(response):
#     if response.method == "POST":
#         form = UserCreationForm(response.POST)
#         if form.is_valid():
#            form.save()
#     else:
#         form = UserCreationForm()
#     return render(response, "register/register.html",{"form":form})

## ####################################################
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login, logout

def register(response):
    if response.method == "POST":
        
        form = RegisterForm(response.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.date_of_birth = form.cleaned_data["date_of_birth"]
            print("date of birth is ",user.date_of_birth)
            user.save()
        # object = User.objects.get(username = "sudhanshu_ranjan").values()
        # object = User.objects.all().get(username = "sudhanshu_ranjan").values()
        # print("object is ",object)

        return redirect("/")
    else:
        form = RegisterForm()

    return render(response,"register/register.html",{"form":form})

def Userlogin(request):
    if request.user.is_authenticated:
            # redundant 
        # if request.path == "/login":
            return redirect('/')
    else:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            print("username is ", username)
            print("password is ", password)
            user = authenticate(username = username, password = password)
            # basically it means user will contain some value or maybe true or false
            print("user is ", user)
            if user is not None:
                login(request,user)
                print(user)
                return redirect('/')
            else:
                # can display message that wrong username or password
                return render(request, 'login.html')
    # else:
    # after login, it will come to index page
    return render(request, 'register/login.html')

# it started working by using forms, over directly using link-button for logout., using forms after logout user can't access the main page.
def Userlogout(request):
    # user authenticated hai means login kiya hai, then only hi woh logout kar sakta hai
    # below if condition maybe redundant because logout button is present only inside the index page
    # if request.user.is_authenticated:
    #     logout(request)

    # directly logout function run hoga and then login page pe redirect kar denge
    logout(request)
    
    # after logout it will redirect to login page
    return redirect('/login')