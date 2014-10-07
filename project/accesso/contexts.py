from django.conf import settings
from django.contrib.sites.models import Site


def project_context(request):
    return {
        'project_name': settings.PROJECT_NAME,
        'site': Site.objects.get_current(),
    }