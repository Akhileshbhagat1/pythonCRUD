from django.shortcuts import render, redirect
from django.views.generic import ListView

from .models import Employee
from .forms import EmployeeForm


def employee_form(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, 'employee_register/employee_form.html', {'form': form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST, instance=employee)

        if form.is_valid():
            form.save()
        return redirect('/employee/list')


def employee_list(request):
    context = {'employee_list': Employee.objects.all()}
    return render(request, 'employee_register/employee_list.html', context)


def employee_delete(request, id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list')


class PostListView(ListView):
    model = Employee
    template_name = 'employee_register/employee_list.html'
    context_object_name = 'post'

