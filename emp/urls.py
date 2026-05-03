from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views   # <-- hadi khassha

urlpatterns = [
    # EMPLOYEE APP
    path("home/", emp_home, name="home"),
    path("profile/", my_profile, name="my_profile"),
    path("add-emp/", add_emp, name="add_emp"),
    path("delete-emp/<int:emp_id>", delete_emp, name="delete_emp"),
    path("update-emp/<int:emp_id>", update_emp, name="update_emp"),
    path("do-update-emp/<int:emp_id>", do_update_emp, name="do_update_emp"),

]
# hii 