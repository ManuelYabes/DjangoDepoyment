from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from APP.forms import SignUp,UserProfileForm,UserForm
from APP.models import user

from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def base(request):
    return render(request, 'html/base.html')

def index(request):
    pengguna = user.objects.order_by('name')
    return render(request, 'html/index.html', {'pengguna': pengguna})

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('APP:index'))
            else:
                return HttpResponse("ACC not activate")
        else:
            print('someone trying')
            print('Username: {} and password {}'.format(username,password))
            return HttpResponse("invalid login detail")
    else:
        return render(request,'html/login.html')
            
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('../index')

@login_required
def special(request):
    return HttpResponse("you ar login")

def signup(request):
    form = SignUp()

    if request.method == "POST":
        form = SignUp(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('EROR')

    return render(request, 'html/signup.html',{'form':form})

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request, 'html/register.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})

