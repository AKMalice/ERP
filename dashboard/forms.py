from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'first_name',
            'last_name',
            'mother_phone_no',
            'father_phone_no',
            'dob',
            'parent_email',
            'enrollment_date',
        ]
