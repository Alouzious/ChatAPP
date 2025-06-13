from django.contrib import admin
from chat.models import FriendRequest

@admin.register(FriendRequest)
class FriendRequestAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'is_accepted', 'timestamp')
    list_filter = ('is_accepted', 'timestamp')  
    search_fields = ('sender__username', 'receiver__username')  
    ordering = ('-timestamp',)  
    list_per_page = 20  


    readonly_fields = ('timestamp',)


