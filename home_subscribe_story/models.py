from django.db import models

# Create your models here.
class homepage_banner(models.Model):
    banner_name = models.CharField(max_length=50)
    banner_image = models.ImageField(upload_to='banner_image/',help_text="width 1520px by height 695px, try to maintain. This banner will be displayed in your homepage")
    
    def __str__(self):
        return self.banner_name

# making a choices pages list for admin
PAGE_LINKS = [
    ('homepage', 'Homepage'),
    ('about_page', 'About Us page'),
    ('contact_page', 'Contact page'),
    ('programs_page', 'Programs page'),
    ('blog_page', 'Story page'),
    ('teacher_page', 'Teachers page'),
    ('events_page', 'Events page'),
    ('notice_page', 'Notice page'),
    ('registration_page','Registration Page'),
    ('course_registration_page','Course Registration Page')
    ]
class homepage_banner_content(models.Model):
    banner_title = models.TextField(help_text="This text will be displayed over the Homepage banner image")
    banner_message = models.TextField(blank=True,null=True,help_text="Below the banner title this message will be displayed")
    target_page_link = models.CharField(
        max_length=100,
        choices=PAGE_LINKS,
        help_text="Select the page this banner should link to. People will redirect to this page."
    )

    def __str__(self):
        return self.banner_title

# success story 
class success_story(models.Model):
    story_title = models.TextField()
    story_background_image = models.ImageField(upload_to='background_story_image/',help_text="width 1520px by height 695px, try to maintain.")
    story_youtube_video_link = models.TextField(help_text="provide a you-tube video link.People will show the story from your website.")
    story_short_message = models.TextField(blank=True,null=True)
    story_details = models.TextField(blank=True,null=True)
    published_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.story_title


# our features
class our_features_section(models.Model):
    feature_image = models.ImageField(upload_to='feature_image/',help_text="provide 550px by 450px image for better preview")
    feature_name1 = models.CharField(max_length=30)
    feature_description1 = models.TextField()
    feature_name2 = models.CharField(max_length=30)
    feature_description2 = models.TextField()
    feature_name3 = models.CharField(max_length=30)
    feature_description3 = models.TextField()
    feature_name4 = models.CharField(max_length=30)
    feature_description4 = models.TextField()

    def __str__(self):
        return f"Four features: {self.feature_name1},{self.feature_name2},{self.feature_name3},{self.feature_name4}"


# subscribe number
class subscriber_mobile_number(models.Model):
    mobile_number = models.CharField(max_length=11)
    date_of_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.mobile_number