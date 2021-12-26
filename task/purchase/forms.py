from django import forms
from datetime import datetime

from django.forms import widgets


from .models import Purchasetask


def get_today():
    return datetime.now()


x = slice(20)


TODAY = (get_today)

DATE_SELECTION = (
    (TODAY, TODAY),

)


class PurchasetaskForm(forms.ModelForm):
    submision_date = forms.CharField(
        widget=forms.Select(choices=DATE_SELECTION))

    class Meta:
        model = Purchasetask
        fields = [

            "status",
            "ramark",
            "checked",
            "submision_date",
            "created_by"
        ]

        widgets = {
            "created_by": forms.TextInput(attrs={"class": "visually-hidden creator"})
        }
