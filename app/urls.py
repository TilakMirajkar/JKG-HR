from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    path('employees/<int:pk>/', views.employee_detail, name='employee_detail'),
    path('employees/create/', views.employee_create, name='employee_create'),
    path('employees/<int:pk>/update/', views.employee_update, name='employee_update'),
    path('employees/<int:pk>/delete/', views.employee_delete, name='employee_delete'),

    path('attendance/', views.attendance_list, name='attendance_list'),
    path('attendance/<int:pk>/', views.attendance_detail, name='attendance_detail'),
    path('attendance/create/', views.attendance_create, name='attendance_create'),
    path('attendance/<int:pk>/update/', views.attendance_update, name='attendance_update'),
    path('attendance/<int:pk>/delete/', views.attendance_delete, name='attendance_delete'),

    path('leave/', views.leave_list, name='leave_list'),
    path('leave/<int:pk>/', views.leave_detail, name='leave_detail'),
    path('leave/create/', views.leave_create, name='leave_create'),
    path('leave/<int:pk>/update/', views.leave_update, name='leave_update'),
    path('leave/<int:pk>/delete/', views.leave_delete, name='leave_delete'),

    path('payroll/', views.payroll_list, name='payroll_list'),
    path('payroll/<int:pk>/', views.payroll_detail, name='payroll_detail'),
    path('payroll/create/', views.payroll_create, name='payroll_create'),
    path('payroll/<int:pk>/update/', views.payroll_update, name='payroll_update'),
    path('payroll/<int:pk>/delete/', views.payroll_delete, name='payroll_delete'),

    path('performance/', views.performance_list, name='performance_list'),
    path('performance/<int:pk>/', views.performance_detail, name='performance_detail'),
    path('performance/create/', views.performance_create, name='performance_create'),
    path('performance/<int:pk>/update/', views.performance_update, name='performance_update'),
    path('performance/<int:pk>/delete/', views.performance_delete, name='performance_delete'),

    path('recruitment/', views.recruitment_list, name='recruitment_list'),
    path('recruitment/<int:pk>/', views.recruitment_detail, name='recruitment_detail'),
    path('recruitment/create/', views.recruitment_create, name='recruitment_create'),
    path('recruitment/<int:pk>/update/', views.recruitment_update, name='recruitment_update'),
    path('recruitment/<int:pk>/delete/', views.recruitment_delete, name='recruitment_delete'),

    path('training/', views.training_list, name='training_list'),
    path('training/<int:pk>/', views.training_detail, name='training_detail'),
    path('training/create/', views.training_create, name='training_create'),
    path('training/<int:pk>/update/', views.training_update, name='training_update'),
    path('training/<int:pk>/delete/', views.training_delete, name='training_delete'),

    path('reports/', views.reports, name='reports'),
]