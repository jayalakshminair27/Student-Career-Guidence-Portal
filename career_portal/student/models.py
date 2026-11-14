from django.db import models



class Student(models.Model):

    name = models.CharField(max_length=100)

    email = models.EmailField()

    qualification = models.CharField(max_length=100)

    interests = models.CharField(max_length=200)

    password = models.CharField(max_length=100)

    def __str__(self):

        return self.name




class Course(models.Model):

    title = models.CharField(max_length=100)

    description = models.TextField()

    image = models.ImageField(upload_to='course_images/')

    def __str__(self):

        return self.title