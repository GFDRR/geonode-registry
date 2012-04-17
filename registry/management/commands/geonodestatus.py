from django.core.management.base import BaseCommand
from registry.models import GeoNodeInstance
import requests

def ping_geonode(instance):
    try:
        req = requests.get(instance.url)
        geoserver_req = requests.get(instance.geoserver_base_url)
        geonetwork_req = requests.get(instance.geonetwork_base_url)
    except requests.exceptions.ConnectionError, e:
        return instance
def check_geonodes():
    #we get a list of geonodes to query
    instances = GeoNodeInstance.objects.all()
    failed_geonodes = []
    for instance in instances:
       faultyinstance = ping_geonode(instance)
       if faultyinstance is not None:
           failed_geonodes.append(faultyinstance)
    return failed_geonodes
def send_admin_email(geonodes):
    """This is the function that sends the site administrators an email on failed geonodes"""
    # Do not send email of that setting is not defined.
    if len(geonodes) == 0:
        return
    subject = 'Problematic layers at %s' % settings.SITENAME
    message = render_to_string('../templates/mail.txt', geonodes)
    mail_admins(subject, message, fail_silently=False) 
class Command(BaseCommand):
    help = 'Ping all the geonodes we have to see their status'
    args = '[none]'

    def handle(self, *args, **keywordargs):
        context = check_geonodes()
        send_admin_email(context)
