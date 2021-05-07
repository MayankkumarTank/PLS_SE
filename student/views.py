from django.shortcuts import render,redirect
from guest.models import Faculty_Course,Faculty_Feedback,Faculty,Student,Course,Course_Feedback,Task,Submission,Comment
from django.utils import timezone
from . import views

# Create your views here.
def facultyfeedback(request,course_id):
    facultys = Faculty_Course.objects.filter(Course_Id=course_id)
    #faculty = Faculty.objects.get(Id=faculty_id)
    student = Student.objects.get(Id=request.session["Id"])
    course = Course.objects.get(Id=course_id)
    #record = Faculty_Feedback.objects.filter(Student_Id=student,Course_Id=course)
    context={
        'facultys':facultys,
    }
    tf_list = []
    obj_list  = []
    for faculty in facultys:
        fc_id = faculty.Faculty_Id.Id
        obj = Faculty_Feedback.objects.filter(Faculty_Id=faculty.Faculty_Id,Student_Id=student,Course_Id=course)
        if(obj.exists()):
            tf_list.append(True)
            obj_list.append(obj.get())
        else:
            tf_list.append(False)
            obj_list.append(None)
        # tf_list.append(Faculty_Feedback.objects.filter(Faculty_Id=faculty.Faculty_Id,Student_Id=student,Course_Id=course).exists())
    final_roc = zip(facultys, tf_list, obj_list)
    context={
        'final_rocs':final_roc,
        'course_id' : course_id,
    }
    return render(request,'faculty_feedback.html',context=context)

def submitfacultyfeedback(request,faculty_id,course_id):
    if request.method == "POST":
        rating = request.POST.get("rating")
        desc = request.POST.get("desc")
        print(faculty_id)
        faculty = Faculty.objects.get(Id=faculty_id)
        student = Student.objects.get(Id=request.session["Id"])
        course = Course.objects.get(Id=course_id)
        record = Faculty_Feedback(Faculty_Id=faculty,Student_Id=student,Course_Id=course,Rating=rating,Description=desc,TimeStamp=timezone.now())
        record.save()
        return redirect('facultyfeedback',course_id)
        
def coursefeedback(request,course_id):
    course = Course.objects.get(Id=course_id)
    #print(course)
    student = Student.objects.get(Id=request.session["Id"])
    obj = Course_Feedback.objects.filter(Student_Id=student,Course_Id=course)
    #print(faculty)
    context={
        'course':course,
        'status': obj.exists(),
        'feedback_data' : obj.get() if obj.exists() else None,
    }
    return render(request,'course_feedback.html',context=context)

def submitcoursefeedback(request,course_id):
    if request.method == "POST":
        rating = request.POST.get("rating")
        desc = request.POST.get("desc")
        #print(faculty_id)
        #faculty = Faculty.objects.get(Id=faculty_id)
        student = Student.objects.get(Id=request.session["Id"])
        course = Course.objects.get(Id=course_id)
        record = Course_Feedback(Student_Id=student,Course_Id=course,Rating=rating,Description=desc,TimeStamp=timezone.now())
        record.save()
        return redirect('coursefeedback',course_id) 

def addsubmission(request,course_id,task_id):
    student = Student.objects.get(Id=request.session["Id"])
    course = Course.objects.get(Id=course_id)
    task = Task.objects.get(Id = task_id)
    #record = Submission.objects.filter()
    record = Submission.objects.filter(Student_Id=student,Task_Id=task)
    if(record.exists()):
        status=True
        obj=record.get()
    else:
        status=False
        obj=None
    context={
        'task':task,
        'course':course,
        'obj':obj,
        'status':status,
    }
    return render(request,'add_submission.html',context=context)

def submitsubmission(request,course_id,task_id):
    if request.method=='POST':
        content = request.POST.get('submission_desc')
        student = Student.objects.get(Id=request.session["Id"])
        course = Course.objects.get(Id=course_id)
        task = Task.objects.get(Id = task_id)
        record = Submission(Student_Id=student,Task_Id=task,Timestamp=timezone.now(),Status=False,Content=content)
        record.save()
        return redirect('addsubmission',course_id,task_id)

def addcomment(request,course_id,task_id,submission_id):
    if request.method == "POST":
        s = Submission.objects.get(id=submission_id)
        student = Student.objects.get(Id=request.session["Id"])
        comment = request.POST.get("comment")
        record = Comment(Submission_Id=s,Student_Id=student,Content=comment,Timestamp=timezone.now())
        record.save()
        return redirect('GradeSubmission', course_id=course_id,task_id=task_id,submission_id=submission_id)