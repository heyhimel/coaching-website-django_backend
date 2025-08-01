from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.messages import get_messages
from .models import *

# Create your views here.
#blog story
def all_blog_story(request):
    banner = blog_banner.objects.order_by('-id').first()
    blogs = blog_details.objects.order_by('-id')
    return render(request, 'blog.html',
                  {
                      'banner':banner,
                      'blogs':blogs
                  })

# blog story single
def blog_single(request,blog_id):
    # banner blog page
    banner = blog_banner.objects.order_by('-id').first()
    # target blog deatils
    blog = blog_details.objects.filter(id=blog_id).first()
    # latest 3 blog
    blogs = blog_details.objects.order_by('-id')[:3]

    # blog comment save portion
    if request.method == "POST":
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        comment = request.POST.get('comment')
        blog_comments.objects.create(
                blog=blog,
                commenter_name=name,
                commenter_mobile=mobile,
                details_comments=comment
            )
        # Clear old messages
        storage = get_messages(request)
        list(storage)  # just iterate so they get removed
        messages.success(request, "Thanks for your valuable comment. Soon we will reach you.")
        # redirect to same page to prevent resubmission
        return redirect('blog_single', blog_id=blog.id)
        
    return render(request,'blog-single.html',
                  {
                      'banner':banner,
                      'blog':blog,
                      'blogs':blogs
                  })

#blog story
def events(request):
    # banner
    banner = events_banner.objects.order_by('-id').first()
    # events
    events = events_details.objects.order_by('-id')
    return render(request, 'events.html',
                  {
                      'banner':banner,
                      'events':events
                  })

# blog story single
def event_single(request,event_id):
    # target event deatils
    event = events_details.objects.filter(id=event_id).first()
    banner = events_banner.objects.order_by('-id').first()
    # events
    events = events_details.objects.order_by('-id')

    # event speakers
    speakers = event.all_speakers.all()
    return render(request,'event-single.html',
                  {
                      'banner':banner,
                      'event':event,
                      'events':events,
                      'speakers':speakers
                  })


# notice
def all_notice(request):
    # banner
    banner = notice_banner.objects.order_by('-id').first()
    # all notices
    all_notices = notice_details.objects.all().order_by('-published_date')
    return render(request,'notice.html',
                  {
                      'banner':banner,
                      'notices':all_notices
                  })

# notice single
def notice_single(request,notice_id):
    # banner
    banner = notice_banner.objects.order_by('-id').first()
    # notice
    notice = notice_details.objects.filter(id=notice_id).first()
    notice_bullet_text = notice.notice_bullet_point.strip()
    notice_bullet_text = notice_bullet_text.splitlines()
    return render(request,'notice-single.html',
                  {
                      'banner':banner,
                      'notice':notice,
                      'notice_bullet_text':notice_bullet_text
                  })
