from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee, Attendance, Leave, Payroll, Performance, Recruitment, Training
from .forms import EmployeeForm, AttendanceForm, LeaveForm, PayrollForm, PerformanceForm, RecruitmentForm, TrainingForm
from django.db.models import Sum

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'employee_detail.html', {'employee': employee})

def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employee_form.html', {'form': form})

def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employee_form.html', {'form': form})

def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'employee_confirm_delete.html', {'employee': employee})

def attendance_list(request):
    attendances = Attendance.objects.all()
    return render(request, 'attendance_list.html', {'attendances': attendances})

def attendance_detail(request, pk):
    attendance = get_object_or_404(Attendance, pk=pk)
    return render(request, 'attendance_detail.html', {'attendance': attendance})

def attendance_create(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('attendance_list')
    else:
        form = AttendanceForm()
    return render(request, 'attendance_form.html', {'form': form})

def attendance_update(request, pk):
    attendance = get_object_or_404(Attendance, pk=pk)
    if request.method == 'POST':
        form = AttendanceForm(request.POST, instance=attendance)
        if form.is_valid():
            form.save()
            return redirect('attendance_list')
    else:
        form = AttendanceForm(instance=attendance)
    return render(request, 'attendance_form.html', {'form': form})

def attendance_delete(request, pk):
    attendance = get_object_or_404(Attendance, pk=pk)
    if request.method == 'POST':
        attendance.delete()
        return redirect('attendance_list')
    return render(request, 'attendance_confirm_delete.html', {'attendance': attendance})

def leave_list(request):
    leaves = Leave.objects.all()
    return render(request, 'leave_list.html', {'leaves': leaves})

def leave_detail(request, pk):
    leave = get_object_or_404(Leave, pk=pk)
    return render(request, 'leave_detail.html', {'leave': leave})

def leave_create(request):
    if request.method == 'POST':
        form = LeaveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('leave_list')
    else:
        form = LeaveForm()
    return render(request, 'leave_form.html', {'form': form})

def leave_update(request, pk):
    leave = get_object_or_404(Leave, pk=pk)
    if request.method == 'POST':
        form = LeaveForm(request.POST, instance=leave)
        if form.is_valid():
            form.save()
            return redirect('leave_list')
    else:
        form = LeaveForm(instance=leave)
    return render(request, 'leave_form.html', {'form': form})

def leave_delete(request, pk):
    leave = get_object_or_404(Leave, pk=pk)
    if request.method == 'POST':
        leave.delete()
        return redirect('leave_list')
    return render(request, 'leave_confirm_delete.html', {'leave': leave})

def payroll_list(request):
    payrolls = Payroll.objects.all()
    return render(request, 'payroll_list.html', {'payrolls': payrolls})

def payroll_detail(request, pk):
    payroll = get_object_or_404(Payroll, pk=pk)
    return render(request, 'payroll_detail.html', {'payroll': payroll})

def payroll_create(request):
    if request.method == 'POST':
        form = PayrollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payroll_list')
    else:
        form = PayrollForm()
    return render(request, 'payroll_form.html', {'form': form})

def payroll_update(request, pk):
    payroll = get_object_or_404(Payroll, pk=pk)
    if request.method == 'POST':
        form = PayrollForm(request.POST, instance=payroll)
        if form.is_valid():
            form.save()
            return redirect('payroll_list')
    else:
        form = PayrollForm(instance=payroll)
    return render(request, 'payroll_form.html', {'form': form})

def payroll_delete(request, pk):
    payroll = get_object_or_404(Payroll, pk=pk)
    if request.method == 'POST':
        payroll.delete()
        return redirect('payroll_list')
    return render(request, 'payroll_confirm_delete.html', {'payroll': payroll})

def performance_list(request):
    performances = Performance.objects.all()
    return render(request, 'performance_list.html', {'performances': performances})

def performance_detail(request, pk):
    performance = get_object_or_404(Performance, pk=pk)
    return render(request, 'performance_detail.html', {'performance': performance})

def performance_create(request):
    if request.method == 'POST':
        form = PerformanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('performance_list')
    else:
        form = PerformanceForm()
    return render(request, 'performance_form.html', {'form': form})

def performance_update(request, pk):
    performance = get_object_or_404(Performance, pk=pk)
    if request.method == 'POST':
        form = PerformanceForm(request.POST, instance=performance)
        if form.is_valid():
            form.save()
            return redirect('performance_list')
    else:
        form = PerformanceForm(instance=performance)
    return render(request, 'performance_form.html', {'form': form})

def performance_delete(request, pk):
    performance = get_object_or_404(Performance, pk=pk)
    if request.method == 'POST':
        performance.delete()
        return redirect('performance_list')
    return render(request, 'performance_confirm_delete.html', {'performance': performance})

def recruitment_list(request):
    recruitments = Recruitment.objects.all()
    return render(request, 'recruitment_list.html', {'recruitments': recruitments})

def recruitment_detail(request, pk):
    recruitment = get_object_or_404(Recruitment, pk=pk)
    return render(request, 'recruitment_detail.html', {'recruitment': recruitment})

def recruitment_create(request):
    if request.method == 'POST':
        form = RecruitmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recruitment_list')
    else:
        form = RecruitmentForm()
    return render(request, 'recruitment_form.html', {'form': form})

def recruitment_update(request, pk):
    recruitment = get_object_or_404(Recruitment, pk=pk)
    if request.method == 'POST':
        form = RecruitmentForm(request.POST, instance=recruitment)
        if form.is_valid():
            form.save()
            return redirect('recruitment_list')
    else:
        form = RecruitmentForm(instance=recruitment)
    return render(request, 'recruitment_form.html', {'form': form})

def recruitment_delete(request, pk):
    recruitment = get_object_or_404(Recruitment, pk=pk)
    if request.method == 'POST':
        recruitment.delete()
        return redirect('recruitment_list')
    return render(request, 'recruitment_confirm_delete.html', {'recruitment': recruitment})

# Training Views
def training_list(request):
    trainings = Training.objects.all()
    return render(request, 'training_list.html', {'trainings': trainings})

def training_detail(request, pk):
    training = get_object_or_404(Training, pk=pk)
    return render(request, 'training_detail.html', {'training': training})

def training_create(request):
    if request.method == 'POST':
        form = TrainingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('training_list')
    else:
        form = TrainingForm()
    return render(request, 'training_form.html', {'form': form})

def training_update(request, pk):
    training = get_object_or_404(Training, pk=pk)
    if request.method == 'POST':
        form = TrainingForm(request.POST, request.FILES, instance=training)
        if form.is_valid():
            form.save()
            return redirect('training_list')
    else:
        form = TrainingForm(instance=training)
    return render(request, 'training_form.html', {'form': form})

def training_delete(request, pk):
    training = get_object_or_404(Training, pk=pk)
    if request.method == 'POST':
        training.delete()
        return redirect('training_list')
    return render(request, 'training_confirm_delete.html', {'training': training})

# Reports View
def reports(request):
    total_employees = Employee.objects.count()
    total_payroll = Payroll.objects.aggregate(total=Sum('net_pay'))['total']
    return render(request, 'reports.html', {
        'total_employees': total_employees,
        'total_payroll': total_payroll,
    })