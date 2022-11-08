from django import forms
from django.contrib.auth.models import User
from APP.models import user,UserProfileInfo 

class SignUp(forms.ModelForm):
    class Meta():
        model = user 
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput(),
        }

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portofolio_site','profile_pic')
