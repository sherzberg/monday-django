from django.views.generic import TemplateView
from .models import Code

class DeploymentView(TemplateView):
    template_name = 'deployments/index.html'

    def get_context_data(self, **kwargs):
        context = super(DeploymentView, self).get_context_data(**kwargs)
        context['object_list'] = Code.objects.all()
        return context
