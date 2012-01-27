from django.views.generic import ListView
from django.contrib.formtools.wizard.views import SessionWizardView
from django.db.models import Avg

from stats.models import Stat, Asset

__all__ = ('StatView', )


class StatView(ListView):
    """
    Stats for the different forms.

    """
    context_object_name = "stats_list"
    template_name = "haiku/stats.html"
    queryset = Asset.objects.all()

    def get_context_data(self, **kwargs):
        context = super(StatView, self).get_context_data(**kwargs)
        context['form_a'] = Stat.objects.filter(
            asset=self.queryset[0]).aggregate(Avg('cost'))
        context['form_b'] = Stat.objects.filter(
            asset=self.queryset[1]).aggregate(Avg('cost'))

        return context
