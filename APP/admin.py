from django.contrib import admin
from APP.models import user,UserProfileInfo

# Register your models here.

admin.site.register(user)
admin.site.register(UserProfileInfo)