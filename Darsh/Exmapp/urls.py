from . import views
from django . urls import path

app_name = 'Exmapp'

urlpatterns = [
    path('detail/', views.exm),
    path('display/', views.exm_dispay),
]