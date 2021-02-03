from django.conf import settings

def my_site(request):
    return {'SITE_URL': settings.SITE_URL}