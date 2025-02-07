from django.contrib import admin
from .models import Presentation

# # Define the admin class
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('last_name', 'first_name')

class PresentationAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'summary', 'duration', 'status', 'color', 'image')
    
    # fieldsets = (
    #     (None, {
    #         'fields': ('title', 'user', 'summary', 'duration')
    #     }),
    #     ('Background', {
    #         'fields': ('picture', 'color')
    #     }),
    #     )

# Register the admin class with the associated model
# admin.site.register(User, UserAdmin)
admin.site.register(Presentation, PresentationAdmin)


