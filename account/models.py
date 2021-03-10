from django.db import models
from practise.models import Subjects

# Create your models here.
class Schools(models.Model):
    logo = models.ImageField(
        upload_to='schoolLogo', default='static/img/school_placeholder.jpg')
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ('date_added')

    class Meta:
        db_table = "Schools_tb"
        verbose_name = "School"
        verbose_name_plural = "Schools"


class Courses(models.Model):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('date_added')

    class Meta:
        db_table = "courses_tb"
        verbose_name = "Course"
        verbose_name_plural = "Courses"


class Genie_Users(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    """
    SCHOOLS = (
        ('FUTA', 'Federal University Of Technology Akure'),
    )
    """

    profileimg = models.ImageField(
        upload_to='profilepics', default='static/img/profile_placeholder.jpg')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=20)

    username = models.CharField(max_length=20, null=False)
    password = models.CharField(max_length=100)

    subjects = models.ManyToManyField(Subjects)

    institution = models.ForeignKey(Schools, on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)

    cutoff = models.CharField(max_length=20)
    jamb_score = models.CharField(max_length=20)
    asp_score = models.CharField(max_length=20)

    date_joined = models.DateTimeField(auto_now_add=False, auto_now=True)


    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        ordering = ('date_joined')

    class Meta:
        db_table = "Users_tb"
        verbose_name = "Genie User"
        verbose_name_plural = "Genie Users"

