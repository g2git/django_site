# tvgroningen/context_processors/current_time.py
from django.utils import timezone

def current_time(request):
    # Add the current date and time to the context
    return {
        'current_time': timezone.localtime(timezone.now())  # Localized current time
    }
