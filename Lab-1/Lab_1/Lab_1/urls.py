"""test_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from sys import path

from django.conf.urls import url, include
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from univ import views

urlpatterns = [
    url(r'^i18n/', include('django.conf.urls.i18n')),
 ]

urlpatterns += i18n_patterns(
    url(r'^index/', views.sign_in, name='index'),
    url(r'^registration/', views.registration, name='registration'),
    url(r'^register/$',views.register, name="register"),
    url(r'^enrollee/faculty_list/$', views.faculty_list,name="faculty_list"),
    url(r'^enrollee/my_faculties/$', views.enrollee_faculties, name="enrollee_faculties"),
    url(r'^enrollee/change_login/$', views.change_login, name='change_login'),
    url(r'^enrollee/change_password/$', views.change_password, name="change_password"),
    url(r'^enrollee/change_first_name/$', views.change_first_name, name='change_first_name'),
    url(r'^enrollee/change_last_name/$', views.change_last_name, name='change_last_name'),
    url(r'^enrollee/change_email/$', views.change_email, name='change_email'),
    url(r'^enrollee/enrollee_info/$', views.enrollee_info, name="enrollee_info"),
    url(r'^enrollee/my_faculties/(?P<faculty_name>[\w-]+)_faculty_id(?P<faculty_id>[0-9]+)/$',
                                                    views.admission_list, name='admission_list'),
    url(r'^log_out/', views.log_out, name='log_out'),
    url(r'^admin/',admin.site.urls),
    url(r'^enrollee/(?P<faculty_name>[\w-]+)_faculty_id(?P<faculty_id>[0-9]+)/$', views.enroll_form, name='enroll_form'),
    url(r'^enrollee/(?P<faculty_name>[\w-]+)_faculty_id(?P<faculty_id>[0-9]+)/enrollment/$', views.enrollment,
        name='enrollment'),
)
