from django import forms


from .models import Employe


class EmployeForms(forms.ModelForm):
    class Meta:
        model = Employe

        fields = [
            "emp_name", "emp_code", "epm_deparment"
        ]

        widgets = {
            "emp_name": forms.TextInput(attrs={"class": "name"})
        }
