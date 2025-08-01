from django.db.models.signals import pre_save,post_delete
from django.dispatch import receiver
from .models import programm_background_banner_image,teacher_background_banner_image,course_details,teacher_details
import os

# program banner unused image remove
@receiver(pre_save,sender=programm_background_banner_image)
def delete_old_banner_image_on_change(sender, instance, **kwargs):
    
    if not instance.pk:
        # New object being created; nothing to delete
        return

    try:
        old_banner_file = programm_background_banner_image.objects.get(pk=instance.pk).banner_image
    except programm_background_banner_image.DoesNotExist:
        return
    
    new_banner_file = instance.banner_image
    if old_banner_file and old_banner_file != new_banner_file:
        if os.path.isfile(old_banner_file.path):
            os.remove(old_banner_file.path)

@receiver(post_delete,sender=programm_background_banner_image)
def delete_banner_image_on_delete(sender, instance, **kwargs):
   
    if instance.banner_image:
        if os.path.isfile(instance.banner_image.path):
            os.remove(instance.banner_image.path)

# course_details unused image remove
@receiver(pre_save,sender=course_details)
def delete_old_banner_image_on_change(sender, instance, **kwargs):
    
    if not instance.pk:
        # New object being created; nothing to delete
        return

    try:
        old_banner_file = course_details.objects.get(pk=instance.pk).course_image
    except course_details.DoesNotExist:
        return
    
    new_banner_file = instance.course_image
    if old_banner_file and old_banner_file != new_banner_file:
        if os.path.isfile(old_banner_file.path):
            os.remove(old_banner_file.path)

@receiver(post_delete,sender=course_details)
def delete_banner_image_on_delete(sender, instance, **kwargs):
   
    if instance.course_image:
        if os.path.isfile(instance.course_image.path):
            os.remove(instance.course_image.path)

# teacher_background_banner_image unused image remove
@receiver(pre_save,sender=teacher_background_banner_image)
def delete_old_banner_image_on_change(sender, instance, **kwargs):
    
    if not instance.pk:
        return

    try:
        old_banner_file = teacher_background_banner_image.objects.get(pk=instance.pk).banner_image
    except teacher_background_banner_image.DoesNotExist:
        return
    
    new_banner_file = instance.banner_image
    if old_banner_file and old_banner_file != new_banner_file:
        if os.path.isfile(old_banner_file.path):
            os.remove(old_banner_file.path)

@receiver(post_delete,sender=teacher_background_banner_image)
def delete_banner_image_on_delete(sender, instance, **kwargs):
    
    if instance.banner_image:
        if os.path.isfile(instance.banner_image.path):
            os.remove(instance.banner_image.path)

# teacher_details unused image remove
@receiver(pre_save,sender=teacher_details)
def delete_old_banner_image_on_change(sender, instance, **kwargs):
    
    if not instance.pk:
        return

    try:
        old_banner_file = teacher_details.objects.get(pk=instance.pk).teacher_image
    except teacher_details.DoesNotExist:
        return
    
    new_banner_file = instance.teacher_image
    if old_banner_file and old_banner_file != new_banner_file:
        if os.path.isfile(old_banner_file.path):
            os.remove(old_banner_file.path)

@receiver(post_delete,sender=teacher_details)
def delete_banner_image_on_delete(sender, instance, **kwargs):
    
    if instance.teacher_image:
        if os.path.isfile(instance.teacher_image.path):
            os.remove(instance.teacher_image.path)