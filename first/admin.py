from django.contrib import admin
from .models import Hobby

class HobbyAdmin(admin.ModelAdmin):
    list_display = ("user", "hobby")  # Show user and hobby
    search_fields = ("user__username", "hobby")  # Search by username and hobby
    list_filter = ("user",)  # Filter by user

admin.site.register(Hobby, HobbyAdmin)


# from django.contrib import admin
# from .models import Hobby

# class HobbyAdmin(admin.ModelAdmin):
#     list_display = ("name", "hobby")  # Show these fields in the admin table
#     search_fields = ("name", "hobby")  # Add a search box
#     list_filter = ("name",)  # Add a filter sidebar

# admin.site.register(Hobby)

# # Register your models here.
