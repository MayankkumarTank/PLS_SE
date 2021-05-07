from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone

# Create your models here.
#phone number field baki
GENDER_CHOICES = (
    (0, 'male'),
    (1, 'female'),
    (2, 'others'),
)

class University(models.Model):
    Id = models.CharField(max_length=6, primary_key = True)
    Name = models.CharField(max_length=100)
    Address = models.CharField(max_length=300)
    Contact_No = PhoneNumberField(null=False)

class School(models.Model):
    Id = models.CharField(max_length=6, primary_key = True)
    Name = models.CharField(max_length=200)
    University_Id = models.ForeignKey(University , on_delete=models.CASCADE)
    Description = models.CharField(max_length=1000)

class Programme(models.Model):
    Id = models.CharField(max_length=6, primary_key = True)
    Name = models.CharField(max_length=100)
    School_Id = models.ForeignKey(School, on_delete=models.CASCADE)
    Duration = models.IntegerField(max_length=1)

class Major(models.Model):
    Id = models.CharField(max_length=6, primary_key = True)
    Name = models.CharField(max_length=100)
    Programme_Id = models.ForeignKey(Programme, on_delete = models.CASCADE)

class Student(models.Model):
    Id = models.CharField(max_length=6,primary_key = True)
    Email_Id = models.EmailField(max_length=100)
    Password = models.CharField(max_length=100)
    Enrollment_No = models.CharField(max_length=10)
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Middle_Name = models.CharField(max_length=100)
    Gender = models.IntegerField(choices = GENDER_CHOICES, null = False)
    School_Id = models.ForeignKey(School, on_delete=models.CASCADE)
    University_Id = models.ForeignKey(University , on_delete=models.CASCADE)
    Programme_Id = models.ForeignKey(Programme, on_delete = models.CASCADE)
    Major_Id = models.ForeignKey(Major, on_delete=models.CASCADE)
    Admission_Year =  models.IntegerField(max_length=4)
    Contact_No = PhoneNumberField(null=False)

class Course(models.Model):
    Id = models.CharField(max_length=6,primary_key = True)
    Name = models.CharField(max_length=100)
    Semester = models.IntegerField(max_length=2)
    Intake = models.IntegerField(max_length=4)
    School_Id = models.ForeignKey(School, on_delete=models.CASCADE)
    Programme_Id = models.ForeignKey(Programme, on_delete = models.CASCADE)
    Major_Id = models.ForeignKey(Major, on_delete=models.CASCADE)
    Discription = models.CharField(max_length=2000)

class Course_Feedback(models.Model):
    Course_Id = models.ForeignKey(Course , on_delete=models.CASCADE)
    Student_Id = models.ForeignKey(Student, on_delete=models.CASCADE)
    Rating = models.FloatField(max_length=3)
    TimeStamp = models.DateTimeField()
    Description = models.CharField(max_length=1000)

class Faculty(models.Model):
    Id = models.CharField(max_length=6, primary_key=True)
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Email_Id = models.EmailField(max_length=100)
    Password = models.CharField(max_length=100,null=True)
    Years_Of_Experience = models.FloatField(max_length=3)
    Joining_Date = models.DateField()
    Designation = models.CharField(max_length=200)
    Academic_Qualification = models.CharField(max_length=500)
    Contact_No = PhoneNumberField(null=False)
    University_Id = models.ForeignKey(University, on_delete=models.CASCADE,null=True)

class Faculty_Feedback(models.Model):
    Faculty_Id = models.ForeignKey(Faculty , on_delete=models.CASCADE)
    Student_Id = models.ForeignKey(Student, on_delete=models.CASCADE)
    Course_Id = models.ForeignKey(Course, on_delete=models.CASCADE , null=True)
    Rating = models.FloatField(max_length=3)
    TimeStamp = models.DateTimeField()
    Description = models.CharField(max_length=1000)

class Student_Course(models.Model):
    Student_Id = models.ForeignKey(Student, on_delete=models.CASCADE)
    Course_Id = models.ForeignKey(Course , on_delete=models.CASCADE)
    TimeStamp = models.DateTimeField()

class Faculty_Course(models.Model):
    Faculty_Id = models.ForeignKey(Faculty , on_delete=models.CASCADE)
    Course_Id = models.ForeignKey(Course , on_delete=models.CASCADE)
    TimeStamp = models.DateTimeField()

class Admin(models.Model):
    Id = models.CharField(max_length=6, primary_key=True)
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Email_Id = models.EmailField(max_length=100)
    Contact_No = PhoneNumberField(null=False)
    Password = models.CharField(max_length=100,null=True)
    School_Id = models.ForeignKey(School, on_delete=models.CASCADE)

class Course_Admin(models.Model):
    Admin_Id = models.ForeignKey(Admin , on_delete=models.CASCADE)
    Course_Id = models.ForeignKey(Course , on_delete=models.CASCADE)
    TimeStamp = models.DateTimeField()

class Student_Admin(models.Model):
    Student_Id = models.ForeignKey(Student, on_delete=models.CASCADE)
    Course_Id = models.ForeignKey(Course , on_delete=models.CASCADE)
    TimeStamp = models.DateTimeField()

class Faculty_Admin(models.Model):
    Faculty_Id = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    Admin_Id = models.ForeignKey(Admin, on_delete=models.CASCADE)
    Timestamp = models.DateTimeField(null=False)

class Resource(models.Model):
    Id = models.CharField(max_length=6, primary_key=True)
    Faculty_Id = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    Course_Id = models.ForeignKey(Course , on_delete=models.CASCADE)
    Timestamp = models.DateTimeField(null=False)
    Title = models.CharField(max_length=1000,blank=True)
    Content = models.CharField(max_length=10000)
    Added_date = models.DateTimeField(null=True,auto_now_add=True)

class Task(models.Model):
    Id = models.CharField(max_length=6, primary_key=True)
    Faculty_Id = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    Course_Id = models.ForeignKey(Course , on_delete=models.CASCADE)
    Title = models.CharField(max_length=100)
    Content = models.CharField(max_length=2000)
    Deadline = models.DateTimeField(null=False)
    peer_mode = models.BooleanField(default=False)
    Added_date = models.DateTimeField(null=True,auto_now_add=True)

class Q_and_A_University_Wide(models.Model):
    Question_Id = models.IntegerField(max_length=6, unique=False)
    Answer_Id = models.IntegerField(max_length=6, unique=False,blank=True)
    Question = models.BooleanField(default=True)
    Content = models.CharField(max_length=2000)
    Timestamp = models.DateTimeField(null=False)
    User_Id = models.CharField(max_length=6)
    University_Id = models.ForeignKey(University, on_delete=models.CASCADE)

class Q_and_A_Course_Wise(models.Model):
    Question_Id = models.IntegerField(max_length=6, unique=False)
    Answer_Id = models.IntegerField(max_length=6, unique=False,blank=True)
    Question = models.BooleanField(default=True)
    Content = models.CharField(max_length=2000)
    Timestamp = models.DateTimeField(null=False)
    User_Id = models.CharField(max_length=6)
    Course_Id = models.ForeignKey(Course, on_delete=models.CASCADE)

class Submission(models.Model):
    Student_Id = models.ForeignKey(Student, on_delete=models.CASCADE)
    Task_Id = models.ForeignKey(Task, on_delete=models.CASCADE)
    Faculty_Id = models.ForeignKey(Faculty, on_delete=models.CASCADE,null=True)
    Timestamp = models.DateTimeField(null=False)
    Status = models.BooleanField()
    Grade = models.CharField(max_length=2,null=True,blank=True)
    Content = models.CharField(max_length=10000)

class Announcement(models.Model):
    Id = models.CharField(max_length=6, primary_key=True)
    Content = models.CharField(max_length=5000)
    User_Id = models.CharField(max_length=6)
    Timestamp = models.DateTimeField(null=False)

class Comment(models.Model):
    Submission_Id = models.ForeignKey(Submission, on_delete=models.CASCADE)
    Student_Id = models.ForeignKey(Student, on_delete=models.CASCADE)
    Content = models.CharField(max_length=2000)
    Timestamp = models.DateTimeField(null=False)

class Complaint(models.Model):
    Id = models.IntegerField(max_length=6, primary_key=True)
    User_Id = models.CharField(max_length=6)
    Content = models.CharField(max_length=2000)
    Timestamp = models.DateTimeField(null=False)
    Admin_Id = models.ForeignKey(Admin, on_delete=models.CASCADE)
    Status = models.BooleanField()