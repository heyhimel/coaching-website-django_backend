from django.apps import AppConfig


class HomeSubscribeStoryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home_subscribe_story'

    def ready(self):
        import home_subscribe_story.signals
