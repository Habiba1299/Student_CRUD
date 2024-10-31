from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseRedirect 
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView, View, TemplateView
from App_student.models import Student
from django import forms
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from rest_framework import viewsets
from App_student.serializers import StudentSerializers
# Create your views here.

# def student_list(request):
#     return HttpResponse("this is student List")

class student_list(ListView):
    context_object_name = 'students'
    model = Student
    template_name = 'App_student/student_list.html'

class Add_student(CreateView):
    fields = '__all__'
   
    model = Student
    template_name = 'App_student/add_student.html'

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Add a date picker widget to the 'dob' field
        form.fields['dob'].widget = forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
        return form
    
    def form_valid(self, form):
        student_obj = form.save(commit=False)
        student_obj.save()
        return HttpResponseRedirect(reverse('index'))
    

def student_details(request,pk):

    student = Student.objects.get(pk=pk)
    
    dict ={'student':student}
    return render(request, 'App_Student/student_details.html',context = dict)

    

class UpdateStudent(UpdateView):
    fields = '__all__'
    model = Student
    template_name = 'App_student/edit_student.html'

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Add a date picker widget to the 'dob' field
        form.fields['dob'].widget = forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
        return form


    def form_valid(self, form, **kwargs):
        student_obj = form.save(commit=False)
        
        student_obj.save()
        return HttpResponseRedirect(reverse_lazy('App_student:student_details', kwargs={'pk':student_obj.pk}))
    
def delete_student(request, pk):
    student = Student.objects.get(pk=pk)
    student.delete()  # Delete the student record
    messages.success(request, f'Student {student.name} has been deleted successfully.') 
    return  HttpResponseRedirect(reverse_lazy('App_student:student_list'))


       
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers