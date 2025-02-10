from django.contrib import admin

# Register your models here.

from .models import Report, Comment

admin.site.register(Report)
admin.site.register(Comment)
