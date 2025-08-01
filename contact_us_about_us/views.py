from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages import get_messages
from .models import *
from teacher_and_programm.models import course_details
from notice_event_blog.models import events_details

# Create your views here.
# contact
def contact(request):
    banner = banner_contact_page.objects.order_by('-id').first()
    if request.method == "POST":
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Create and save the object
        contact = peoples_contact_information(
            peoples_name=name,
            mobile=mobile,
            subject=subject if subject else None,  # handle empty subject
            peoples_message=message
        )
        contact.save()
        # Clear old messages
        storage = get_messages(request)
        list(storage)  # just iterate so they get removed
        messages.success(request, "Thanks for contact, Soon one of our representative will call you.")
        return redirect('contact_page')
    
    return render(request, 'contact.html',
                  {
                    'banner':banner
                  })
                

# about us
def about_us(request):
    banner = banner_about_page.objects.order_by('-id').first()
    about_details = details_about_page.objects.order_by('-id').first()
    story_details = stories_about_page.objects.order_by('-id').first()
    leaders = leadership_team.objects.order_by('-id')
    return render(request, 'about.html',
                  {
                    'banner':banner,
                    'about_details':about_details,
                    'story_details':story_details,
                    'leaders':leaders
                  })

# single leader
def single_leader(request,leader_id):
    # target leader
    leader =  leadership_team.objects.filter(id=leader_id).first()
    # courses
    courses = course_details.objects.order_by('-id')[:3]
    return render(request, 'leader-single.html',
                  {
                      'leader':leader,
                      'courses':courses
                  })

# registration a programm
def registration_form(request):
    # total events
    events = events_details.objects.order_by('-id')
    # total course
    courses = course_details.objects.order_by('-id')
    # saving form data to databse
    if request.method == "POST":
        # get data from the form
        name = request.POST.get('name')
        father_name = request.POST.get('father_name')
        village = request.POST.get('village')
        school_name = request.POST.get('school_name')
        result = request.POST.get('result')
        group = request.POST.get('group')
        registerd_event_course = request.POST.get('registerd_event_course')  # note: change name below
        student_mobile = request.POST.get('student_mobile')
        guardian_mobile = request.POST.get('guardian_mobile')
        photo = request.FILES.get('photo')

        # save to model
        total_registered_students.objects.create(
            student_full_name = name,
            fathers_full_name = father_name,
            student_mobile = student_mobile,
            gurdian_mobile = guardian_mobile,
            student_address = village,
            school_name = school_name,
            result = result,
            group = group,
            registered_course_event = registerd_event_course,
            student_image = photo
        )
        # Clear old messages
        storage = get_messages(request)
        list(storage)  # just iterate so they get removed
        # optional: show success message
        messages.success(request, 'Registration successful! We will reach you shortly, Thanks!')

        return redirect('registration_page')
    return render(request,'registration.html',
                  {
                      'events':events,
                      'courses':courses
                  })

def academic_addmission_registration(request):
    # total course
    courses = course_details.objects.order_by('-id')
    if request.method == 'POST':
        admission_type = request.POST.get('admission_type')
        group = request.POST.get('group')
        batch_name = request.POST.get('batch_name')
        student_name = request.POST.get('student_name')
        guardian_name = request.POST.get('guardian_name')
        birth_date = request.POST.get('birth_date')
        gender = request.POST.get('gender')
        religion = request.POST.get('religion')
        blood_group = request.POST.get('blood_group')
        ssc_roll = request.POST.get('ssc_roll')
        hsc_roll = request.POST.get('hsc_roll')
        school_name = request.POST.get('school_name')
        college_name = request.POST.get('college_name')
        student_mobile = request.POST.get('student_mobile')
        guardian_mobile = request.POST.get('guardian_mobile')
        email = request.POST.get('email')
        nid_birth_number = request.POST.get('nid_birth')
        present_address = request.POST.get('present_address')
        permanent_address = request.POST.get('permanent_address')
        photo = request.FILES.get('photo')  # important: use request.FILES for file upload

        # Save to database
        student_registration_on_course_programm.objects.create(
            admission_type=admission_type,
            group=group,
            batch_name=batch_name,
            student_name=student_name,
            guardian_name=guardian_name,
            birth_date=birth_date if birth_date else None,
            gender=gender,
            religion=religion,
            blood_group=blood_group,
            ssc_roll=ssc_roll,
            hsc_roll=hsc_roll,
            school_name=school_name,
            college_name=college_name,
            student_mobile=student_mobile,
            guardian_mobile=guardian_mobile,
            email=email,
            nid_birth_number=nid_birth_number,
            present_address=present_address,
            permanent_address=permanent_address,
            photo=photo
        )
        storage = get_messages(request)
        list(storage)
        # Optional: show a success message
        messages.success(request, "Registration Successfull, Thanks!")

        # Redirect to the same page or another page
        return redirect('course_registration_page')
    return render(request,'registration_aa.html',{'courses':courses})