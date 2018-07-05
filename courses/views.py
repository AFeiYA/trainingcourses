# Create your views here.
from django.views import generic

from .models import  Course


class HomeView(generic.TemplateView):
    template_name = 'main.html'


class IndexView(generic.ListView):
    template_name = 'courses/index.html'
    context_object_name = 'latest_course_list'

    def get_queryset(self):
        """Return the last five published courses."""
        return Course.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Course
    template_name = 'courses/detail.html'

