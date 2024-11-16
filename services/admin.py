from django.contrib import admin
from .models import *


# Register your models here.

admin.site.register(Service)
admin.site.register(Mission)
admin.site.register(MissionImage)
admin.site.register(MissionVideo)
admin.site.register(Approach)
admin.site.register(Feature)

