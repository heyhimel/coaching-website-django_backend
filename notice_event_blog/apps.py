from django.apps import AppConfig


class NoticeEventBlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'notice_event_blog'

    def ready(self):
        import notice_event_blog.signals
