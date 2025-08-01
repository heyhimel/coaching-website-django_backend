from django.db import models

# Create your models here.
# notice banner
class notice_banner(models.Model):
    banner_name = models.CharField(max_length=50,blank=True, null=True)
    banner_image = models.ImageField(upload_to='banner_image/',help_text="width 1920px by height 650px, try to maintain 3:1")
    banner_content = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.banner_name

# notice details
class notice_details(models.Model):
    notice_title = models.CharField(max_length=100)
    notice_details = models.TextField(null=True,blank=True)
    notice_bullet_point = models.TextField(null=True,blank=True)
    notice_file = models.FileField(upload_to='notice_documents/',null=True,blank=True,help_text="Provide image or pdf file that the user can download.")
    published_date = models.DateTimeField()

    def __str__(self):
        return self.notice_title

# blog banner
class blog_banner(models.Model):
    banner_name = models.CharField(max_length=50,blank=True, null=True)
    banner_image = models.ImageField(upload_to='banner_image/',help_text="width 1920px by height 650px, try to maintain 3:1")
    banner_content = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.banner_name

# blog details
class blog_details(models.Model):
    blog_posted_by = models.CharField(max_length=30,help_text="name of the person who is written by.")
    blog_title = models.CharField(max_length=110)
    blog_image = models.ImageField(upload_to='blog_image/',help_text="width 1920px by height 650px, try to maintain 3:1")
    blog_details = models.TextField(null=True,blank=True)
    published_date = models.DateTimeField()
    
    def __str__(self):
        return self.blog_title
    
# blog comments
class blog_comments(models.Model):
    blog = models.ForeignKey(blog_details, on_delete=models.CASCADE, related_name='comments')
    commenter_name = models.CharField(max_length=50)
    commenter_mobile = models.CharField(max_length=20)
    details_comments = models.TextField()
    comments_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.commenter_name} on {self.blog.blog_title}"
    
# events 
class events_banner(models.Model):
    banner_name = models.CharField(max_length=50,blank=True, null=True)
    banner_image = models.ImageField(upload_to='banner_image/',help_text="width 1920px by height 650px, try to maintain 3:1")
    banner_content = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.banner_name

# events details
class events_details(models.Model):
    event_title = models.CharField(max_length=60)
    event_image = models.ImageField(upload_to='event_image/',help_text="width 1920px by height 650px, try to maintain 3:1")
    write_about_event = models.TextField()
    event_date_time = models.DateTimeField()
    event_location = models.CharField(max_length=50)
    event_deliverable = models.TextField(blank=True,null=True,help_text="what you will provide? like as free snacks, pen, notebook, file, scale")

    def __str__(self):
        return self.event_title

# event speakers
class event_speakers(models.Model):
    event_for_speaker = models.ForeignKey(events_details,on_delete=models.CASCADE,related_name="all_speakers",help_text="select the event for this speaker")
    speaker_name = models.CharField(max_length=30)
    speaker_designation = models.CharField(max_length=50)
    speaker_photo = models.ImageField(upload_to='speakers_image/',help_text="Small image,80px by 80px")

    def __str__(self):
        return f"speaker {self.speaker_name} on {self.event_for_speaker} event"