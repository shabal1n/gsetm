import os
import sys

# Jelastic virtualenv path - ИСПРАВЛЕНО
virtenv = '/var/www/webroot/virtenv'
activate_this = os.path.join(virtenv, 'bin', 'activate_this.py')

if os.path.exists(activate_this):
    execfile(activate_this, dict(__file__=activate_this))

# Add project to path
project_dir = '/var/www/webroot/ROOT'
sys.path.insert(0, project_dir)
sys.path.insert(0, '/var/www/webroot')

# Django settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'gsetm.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()