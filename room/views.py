from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Room, Message
from django.utils.text import slugify
from django import forms
# Create your views here.

@login_required
def createrooms(request):
    if request.method=='POST':
        name=request.POST['creator']
        passkeys=request.POST['password4']
        slug = slugify(name)
        f=Room(name=name, slug=slug, passwords=passkeys)
        if name=='':
            return render(request, 'room/rooms.html',{'err':True})
        for instance in Room.objects.all():
            if instance.name==name:
                return render(request, 'room/rooms.html',{'error':True})
        else:
            f.save()
            return redirect('rooms')

@login_required
def rooms(request):
    rooms=Room.objects.all().order_by('pk').reverse()
    return render(request,'room/rooms.html',{
        'rooms':rooms
    })

@login_required
def room(request, slug):
    if request.method=='POST':
        passkeys=request.POST['password3']
        
        if passkeys=='':
            return render(request, 'room/rooms.html',{'err1':True})
        
        for instance in Room.objects.all():
            if instance.passwords==passkeys:
                room=Room.objects.get(slug=slug)
                messages=Message.objects.filter(room=room)[0:25]
                return render(request, 'room/room.html',{'room':room,
                'messages':messages
                })
        else:   
            return render(request, 'room/rooms.html',{'error1':True}) 

@login_required
def deleterooms(request):
    if request.method=='POST':
        name=request.POST['creator']
        passkeys=request.POST['password4']
        
        if name=='' or passkeys=='':
            return render(request, 'room/rooms.html',{'err11':True})
        for instance in Room.objects.all():
            if instance.passwords==passkeys and instance.name==name:
                f=Room.objects.get(name=name, passwords=passkeys)
                f.delete()
                return redirect('rooms')
        else:   
            return render(request, 'room/rooms.html',{'error11':True})
        
@login_required
def quickjoin(request):
    if request.method=='POST':
        name=request.POST['creator']
        passkeys=request.POST['password4']
        if name=='' or passkeys=='':
                return render(request, 'room/rooms.html',{'err11':True})
        for instance in Room.objects.all():
            if instance.name==name and instance.passwords==passkeys:
                room=Room.objects.get(name=name,passwords=passkeys)
                messages=Message.objects.filter(room=room)[0:25]
                return render(request, 'room/room.html',{'room':room,
                'messages':messages
                })
        else:   
            return render(request, 'room/rooms.html',{'error11':True}) 