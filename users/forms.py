from django import forms
from .models import User

class EmployeeForm(forms.Form):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'pass_entry']
