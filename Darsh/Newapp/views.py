from django.shortcuts import render, redirect
from .models import Employee
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.
def empdata(request):
    if request.method == "POST":
        name = request.POST['name']
        place = request.POST['place']
        mobile = request.POST['mobile']
        image = request.FILES['image']
        Emp_datas = Employee(name=name, place=place, mobile=mobile, image=image)
        Emp_datas.save()
    return render(request, 'emp_data.html')

def empdisplay(request):
    emp = Employee.objects.all()
    return render(request, 'emp_display.html', {'emp':emp})

def deleteemp(request, id):
    emp = Employee.objects.get(id=id)
    emp.delete()
    return redirect(empdisplay)

def editemp(request, id):
    emp=Employee.objects.get(id=id)
    if request.method=='POST':
        name = request.POST.get('name')
        place = request.POST.get('place')
        mobile = request.POST.get('mobile')
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = Employee.objects.get(id=id).image

        emp.name=name
        emp.place=place
        emp.mobile=mobile
        emp.image=file
        emp.save()
        return redirect(empdisplay)
    return render(request, 'editemp.html', {'emp':emp})
