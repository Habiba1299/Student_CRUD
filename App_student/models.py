from django.db import models

# Create your models here.

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    school_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    dob = models.DateField(blank=True,null=True)
    profile_pic = models.ImageField(upload_to='profile_images',verbose_name="Picture")
    description = models.TextField(blank=True)  
    join_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    study_group = models.CharField(max_length=50, choices=(
                             ("Science","Science"),
                             ('Business Studies','Business Studies'),
                             ('Humanities','Humanities')
                            ))
    
    class Meta:
        ordering = ['-join_date']

    def __str__(self):
        return self.name
