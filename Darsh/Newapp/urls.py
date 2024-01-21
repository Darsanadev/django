from . import views
from django.urls import path

app_name = 'Newapp'

urlpatterns = [
    path('data/', views.empdata, name="data"),
    path('display/', views.empdisplay, name="display"),
    path('deleteemp/<int:id>', views.deleteemp, name='deleteemp'),
    path('editemp/<int:id>', views.editemp, name='editemp'),

]
