import os
import sys

# Jelastic virtualenv path
virtenv = os.path.expanduser('~') + '/virtenv'
activate_this = os.path.join(virtenv, 'bin', 'activate_this.py')

if os.path.exists(activate_this):
    execfile(activate_this, dict(__file__=activate_this))

# Add project to path
project_dir = os.path.expanduser('~') + '/ROOT'
sys.path.insert(0, project_dir)
sys.path.insert(0, os.path.expanduser('~'))

# Django settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'gsetm.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()