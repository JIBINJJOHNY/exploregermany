from django.shortcuts import render
from touristplace.models import State
from django.urls import reverse
# Create your views here.
class PackageListView(ListView):
    model = State
    template_name = 'home.html'
    context_object_name = 'states'
class PackageDetailView(DetailView):
    model = State
    template_name = 'pack_detail.html'
    context_object_name = 'state'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        state_id = self.kwargs['pk'] 
        context['packages'] = Pack.objects.filter(state_id=state_id)
        return context
