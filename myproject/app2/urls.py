
from django.urls import path
from . import views

urlpatterns = [
    path('app2/home',views.home2,name="home"),
    path('app2',views.index2,name="index")
         
]
