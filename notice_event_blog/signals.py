from django.db.models.signals import pre_save,post_delete
from django.dispatch import receiver
from .models import notice_banner,blog_banner,events_banner,blog_details,events_details,event_speakers,notice_details
import os

# banner_about_page banner unused image remove 
@receiver(pre_save,sender=notice_banner)
def delete_old_banner_image_on_change(sender, instance, **kwargs):
    
    if not instance.pk:
        # New object being created; nothing to delete
        return

    try:
        old_banner_file = notice_banner.objects.get(pk=instance.pk).banner_image
    except notice_banner.DoesNotExist:
        return
    
    new_banner_file = instance.banner_image
    if old_banner_file and old_banner_file != new_banner_file:
        if os.path.isfile(old_banner_file.path):
            os.remove(old_banner_file.path)

@receiver(post_delete,sender=notice_banner)
def delete_banner_image_on_delete(sender, instance, **kwargs):
    
    if instance.banner_image:
        if os.path.isfile(instance.banner_image.path):
            os.remove(instance.banner_image.path)

# blog_banner banner unused image remove 
@receiver(pre_save,sender=blog_banner)
def delete_old_banner_image_on_change(sender, instance, **kwargs):
    
    if not instance.pk:
        # New object being created; nothing to delete
        return

    try:
        old_banner_file = blog_banner.objects.get(pk=instance.pk).banner_image
    except blog_banner.DoesNotExist:
        return
    
    new_banner_file = instance.banner_image
    if old_banner_file and old_banner_file != new_banner_file:
        if os.path.isfile(old_banner_file.path):
            os.remove(old_banner_file.path)

@receiver(post_delete,sender=blog_banner)
def delete_banner_image_on_delete(sender, instance, **kwargs):
    
    if instance.banner_image:
        if os.path.isfile(instance.banner_image.path):
            os.remove(instance.banner_image.path)

# blog_details unused image remove 
@receiver(pre_save,sender=blog_details)
def delete_old_banner_image_on_change(sender, instance, **kwargs):
    
    if not instance.pk:
        # New object being created; nothing to delete
        return

    try:
        old_banner_file = blog_details.objects.get(pk=instance.pk).blog_image
    except blog_details.DoesNotExist:
        return
    
    new_banner_file = instance.blog_image
    if old_banner_file and old_banner_file != new_banner_file:
        if os.path.isfile(old_banner_file.path):
            os.remove(old_banner_file.path)

@receiver(post_delete,sender=blog_details)
def delete_banner_image_on_delete(sender, instance, **kwargs):
    
    if instance.blog_image:
        if os.path.isfile(instance.blog_image.path):
            os.remove(instance.blog_image.path)

# events_banner banner unused image remove 
@receiver(pre_save,sender=events_banner)
def delete_old_banner_image_on_change(sender, instance, **kwargs):
    
    if not instance.pk:
        # New object being created; nothing to delete
        return

    try:
        old_banner_file = events_banner.objects.get(pk=instance.pk).banner_image
    except events_banner.DoesNotExist:
        return
    
    new_banner_file = instance.banner_image
    if old_banner_file and old_banner_file != new_banner_file:
        if os.path.isfile(old_banner_file.path):
            os.remove(old_banner_file.path)

@receiver(post_delete,sender=events_banner)
def delete_banner_image_on_delete(sender, instance, **kwargs):
   
    if instance.banner_image:
        if os.path.isfile(instance.banner_image.path):
            os.remove(instance.banner_image.path)

# events_details unused image remove 
@receiver(pre_save,sender=events_details)
def delete_old_banner_image_on_change(sender, instance, **kwargs):
    
    if not instance.pk:
        # New object being created; nothing to delete
        return

    try:
        old_banner_file = events_details.objects.get(pk=instance.pk).event_image
    except events_details.DoesNotExist:
        return
    
    new_banner_file = instance.event_image
    if old_banner_file and old_banner_file != new_banner_file:
        if os.path.isfile(old_banner_file.path):
            os.remove(old_banner_file.path)

@receiver(post_delete,sender=events_details)
def delete_banner_image_on_delete(sender, instance, **kwargs):
    
    if instance.event_image:
        if os.path.isfile(instance.event_image.path):
            os.remove(instance.event_image.path)

# event_speakers unused image remove 
@receiver(pre_save,sender=event_speakers)
def delete_old_banner_image_on_change(sender, instance, **kwargs):
    
    if not instance.pk:
        # New object being created; nothing to delete
        return

    try:
        old_banner_file = event_speakers.objects.get(pk=instance.pk).speaker_photo
    except event_speakers.DoesNotExist:
        return
    
    new_banner_file = instance.speaker_photo
    if old_banner_file and old_banner_file != new_banner_file:
        if os.path.isfile(old_banner_file.path):
            os.remove(old_banner_file.path)

@receiver(post_delete,sender=event_speakers)
def delete_banner_image_on_delete(sender, instance, **kwargs):
   
    if instance.speaker_photo:
        if os.path.isfile(instance.speaker_photo.path):
            os.remove(instance.speaker_photo.path)


# notice_details unused file remove
@receiver(pre_save, sender=notice_details)
def delete_old_notice_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        # New object being created; nothing to delete
        return

    try:
        old_file = notice_details.objects.get(pk=instance.pk).notice_file
    except notice_details.DoesNotExist:
        return

    new_file = instance.notice_file
    if old_file and old_file != new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)

@receiver(post_delete, sender=notice_details)
def delete_notice_file_on_delete(sender, instance, **kwargs):
    if instance.notice_file:
        if os.path.isfile(instance.notice_file.path):
            os.remove(instance.notice_file.path)