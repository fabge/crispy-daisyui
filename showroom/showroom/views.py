from django.views.generic import TemplateView

from .forms import Form1


class ShowroomView(TemplateView):
    template_name = 'showroom.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = Form1()
        return context
