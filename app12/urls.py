from django.urls import path
#now import the views.py file into this code
from . import views
urlpatterns=[
  path('',views.main, name="main"),
  path('home/',views.home, name="home"),
  path('opp/',views.opp, name="opp"),
  path('sub/', views.sub, name="sub")
]