from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(University)
admin.site.register(School)
admin.site.register(Programme)
admin.site.register(Major)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Course_Feedback)
admin.site.register(Faculty)
admin.site.register(Faculty_Feedback)
admin.site.register(Student_Course)
admin.site.register(Faculty_Course)
admin.site.register(Admin)
admin.site.register(Course_Admin)
admin.site.register(Student_Admin)
admin.site.register(Faculty_Admin)
admin.site.register(Resource)
admin.site.register(Task)
admin.site.register(Q_and_A_University_Wide)
admin.site.register(Q_and_A_Course_Wise)
admin.site.register(Submission)
admin.site.register(Announcement)
admin.site.register(Comment)
admin.site.register(Complaint)