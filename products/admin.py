from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(RobotType)
admin.site.register(Robot)
admin.site.register(ComponentType)
admin.site.register(ComponentModel)
admin.site.register(RobotComponent)
