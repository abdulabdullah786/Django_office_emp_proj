from django.shortcuts import render, HttpResponse
from . models import Employee, Role, Department
from datetime import datetime
from django.db.models import Q
# Create your views here.
def index(request):
    return render(request, "index.html")


def All_emp(request):
    emp = Employee.objects.all()
    context = {
        'emps' : emp
    }
    print(context)
    return render(request, "viewall.html", context)

def Add_emp(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        salary = int(request.POST["salary"])
        bonus = int(request.POST["bonus"])
        phone = int(request.POST["phone"])
        dept = int(request.POST["dept"])
        role = int(request.POST["role"])
        new_emp = Employee(first_name=first_name, last_name=last_name, salary=salary, bonus=bonus, phone=phone, dept_id=dept, role_id=role, hire_date=datetime.now())
        new_emp.save()
        return HttpResponse("Employee added Successfully")
    elif request.method == "GET":
        return render(request, "Add.html")
    else:
        return HttpResponse("An exception Occured! Employee has not Been Added")

def remove_emp(request, emp_id =0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse(" Employee Removed successfully ")
        except:
            return HttpResponse("please enter a valid EMP ID")
    emp = Employee.objects.all()
    context = {
        "emps" : emp
    }
    return render(request, "remove.html", context)

def change_emp(request):
    if request.method =='POST':
        Name= request.POST['Name']
        dept= request.POST['dept']
        role= request.POST['role']
        emps= Employee.objects.all()
        if Name:
            emps = emps.filter(Q(first_name__icontains = Name) | Q(last_name__icontains = Name))
        elif dept:
            emps = emps.filter(dept__name__icontains = dept)
        elif role:
            emps = emps.filter(role__name__icontains = role)
        context = {
            emps: emps
        }
        return render(request, "viewall.html", context)
    if request.method == 'GET':
        return render(request, "change.html")
    else:
        return HttpResponse("An Expectional Occured")