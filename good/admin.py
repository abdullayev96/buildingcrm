from django.contrib import admin
from .models import *


#
# class DiscordAdmin(admin.ModelAdmin):
#     list_display = ("id", "","title", "image")
#     list_display_links = ("id", "name")
#     search_fields = ("id", "name")

class ResultdAdmin(admin.ModelAdmin):
    list_display = ("id", "number","name")
    list_display_links = ("id", "name")
    search_fields = ("id", "name")

class ChangeAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")
    search_fields = ("id", "name")


class HelperAdmin(admin.ModelAdmin):
    list_display = ("id", "name","title", "number")
    list_display_links = ("id", "title")
    search_fields = ("id", "title")
    list_filter = ('title', )



class UsersdAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "phone", "subject", "message")
    list_display_links = ("id", "name")
    search_fields = ("id", "name")

class PhotoAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "image", "img", "created")
    list_display_links = ("id", "title")
    search_fields = ("id", "title")

admin.site.register(Discord)
admin.site.register(Change, ChangeAdmin)
admin.site.register(ChangePrice)
admin.site.register(ChangePrices)

admin.site.register(Result, ResultdAdmin)
admin.site.register(Helper, HelperAdmin)
admin.site.register(Users, UsersdAdmin)
admin.site.register(Photos, PhotoAdmin)


