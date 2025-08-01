from django.db import models

# Create your models here.
# about us
class banner_about_page(models.Model):
    banner_name = models.CharField(max_length=50,blank=True, null=True)
    banner_image = models.ImageField(upload_to='banner_image/',help_text="width 1920px by height 650px, try to maintain 3:1")
    banner_content = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.banner_name

class details_about_page(models.Model):
    title_about_page = models.CharField(max_length=100)
    image_about_page = models.ImageField(upload_to='about_image/',help_text="width 1080px by height 600px, try to maintain 3:1")
    short_content_about_page = models.TextField(null=True,blank=True)
    details_content_about_page = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.title_about_page
    
class stories_about_page(models.Model):
    title_stories = models.CharField(max_length=100)
    story_short_content = models.TextField(blank=True, null=True)
    story_details_content = models.TextField(blank=True, null=True)
    story_youtube_video_link = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title_stories
    
class leadership_team(models.Model):
    name = models.CharField(max_length=30)
    designation = models.TextField(blank=True,null=True)
    image = models.ImageField(upload_to='about_image/',help_text="provide image 400px by 300 px for better preview")
    short_message = models.TextField(blank=True,null=True,help_text="short message to all")
    details_message = models.TextField(blank=True,null=True,help_text="short message to all")
    contact_email = models.CharField(max_length=50,blank=True,null=True)
    contact_mobile = models.CharField(max_length=50,blank=True,null=True,help_text="like as 017******")
    contact_location = models.CharField(max_length=50,blank=True,null=True)
    contact_facebook = models.TextField(blank=True,null=True,help_text="Provide the facbook link, if necessary.")

    def __str__(self):
        return self.name
    
# contact us info
class banner_contact_page(models.Model):
    banner_name = models.CharField(max_length=50,blank=True, null=True)
    banner_image = models.ImageField(upload_to='banner_image/',help_text="width 1920px by height 650px, try to maintain 3:1")
    banner_content = models.TextField(null=True,blank=True)
    content_body = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.banner_name

class peoples_contact_information(models.Model):
    peoples_name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=20)
    subject = models.CharField(max_length=100, blank=True,null=True)
    peoples_message = models.TextField()

    def __str__(self):
        return self.peoples_name

class total_registered_students(models.Model):
    student_full_name = models.CharField(max_length=50)
    fathers_full_name = models.CharField(max_length=50)
    student_mobile = models.CharField(max_length=16)
    gurdian_mobile = models.CharField(max_length=16)
    student_address = models.TextField()
    school_name = models.TextField()
    result = models.CharField(max_length=20)
    group = models.CharField(max_length=15)
    registered_course_event = models.TextField()
    registered_at = models.DateTimeField(auto_now_add=True)
    student_image = models.ImageField(upload_to='student_image/',help_text="image from the registration")

    def __str__(self):
        return f"{self.student_full_name} registered for {self.registered_course_event} at {self.registered_at}"
    
    from django.db import models

class student_registration_on_course_programm(models.Model):
    # Fields
    admission_type = models.CharField(
        max_length=20,
        help_text="Select the type of admission (e.g., Academic or Admission)."
    )

    group = models.CharField(
        max_length=20,
        help_text="Select the group: Science, Humanities, or Commerce."
    )

    batch_name = models.CharField(
        max_length=150,blank=True,null=True,
        help_text="Enter the name of the batch or program the student is enrolling in."
    )

    student_name = models.CharField(
        max_length=150,
        help_text="Full name of the student as per official documents."
    )

    guardian_name = models.CharField(
        max_length=100,
        help_text="Full name of parent or guardian."
    )

    birth_date = models.DateField(
        blank=True, null=True,
        help_text="Date of birth (e.g., YYYY-MM-DD)."
    )

    gender = models.CharField(
        max_length=10,
        blank=True, null=True,
        help_text="Student’s gender (Male, Female, or Other)."
    )

    religion = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Religion of the student."
    )

    blood_group = models.CharField(
        max_length=3,
        blank=True, null=True,
        help_text="Student's blood group (e.g., A+, B-, O+)."
    )

    ssc_roll = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="SSC exam roll number (if applicable)."
    )

    hsc_roll = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="HSC exam roll number (if applicable)."
    )

    school_name = models.CharField(
        max_length=150,
        blank=True, null=True,
        help_text="Name of the school the student attended."
    )

    college_name = models.CharField(
        max_length=150,
        blank=True, null=True,
        help_text="Name of the college the student attended."
    )

    student_mobile = models.CharField(
        max_length=20,
        help_text="Active mobile number of the student."
    )

    guardian_mobile = models.CharField(
        max_length=20,
        help_text="Active mobile number of the guardian or parent."
    )

    email = models.CharField(
        max_length=50, blank=True, null=True,
        help_text="Student's email address (if available)."
    )

    nid_birth_number = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Birth certificate number or NID number of the student."
    )

    present_address = models.TextField(
        help_text="Current address where the student lives."
    )

    permanent_address = models.TextField(
        help_text="Permanent home address of the student."
    )

    photo = models.ImageField(
        upload_to='registered_student_photos/',
        help_text="Upload a clear photo of the student."
    )

    registration_date = models.DateTimeField(
        auto_now_add=True,
        help_text="Date and time when the student registered (auto-filled)."
    )

    def __str__(self):
        return f"{self.student_name} applied on {self.batch_name} at {self.registration_date}"
