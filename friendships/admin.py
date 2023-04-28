from django.contrib import admin
from .models import Friendship


class FriendshipAdmin(admin.ModelAdmin):
    model = Friendship
    list_display = ('request_from', 'request_to', 'is_accepted', 'created_at')


admin.site.register(Friendship, FriendshipAdmin)
