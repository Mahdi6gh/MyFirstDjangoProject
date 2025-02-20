from django.contrib import admin
from .models import projects
from .models import ticket
# Register your models here.
admin.site.register(projects)
admin.site.register(ticket)