from django.urls import path
from . import views

urlpatterns = [
    path("hello", views.say_hello),
    path("welcome/<str:name>/", views.welcome),
    path('register/',views.register)

]
