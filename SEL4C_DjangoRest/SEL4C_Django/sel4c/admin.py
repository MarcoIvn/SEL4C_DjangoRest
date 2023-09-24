from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin

admin.site.register(models.Entrepreneur)
admin.site.register(models.Admin, UserAdmin)
admin.site.register(models.Activity)
admin.site.register(models.File)
admin.site.register(models.Question)
admin.site.register(models.Answer)