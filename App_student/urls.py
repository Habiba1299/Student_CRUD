from django.urls import path ,include
from App_student import views
from rest_framework import routers
app_name = 'App_student'

router = routers.DefaultRouter()
router.register(r'students', views.StudentViewSet)
urlpatterns = [
    path('',views.student_list.as_view(),name='student_list'),
    path('add-student/',views.Add_student.as_view(),name='add-student'),
    path('details/<pk>/',views.student_details,name='student_details'),
    path('edit/<pk>/',views.UpdateStudent.as_view(),name='edit_student'),  
    path('delete/<pk>/', views.delete_student, name='delete_student'),
    path('api/',include(router.urls))
]