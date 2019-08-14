from django.contrib import admin
# from . models import *
from . interestModel import interest
from . userModel import user
# Register your models here.

admin.site.register(user)
admin.site.register(interest)
# admin.site.register(questions)
