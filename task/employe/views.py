
from django.shortcuts import get_object_or_404, redirect, render

from .forms import EmployeForms


# Create your views here.
from.models import Employe


def emp_list(request):
    list = Employe.objects.all()

    context = {
        "list": list
    }
    return render(request, "employe/list.html", context)


def employe(request):
    if request.method == "POST":
        emp_name = request.POST['emp_name']
        emp_code = request.POST['emp_code']
        epm_deparment = request.POST['epm_deparment']

        employe = Employe(emp_name=emp_name, emp_code=emp_code,
                          epm_deparment=epm_deparment)
        employe.save()

    return redirect('home')


def emp_detail(request, id):
    emp_list = get_object_or_404(Employe, id=id)
    if request.method == "POST":
        emp_list.delete()
        return redirect("home")

    contex = {
        "emp_list": emp_list
    }
    return render(request, "employe/employe.html", contex)


def emp_update(request, id):
    emp_data = get_object_or_404(Employe, id=id)
    form = EmployeForms(request.POST or None, instance=emp_data)
    if form.is_valid():
        form.save()
        return redirect('home')

    context = {
        "emp_data": emp_data,
        "form": form
    }

    return render(request, "employe/empupdate.html", context)
