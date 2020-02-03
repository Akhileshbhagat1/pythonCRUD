from django import forms
from .models import Employee, Position


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        # fields = '__all__'  # for showing all the attributes of Database
        fields = ['fullname', 'emp_code', 'mobile', 'position']
        labels = {                             # for updating the templates or customize the forms labels
            'Fullname': 'Full Name',
            'Emp code': 'EMP. Code'
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select"
        self.fields['emp_code'].required = False
