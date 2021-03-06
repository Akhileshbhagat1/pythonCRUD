from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_form, name='employee_insert'),    # get and post req. for insert operations
    path('<int:id>/', views.employee_form, name='employee_update'),  # get and post request for update operations
    path('delete/<int:id>/', views.employee_delete, name='employee_delete'),
    path('list/', views.employee_list, name='employee_list'),   # get req. to retrieve and display all records

]