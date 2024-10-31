from rest_framework import serializers
from App_student.models import Student


class StudentSerializers(serializers.ModelSerializer):
    # student_id = serializers.ReadOnlyField()

    class Meta:
        model= Student
        fields= ['student_id', 'name', 'school_name','dob','address','study_group','description'] 
