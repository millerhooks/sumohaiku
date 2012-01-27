from django.views.generic import ListView
from django.contrib.formtools.wizard.views import SessionWizardView
from django.http import HttpResponseRedirect

from haiku.models import Haiku
from stats.models import Stat, Asset
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

__all__ = ('DashboardView', 'RegistrationFormTestWizard')


class DashboardView(ListView):
    """
    The main view with the haiku.

    """
    context_object_name = "haiku_list"
    template_name = "haiku/dashboard.html"
    queryset = Haiku.objects.all()

class RegistrationFormTestWizard(SessionWizardView):
    template_name = 'stats/registration_wizard.html'

    def done(self, form_list, **kwargs):
        """
        Process the forms and save the stats for processing time.

        """
        for (counter, form) in enumerate(form_list):
            if counter == 0:
                user = form.save()
            else:
                profile = form.save(commit=False)
                profile.user = user
                profile.save()

        asset_dict = {
            'a': 'UserProfileFormA',
            'b': 'UserProfileFormB',
        }
        cost = datetime.now() - datetime.strptime(
            form_list[0].cleaned_data['start_stamp'], "%Y-%m-%d %H:%M:%S.%f"
        )

        try:
            name = asset_dict[form_list[1].cleaned_data['form_version']]
            Stat(
                asset = Asset.objects.get(name = name),
                start_stamp = form_list[0].cleaned_data['start_stamp'],
                end_stamp = datetime.now(),
                cost = cost.seconds
            ).save()
        except:
            logger.error('failed to capture stat: %s' % datetime.now())

        return HttpResponseRedirect('/')
