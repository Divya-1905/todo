from django.contrib import admin

# Register your models here.
from.models import user
from todoapp.models import Todo
admin.site.register(Todo)
admin.site.register(user)
