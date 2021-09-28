from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from chatapp.models import MessageBox
from django.views.generic import TemplateView
import json


def home(request):
    if request.method == "POST":
        m = request.POST.get("message")
        print(m + "   bye")
        MessageBox(message=m).save()
    context = {"messages": MessageBox.objects.all()}
    return render(request, "chatapp/index.html", context)
