from django.contrib import admin
from .models import Presentation

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


