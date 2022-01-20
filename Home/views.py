from email import message
from django.shortcuts import render,HttpResponse
from Home.models import Feedback
from django.contrib import messages


# Create your views here.
def index(request):
    content={
        "name":"Anshuman",
        "age":"18"
    }
    # messages.success(request,"Hello Happy to see you")
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        full_message=Feedback(name=name,email=email,message=message)
        full_message.save()
        messages.success(request, 'Thank You !!!.')



    return render(request,'index.html',content)

# def experience(request):
#     return render(request,'experience.html')

def projects(request):
    return render(request,'projects.html')

def blogs(request):
    return render(request,'blogs.html')


def search(request):
    return HttpResponse("This is search result")