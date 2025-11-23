from django.contrib import admin
from .models import Questions, Answers

# Register your models here.

admin.site.register([Questions, Answers])