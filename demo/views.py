from django.shortcuts import render, HttpResponse


# Create your views here.
# localhost:8000/demo/hello
def say_hello(request):
   return HttpResponse("Welcome to semicolon")


# def say_hello(request,name):
#     return HttpResponse(f"welcome {name}")


def welcome(request, name):
    return render(request,'index.html',{"name": ""})


def register(request):
    return render(request,'index.html',{'request':""})

def get_name():
    pass