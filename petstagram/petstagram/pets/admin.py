from django.contrib import admin
from petstagram.pets.models import Pet, Like


class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'age')


admin.site.register(Pet, PetAdmin)
admin.site.register(Like)
