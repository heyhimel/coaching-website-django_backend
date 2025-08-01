"""
URL configuration for eduspringaac project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home_subscribe_story.views import homepage, subscrible_number
from teacher_and_programm.views import programs,teachers,single_program,single_teacher
from contact_us_about_us.views import contact,about_us,registration_form,single_leader,academic_addmission_registration
from notice_event_blog.views import blog_single,all_blog_story,event_single,events,all_notice,notice_single
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage,name='homepage'),
    # subscribe, mobile number
    path('subscribe/',subscrible_number, name='subscribe'),
    # teacher,programs
    path('all_programs/',programs, name="programs_page"),
    path('single_program/<int:course_id>/',single_program, name="single_program"),
    path('all_teachers/',teachers,name="teacher_page"),
    path('single_teacher/<int:teacher_id>/',single_teacher, name="single_teacher"),
    #contact,about us,registration
    path('contact_us/',contact,name="contact_page"),
    path('about_us/',about_us,name="about_page"),
    path('single_leader/<int:leader_id>/',single_leader,name="single_leader"),
    path('register_a_programm_or_event/',registration_form,name="registration_page"),
    path('register_a_programm/',academic_addmission_registration,name="course_registration_page"),
    # notice blog event
    path('all_blog/',all_blog_story,name="blog_page"),
    path('blog_individual/<int:blog_id>/',blog_single,name="blog_single"),
    path('all_events/',events,name="events_page"),
    path('event_individual/<int:event_id>/',event_single,name="event_single"),
    path('all_notices/',all_notice,name="notice_page"),
    path('notice_individual/<int:notice_id>/',notice_single,name="notice_single")
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
