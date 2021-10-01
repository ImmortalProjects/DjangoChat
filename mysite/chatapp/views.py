from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from chatapp.models import MessageBox
from django.views.generic import TemplateView
import json


def home(request):
    return render(request, "chatapp/index.html")


def room(request, room_name):
    context = {"messages": MessageBox.objects.all().filter(
        room_name=room_name), "room_name": room_name}
    return render(request, 'chatapp/room.html', context)
