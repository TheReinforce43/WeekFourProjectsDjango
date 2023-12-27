from .models import StudentModel
from django import forms


class StudentForm(forms.ModelForm):

    class Meta:
        model=StudentModel
        fields='__all__'

        labels={
            'EnrollmentDate':'Enrollment Date',
            'StudentId':'Student Id',
            'Name':'Student Name',
            'OfficialPicture':'Official Picture',
            'EducationLevel':'Education Level',
        }
        widgets={
            'EnrollmentDate':forms.DateInput(attrs={'type': 'date'}),
            'Password':forms.PasswordInput(attrs={'type': 'password'}),
           
        }
        help_texts={
            'OfficialPicture':'Enter Your Profile Picture ',
            'Resume':'Drop Your Resume'
        }

