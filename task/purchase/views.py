
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from employe.models import Employe
from reply.models import Reply
from .forms import PurchasetaskForm
from django.shortcuts import get_object_or_404, redirect, render
from . models import Purchasetask
from django.http import HttpResponse
import csv


@login_required(login_url="login")
def home(request):
    data = Employe.objects.order_by('emp_code')
    context = {
        "data": data
    }
    return render(request, "webpage/home.html", context)


@login_required(login_url="login")
def download_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=worklist.csv'

    # Create a csv writer
    writer = csv.writer(response)

    # Designate The Model
    downloads = Purchasetask.objects.all()

    # Add column headings to the csv file
    writer.writerow(['Assing to', 'Discription', 'Department',
                    'Given by', 'Remark', 'Reporting Date', 'Date', 'Status', "CHecked"])

    # Loop Thu and output
    for download in downloads:
        writer.writerow([download.first_name, download.discription, download.deaprtment,
                        download.created_by, download.ramark, download.repoting_data, download.date, download.status, download.checked])

    return response


@login_required(login_url="login")
def purchasetask(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        discription = request.POST['discription']
        ramark = request.POST['ramark']
        created_by = request.POST['created_by']
        repoting_data = request.POST['repoting_data']
        deaprtment = request.POST['deaprtment']
        submision_date = request.POST.get('submision_date', False)

    purchasetask = Purchasetask(first_name=first_name, discription=discription,
                                ramark=ramark, created_by=created_by, repoting_data=repoting_data, deaprtment=deaprtment, submision_date=submision_date)
    purchasetask.save()

    return redirect("purchase-task")


@login_required(login_url="login")
def purchese(request):
    return render(request, "purchese/create.html")


@login_required(login_url="login")
def purchase_task(request):
    data = Purchasetask.objects.order_by('-date')

    empData = Employe.objects.values_list('emp_name', flat=True).distinct()
    empdep = Employe.objects.values_list('epm_deparment', flat=True).distinct()

    to = Purchasetask.objects.values_list('first_name', flat=True).distinct()
    given_by = Purchasetask.objects.values_list(
        'created_by', flat=True).distinct()
    last_date = Purchasetask.objects.values_list(
        'repoting_data', flat=True).distinct()

    if "keyword" in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            data = data.filter(first_name__icontains=keyword)

    if "keyword1" in request.GET:
        keyword1 = request.GET['keyword1']
        if keyword1:
            data = data.filter(created_by__icontains=keyword1)

    if "keyword2" in request.GET:
        keyword2 = request.GET['keyword2']
        if keyword2:
            data = data.filter(repoting_data__icontains=keyword2)

    contex = {
        "data": data,
        "given_by": given_by,
        "to": to,
        "last_date": last_date,
        "empData": empData,
        "empdep": empdep
    }
    return render(request, "purchese/create.html", contex)


@login_required(login_url="login")
def purchsedep_detail(request, id):
    data = get_object_or_404(Purchasetask, id=id)
    remark_data = Reply.objects.all()
    if request.method == "POST":
        data.delete()
        return redirect('purchase-task')
    context = {
        "data": data,
        "remark_data": remark_data
    }
    return render(request, "purchese/purchsedep_detail.html", context)


@login_required(login_url="login")
def update_product(request, id):
    tuber = get_object_or_404(Purchasetask, id=id)
    form = PurchasetaskForm(request.POST or None, instance=tuber)
    if form.is_valid():
        form.save()
        return redirect('purchase-task')

    context = {
        "tuber": tuber,
        "form": form
    }

    return render(request, "purchese/product_update.html", context)


@login_required(login_url="login")
def search(request):
    data = Purchasetask.objects.order_by('-date')
    to = Purchasetask.objects.values_list('first_name', flat=True).distinct()
    given_by = Purchasetask.objects.values_list(
        'created_by', flat=True).distinct()
    last_date = Purchasetask.objects.values_list(
        'repoting_data', flat=True).distinct()

    if "keyword" in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            data = data.filter(first_name__icontains=keyword)

    if "keyword1" in request.GET:
        keyword1 = request.GET['keyword1']
        if keyword1:
            data = data.filter(created_by__icontains=keyword1)

    if "keyword2" in request.GET:
        keyword2 = request.GET['keyword2']
        if keyword2:
            data = data.filter(repoting_data__icontains=keyword2)

    contex = {
        "data": data,
        "given_by": given_by,
        "to": to,
        "last_date": last_date
    }
    return render(request, "purchese/search.html", contex)
