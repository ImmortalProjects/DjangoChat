from django.http import HttpResponse
from django.shortcuts import render, redirect
from mysite.models import user
from django.views.generic import TemplateView


def home(request):
    p1 = user(user_name="Amritansh")
    p1.save()
    return render(request, "mysite/index.html")


# class Home(TemplateView):
#     template_name = "mysite/index.html"

#     def get(self, request):
#         users = User.objects.all()

#     def post(self, request):
#         return render(request, self.template_name)
