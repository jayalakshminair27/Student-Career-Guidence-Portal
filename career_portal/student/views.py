from .models import Student
from django.shortcuts import render, redirect, get_object_or_404
from .models import Course
from django.contrib.auth import logout


def index(request):
    return render(request, 'student/index.html')


def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        qualification = request.POST['qualification']
        interests = request.POST['interests']
        password = request.POST['password']

        Student.objects.create(
            name=name,
            email=email,
            qualification=qualification,
            interests=interests,
            password=password
        )

        return redirect('dashboard')

    return render(request, 'student/register.html')



def login_page(request):

    if request.method == 'POST':

        email = request.POST['email']
        password = request.POST['password']

        student = Student.objects.filter(
            email=email,
            password=password
        )

        if student.exists():
            return redirect('index')

        else:
            return render(request, 'student/login.html', {
                'error': 'Invalid Email or Password'
            })

    return render(request, 'student/login.html')



def test(request):
    return render(request, 'student/test.html')


def result(request):

    career = request.GET.get('career')

    if career == "developer":

        career_name = "Software Developer"

    elif career == "designer":

        career_name = "Graphic Designer"

    elif career == "doctor":

        career_name = "Doctor"

    else:

        career_name = "Career Not Found"

    return render(request, 'student/result.html', {

        'career': career_name

    })

def courses(request):

    all_courses = Course.objects.all()

    return render(request, 'student/courses.html', {

        'courses': all_courses

    })


def add_course(request):

    if request.method == "POST":

        title = request.POST['title']

        description = request.POST['description']

        image = request.FILES['image']

        Course.objects.create(

            title=title,

            description=description,

            image=image

        )

        return redirect('courses')

    return render(request, 'student/add_course.html')

def delete_course(request, id):

    course = Course.objects.get(id=id)

    course.delete()

    return redirect('courses')


def edit_course(request, id):

    course = get_object_or_404(Course, id=id)

    if request.method == "POST":

        course.title = request.POST['title']

        course.description = request.POST['description']

        if 'image' in request.FILES:

            course.image = request.FILES['image']

        course.save()

        return redirect('courses')

    return render(request, 'student/edit_course.html', {

        'course': course

    })


def logout_view(request):
    logout(request)
    return redirect('login')