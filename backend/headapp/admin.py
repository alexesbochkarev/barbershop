from django.contrib import admin

from .models import Feedback

admin.site.site_header = 'Панель администрирования'
admin.site.site_title = 'Панель администрирования'

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    """
    Админ-панель модели профиля
    """
    list_display = ('name', 'phone', 'ip_address', 'time_create', 'time', 'date', 'actual_time', 'status')
    list_display_links = ('phone', 'ip_address')