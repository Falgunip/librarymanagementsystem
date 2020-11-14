from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Users)
admin.site.register(Admin)
admin.site.register(Genres)
admin.site.register(Books)
admin.site.register(Issues)


