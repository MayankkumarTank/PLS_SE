from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Student,Admin,Faculty,School,Programme,Major
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def home_page(request):
    return render(request, 'guest/templates/home.html')

@csrf_exempt
def login_page(request):
    if request.method=='POST':
        email=request.POST.get('emailId')
        password=request.POST.get('password')
        role=request.POST.get('Role')
        if role=='Student':
            try: 
                if not Student.objects.filter(Email_Id = email, Password=password).exists():
                    print("Invalid Credentials")
                    return render(request,'Home.html')
                else:
                    request.session['Id'] = Student.objects.filter(Email_Id = email).values('Id')[0]['Id']
                    request.session['is_logged_in'] = True
                    request.session['Name'] = Student.objects.filter(Email_Id=email).values('First_Name')[0]['First_Name']
                    request.session['student'] = True
                    print(request.session['Name'])
                    return redirect('dashboard')
            except:
                context={
                    'msg':'Please provide valid credentials',
                    'title':'Error',
                }
                return render(request,'login.html',context=context)
        elif role=='Faculty':
            try: 
                if not Faculty.objects.filter(Email_Id = email, Password=password).exists():
                    print("Invalid Credentials")
                    return render(request,'Home.html')
                else:
                    request.session['Id'] = Faculty.objects.filter(Email_Id = email).values('Id')[0]['Id']
                    request.session['is_logged_in'] = True
                    request.session['Name'] = Faculty.objects.filter(Email_Id=email).values('First_Name')[0]['First_Name']
                    request.session['faculty'] = True
                    print(request.session['Name'])
                    return redirect('dashboard')
            except:
                context={
                    'msg':'Please provide valid credentials',
                    'title':'Error',
                }
                return render(request,'login.html',context=context)
        """
        elif role=='Admin':
            if not Admin.objects.filter(Email_Id = email, Password=password).exists():
                print("Invalid Credentials")
                return render(request,'Home.html')
            else:
                request.session['Id'] = Admin.objects.filter(Email_Id = email).values('Id')[0]['Id']
                request.session['is_logged_in'] = True
                request.session['Name'] = Admin.objects.filter(Email_Id=email).values('First_Name')[0]['First_Name']
                print(request.session['Name'])
                return render(request,'Dashboard.html')
        """
    return render(request, 'guest/templates/login.html')

def Logout(request):
    request.session.flush()
    return redirect('home_page')

def school(request, s_name):
    chemical = ['Org', 'Norg']
    mechanical = ['FM', 'TH']
    computer = ['DSP', 'ML']
    school = School.objects.get(Id="SC1")
    programmes = Programme.objects.filter(School_Id=school)
    
    # for programme in programmes:
    #     majors = Major.objects.filter(Programme_Id = programme)
    #     major_course = []
    #     for major in majors:
    #         courses = Course.objects.filter(School_Id=school,Programme_Id = programme, Major_id=major)
    #         major_course.append{'Courses':courses,'Majors':major}

    context = {
        'school': school,
        'programs': {
            'Chemical': chemical,
            'Computer Science': computer,
            'Mechanical': mechanical,
        },
    }
    return render(request, 'guest/templates/school.html', context)

def course(request, course):
    course_name = course
    print(course)
    print(course_name)
    context = {
        'course_name': course_name,
    }
    return render(request, 'guest/templates/course_prev.html', context)

def after_login(request):
    if request.method == 'POST':
        request.session['status_login'] = False
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_type = request.POST.get('user-type')
        # print("------------------------------")
        # print(email)
        # print(password)
        # print(user_type)
        # print("------------------------------")
        if user_type == "faculty":
            courses = ['course-1', 'course-2','course-3','course-4']
            context = {
                'f_name' : "Dr. Khusharu",
                'courses': courses,
            }
            return render(request, 'faculty/templates/start_base.html', context)
        if user_type == "student":
            return HttpResponse("Wellcome Student")
        if user_type == "admin":
            return HttpResponse("Wellcome Admin")
        return HttpResponse(context)
    return HttpResponse("Don't know what happened.")
