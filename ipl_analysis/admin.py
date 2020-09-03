from django.contrib import admin
from .models import Deliveries, Matches, Umpires
# Register your models here.

admin.site.register(Deliveries)
admin.site.register(Matches)
admin.site.register(Umpires)