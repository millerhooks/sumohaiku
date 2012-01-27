from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

import settings

from haiku.views import DashboardView, RegistrationFormTestWizard
from stats.views import StatView
from random import choice
from haiku.forms import UserForm, UserProfileFormA, UserProfileFormB

profile_form = choice([UserProfileFormA, UserProfileFormB])
form_list = [UserForm, profile_form]

urlpatterns = patterns('',
    # Examples:
    # url(r'^sumohaiku/', include('sumohaiku.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),

    url(r'^$', DashboardView.as_view(), name='dashboard'),
    url(r'^stats/$', StatView.as_view(), name='stats'),

    url(r'^register/$',
        RegistrationFormTestWizard.as_view(form_list), name='test_register'),
)


if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.map_path('media'),
        }),
)