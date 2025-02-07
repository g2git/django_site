from django.db import models
from django.urls import reverse # Used in get_absolute_url() to get URL for specified ID
from django.conf import settings
from django.db.models import UniqueConstraint # Constrains fields to unique values
from django.db.models.functions import Lower # Returns lower cased value of field
from datetime import timedelta
from colorfield.fields import ColorField

# class User(models.Model):
#     """Model representing an gebruiker."""
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)


#     class Meta:
#         ordering = ['last_name', 'first_name']

#     def get_absolute_url(self):
#         """Returns the URL to access a particular user instance."""
#         return reverse('gebruiker-detail', args=[str(self.id)])

#     def __str__(self):
#         """String for representing the Model object."""
#         return f'{self.last_name}, {self.first_name}'

class Presentation(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    title = models.CharField(max_length=200)
    
    # Foreign Key used because book can only have one user, but users can have multiple presentations.
    # user = models.ForeignKey(User, on_delete=models.RESTRICT, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    
    date = models.DateField(auto_now_add=True)
    
    summary = models.TextField(
        max_length=1000, help_text="Enter a summary of the presentation")

    duration = models.DurationField(default=timedelta(seconds=15),help_text="Enter the duration of the presentation")
    
    color = ColorField(default='#FFFFFF')  # default is white
    
    ACTIVE = 'active'
    INACTIVE = 'inactive'
    
    STATUS_CHOICES = [
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive'),
    ]
    
    # Show instance of odel in slides only if status is active
    status = models.CharField(
        max_length=8,
        choices=STATUS_CHOICES,
        default=ACTIVE,
    )
    
    image = models.ImageField(upload_to='images/',  null=True, blank=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.title

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this presentation."""
        return reverse('presentation-detail', args=[str(self.id)])
