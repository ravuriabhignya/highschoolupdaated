from django.contrib import admin
from .models import Schooldata, Studentdata, Bookdata

admin.site.register(Schooldata)
admin.site.register(Studentdata)
admin.site.register(Bookdata)