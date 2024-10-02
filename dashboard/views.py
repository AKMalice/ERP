from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import StudentForm
from .models import Student
from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_students')  # Redirect to the student list after saving
    else:
        form = StudentForm()  # Create a new instance of the form
    
    return render(request, 'add_student.html', {'form': form})


def view_students(request):
    query = request.GET.get('q')
    if query:
        students = Student.objects.filter(first_name__icontains=query)
    else:
        students = Student.objects.all()
        paginator = Paginator(students, 1)  # Show 10 students per page
        page_number = request.GET.get('page')  # Get the current page number from the request
        students = paginator.get_page(page_number)  # Get the students for the current page

    return render(request, 'adminpannel/students.html', {'students': students})

def custom_dashboard(request):
    return render(request,'adminpannel/custom_dashboard.html')
def student_details(request):
    return render(request,'adminpannel/students.html')
def add_student(request):
    return render(request, 'adminpannel/addstudent.html')
def student_detail(request, first_name):
    student = get_object_or_404(Student, first_name=first_name)
    return render(request, 'adminpannel/student_details.html', {'student': student})
