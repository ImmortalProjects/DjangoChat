from django.http import HttpResponse
from django.shortcuts import render, redirect
from chatapp.models import user
from django.views.generic import TemplateView
import json


def home(request):
    # p1 = user(user_name="Amritansh")
    # p1.save()
    p2 = user.objects.all()
    print(p2[0].user_name)
    return render(request, "chatapp/index.html")


# class Home(TemplateView):
#     template_name = "mysite/index.html"

#     def get(self, request):
#         users = User.objects.all()

#     def post(self, request):
#         return render(request, self.template_name)
