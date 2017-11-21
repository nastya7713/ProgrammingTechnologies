import operator

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.db import IntegrityError
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
import logging
import itertools

logger = logging.getLogger(__name__)

def set_language(request):
    return HttpResponse(render(request, request.GET['template'] + '.html'))

""" provides view for registration page """
def registration(request):
    return render(request, 'registration.html', context={'info': ''})

""" gets the list of enrollees admitted to the faculty, sorts enrollees """
@login_required(login_url='/index')
def admission_list(request, faculty_name, faculty_id):
    enrollees = RegisterList.objects.get(faculty=faculty_id).register_enrollees.all()
    ordered = sorted(enrollees, key= operator.attrgetter('average_grade'), reverse=True)
    return render(request, "admission_list.html", context={'faculty_name':faculty_name, 'enrollees':ordered})

""" enroll_form forms the list of faculties available for admission, 
    if user ia already enrolled average_grade is shown"""
@login_required(login_url='/index')
def enroll_form(request, faculty_id, faculty_name):
    faculty_subjects = []
    success = False
    average_grade = 0
    enrollee = Enrollee.objects.filter(user=request.user)
    if FacultyEnrollee.objects.filter(enrollee=enrollee, faculty=faculty_id).exists():
        average_grade = FacultyEnrollee.objects.get(enrollee=enrollee, faculty=faculty_id).average_grade
        success = True
    elif FacultySubject.objects.filter(faculty=faculty_id):
        faculty_subjects = FacultySubject.objects.get(faculty=faculty_id).subject.all()
    else:
        messages.error(request, 'No subjects available')
    return render(request, 'enroll_form.html', locals())

""" enrollment is used when the form is processed, counts average_grade field, adds record to database"""
@login_required(login_url='/index')
def enrollment(request, faculty_id, faculty_name):
    success = False
    average_grade = 0
    if request.method == 'POST':
        faculty_subjects = FacultySubject.objects.get(faculty=faculty_id).subject.all()
        #calculating the average grade of student
        for subject in faculty_subjects:
            average_grade += int(request.POST['subject_grade' + str(subject.id)])
        average_grade += int(request.POST['grade'])
        average_grade /= faculty_subjects.count()+1
        average_grade = round(average_grade , 2)
        faculty_enrollee = FacultyEnrollee(faculty=Faculty.objects.get(id=faculty_id),
                                           enrollee=Enrollee.objects.get(user=request.user),
                                           average_grade= average_grade)
        faculty_enrollee.save()
        logger.warning('faculty  %s enrollee %s was successfully saved!' % (faculty_enrollee.faculty, faculty_enrollee.enrollee))
        success = True
    return render(request, 'enroll_form.html', locals())

"""changes login is used in enrollee info"""
@login_required(login_url='/index')
def change_login(request):
    user = request.user
    if request.method == 'POST':
        try:
            user.username = request.POST['login']
            user.save()
        except IntegrityError as e:
            messages.error(request, "Incorrect data!")
            logger.error('Error occurred when %s login was updating! %s' % (request.user.username, e))
    return enrollee_info(request)

"""changes first name is used in enrollee info"""
@login_required(login_url='/index')
def change_first_name(request):
    user = request.user
    if request.method == 'POST':
            user.first_name = request.POST['first_name']
            user.save()
            logger.warning('user %s first_name was successfully updated!'%(request.user))
    return enrollee_info(request)

"""changes last name is used in enrollee info"""
@login_required(login_url='/index')
def change_last_name(request):
    user = request.user
    if request.method == 'POST':
        user.last_name = request.POST['last_name']
        user.save()
        logger.warning('user %s last_name was successfully updated!'%(request.user))
    return enrollee_info(request)

"""changes user email is used in enrollee info if data incorrect returns error"""
@login_required(login_url='/index')
def change_email(request):
    user = request.user
    if request.method == 'POST':
        try:
            user.email = request.POST['email']
            user.save()
            logger.warning('user %s email was successfully updated!' %(request.user))
        except IntegrityError as e:
            messages.error(request,"Incorrect data!")
            logger.error('Error occurred when %s email was updating! %s'%(request.user.username, e))
    return enrollee_info(request)

"""changes user password is used in enrollee info"""
@login_required(login_url='/index')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid(): #checks form
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            logger.warning('user %s , password was successfully updated!' %(request.user))
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
            logger.error('Error occurred when ',request.user.username ,' password was updating!')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })

""" processes registration form, checks data for duplicates creates new enrollee if data is correct """
@ensure_csrf_cookie
def register(request):
    if request.method == "POST":
        if User.objects.filter(username=request.POST['name']).exists() or\
                User.objects.filter(email=request.POST['email']).exists():
            logger.error('Duplicate entry was founded during registration')
            return render(request, 'registration.html',
                          context={'info': 'Incorrect data!Please, enter your credentials'})
        else:
            user = User.objects._create_user(request.POST['name'], request.POST['email'], request.POST['password'],
                                             first_name=request.POST['first_name'],
                                             last_name=request.POST['second_name'])
            enrollee = Enrollee(user=user)
            enrollee.save()
            logger.warning('Enrollee ',user.username,'was registrated')
    return redirect('index')

""" provides log_out for the current request """
@login_required(login_url='/index')
def log_out(request):
    logger.warning("%s log out" % (request.user.username))
    logout(request)
    return redirect('index')

""" provides view for faculty list to show all available faculties """
@login_required(login_url='/index')
def faculty_list(request):
    faculties = Faculty.objects.all()
    return render(request, 'faculty_list.html', context={'faculties': faculties})

""" provides  view for enrollee info page set enrollee context data """
@login_required(login_url='/index')
def enrollee_info(request):
    enrollee = Enrollee.objects.get(user=request.user).user
    return render(request, 'enrollee_info.html', context={'enrollee': enrollee})

"""
    provides view for my faculties page, finds link_faculties(faculties connected to the current user),
    checks faculty_status 
"""

@login_required(login_url='/index')
def enrollee_faculties(request):
    link_faculties = []
    for l in FacultyEnrollee.objects.filter(enrollee=Enrollee.objects.get(user=request.user)):
        if  RegisterList.objects.filter(faculty=l.faculty).exists():
                     if Enrollee.objects.get(user=request.user) in RegisterList.objects.get(faculty=l.faculty).register_enrollees.all():
                         l.status = FacultyEnrollee.CONFIRMED_STATUS
                     else:
                         l.status =FacultyEnrollee.DENIED_STATUS
        else:
                    l.status = FacultyEnrollee.WAIT_STATUS
        l.save()
        link_faculties.append(l)
    return render(request, 'faculty_enrollee.html', context={'faculty_enrollee': link_faculties})

"""
    sign_in view is used to authenticate
    user, data check provided, redirects to 'admin' url if superuser 
    visa versa enrollee home is showed 
"""
def sign_in(request):
    if request.method == "POST":
        user = authenticate(username=request.POST['name'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            u = User.objects.get(username=request.POST['name'])
            if u.is_superuser:
                logger.warning('Admin %s logged in' %(u.username))
                return HttpResponseRedirect(reverse('admin:index'))
            else:
                logger.warning('Student %s logged in' %(u.username))
                return render(request, 'enrollee.html')
        else:
            logger.error('Sign in error occurred')
            return render(request, 'index.html', context={'info': "Incorrect data!"})

    elif request.user.is_authenticated():
        if request.user.is_superuser:
            return HttpResponseRedirect(reverse('admin:index'))
        else:
            return render(request, 'enrollee.html')

    return render(request, 'index.html', context={'info': ''})

