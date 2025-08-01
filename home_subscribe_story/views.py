from django.shortcuts import render,redirect
from .models import homepage_banner, subscriber_mobile_number, success_story,homepage_banner_content,our_features_section
from teacher_and_programm.models import course_details,teacher_details
from notice_event_blog.models import blog_details,events_details
from contact_us_about_us.models import details_about_page

# Create your views here.
def homepage(request):
    # banner image data 
    banner = homepage_banner.objects.all() # returns a queryset
    # banner content data
    banner_contents = homepage_banner_content.objects.all()
    # success story data
    try:
        latest_obj = success_story.objects.latest('published_date')
    except success_story.DoesNotExist:
        latest_obj = None

    #course section adding to hompage
    courses = course_details.objects.order_by('-id')[:6]
    #teacher adding to homepage
    teachers = teacher_details.objects.order_by('-id')[:3]
    # latest blog
    blog_story = blog_details.objects.order_by('-id')[:3]
    # latest events
    events = events_details.objects.order_by('-id')[:3]
    # about section
    about_details = details_about_page.objects.order_by('-id').first()
    # our features
    feature = our_features_section.objects.order_by('-id').first()
    return render(request, 'index.html',
                  {'banners':banner,
                   'latest_story':latest_obj,
                   'banner_contents':banner_contents,
                   'courses':courses,
                   'teachers':teachers,
                   'blog_story':blog_story,
                   'events':events,
                   'about_details':about_details,
                   'feature': feature
                   })


# subscribe mobile view
def subscrible_number(request):
    if request.method =="POST":
        mob_num = request.POST.get('newsletter')
        obj, created = subscriber_mobile_number.objects.get_or_create(mobile_number=mob_num)
        if created:
            print("successfully mobile saved")
    return redirect('homepage')
