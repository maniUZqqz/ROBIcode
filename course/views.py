from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView, View

def index(request):
    return render(
        request,
        "index/index.html",
        {},
    )

