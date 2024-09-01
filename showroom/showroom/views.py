from django.shortcuts import render
from .forms import Form1
from bakery.views import BuildableTemplateView

class ShowroomView(BuildableTemplateView):
    template_name = 'showroom.html'
    build_path = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = Form1()
        return context
