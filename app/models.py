# hr/models.py
from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=255)
    role = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    joining_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to='employee_photos/', null=True, blank=True)

    def __str__(self):
        return self.name

class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    clock_in = models.TimeField()
    clock_out = models.TimeField()

    def __str__(self):
        return f"{self.employee.name} - {self.date}"

class Leave(models.Model):
    LEAVE_TYPES = [
        ('Sick', 'Sick Leave'),
        ('Vacation', 'Vacation Leave'),
        ('Personal', 'Personal Leave'),
    ]
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=50, choices=LEAVE_TYPES)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=50, default='Pending')

    def __str__(self):
        return f"{self.employee.name} - {self.leave_type}"

class Payroll(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    deductions = models.DecimalField(max_digits=10, decimal_places=2)
    net_pay = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()

    def __str__(self):
        return f"{self.employee.name} - {self.payment_date}"

class Performance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    goals = models.TextField()
    reviews = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return f"{self.employee.name} - Performance"

class Recruitment(models.Model):
    job_title = models.CharField(max_length=255)
    description = models.TextField()
    applicants = models.TextField()
    interview_date = models.DateField()

    def __str__(self):
        return self.job_title

class Training(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    attendees = models.ManyToManyField(Employee)
    materials = models.FileField(upload_to='training_materials/')

    def __str__(self):
        return self.title