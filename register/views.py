from django.shortcuts import redirect, render
from .models import *
from .forms import *

# Create your views here.

def createTrainees(request):
    if request.method == "POST":  
        form = TreaineesForms(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/listtrainees')  
            except:  
                pass  
    else:  
        form = TreaineesForms()     
    return render(request, "createTraineeForm.html",{'form':form})

def listAllTrainees(request):
    train = Trainees.objects.all()
  
    return render(request, "listAllTraineesForm.html",{'trainees': train})

def editTrainees(request, id):
    form = Trainees.objects.get(id=id)

    return render(request, "editerTraineesform.html",{'form':form})


def updateTrainees(request, id):
    form = Trainees.objects.get(id=id)
    forms = TreaineesForms(request.POST, instance = form)
    if forms.is_valid():
        forms.save()
        return redirect('/listtrainees')

    return render(request, "editerTraineesform.html",{'form': form})

def deleteTraineer(request, id):
    form = Trainees.objects.get(id=id)
    form.delete()
    return redirect('/listtrainees')


    

def login(request):

    return render(request, "login.html")
