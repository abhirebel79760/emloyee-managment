from django.urls import path


from . import views

urlpatterns = [
    path("employe", views.employe, name="employe"),
    path("list", views.emp_list, name="list"),
    path("<int:id>", views.emp_detail, name="empl_detail"),
    path("<int:id>/update", views.emp_update, name="empl_update")
]
