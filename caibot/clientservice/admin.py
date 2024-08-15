from django.contrib import admin
from .models import Client, Message


admin.site.site_header = 'GTrader'


class ClientAdmin(admin.ModelAdmin):
    list_filter = ('account_number', 'created_at', 'date_to')
    list_display = ('account_number', 'created_at', 'date_to')
    search_fields = ('account_number',)


admin.site.register(Client, ClientAdmin)
admin.site.register(Message)
