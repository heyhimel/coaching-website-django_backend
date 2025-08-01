from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(notice_banner)
admin.site.register(notice_details)
admin.site.register(blog_banner)
admin.site.register(blog_details)
admin.site.register(blog_comments)
admin.site.register(events_banner)
admin.site.register(events_details)
admin.site.register(event_speakers)