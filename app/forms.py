# hr/forms.py
from django import forms
from .models import Employee, Attendance, Leave, Payroll, Performance, Recruitment, Training

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = '__all__'

class LeaveForm(forms.ModelForm):
    class Meta:
        model = Leave
        fields = '__all__'

class PayrollForm(forms.ModelForm):
    class Meta:
        model = Payroll
        fields = '__all__'

class PerformanceForm(forms.ModelForm):
    class Meta:
        model = Performance
        fields = '__all__'

class RecruitmentForm(forms.ModelForm):
    class Meta:
        model = Recruitment
        fields = '__all__'

class TrainingForm(forms.ModelForm):
    class Meta:
        model = Training
        fields = '__all__'