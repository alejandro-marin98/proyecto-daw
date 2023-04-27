from django.shortcuts import render
from django.contrib import admin
from django.views.generic import View
from django .contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import User

admin.site.register(User)

