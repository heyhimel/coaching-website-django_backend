from django.contrib import admin
from .models import homepage_banner,homepage_banner_content,success_story,subscriber_mobile_number,our_features_section
# Register your models here.
admin.site.register(homepage_banner)
admin.site.register(homepage_banner_content)
admin.site.register(success_story)
admin.site.register(subscriber_mobile_number)
admin.site.register(our_features_section)