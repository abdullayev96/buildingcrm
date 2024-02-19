from django.shortcuts import render
from .models import *


def home(request):
    changes = Change.objects.all()
    results = Result.objects.all().order_by('-id')
    place = Helper.objects.all()
    discord   = Discord.objects.all()

    if request.POST:
        model = Users()

        model.name  = request.POST.get("name")
        model.phone = request.POST.get("phone")
        model.subject = request.POST.get("subject")
        model.message  = request.POST.get("message")
        model.save()

    ctx  = {
        "changes": changes,
        "results":results,
        "place":place,
        "discord":discord,
        "page": "home"
    }

    return render(request, "index.html", ctx)



def More_page(request):
    ctx = {

        "page": "more"

    }
    return render(request, 'more.html', ctx)




def Discords(request):
    posts = Change.objects.all().order_by('-id')

    ctx  = {
        'posts':posts
    }
    return render(request, 'discord-server.html', ctx)




def Online(request):
    post = ChangePrice.objects.all().order_by('-id')

    ctx = {
        'post': post
    }
    return render(request, 'online-darslar.html', ctx)


def Robot(request):
    posts = ChangePrices.objects.all()

    ctx = {
        'posts': posts
    }
    return render(request, 'savdo-robot.html', ctx)



def calculator(request):
    images = Photos.objects.all().order_by('-id')
    ctx = {
        "images":images
    }
    return render(request, 'cul.html', ctx)

