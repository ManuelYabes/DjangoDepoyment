from django.urls import path
from APP import views

app_name = 'APP'

urlpatterns = [
    path('',views.base,name='base'),
    path('index/',views.index,name='index'),
    path('signup/',views.signup,name='signup'),
    path('register/',views.register,name='register'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('special/',views.special,name='special'),
]