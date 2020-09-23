from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Employee
from .forms import EmployeeForm


def employee_create_and_list_view(request):
    qs = Employee.objects.all()
    e_form = EmployeeForm()

    if 'submit_e_form' in request.POST:
        e_form = EmployeeForm(request.POST)
        if e_form.is_valid():
            e_form.save()
    context = {
        'qs': qs,
        'e_form': e_form,
    }

    return render(request, 'main.html', context)
