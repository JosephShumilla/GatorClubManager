from django.contrib import admin
from members.models import Club, Membership, Event

# Register your models here.

admin.site.register(Club)
admin.site.register(Membership)
admin.site.register(Event)