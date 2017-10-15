from django.contrib import admin
from pups.models import UserProfile, Puppy
# Register your models here.

class PuppyAdmin(admin.ModelAdmin):
    list_display = ('owner', 'name', 'breed', 'age')


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('active_user', 'renter',)

admin.site.register(Puppy, PuppyAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
