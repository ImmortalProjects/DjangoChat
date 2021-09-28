from django.http import HttpResponse
from django.shortcuts import render, redirect
from chatapp.models import MessageBox
from django.views.generic import TemplateView
import json


class home(TemplateView):
    template_name = "chatapp/index.html"

    def post(self, request):
        message = request.POST.get("message")
        MessageBox(message=message).save()
        return render(request, self.template_name)
