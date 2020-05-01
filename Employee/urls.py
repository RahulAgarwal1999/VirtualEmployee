from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('register/',views.adduser,name='register'),
    path('',views.userlogin,name='login'),
    path('logout/', views.logout, name='logout'),
    path('admindashboard',views.adminDashboard,name="admindashboard"),
    path('courses/',views.adminCourses,name='admincourse'),
    path('add_course/',views.adminAddcourse,name='adminaddcourse'),
    path('projects/',views.adminProjects,name='adminprojects'),
    # User Section
    path('userdashboard/',views.userdashboard,name='dashboard'),

    ]