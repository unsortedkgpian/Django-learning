
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_atom, name="all_atom"),
    path('<int:atom_id>/', views.atom_details, name="atom_details"),
]

