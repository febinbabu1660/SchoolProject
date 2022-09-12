from django.shortcuts import render,redirect
from.models import tbl_login,tbl_studreg
# Create your views here.
from django.shortcuts import render


def index(request):
    if request.method=='POST':
        name = request.POST.get("name")
        p_name = request.POST.get("p_name")
        course = request.POST.get("course")
        sl_course = request.POST.get("sl_course")
        phone = request.POST.get("phone")
        mark = request.POST.get("mark")
        place = request.POST.get("place")
        username = request.POST.get("username")
        password = request.POST.get("password")


        new_reg=tbl_studreg(name=name,p_name=p_name,course=course,sl_course=sl_course,phone=phone,mark=mark,place=place,username=username,email=email,password=password)
        new_reg.save()
        new_log=tbl_login(username=username,email=email,password=password)
        new_log.save()
        return redirect('/')

    if request.method=='POST':
        email=request.POST.get('email')
        password = request.POST.get('password')

        student=tbl_login.objects.filter(email=email,password=password)
        if student:
            return redirect('/')


    return render(request, "index.html")

