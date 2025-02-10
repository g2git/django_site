from django.shortcuts import render
from django.views import generic
from .models import Presentation

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_presentations = Presentation.objects.all().count()

    context = {
        'num_presentations': num_presentations,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

def slideshow_view(request):
    # Get all objects
    instances = Presentation.objects.filter(status=Presentation.ACTIVE)

    # Convert the `timedelta` to milliseconds for each object
    for obj in instances:
        # Assuming you have a `duration` field in your model
        if obj.duration:
            # Convert to milliseconds
            obj.duration = int(obj.duration.total_seconds() * 1000)
        else:
            obj.duration = 0
    return render(request, 'slideshow.html', {'instances': instances})

def privacy(request):
    """View function for privacy page of site."""

    # Render the HTML template privacy.html
    return render(request, 'privacy.html')

class PresentationListView(generic.ListView):
    model = Presentation
    context_object_name = 'presentation_list'   # name for the list as a template variable
    paginate_by = 2

    def get_queryset(self):
        return Presentation.objects.all().order_by('id')
    
class PresentationDetailView(generic.DetailView):
    model = Presentation