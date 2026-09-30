from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect

def index_view(request):

    if request.user.is_authenticated:

        return redirect('dashboard')

    return redirect('login')

from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .forms import EmployeeForm, RegisterForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


# Register
def register(request):

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            return redirect('login')

    else:

        form = RegisterForm()

    return render(request,
                  'register.html',
                  {'form': form})


# Employee List
@login_required
def employee_list(request):

    employees = Employee.objects.all()

    return render(request,
                  'employee_list.html',
                  {'employees': employees})


# Add Employee
@login_required
def add_employee(request):

    if request.method == 'POST':

        form = EmployeeForm(request.POST,
                            request.FILES)

        if form.is_valid():

            form.save()

            return redirect('employee_list')

    else:

        form = EmployeeForm()

    return render(request,
                  'employee_form.html',
                  {'form': form})


# Employee Detail
@login_required
def employee_detail(request, pk):

    employee = get_object_or_404(Employee, pk=pk)

    return render(request,
                  'employee_detail.html',
                  {'employee': employee})


# Update Employee
@login_required
def update_employee(request, pk):

    employee = get_object_or_404(Employee, pk=pk)

    if request.method == 'POST':

        form = EmployeeForm(request.POST,
                            request.FILES,
                            instance=employee)

        if form.is_valid():

            form.save()

            return redirect('employee_list')

    else:

        form = EmployeeForm(instance=employee)

    return render(request,
                  'employee_edit.html',
                  {'form': form})


# Delete Employee
@login_required
def delete_employee(request, pk):

    employee = get_object_or_404(Employee, pk=pk)

    if request.method == 'POST':

        employee.delete()

        return redirect('employee_list')

    return render(request,
                  'employee_delete.html',
                  {'employee': employee})


# Change Password
@login_required
def change_password(request):

    if request.method == 'POST':

        form = PasswordChangeForm(request.user,
                                  request.POST)

        if form.is_valid():

            user = form.save()

            update_session_auth_hash(request, user)

            return redirect('employee_list')

    else:

        form = PasswordChangeForm(request.user)

    return render(request,
                  'change_password.html',
                  {'form': form})
@login_required
def dashboard(request):

    return render(request,
                  'dashboard.html')