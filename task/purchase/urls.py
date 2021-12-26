from django.urls import path


from . import views

urlpatterns = [
    path("", views.purchese, name="purchese"),
    path("task", views.purchase_task, name="purchase-task"),
    path("<int:id>", views.purchsedep_detail, name="purchsedep-detail"),
    path('<int:id>/update', views.update_product, name='update-product'),
    path("purchasetask", views.purchasetask, name="purchasetask"),
    path("search", views.search, name="search"),
    path('download_csv', views.download_csv, name='download_csv'),

]
