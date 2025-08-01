from django.apps import AppConfig


class ContactUsAboutUsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'contact_us_about_us'

    def ready(self):
        import contact_us_about_us.signals
