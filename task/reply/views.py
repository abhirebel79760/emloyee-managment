from django.shortcuts import render, redirect

# Create your views here.
from.models import Reply


def reply(request):
    if request.method == "POST":
        user_name = request.POST['user_name']
        remark = request.POST['remark']

        reply = Reply(user_name=user_name, remark=remark)
        reply.save()

    if request.method == "POST":
        data = Reply.objects.all()
        data.delete()
        return redirect('purchase-task')

    return redirect('home')
