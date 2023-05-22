from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Tarif)
admin.site.register(Client)
admin.site.register(Operator)
admin.site.register(Sity)
