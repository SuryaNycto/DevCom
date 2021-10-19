from django.contrib.auth import login
from django.shortcuts import render , redirect
from fullApp.forms  import SignUpForm,DsaForm
from django.contrib.auth.decorators import login_required

from . models import Dsa
def baseView(request):
    return render(request,"base.html")


def registrationView(request):
    form=SignUpForm()
    context={'form':form}
    
    if request.method=='POST':
        print("=================================")
        form=SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
            return redirect("/")
    return render(request,"fullApp/registration.html",context)

@login_required
def dsaView(request):
    form=DsaForm()
    vals=Dsa.objects.all()

    if request.method=="POST":
        form=DsaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/dsa")
    context={'form':form,'obj':vals}

    return render(request,'fullApp/DSA.html',context)

@login_required
def delete(request,id):
    toDelete=Dsa.objects.get(id=id)
    toDelete.delete()

    return redirect("/dsa")

def logoutView(request):
    return render(request,'logout.html')