from django.contrib import admin

# Register your models here.

from .models import CrimeReport, Comment

admin.site.register(CrimeReport)
admin.site.register(Comment)
