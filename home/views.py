from django.shortcuts import render, HttpResponse
from home import models
# Create your views here.

def  home(request):
    return render(request, "home.html")
# def index(request):
#     return HttpResponse("This is my homepage ")
def about(request):
    # return HttpResponse("This is about")
    return render(request, "about.html")
def statestic(request):
    # return HttpResponse("This is my project ")
    return render(request, "statestic.html")
def hospital(request):
    allHospital = models.Hospital.objects.all()
    for item in allHospital:
        print(item.state)
    context ={
        'hospitals' : allHospital
    }
    return render(request,'hospital.html',context)
def awareness(request):
    return render(request,'awareness.html')
def contacts(request):
    if request.method == "POST" :
        print("This is post")
        name =request.POST['name']
        email= request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        # print(name,email,phone,desc)
        ins = models.Contact(name=name,email=email,phone=phone,desc=desc)
        ins.save()
        print("The data has been written to the db")

    # return HttpResponse("This is contact")
    return render(request, "contact.html")


    