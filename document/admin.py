from django.contrib import admin
from .models import Document

# Register your models here.
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['catch_word','slug','station','date','author']
    search_fields = ['catch_word','date','station']

admin.site.register(Document,DocumentAdmin)
