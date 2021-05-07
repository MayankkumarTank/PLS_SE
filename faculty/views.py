from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from guest.models import Course,Faculty,Faculty_Course, Student,Task,Submission,Resource,Q_and_A_University_Wide, University,Q_and_A_Course_Wise, Announcement
from guest.models import Student_Course,Comment
from django.db.models import Subquery
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def home_page(request):
    if 'is_logged_in' in request.session and request.session['is_logged_in']==True:
        id=request.session['Id']
        if 'faculty' in request.session:
            courses=Faculty_Course.objects.filter(Faculty_Id=id).values('Course_Id')
            courses=Course.objects.filter(Id__in=Subquery(courses))
            print(courses)
        elif 'student' in request.session:
            print("here")
            courses=Student_Course.objects.filter(Student_Id=id).values('Course_Id')
            courses=Course.objects.filter(Id__in=Subquery(courses))
        context={'courses':courses}
        return render(request,'Dashboard.html',context=context)

    return redirect('login_page')

def Profile(request):
    id = request.session['Id']
    if 'faculty' in request.session:
        record = Faculty.objects.get(Id=id)
    elif 'student' in request.session:
        record = Student.objects.get(Id=id)
    
    context={'record':record}
    return render(request,'Profile.html',context=context)

def Announcement_view(request):
    announcement = Announcement.objects.all()
    # id = request.session['Id']
    # print(id[0])
    # if(id[0] == "F"):
    #     user_faculty = True
    # else:
    #     user_faculty = False
    context={
        'announcements':announcement,
    }
    return render(request,'Announcement.html',context=context)

def faculty_course(request,course_id):
    course=Course.objects.get(Id=course_id)
    context={
        'course':course
    }
    return render(request,'Course.html',context=context)



def tasks(request,course_id):
    tasks=(Task.objects.filter(Course_Id=course_id))
    course=Course.objects.get(Id=course_id)
    #print(tasks)
    context={
        'tasks':tasks,
        'course':course
    }
    return render(request,'Tasks.html',context=context)

def addtask(request,course_id):
    course=Course.objects.get(Id=course_id)
    faculty_id = request.session["Id"]
    context={
        'course':course,
        'faculty_id':faculty_id
    }
    return render(request,'Task_details.html',context=context)

def addresource(request,course_id):
    course=Course.objects.get(Id=course_id)
    faculty_id = request.session["Id"]
    context={
        'course':course,
        'faculty_id':faculty_id
    }
    return render(request,'Resource_details.html',context=context)

@csrf_exempt
def newtask(request,course_id):
    if request.method == "POST":
        course=Course.objects.get(Id=course_id)
        faculty_id = request.session["Id"]
        faculty = Faculty.objects.get(Id=faculty_id)
        title = request.POST.get("task_name")
        content = request.POST.get("task_desc")
        Deadline = request.POST.get("deadline")
        peer_mode = request.POST.get('peer_mode')
        peer_mode = True if peer_mode else False
        Pre_task_id = Task.objects.all().order_by("-Added_date")
        print(len(Pre_task_id))
        if(len(Pre_task_id) ==0):
            Task_Id = "T1"
        else:
            Pre_task_id = Pre_task_id[0].Id
            num = Pre_task_id[1:]
            Task_Id = ("T"+str(int(num)+1))
            print("\n\nTitle: ",Task_Id)
        record = Task(Id=Task_Id,Faculty_Id=faculty,Course_Id=course,Title=title,Content=content,Deadline=Deadline,peer_mode=peer_mode)
        record.save()
        context={
            'message':'Added Successfully',
            'course_id':course_id
        }
        return redirect('tasks', course_id=course_id)

def Updatetask(request,course_id,task_id):
    course=Course.objects.get(Id=course_id)
    faculty_id = request.session["Id"]
    task=Task.objects.get(Id=task_id)
    context={
        'course':course,
        'faculty_id':faculty_id,
        'task':task,
        'update':True
    }
    return render(request,'Task_details.html',context=context)

@csrf_exempt
def UpdatetaskAfter(request,course_id,task_id):
    if request.method == "POST":
        course=Course.objects.get(Id=course_id)
        faculty_id = request.session["Id"]
        faculty = Faculty.objects.get(Id=faculty_id)
        title = request.POST.get("task_name")
        content = request.POST.get("task_desc")
        deadline=request.POST.get("deadline")
        peer_mode = request.POST.get("peer_mode")
        print(peer_mode)
        task=Task.objects.get(Id=task_id)
        task.Title=title
        task.Content=content
        task.Deadline=deadline
        task.peer_mode = True if peer_mode else False
        task.save()
        return redirect('tasks',course_id=course_id)

@csrf_exempt
def newresource(request,course_id):
    if request.method == "POST":
        course=Course.objects.get(Id=course_id)
        faculty_id = request.session["Id"]
        faculty = Faculty.objects.get(Id=faculty_id)
        title = request.POST.get("ResourceName")
        content = request.POST.get("resource_desc")
        Pre_resource_id = Resource.objects.all().order_by("-Added_date")
        if(len(Pre_resource_id) ==0):
            Resource_id = "R1"
        else:
            Pre_resource_id = Pre_resource_id[0].Id
            num = Pre_resource_id[1:]
            Resource_id = ("R"+str(int(num)+1))
            #print("\n\nTitle: ",Task_Id)
            #print(Resource_id,faculty,course,title,content)
        record = Resource(Id=Resource_id,Faculty_Id=faculty,Course_Id=course,Timestamp=timezone.now(),Title=title,Content=content)
        record.save()
        
        # context={
        #     'message':'Added Successfully',
        #     'course_id':course_id
        # }
        return redirect('resources', course_id=course_id)

def ViewTask(request,course_id,task_id):
    print("here")
    course=Course.objects.get(Id=course_id)
    task = Task.objects.get(Id=task_id)
    submissions = Submission.objects.filter(Task_Id=task) 
    
    print(submissions)
    context={
        'course':course,
        'task':task,
        'submissions':submissions,
    }
    return render(request,'Individual_Task.html',context=context)

def DeleteTask(request,course_id,task_id):
    Task.objects.filter(Id=task_id).delete()
    return redirect('tasks',course_id=course_id)

def viewresource(request,course_id,resource_id):
    print("here")
    course=Course.objects.get(Id=course_id)
    resource = Resource.objects.get(Id=resource_id)
    context={
        'course':course,
        'resource':resource,
    }
    return render(request,'Individual_Resource.html',context=context)

def DeleteResources(request,course_id,resource_id):
    Resource.objects.filter(Id=resource_id).delete()
    return redirect('resources',course_id=course_id)

def UpdateResources(request,course_id,resource_id):
    course=Course.objects.get(Id=course_id)
    faculty_id = request.session["Id"]
    resource=Resource.objects.get(Id=resource_id)
    context={
        'course':course,
        'faculty_id':faculty_id,
        'resource':resource,
        'update':True
    }
    return render(request,'Resource_details.html',context=context)

@csrf_exempt
def UpdateResourcesAfter(request,course_id,resource_id):
    if request.method == "POST":
        title = request.POST.get("ResourceName")
        content = request.POST.get("resource_desc")
        resource=Resource.objects.get(Id=resource_id)
        resource.Title=title
        resource.Content=content
        resource.save()
        return redirect('resources', course_id=course_id)

def GradeSubmission(request,course_id,task_id,submission_id):
    course=Course.objects.get(Id=course_id)
    submissions = Submission.objects.get(id=submission_id) 
    comments = Comment.objects.filter(Submission_Id=submissions).order_by('-Timestamp')
    print(comments)
    context={
        'course':course,
        'submissions':submissions,
        'task_id':task_id,
        'comments':comments,
    }
    return render(request,'Grade_Submission.html',context=context)

@csrf_exempt
def UpdateGrade(request,course_id,task_id,submission_id):
    if request.method == "POST":
        s = Submission.objects.get(id=submission_id)
        s.Status = 1
        s.Grade = request.POST.get("grade")
        s.save()
        return redirect('ViewTask', course_id=course_id,task_id=task_id)

def resources(request,course_id):
    resources=(Resource.objects.filter(Course_Id=course_id))
    course=Course.objects.get(Id=course_id)
    context={
        'resources':resources,
        'course':course
    }
    return render(request,'Resources.html',context=context)



def QNAUniversity(request):
    questions=Q_and_A_University_Wide.objects.filter(Question=True).order_by('-Timestamp')
    context={
        'questions':questions,
        'type':'university',
    }
    return render(request,'QnA.html',context=context)

def QNACourse(request,course_id):
    questions=Q_and_A_Course_Wise.objects.filter(Question=True,Course_Id=course_id).order_by('-Timestamp')
    
    context={
        'questions':questions,
        'course':Course.objects.get(Id=course_id),
        'type':'course'
    }
    return render(request,'QnA.html',context=context)


def Question_university(request,question_id):
    question=Q_and_A_University_Wide.objects.get(Question_Id=question_id,Question=True)
    answers=Q_and_A_University_Wide.objects.filter(Question_Id=question_id,Question=False).order_by('Timestamp')
    context={
        'question':question,
        'answers':answers,
        'type':'university'
    }
    return render(request,'Question.html',context=context)

def Question_course(request,course_id,question_id):
    question=Q_and_A_Course_Wise.objects.get(Question_Id=question_id,Course_Id=course_id,Question=True)
    answers=Q_and_A_Course_Wise.objects.filter(Question_Id=question_id,Course_Id=course_id,Question=False).order_by('Timestamp')
    context={
        'question':question,
        'answers':answers,
        'type':'course',
        'course':Course.objects.get(Id=course_id)
    }
    return render(request,'Question.html',context=context)

def AskQuestion_uni(request):
    question=request.POST['ans']
    user_id=request.session['Id']
    if (user_id[0]=='S' ):
        uni_id=Student.objects.get(Id=user_id)

    else:
        uni_id=Faculty.objects.get(Id=user_id)
    
    que_id=Q_and_A_University_Wide.objects.values_list('Question_Id',flat = True).last()+1
    question=Q_and_A_University_Wide(Question_Id=que_id,Answer_Id=0,Question=True,Content=question,Timestamp=timezone.now(),User_Id=user_id,University_Id=uni_id.University_Id)
    question.save()
    return redirect('QNAUniversity')

def AskQuestion_course(request,course_id):
    question=request.POST['ans']
    user_id=request.session['Id']
    
    course_inst=Course.objects.get(Id=course_id)
    que_id=Q_and_A_Course_Wise.objects.values_list('Question_Id',flat = True).last()+1
    question=Q_and_A_Course_Wise(Question_Id=que_id,Answer_Id=0,Question=True,Content=question,Timestamp=timezone.now(),User_Id=user_id,Course_Id=course_inst)
    question.save()
    return redirect('QNACourse',course_id=course_id)

def DeleteQuestion_uni(request,question_id):
    Q_and_A_University_Wide.objects.filter(Question_Id=question_id).delete()
    return redirect('QNAUniversity')

def DeleteQuestion_course(request,course_id,question_id):
    Q_and_A_Course_Wise.objects.filter(Question_Id=question_id,Course_Id=course_id).delete()
    return redirect('QNACourse',course_id=course_id)

def AddAnswer_uni(request,question_id):
    ans=request.POST['ans']
    user_id=request.session['Id']
    if (user_id[0]=='S' ):
        uni_id=Student.objects.get(Id=user_id)

    else:
        uni_id=Faculty.objects.get(Id=user_id)
    
    print(uni_id.University_Id)
    ans_id=Q_and_A_University_Wide.objects.values_list('Answer_Id',flat = True).last()+1
    answer=Q_and_A_University_Wide(Question_Id=question_id,Answer_Id=ans_id,Question=False,Content=ans,Timestamp=timezone.now(),User_Id=user_id,University_Id=uni_id.University_Id)
    answer.save()
    return redirect('Question_university',question_id=question_id)


def AddAnswer_course(request,course_id,question_id):
    ans=request.POST['ans']
    user_id=request.session['Id']
    if (user_id[0]=='S' ):
        uni_id=Student.objects.get(Id=user_id)

    else:
        uni_id=Faculty.objects.get(Id=user_id)
    course_inst=Course.objects.get(Id=course_id)
    
    print(uni_id.University_Id)
    ans_id=Q_and_A_Course_Wise.objects.values_list('Answer_Id',flat = True).last()+1
    answer=Q_and_A_Course_Wise(Question_Id=question_id,Answer_Id=ans_id,Question=False,Content=ans,Timestamp=timezone.now(),User_Id=user_id,Course_Id=course_inst)
    answer.save()
    return redirect('Question_course',course_id=course_id,question_id=question_id)