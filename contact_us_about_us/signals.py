from django.db.models.signals import pre_save,post_delete
from django.dispatch import receiver
from .models import banner_about_page,details_about_page,leadership_team,banner_contact_page,total_registered_students,student_registration_on_course_programm
import os

# banner_about_page banner unused image remove 
@receiver(pre_save,sender=banner_about_page)
def delete_old_banner_image_on_change(sender, instance, **kwargs):
    """
    Before saving, check if the image is changed; if yes, delete old file from disk.
    """
    if not instance.pk:
        # New object being created; nothing to delete
        return

    try:
        old_banner_file = banner_about_page.objects.get(pk=instance.pk).banner_image
    except banner_about_page.DoesNotExist:
        return
    
    new_banner_file = instance.banner_image
    if old_banner_file and old_banner_file != new_banner_file:
        if os.path.isfile(old_banner_file.path):
            os.remove(old_banner_file.path)

@receiver(post_delete,sender=banner_about_page)
def delete_banner_image_on_delete(sender, instance, **kwargs):
    """
    After deleting BackgroundBanner object, remove its image file from disk.
    """
    if instance.banner_image:
        if os.path.isfile(instance.banner_image.path):
            os.remove(instance.banner_image.path)


# details_about_page unused image remove 
@receiver(pre_save,sender=details_about_page)
def delete_old_banner_image_on_change(sender, instance, **kwargs):
    """
    Before saving, check if the image is changed; if yes, delete old file from disk.
    """
    if not instance.pk:
        # New object being created; nothing to delete
        return

    try:
        old_banner_file = details_about_page.objects.get(pk=instance.pk).image_about_page
    except details_about_page.DoesNotExist:
        return
    
    new_banner_file = instance.image_about_page
    if old_banner_file and old_banner_file != new_banner_file:
        if os.path.isfile(old_banner_file.path):
            os.remove(old_banner_file.path)

@receiver(post_delete,sender=details_about_page)
def delete_banner_image_on_delete(sender, instance, **kwargs):
    """
    After deleting BackgroundBanner object, remove its image file from disk.
    """
    if instance.image_about_page:
        if os.path.isfile(instance.image_about_page.path):
            os.remove(instance.image_about_page.path)

# leadership_team unused image remove 
@receiver(pre_save,sender=leadership_team)
def delete_old_banner_image_on_change(sender, instance, **kwargs):
    """
    Before saving, check if the image is changed; if yes, delete old file from disk.
    """
    if not instance.pk:
        # New object being created; nothing to delete
        return

    try:
        old_banner_file = leadership_team.objects.get(pk=instance.pk).image
    except leadership_team.DoesNotExist:
        return
    
    new_banner_file = instance.image
    if old_banner_file and old_banner_file != new_banner_file:
        if os.path.isfile(old_banner_file.path):
            os.remove(old_banner_file.path)

@receiver(post_delete,sender=leadership_team)
def delete_banner_image_on_delete(sender, instance, **kwargs):
    """
    After deleting BackgroundBanner object, remove its image file from disk.
    """
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)

# banner_contact_page unused image remove 
@receiver(pre_save,sender=banner_contact_page)
def delete_old_banner_image_on_change(sender, instance, **kwargs):
    """
    Before saving, check if the image is changed; if yes, delete old file from disk.
    """
    if not instance.pk:
        # New object being created; nothing to delete
        return

    try:
        old_banner_file = banner_contact_page.objects.get(pk=instance.pk).banner_image
    except banner_contact_page.DoesNotExist:
        return
    
    new_banner_file = instance.banner_image
    if old_banner_file and old_banner_file != new_banner_file:
        if os.path.isfile(old_banner_file.path):
            os.remove(old_banner_file.path)

@receiver(post_delete,sender=banner_contact_page)
def delete_banner_image_on_delete(sender, instance, **kwargs):
    """
    After deleting BackgroundBanner object, remove its image file from disk.
    """
    if instance.banner_image:
        if os.path.isfile(instance.banner_image.path):
            os.remove(instance.banner_image.path)

# total_registered_students unused image remove 
@receiver(pre_save,sender=total_registered_students)
def delete_old_banner_image_on_change(sender, instance, **kwargs):
    """
    Before saving, check if the image is changed; if yes, delete old file from disk.
    """
    if not instance.pk:
        # New object being created; nothing to delete
        return

    try:
        old_banner_file = total_registered_students.objects.get(pk=instance.pk).student_image
    except total_registered_students.DoesNotExist:
        return
    
    new_banner_file = instance.student_image
    if old_banner_file and old_banner_file != new_banner_file:
        if os.path.isfile(old_banner_file.path):
            os.remove(old_banner_file.path)

@receiver(post_delete,sender=total_registered_students)
def delete_banner_image_on_delete(sender, instance, **kwargs):
    """
    After deleting BackgroundBanner object, remove its image file from disk.
    """
    if instance.student_image:
        if os.path.isfile(instance.student_image.path):
            os.remove(instance.student_image.path)
            
# student_registration_on_course_programm unused image remove 
@receiver(pre_save,sender=student_registration_on_course_programm)
def delete_old_banner_image_on_change(sender, instance, **kwargs):
    """
    Before saving, check if the image is changed; if yes, delete old file from disk.
    """
    if not instance.pk:
        # New object being created; nothing to delete
        return

    try:
        old_banner_file = student_registration_on_course_programm.objects.get(pk=instance.pk).photo
    except student_registration_on_course_programm.DoesNotExist:
        return
    
    new_banner_file = instance.photo
    if old_banner_file and old_banner_file != new_banner_file:
        if os.path.isfile(old_banner_file.path):
            os.remove(old_banner_file.path)

@receiver(post_delete,sender=student_registration_on_course_programm)
def delete_banner_image_on_delete(sender, instance, **kwargs):
    """
    After deleting BackgroundBanner object, remove its image file from disk.
    """
    if instance.photo:
        if os.path.isfile(instance.photo.path):
            os.remove(instance.photo.path)