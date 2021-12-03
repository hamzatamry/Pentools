from django.urls import path
from .views import *


urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^$', index, name="homepage"),
    re_path(r'^contact/$', contact, name='contact'),
    re_path(r'^register/$', Registration.as_view(), name='register' ),
    re_path(r'^login/$', Authentication.as_view(), name='login'),
    re_path(r'^logout$', logout_view, name='logout'),
    re_path(r'^activerecon/nmap$', nmap, name='nmap'),
    re_path(r'^activerecon/hydra$', hydra, name='hydra'),
    re_path(r'passiverecon/sherlock$', sherlock, name='sherlock'),
    re_path(r'passiverecon/theharvester$', theharvester, name='theharvester'),
    re_path(r'enumeration/gobuster$', gobuster, name='gobuster'),
    re_path(r'enumeration/nikto$', nikto, name='nikto'),
]