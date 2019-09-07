from django.contrib import admin
from .models import Spaceport, Launch, Company

# Register your models here.

admin.site.register(Spaceport)
admin.site.register(Launch)
admin.site.register(Company)