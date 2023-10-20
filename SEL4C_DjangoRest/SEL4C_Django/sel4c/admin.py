from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Permission, Group
from django.contrib.auth.forms import UserChangeForm, UserCreationForm


class CustomUserAdmin(UserAdmin):
     # permisos de la app SEL4C
    sel4c_permissions = Permission.objects.filter(content_type__app_label='sel4c')

    # campos
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', 'first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_superuser','user_permissions',)}),
    )
    
    # Visualización
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_superuser')
    
    # Add 
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_superuser', 'user_permissions'),
        }),
    )
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "user_permissions":
            kwargs["queryset"] = self.sel4c_permissions
        return super().formfield_for_manytomany(db_field, request, **kwargs)



admin.site.register(models.Entrepreneur)
admin.site.register(models.Administrator,CustomUserAdmin)
admin.site.register(models.Activity)
admin.site.register(models.File)
admin.site.register(models.Question)
admin.site.register(models.Answer)
admin.site.register(models.ActivitiesCompleted)
admin.site.register(models.EntrepreneurProfile)
admin.site.register(models.EntrepreneurEcomplexity)