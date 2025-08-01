from django.shortcuts import render
from .models import programm_background_banner_image,course_details,teacher_background_banner_image,teacher_details,GROUP_CHOICES

# Create your views here.
#all programs
def programs(request):
    banner = programm_background_banner_image.objects.order_by('-id').first()
    courses = course_details.objects.order_by('-id')
    return render(request,'courses.html',
                  {
                      'banner':banner,
                      'courses':courses
                  })

# single programs
def single_program(request,course_id):
    # program banner info 
    banner = programm_background_banner_image.objects.order_by('-id').first()
    # latest related course
    courses = course_details.objects.order_by('-id')[:3]
    # course info
    course = course_details.objects.filter(id=course_id).first()# target course
    course_highlights = course.course_highlight
    course_highlights = course_highlights.splitlines()
    # teacher associated with the course
    if course:
        teachers = course.teachers.all()
    else:
        teachers = []
    return render(request, 'course-single.html',
                  {
                      'banner':banner,
                      'teachers':teachers,
                      'target_course_id':course_id,
                      'course':course,
                      'courses':courses,
                      'course_highlights':course_highlights
                  })
# all teachers
def teachers(request):
    #banner image
    banner = teacher_background_banner_image.objects.order_by('-id').first()
    #teacher details
    all_groups = GROUP_CHOICES
    teachers = teacher_details.objects.all()
    return render(request,'teacher.html',
                  {
                      'banner':banner,
                      'all_groups':all_groups,
                      'teachers':teachers
                  })

# single teacher view
def single_teacher(request,teacher_id):
    #banner image
    banner = teacher_background_banner_image.objects.order_by('-id').first()
    print(banner)
    # teacher info
    teacher = teacher_details.objects.filter(id=teacher_id).first()# target teacher
    teacher_experience = teacher.experience_and_activities.strip()
    teacher_experience = teacher_experience.splitlines()
    courses = course_details.objects.order_by('-id')
    return render(request,'teacher-single.html',
                  {
                      'banner':banner,
                      'teacher':teacher,
                      'courses':courses,
                      'teacher_experience':teacher_experience
                  })
