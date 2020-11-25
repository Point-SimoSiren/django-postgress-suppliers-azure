import os

from django.core.wsgi import get_wsgi_application

###################### Lisätty ####################################

# If WEBSITE_HOSTNAME is defined as an environment variable, then we're running
# on Azure App Service and should use the production settings in production.py.
settings_module = "azuresite.production" if 'WEBSITE_HOSTNAME' in os.environ else 'app.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)
######################################################################

'''
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'suppliers.settings')
'''

application = get_wsgi_application()
