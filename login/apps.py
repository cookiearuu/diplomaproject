from django.apps import AppConfig

from website import templates
import website

class LoginConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'login'
