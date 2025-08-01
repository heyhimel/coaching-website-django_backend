from django.db import models

# Create your models here.
# all about banner 
class programm_background_banner_image(models.Model):
    banner_name = models.CharField(max_length=50,blank=True, null=True)
    banner_image = models.ImageField(upload_to='banner_image/',help_text="width 1920px by height 650px, try to maintain 3:1")
    banner_content = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.banner_name


GROUP_CHOICES = [
    ('science', 'Science'),
    ('humanities', 'Humanities'),
    ('commerce', 'Commerce'),
]

class course_details(models.Model):
    CATEGORY_CHOICES = [
        ('admission', 'Admission'),
        ('academic', 'Academic'),
    ]
    course_image = models.ImageField(upload_to='course_image/',blank=True, null=True,help_text="width 450px by height 300px, try to maintain")
    course_name_title = models.CharField(max_length=100,blank=True, null=True)
    course_category = models.CharField(
        max_length=20, 
        choices=CATEGORY_CHOICES, 
        default='admission'
    )
    course_under_group = models.CharField(
    max_length=20,
    choices=GROUP_CHOICES,
    blank=True,  # optional: allow blank (can be required if you remove blank=True)
    null=True,   # optional: allow null in DB
    help_text="In which gorup the course belong to."
    )
    course_approximate_duration_month = models.IntegerField(null=True,blank=True)
    course_class_duration_hour = models.IntegerField(null=True,blank=True)
    course_fee = models.IntegerField(null=True,blank=True)
    about_course = models.TextField(null=True,blank=True,help_text="Tells details about course in plain text")
    course_highlight = models.TextField(null=True,blank=True,help_text="Write line by line important point about coruse. Like as how many class,model test, sheet, exam etc")
    course_others_info = models.TextField(null=True,blank=True,help_text="Write extra messages.Such as how to apply,how you deal with fees and policy etc")
    course_start_at = models.DateTimeField()
    def __str__(self):
        return self.course_name_title

# all about teacher
class teacher_background_banner_image(models.Model):
    banner_name = models.CharField(max_length=50,blank=True, null=True)
    banner_image = models.ImageField(upload_to='banner_image/',help_text="width 1520px by height 350px, try to maintain")
    banner_content = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.banner_name


class teacher_details(models.Model):
    teacher_image = models.ImageField(upload_to='teacher_image/',blank=True, null=True,help_text="width 450px by height 300px, try to maintain")
    teacher_name = models.CharField(max_length=50,blank=True,null=True)
    teacher_group = models.CharField(
    max_length=20,
    choices=GROUP_CHOICES,
    blank=True,  # optional: allow blank (can be required if you remove blank=True)
    null=True,   # optional: allow null in DB
    help_text="In which gorup the teacher take classes."
    )
    teacher_university_subject = models.CharField(max_length=100,blank=True,null=True,help_text="Provide the current University and subject name of the teacher")
    message_from_teacher = models.TextField(null=True,blank=True,help_text="if any guidance or message to all from teacher, please include")
    experience_and_activities = models.TextField(null=True,blank=True,help_text="Write Line by Line all point.")
    teacher_biography = models.TextField(null=True,blank=True,help_text="Write about teacher")
    teacher_contact_email = models.CharField(max_length=50,blank=True,null=True)
    teacher_contact_mobile = models.CharField(max_length=50,blank=True,null=True)
    teacher_contact_location = models.CharField(max_length=50,blank=True,null=True)
    teacher_contact_facebook = models.TextField(blank=True,null=True,help_text="Provide the facbook link of teacher if necessary.")
    # ManyToMany relationship to Program
    courses_teacher = models.ManyToManyField(course_details, related_name='teachers')

    def __str__(self):
        return self.teacher_name
