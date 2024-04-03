from django.contrib import admin
from authentication import models
from django.contrib.auth.admin import UserAdmin

# Register your models here.
@admin.register(models.Procfile)
class ProcfileAdmin(UserAdmin):
    # Los fieldsets originales de UserAdmin, puedes modificar según tus necesidades
    procfile_fields = ()
    fieldsets = UserAdmin.fieldsets + (
        ('Extra Info', {'fields': procfile_fields}),
    )