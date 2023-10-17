from django.contrib import admin
from .models import Relation, Profile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Register your models here.

admin.site.register(Relation)
