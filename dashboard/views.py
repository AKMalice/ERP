from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


DUMMY_STUDENTS = [
    {'id_number': '001', 'name': 'priya', 'class': '10', 'section': 'A', 'marks': '85'},
    {'id_number': '002', 'name': 'riya', 'class': '10', 'section': 'B', 'marks': '90'},
    {'id_number': '003', 'name': 'ram', 'class': '10', 'section': 'A', 'marks': '78'},
    {'id_number': '005', 'name': 'arjun', 'class': '10', 'section': 'C', 'marks': '88'},
     {'id_number': '006', 'name': 'sudeeksha', 'class': '10', 'section': 'A', 'marks': '85'},
    {'id_number': '007', 'name': 'sreya', 'class': '10', 'section': 'B', 'marks': '90'},
    {'id_number': '008', 'name': 'preethi', 'class': '10', 'section': 'A', 'marks': '78'},
    {'id_number': '009', 'name': 'rahul', 'class': '10', 'section': 'C', 'marks': '88'},
     {'id_number': '010', 'name': 'raj', 'class': '10', 'section': 'A', 'marks': '85'},
    {'id_number': '011', 'name': 'arjun', 'class': '10', 'section': 'B', 'marks': '90'},
    {'id_number': '012', 'name': 'arvind', 'class': '10', 'section': 'A', 'marks': '78'},
]
def student_list(request):
    query = request.GET.get('query', '').strip()
    view_students = request.GET.get('view_students') == 'true'
    if query:
        students = [student for student in DUMMY_STUDENTS if query.lower() in student['name'].lower() or query.lower() in student['id_number'].lower()]
    else:
        students = DUMMY_STUDENTS

    if view_students:
        paginator = Paginator(students, 5)
        page = request.GET.get('page')
        try:
            students = paginator.page(page)
        except PageNotAnInteger:
            students = paginator.page(1)
        except EmptyPage:
            students = paginator.page(paginator.num_pages)
    return render(request, 'admin/students.html', {'students': students})   
def admin_dashboard(request):
    return render(request,'admin/dashboard.html')
def student_details(request):
    return render(request,'admin/students.html')