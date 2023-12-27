from django.db import models
from django.utils.timezone import now
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator

# Create your models here.


def validate_file(value):
    max_length=1000000
    if len(str(value)) >=max_length:
        raise ValidationError('Please reduce your file size')
        

class StudentModel(models.Model):
    Education_level=[
        ('primary','Primary'),
        ('high_school','High School'),
        ('college','College'),
        ('diploma','Diploma'),
        ('bsc','BSc'),
        ('honurs','Honours'),
        ('bba','BBA'),
    ]

    StudentId=models.IntegerField(primary_key=True)
    Name=models.CharField(max_length=100)
    Email=models.EmailField(max_length=100,unique=True)
    Password=models.CharField(max_length=50)
    EducationLevel=models.CharField(max_length=100,choices=Education_level)
    EnrollmentDate=models.DateField()
    OfficialPicture=models.ImageField(upload_to='./static/Image/')
    Resume=models.FileField(validators=[validate_file,FileExtensionValidator(['pdf','docx'])],upload_to='app/Files/')

    def __str__(self):
        return str(self.StudentId)
   
    

