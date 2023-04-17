from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("projects/<int:id>",views.view_project,name="view_project"),
    path("projects",views.view_all_project,name="view_all_project"),
]