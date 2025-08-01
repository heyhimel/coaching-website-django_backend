from django.db.models.signals import pre_save,post_delete
from django.dispatch import receiver
from .models import homepage_banner,our_features_section,success_story
import os

# homepage banner unused image remove 
@receiver(pre_save,sender=homepage_banner)
def delete_old_banner_image_on_change(sender, instance, **kwargs):
    """
    Before saving, check if the image is changed; if yes, delete old file from disk.
    """
    if not instance.pk:
        # New object being created; nothing to delete
        return

    try:
        old_banner_file = homepage_banner.objects.get(pk=instance.pk).banner_image
    except homepage_banner.DoesNotExist:
        return
    
    new_banner_file = instance.banner_image
    if old_banner_file and old_banner_file != new_banner_file:
        if os.path.isfile(old_banner_file.path):
            os.remove(old_banner_file.path)

@receiver(post_delete,sender=homepage_banner)
def delete_banner_image_on_delete(sender, instance, **kwargs):
    """
    After deleting BackgroundBanner object, remove its image file from disk.
    """
    if instance.banner_image:
        if os.path.isfile(instance.banner_image.path):
            os.remove(instance.banner_image.path)


# homepage success story back unused image remove 
@receiver(pre_save,sender=success_story)
def delete_old_banner_image_on_change(sender, instance, **kwargs):
    """
    Before saving, check if the image is changed; if yes, delete old file from disk.
    """
    if not instance.pk:
        # New object being created; nothing to delete
        return

    try:
        old_banner_file = success_story.objects.get(pk=instance.pk).story_background_image
    except success_story.DoesNotExist:
        return
    
    new_banner_file = instance.story_background_image
    if old_banner_file and old_banner_file != new_banner_file:
        if os.path.isfile(old_banner_file.path):
            os.remove(old_banner_file.path)

@receiver(post_delete,sender=success_story)
def delete_banner_image_on_delete(sender, instance, **kwargs):
    """
    After deleting BackgroundBanner object, remove its image file from disk.
    """
    if instance.story_background_image:
        if os.path.isfile(instance.story_background_image.path):
            os.remove(instance.story_background_image.path)


# homepage features section unused image remove 
@receiver(pre_save,sender=our_features_section)
def delete_old_banner_image_on_change(sender, instance, **kwargs):
    """
    Before saving, check if the image is changed; if yes, delete old file from disk.
    """
    if not instance.pk:
        # New object being created; nothing to delete
        return

    try:
        old_banner_file = our_features_section.objects.get(pk=instance.pk).feature_image
    except our_features_section.DoesNotExist:
        return
    
    new_banner_file = instance.feature_image
    if old_banner_file and old_banner_file != new_banner_file:
        if os.path.isfile(old_banner_file.path):
            os.remove(old_banner_file.path)

@receiver(post_delete,sender=our_features_section)
def delete_banner_image_on_delete(sender, instance, **kwargs):
    """
    After deleting BackgroundBanner object, remove its image file from disk.
    """
    if instance.feature_image:
        if os.path.isfile(instance.feature_image.path):
            os.remove(instance.feature_image.path)