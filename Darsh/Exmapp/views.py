from django.shortcuts import render
from.models import Exam
# Create your views here.
def exm(request):
    return render(request, 'exm_detail.html')

def exm_dispay(request):
    datas=Exam.objects.all()
    return render(request, 'exm_display.html', {'datas':datas})
