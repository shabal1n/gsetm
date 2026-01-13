import os
import sys

# Jelastic virtualenv path
virtenv = '/var/www/webroot/virtenv'
activate_this = os.path.join(virtenv, 'bin', 'activate_this.py')

if os.path.exists(activate_this):
    with open(activate_this) as f:
        exec(f.read(), {'__file__': activate_this})

# Add project to path
project_dir = '/var/www/webroot/ROOT'
sys.path.insert(0, project_dir)
sys.path.insert(0, '/var/www/webroot')

# Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gsetm.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()