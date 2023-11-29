from django.shortcuts import render, redirect
from FinalProject.models import Member
# Create your views here.


def login(request):
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        member = Member(firstname=request.POST['firstname'],lastname=request.POST['lastname'],
                       email=request.POST['email'], username=request.POST['username'],
                       password=request.POST['password'])
        member.save()
        return redirect('/')
    else:
        return render(request, 'register.html')


def index(request):
    mem=Member.objects.all()
    return render(request, 'index.html', {'mem':mem})


def add(request):
    return render(request, 'add.html')


def addrec(request):
    x = request.POST['first']
    y = request.POST['last']
    z = request.POST['country']
    mem = Member(first_name=x, last_name=y, country=z,)
    mem.save()
    return redirect('/')


def delete(request, id):
    mem = Member.objects.get(id=id)
    mem.delete()
    return redirect('/')


def update(request, id):
    mem = Member.objects.get(id=id)
    return render(request, 'update.html', {'mem':mem})


def uprec(request, id):
    x = request.POST['first']
    y = request.POST['last']
    z = request.POST['country']
    mem = Member.objects.get(id=id)
    mem.first_name=x,
    mem.last_name=y,
    mem.country=z,
    mem.save()
    return redirect('/')


