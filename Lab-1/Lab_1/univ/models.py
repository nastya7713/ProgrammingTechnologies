from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

#model of faculty enrollee
class Enrollee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    User._meta.get_field('email')._unique = True
    def __str__(self):
        return "%s %s %s %s" %(self.user,self.user.email, self.user.first_name, self.user.last_name)

#model to describe faculty subjects
class Subject(models.Model):
    name = models.CharField(max_length=30, unique=True)
    def __str__(self):
        return "%s subject" %(self.name)

#model to describe faculties
class Faculty(models.Model):
    name = models.CharField(max_length=30, unique=True)
    faculty_limit = models.PositiveIntegerField(validators=[MinValueValidator(3), MaxValueValidator(10)])
    class Meta:
      verbose_name_plural= "Faculties"
    def __str__(self):
        return "%s faculty has %s faculty_limit" %(self.name, self.faculty_limit)

#link table between faculty and enrollee
class FacultyEnrollee(models.Model):
    #status field needed to define the state of admission
    WAIT_STATUS = 1
    DENIED_STATUS = 2
    CONFIRMED_STATUS = 3
    STATUS_CHOICES = (
        (WAIT_STATUS, 'WAIT'),
        (DENIED_STATUS, 'DENIED'),
        (CONFIRMED_STATUS, 'CONFIRMED'),
    )
    enrollee = models.ForeignKey(Enrollee)
    faculty = models.ForeignKey(Faculty)
    #average_grade counted during student application
    average_grade = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    status = models.IntegerField(choices=STATUS_CHOICES, default=WAIT_STATUS)

    #check_status defines when register list is available
    def check_status(self):
        if RegisterList.objects.filter(faculty = self.faculty).exists():
            if RegisterList.objects.get(faculty=self.faculty).register_enrollees.all().filter(enrollee=self.enrollee).exists():
                self.status = self.CONFIRMED_STATUS
            else:
                self.status = self.DENIED_STATUS
        else:
            self.status = self.WAIT_STATUS
        self.save()
        return FacultyEnrollee.STATUS_CHOICES.__getitem__(self.status-1)[1]

    def __str__(self):
        return "%s %s %s" % (self.faculty.name, self.enrollee.user, self.check_status())

#link table between faculty and subject
class FacultySubject(models.Model):
    faculty = models.OneToOneField(Faculty)
    subject = models.ManyToManyField(Subject)
    def __str__(self):
        return "Faculty %s subjects" % (self.faculty.name)

#list which is used by admin to registrate enrollees
class RegisterList(models.Model):
    faculty = models.OneToOneField(Faculty)
    register_enrollees = models.ManyToManyField(FacultyEnrollee)
    def __str__(self):
        return "Faculty %s admission count %d" % (self.faculty.name, self.register_enrollees.count())
