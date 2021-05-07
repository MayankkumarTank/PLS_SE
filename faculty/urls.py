from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.home_page, name='dashboard'),
    path('dashboard/Profile', views.Profile, name='Profile'),
    path('dashboard/Announcement', views.Announcement_view, name='Announcement_view'),
    path('dashboard/<slug:course_id>', views.faculty_course, name='course'),
    path('dashboard/<slug:course_id>/tasks', views.tasks, name='tasks'),
    path('dashboard/<slug:course_id>/tasks/addtask', views.addtask, name='addtask'),
    path('dashboard/<slug:course_id>/tasks/addtask/newtask', views.newtask, name='newtask'),
    path('dashboard/<slug:course_id>/tasks/<slug:task_id>/updatetask', views.Updatetask, name='Updatetask'),
    path('dashboard/<slug:course_id>/tasks/<slug:task_id>/updatetask/after', views.UpdatetaskAfter, name='UpdatetaskAfter'),
    path('dashboard/<slug:course_id>/tasks/viewtask/<slug:task_id>', views.ViewTask, name='ViewTask'),
    path('dashboard/<slug:course_id>/tasks/viewtask/<slug:task_id>/deletetask', views.DeleteTask, name='DeleteTask'),
    path('dashboard/<slug:course_id>/tasks/viewtask/<slug:task_id>/Grade/<slug:submission_id>', views.GradeSubmission, name='GradeSubmission'),
    path('dashboard/<slug:course_id>/tasks/viewtask/<slug:task_id>/Grade/<slug:submission_id>/UpdateGrade', views.UpdateGrade, name='UpdateGrade'),
    path('dashboard/<slug:course_id>/resources', views.resources, name='resources'),
    path('dashboard/<slug:course_id>/resources/addresource', views.addresource, name='addresource'),
    path('dashboard/<slug:course_id>/resources/addresource/newresource', views.newresource, name='newresource'),
    path('dashboard/<slug:course_id>/resources/viewresource/<slug:resource_id>', views.viewresource, name='viewresource'),
    path('dashboard/<slug:course_id>/resources/deleteresource/<slug:resource_id>', views.DeleteResources, name='DeleteResources'),
    path('dashboard/<slug:course_id>/resources/updateresource/<slug:resource_id>', views.UpdateResources, name='UpdateResources'),
    path('dashboard/<slug:course_id>/resources/updateresource/<slug:resource_id>/after', views.UpdateResourcesAfter, name='UpdateResourcesAfter'),
    path('dashboard/QnA/University', views.QNAUniversity, name='QNAUniversity'),
    path('dashboard/QnA/course/<slug:course_id>', views.QNACourse, name='QNACourse'),
    path('dashboard/QnA/University/<slug:question_id>/deletequestion', views.DeleteQuestion_uni, name='DeleteQuestion_uni'),
    path('dashboard/QnA/University/askquestion', views.AskQuestion_uni, name='AskQuestion_uni'),
    path('dashboard/QnA/University/<slug:question_id>', views.Question_university, name='Question_university'),
    path('dashboard/course/<slug:course_id>/askquestion', views.AskQuestion_course, name='AskQuestion_course'),
    path('dashboard/QnA/<slug:course_id>/<slug:question_id>', views.Question_course, name='Question_course'),
    path('dashboard/QnA/University/<slug:question_id>/addanswer', views.AddAnswer_uni, name='addanswer_uni'),
    path('dashboard/QnA/<slug:course_id>/<slug:question_id>/deletequestion', views.DeleteQuestion_course, name='DeleteQuestion_course'),
    path('dashboard/QnA/course/<slug:course_id>/<slug:question_id>/addanswer', views.AddAnswer_course, name='addanswer_course'),
]