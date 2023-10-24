from django.shortcuts import render

# Create your views here.
class PackageListView(ListView):
    model = State
    template_name = 'pack_list.html'
    context_object_name = 'states'
