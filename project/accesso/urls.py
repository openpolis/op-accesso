# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from .users.views import UserProfileView

# load admin modules
from django.contrib import admin
admin.autodiscover()

urls = (
    # public urls
    url(r'^$', TemplateView.as_view(template_name='homepage.html')),

    # oauth urls
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),

    url(r'^accounts/', include('allauth.urls')),
    url(r'^%s$' % settings.LOGIN_REDIRECT_URL.lstrip('/'), UserProfileView.as_view(), name='account_profile'),
    url(r'^admin/', include(admin.site.urls)),
)
urlpatterns = patterns('', *urls)

# static and media urls not works with DEBUG = True, see static function.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('', url(r'^__debug__/', include(debug_toolbar.urls)), )
