from django.shortcuts import render, redirect
from .models import Emp
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# 🟢 HOME (غير RH)
@login_required
def emp_home(request):
    if not request.user.is_staff:
        return redirect('my_profile')

    emps = Emp.objects.all()
    return render(request, "emp/home.html", {'emps': emps})


# 🟢 PROFILE (Employee يشوف غير راسو)
@login_required
def my_profile(request):
    emp = Emp.objects.get(user=request.user)  # فقط معلومات هذا المستخدم
    return render(request, "emp/Profile.html", {'emp': emp})


# 🟢 ADD EMPLOYEE (غير RH)
@login_required
def add_emp(request):
    if not request.user.is_staff:
        return redirect('my_profile')

    if request.method == "POST":
        name = request.POST.get('emp_name')
        emp_id = request.POST.get('emp_id')
        phone = request.POST.get('emp_phone')
        address = request.POST.get('emp_address')
        working = request.POST.get('emp_working') == 'on'
        department = request.POST.get('emp_department')
        salary = request.POST.get('emp_salary')

        # إنشاء User جديد
        user = User.objects.create_user(username=emp_id, password="1234")

        Emp.objects.create(
            user=user,
            name=name,
            emp_id=emp_id,
            phone=phone,
            address=address,
            working=working,
            department=department,
            salary=salary
        )

        return redirect('/emp/home/')

    return render(request, "emp/add_emp.html")


# 🟢 UPDATE (عرض الفورم)
@login_required
def update_emp(request, emp_id):
    if not request.user.is_staff:
        return redirect('my_profile')

    emp = Emp.objects.get(id=emp_id)
    return render(request, "emp/update_emp.html", {'emp': emp})


# 🟢 UPDATE (تنفيذ التعديل)
@login_required
def do_update_emp(request, emp_id):
    if not request.user.is_staff:
        return redirect('my_profile')

    emp = Emp.objects.get(id=emp_id)

    if request.method == "POST":
        emp.name = request.POST.get('emp_name')
        emp.emp_id = request.POST.get('emp_id')
        emp.phone = request.POST.get('emp_phone')
        emp.address = request.POST.get('emp_address')
        emp.working = request.POST.get('emp_working') == 'on'
        emp.department = request.POST.get('emp_department')
        emp.salary = request.POST.get('emp_salary')

        emp.save()

    return redirect('/emp/home/')


# 🟢 DELETE (غير RH)
@login_required
def delete_emp(request, emp_id):
    if not request.user.is_staff:
        return redirect('my_profile')

    emp = Emp.objects.get(id=emp_id)
    emp.delete()
    return redirect('/emp/home/')