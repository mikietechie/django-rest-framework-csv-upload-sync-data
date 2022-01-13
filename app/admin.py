from django.contrib import admin
from app.models import TempFile, Data

# Register your models here
@admin.register(TempFile)
class TempFileAdmin(admin.ModelAdmin):
    list_display = ["id"]


@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    list_display = ["id", "state"]