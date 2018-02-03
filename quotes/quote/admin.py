from django.contrib import admin
from .models import Tag,Quote
# Register your models here.

class TagAdmin(admin.ModelAdmin):
    list_display = ['name']

class QuoteAdmin(admin.ModelAdmin):
    list_display = ['text','author','created_time']

admin.site.register(Tag,TagAdmin)
admin.site.register(Quote,QuoteAdmin)
