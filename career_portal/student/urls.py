from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login_page, name='login'),
    path('test/', views.test, name='test'),
    path('result/', views.result, name='result'),
    path('courses/', views.courses, name='courses'),
    path('add-course/', views.add_course, name='add_course'),
    path('delete-course/<int:id>/', views.delete_course, name='delete_course'),
    path('edit-course/<int:id>/', views.edit_course, name='edit_course'),
    path('logout/', views.logout_view, name='logout'),]